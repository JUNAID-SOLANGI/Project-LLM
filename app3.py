import streamlit as st
from sqlalchemy import create_engine, text
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent_toolkits import create_sql_agent
from langchain.chat_models import ChatOpenAI
import re

# ---- UI Elements ----
st.title("🧠 Natural Language to SQL - Ask your Data")

# Initialize session state for connection objects
if "db" not in st.session_state:
    st.session_state.db = None
if "agent_executor" not in st.session_state:
    st.session_state.agent_executor = None

with st.sidebar:
    st.header("🔌 Database Connection")
    db_type = st.selectbox("Select DB Type", ["postgresql", "sqlite", "mysql"])
    db_name = st.text_input("Database Name", placeholder="e.g. neondb")
    username = st.text_input("Username", placeholder="e.g. root")
    password = st.text_input("Password", type="password")
    host = st.text_input("Host", placeholder="e.g. localhost or Neon endpoint")
    port = st.text_input("Port", placeholder="e.g. 5432")

    connect_clicked = st.button("🔗 Connect")

# ---- Connect to DB and Setup Agent ----
def setup_connection():
    try:
        if not all([db_type, db_name, host, port, username, password]):
            st.warning("⚠️ Please fill out all connection fields.")
            st.stop()

        if db_type == "sqlite":
            engine_url = f"sqlite:///{db_name}"
        elif db_type == "postgresql":
            engine_url = f"postgresql://{username}:{password}@{host}:{port}/{db_name}?sslmode=require"
        elif db_type == "mysql":
            engine_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}"
        else:
            raise ValueError("Unsupported DB type.")

        engine = create_engine(engine_url)
        db = SQLDatabase(engine, sample_rows_in_table_info=2)

        llm = ChatOpenAI(
            openai_api_base="https://openrouter.ai/api/v1",
            openai_api_key="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",
            model="deepseek/deepseek-chat-v3.1",
            temperature=0,
            max_tokens=512,
        )

        toolkit = SQLDatabaseToolkit(db=db, llm=llm)
        agent_executor = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True,
            handle_parsing_errors=True
        )

        return db, agent_executor

    except Exception as e:
        st.error(f"❌ Connection/setup failed: {e}")
        return None, None

# ---- Trigger connection and store in session state ----
if connect_clicked:
    st.session_state.db, st.session_state.agent_executor = setup_connection()
    if st.session_state.agent_executor:
        st.success("✅ Connected to database and agent initialized!")

# ---- Handle user query ----
# Check if the connection objects exist in session state before showing the query box
if st.session_state.agent_executor:
    with st.expander("📋 Show Tables"):
        try:
            tables = st.session_state.db.get_usable_table_names()
            st.write("Tables found:", tables)
        except Exception as e:
            st.error(f"Error listing tables: {e}")

    user_query = st.text_input("Ask your question:", placeholder="e.g., Which customer spent the most?")

    if user_query:
        with st.spinner("Thinking..."):
            try:
                # Use the agent from session state
                response = st.session_state.agent_executor.invoke({"input": user_query})
                output_text = response.get("output", str(response))
                match = re.search(r"Final Answer:\s*(.+)", output_text)

                if match:
                    st.success(match.group(1).strip())
                else:
                    st.info("🤖 Agent response:")
                    st.code(output_text.strip())

            except Exception as e:
                match = re.search(r"Final Answer:\s*(.+)", str(e))
                if match:
                    st.success(f"(Recovered): {match.group(1).strip()}")
                else:
                    st.error(f"❌ Agent Error: {e}")
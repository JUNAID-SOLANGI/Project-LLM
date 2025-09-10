import streamlit as st
from sqlalchemy import create_engine, inspect
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain.chat_models import ChatOpenAI
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting
import re
import plotly.express as px

user_query = None
df = None
st.title("Talk To Your Database")

# ---- Session State ----
if "db" not in st.session_state:
    st.session_state.db = None
if "chain" not in st.session_state:
    st.session_state.chain = None
if "llm" not in st.session_state:
    st.session_state.llm = None

# ---- Sidebar Connection ----
with st.sidebar:
    st.header("🔌 Database Connection")
    db_type = st.selectbox("Select DB Type", ["postgresql", "sqlite", "mysql"])
    db_name = st.text_input("Database Name", placeholder="e.g. neondb")
    username = st.text_input("Username", placeholder="e.g. root")
    password = st.text_input("Password", type="password")
    host = st.text_input("Host", placeholder="e.g. localhost or Neon endpoint")
    port = st.text_input("Port", placeholder="e.g. 5432")
    connect_clicked = st.button("🔗 Connect")

# ---- Setup Connection ----
def setup_connection():
    try:
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
            openai_api_key=st.secrets["OPENROUTER_API_KEY"],  # Replace with secure input method
            model="mistralai/codestral-2508",
            temperature=0,
        )

        chain = create_sql_query_chain(llm, db)
        return db, chain, llm

    except Exception as e:
        st.error(f"❌ Connection/setup failed: {e}")
        return None, None, None

if connect_clicked:
    st.session_state.db, st.session_state.chain, st.session_state.llm = setup_connection()
    if st.session_state.chain:
        st.success("✅ Connected to database and chain initialized!")

        # ---- Show schema immediately ----
        try:
            inspector = inspect(st.session_state.db._engine)
            tables = inspector.get_table_names()

            st.subheader("📂 Database Schema")
            for table in tables:
                with st.expander(f"Table: {table}"):
                    columns = inspector.get_columns(table)
                    col_info = pd.DataFrame(columns)
                    st.dataframe(col_info[["name", "type"]])
        except Exception as e:
            st.warning(f"Could not fetch schema: {e}")

# ---- User Query ----
if st.session_state.chain:
    user_query = st.text_input("Ask your question:", placeholder="e.g., Which customer spent the most?")

if user_query:
    with st.spinner("Thinking..."):
        try:
            # Force SQL-only output
            prompt = f"""
            You are a helpful SQL assistant. 
            Only return a valid SQL query that can run directly on the database.
            Do NOT include explanations or natural language.
            
            Question: {user_query}
            
            Return ONLY the SQL query.
            """

            sql_query = st.session_state.chain.invoke({"question": prompt})

            # --- Extract SQL cleanly ---
            sql_match = re.search(r"```sql\n(.*?)```", sql_query, re.DOTALL | re.IGNORECASE)
            if sql_match:
                sql_query = sql_match.group(1).strip()
            else:
                sql_match = re.search(r"(SELECT[\s\S]+?;)", sql_query, re.IGNORECASE)
                if sql_match:
                    sql_query = sql_match.group(1).strip()

            st.subheader("📝 SQL Query")
            st.code(sql_query, language="sql")

            # Run SQL
            df = pd.read_sql(sql_query, st.session_state.db._engine)

            st.subheader("📋 Data Preview")
            st.dataframe(df.head(20))
            
            # ---- Automatic Charting ----
            if not df.empty:
                st.subheader("📊 Automatic Chart")
                numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
                date_cols = df.select_dtypes(include=['datetime', 'datetime64']).columns.tolist()

                

                if len(numeric_cols) >= 3:  # 3D-like data -> 2D bubble chart
                    st.write(f"Displaying 2D bubble chart for {numeric_cols[:3]} (size/color encode third dimension)")

                    # Assign first 2 numeric columns to axes, 3rd to bubble size
                    x_col, y_col, z_col = numeric_cols[:3]

                    # Optional: categorical column for color
                    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
                    color_col = categorical_cols[0] if categorical_cols else None

                    fig = px.scatter(
                        df,
                        x=x_col,
                        y=y_col,
                        size=z_col,              # size encodes third numeric column
                        color=color_col,         # color encodes category or city
                        hover_data=df.columns,   # show full row on hover
                        size_max=60,
                    )

                    st.plotly_chart(fig, use_container_width=True)



                elif len(numeric_cols) >= 2 and len(date_cols) == 0:
                    x_col, y_col = numeric_cols[0], numeric_cols[1]
                    st.write(f"Displaying scatter plot for '{x_col}' vs '{y_col}'")
                    st.scatter_chart(df, x=x_col, y=y_col)

                elif len(numeric_cols) >= 1 and len(date_cols) >= 1:
                    date_col, numeric_col = date_cols[0], numeric_cols[0]
                    st.write(f"Displaying line chart for '{date_col}' vs '{numeric_col}'")
                    st.line_chart(df.set_index(date_col)[numeric_col])

                elif len(numeric_cols) >= 1 and len(df.columns) == 2:
                    numeric_col = numeric_cols[0]
                    categorical_col = df.columns.difference(numeric_cols)[0]
                    st.write(f"Displaying bar chart for '{categorical_col}' vs '{numeric_col}'")
                    st.bar_chart(df.set_index(categorical_col)[numeric_col])

                elif len(numeric_cols) == 1:
                    st.write(f"Displaying histogram for '{numeric_cols[0]}'")
                    fig, ax = plt.subplots()
                    df[numeric_cols[0]].hist(ax=ax)
                    st.pyplot(fig)

                else:
                    st.info("No suitable data for an automatic chart found.")

            # ---- Analysis Section ----
            if df is not None and not df.empty:
                analysis_prompt = f"""
                You are a data analyst. 
                Provide a brief, high-level analysis of the following query result.
                Be concise, avoid SQL details, and summarize any key insights.

                Result sample:
                {df.head(10).to_string(index=False)}
                """

                analysis = st.session_state.llm.invoke(analysis_prompt)

                # Extract clean text if it's a dict/message
                if hasattr(analysis, "content"):  
                    analysis_text = analysis.content  
                elif isinstance(analysis, dict) and "content" in analysis:  
                    analysis_text = analysis["content"]  
                else:  
                    analysis_text = str(analysis)

                st.subheader("🔎 Analysis")
                st.markdown(analysis_text)

        except Exception as e:
            st.error(f"❌ An error occurred while processing your query: {e}")

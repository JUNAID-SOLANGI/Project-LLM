# 🗣️ Talk To Your Database

> Transform your database queries from complex SQL to natural language conversations with AI-powered insights and automatic visualizations!

![Demo](https://via.placeholder.com/800x400/4CAF50/FFFFFF?text=Replace+with+main+demo+GIF)

## ✨ Features

### 🤖 Natural Language to SQL
Ask questions in plain English and get perfect SQL queries generated automatically.

![Natural Language Query](https://via.placeholder.com/600x300/2196F3/FFFFFF?text=Replace+with+query+demo+GIF)

### 📊 Automatic Visualizations
Smart chart generation based on your data:
- **3D Data** → Interactive bubble charts with Plotly
- **Time Series** → Dynamic line charts
- **Categorical** → Beautiful bar charts
- **Distributions** → Histograms and scatter plots

![Auto Charts](https://via.placeholder.com/600x300/FF9800/FFFFFF?text=Replace+with+charts+demo+GIF)

### 🔍 AI-Powered Analysis
Get intelligent insights and summaries of your query results automatically.

![AI Analysis](https://via.placeholder.com/600x300/9C27B0/FFFFFF?text=Replace+with+analysis+demo+GIF)

### 🗄️ Multi-Database Support
Connect to various database types:
- **PostgreSQL** (including Neon, Supabase)
- **MySQL** 
- **SQLite**

![Database Connection](https://via.placeholder.com/600x300/607D8B/FFFFFF?text=Replace+with+connection+demo+GIF)

## 🚀 Quick Start

### Prerequisites
```bash
pip install streamlit sqlalchemy langchain pandas matplotlib plotly
```

### Environment Setup
Create a `.streamlit/secrets.toml` file:
```toml
[secrets]
OPENROUTER_API_KEY = "your-openrouter-api-key-here"
```

### Run the Application
```bash
streamlit run app.py
```

![Quick Start](https://via.placeholder.com/600x200/4CAF50/FFFFFF?text=Replace+with+startup+GIF)

## 🎯 How It Works

### 1. Connect Your Database
![Step 1](https://via.placeholder.com/400x250/E91E63/FFFFFF?text=Step+1+Connection)

Use the sidebar to enter your database credentials:
- Select database type (PostgreSQL/MySQL/SQLite)
- Enter connection details
- Click "Connect" to establish connection

### 2. Explore Your Schema
![Step 2](https://via.placeholder.com/400x250/3F51B5/FFFFFF?text=Step+2+Schema)

Once connected, instantly see:
- All tables in your database
- Column names and data types
- Sample data preview

### 3. Ask Natural Questions
![Step 3](https://via.placeholder.com/400x250/009688/FFFFFF?text=Step+3+Questions)

Examples of questions you can ask:
- "Which customer spent the most money?"
- "Show me sales trends by month"
- "What are the top 10 products by revenue?"
- "Find all orders from the last 30 days"

### 4. Get Instant Results
![Step 4](https://via.placeholder.com/400x250/FF5722/FFFFFF?text=Step+4+Results)

Receive:
- ✅ Generated SQL query
- 📊 Automatic visualizations
- 📋 Data preview
- 🔍 AI analysis and insights

## 🎨 Visualization Examples

### Interactive Bubble Charts
Perfect for 3-dimensional data relationships.
![Bubble Chart](https://via.placeholder.com/600x400/673AB7/FFFFFF?text=Replace+with+bubble+chart+GIF)

### Time Series Analysis
Automatic detection and visualization of temporal data.
![Time Series](https://via.placeholder.com/600x400/795548/FFFFFF?text=Replace+with+timeseries+GIF)

### Distribution Analysis
Histograms and statistical visualizations for numeric data.
![Distribution](https://via.placeholder.com/600x400/FF9800/FFFFFF?text=Replace+with+histogram+GIF)

## 🔧 Configuration

### Supported Database URLs

#### PostgreSQL (Neon, Supabase, etc.)
```
postgresql://username:password@host:port/database?sslmode=require
```

#### MySQL
```
mysql+pymysql://username:password@host:port/database
```

#### SQLite
```
sqlite:///path/to/database.db
```

### AI Model Configuration
Currently using **Mistral Codestral** via OpenRouter for optimal SQL generation. You can modify the model in the code:

```python
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    model="mistralai/codestral-2508",  # Change this
    temperature=0,
)
```

## 📝 Example Queries

| Question | Generated Visualization |
|----------|------------------------|
| "Show sales by region" | Bar chart |
| "Revenue trends over time" | Line chart |
| "Customer age vs spending vs order count" | Bubble chart |
| "Product price distribution" | Histogram |

![Example Queries](https://via.placeholder.com/700x350/4CAF50/FFFFFF?text=Replace+with+examples+showcase+GIF)

## 🛠️ Technical Architecture

```mermaid
graph TD
    A[User Question] --> B[LangChain SQL Chain]
    B --> C[Generated SQL Query]
    C --> D[Database Execution]
    D --> E[Pandas DataFrame]
    E --> F[Auto Chart Detection]
    E --> G[AI Analysis]
    F --> H[Plotly/Streamlit Charts]
    G --> I[Insights & Summary]
```

## 🚨 Security Best Practices

- ✅ Use environment variables for API keys
- ✅ SSL connections for remote databases
- ✅ Read-only database users recommended
- ⚠️ Never commit credentials to version control

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain** for SQL chain functionality
- **Streamlit** for the beautiful web interface
- **Plotly** for interactive visualizations
- **OpenRouter** for AI model access

## 📞 Support

Having issues? Check out these resources:
- [GitHub Issues](https://github.com/yourusername/talk-to-database/issues)
- [Documentation](https://github.com/yourusername/talk-to-database/wiki)
- [Discussions](https://github.com/yourusername/talk-to-database/discussions)

---

<p align="center">
  <img src="https://via.placeholder.com/600x100/1976D2/FFFFFF?text=Made+with+❤️+for+Data+Enthusiasts" alt="Made with love">
</p>

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/talk-to-database&type=Date)](https://star-history.com/#yourusername/talk-to-database&Date)

![Footer GIF](https://via.placeholder.com/800x200/FF6B6B/FFFFFF?text=Replace+with+footer+animation+GIF)

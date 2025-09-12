# 🗣️ Talk To Your Database

> Transform your database queries from complex SQL to natural language conversations with AI-powered insights and automatic visualizations!

<div align="center">
  
  <!-- Replace this with your main demo GIF -->
  <!-- ![Demo](./assets/demo.gif) -->
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
  [![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
  [![Stars](https://img.shields.io/github/stars/yourusername/talk-to-database?style=social)](https://github.com/yourusername/talk-to-database)
  
</div>

## ✨ What Makes This Special

🤖 **Natural Language Processing** - Ask questions in plain English  
📊 **Smart Visualizations** - Automatic chart generation based on data type  
🔍 **AI Analysis** - Get insights and summaries automatically  
🗄️ **Multi-Database** - PostgreSQL, MySQL, SQLite support  
⚡ **Real-time Results** - Instant query execution and visualization  

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install streamlit sqlalchemy langchain pandas matplotlib plotly pymysql
```

### 2. Set Up API Key
Create `.streamlit/secrets.toml`:
```toml
[secrets]
OPENROUTER_API_KEY = "your-openrouter-api-key-here"
```

### 3. Run the App
```bash
streamlit run app.py
```

<!-- Replace with actual startup GIF -->
<!-- ![Quick Start](./assets/quickstart.gif) -->

---

## 🎯 How It Works

<table>
<tr>
<td width="50%">

### 1. 🔌 Connect Database
- Select your database type
- Enter connection details  
- Instant schema exploration

</td>
<td width="50%">

<!-- Replace with connection demo -->
<!-- ![Connect](./assets/connect.gif) -->
**Supported Databases:**
- PostgreSQL (Neon, Supabase)
- MySQL
- SQLite

</td>
</tr>
<tr>
<td width="50%">

### 2. 💬 Ask Questions
Natural language queries like:
- "Which customer spent the most?"
- "Show sales trends by month"
- "Top 10 products by revenue"

</td>
<td width="50%">

<!-- Replace with query demo -->
<!-- ![Query](./assets/query.gif) -->

</td>
</tr>
<tr>
<td width="50%">

### 3. 📊 Get Visualizations
Automatic chart detection:
- **3D Data** → Bubble charts
- **Time Series** → Line charts
- **Categories** → Bar charts
- **Distributions** → Histograms

</td>
<td width="50%">

<!-- Replace with charts demo -->
<!-- ![Charts](./assets/charts.gif) -->

</td>
</tr>
</table>

---

## 📊 Visualization Examples

<div align="center">

| Data Type | Visualization | Example |
|-----------|--------------|---------|
| **3+ Numeric Columns** | Interactive Bubble Chart | Sales vs Profit vs Quantity |
| **Time + Numeric** | Line Chart | Revenue over time |
| **Category + Numeric** | Bar Chart | Sales by region |
| **Single Numeric** | Histogram | Price distribution |

</div>

<!-- Replace with visualization showcase -->
<!-- ![Visualizations](./assets/visualizations.gif) -->

---

## 🛠️ Installation & Setup

### Environment Requirements
```bash
# Core dependencies
streamlit>=1.28.0
sqlalchemy>=2.0.0
langchain>=0.1.0
pandas>=1.5.0
matplotlib>=3.6.0
plotly>=5.15.0

# Database drivers
pymysql>=1.0.0  # For MySQL
psycopg2>=2.9.0  # For PostgreSQL
```

### Database Connection Examples

#### PostgreSQL (Neon/Supabase)
```python
# Format: postgresql://username:password@host:port/database
# Example: postgresql://user:pass@ep-example.neon.tech:5432/mydb?sslmode=require
```

#### MySQL
```python
# Format: mysql+pymysql://username:password@host:port/database
# Example: mysql+pymysql://root:password@localhost:3306/mydb
```

#### SQLite
```python
# Format: sqlite:///path/to/database.db
# Example: sqlite:///./data/mydb.sqlite
```

---

## 🎮 Interactive Features

### 🔍 Schema Explorer
Automatically displays:
- ✅ All database tables
- ✅ Column names and types
- ✅ Sample data preview

<!-- Replace with schema demo -->
<!-- ![Schema](./assets/schema.gif) -->

### 🤖 Smart SQL Generation
- Converts natural language to optimized SQL
- Handles complex joins and aggregations
- Error handling and query validation

### 📈 Dynamic Chart Selection
The app automatically chooses the best visualization:

```python
# Algorithm logic:
if numeric_columns >= 3:
    → Bubble chart (3D effect)
elif numeric_columns >= 2:
    → Scatter plot
elif date_columns >= 1 and numeric_columns >= 1:
    → Time series line chart
elif categorical + numeric:
    → Bar chart
else:
    → Histogram or table view
```

---

## 💡 Example Queries

<details>
<summary><b>🛒 E-commerce Database</b></summary>

```
"Show me the top 5 customers by total spending"
"What are the monthly sales trends for 2024?"
"Which products have the highest profit margins?"
"Find customers who haven't ordered in the last 90 days"
```
</details>

<details>
<summary><b>📊 Sales Database</b></summary>

```
"Compare sales performance by region"
"Show seasonal trends in our product categories"
"Which sales reps are performing above average?"
"What's the correlation between discount and sales volume?"
```
</details>

<details>
<summary><b>👥 HR Database</b></summary>

```
"Show employee count by department"
"What's the average salary by job title?"
"Find departments with highest turnover rates"
"Show hiring trends over the past 2 years"
```
</details>

<!-- Replace with examples showcase -->
<!-- ![Examples](./assets/examples.gif) -->

---

## 🏗️ Technical Architecture

```mermaid
graph TB
    A[👤 User Input] --> B[🧠 LangChain SQL Chain]
    B --> C[📝 Generated SQL]
    C --> D[🗄️ Database Query]
    D --> E[📊 Pandas DataFrame]
    E --> F{📈 Chart Type Detection}
    F -->|3+ Numeric| G[🫧 Bubble Chart]
    F -->|Time Series| H[📈 Line Chart]
    F -->|Categorical| I[📊 Bar Chart]
    F -->|Distribution| J[📉 Histogram]
    E --> K[🤖 AI Analysis]
    G --> L[🎯 Final Output]
    H --> L
    I --> L
    J --> L
    K --> L
```

---

## 🔒 Security & Best Practices

### ✅ Recommended Setup
- Use **read-only database users**
- Enable **SSL connections** for remote DBs
- Store **API keys in secrets.toml**
- Implement **query timeouts**

### ⚠️ Important Notes
```bash
# Never commit secrets
echo ".streamlit/secrets.toml" >> .gitignore

# Use environment variables in production
export OPENROUTER_API_KEY="your-key-here"
```

---

## 🎨 Customization

### Change AI Model
```python
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    model="mistralai/codestral-2508",  # Try other models
    temperature=0,
)
```

### Modify Chart Colors
```python
# In the Plotly section
fig = px.scatter(
    df, x=x_col, y=y_col, size=z_col,
    color_discrete_sequence=px.colors.qualitative.Set3  # Custom colors
)
```

---

## 🐛 Troubleshooting

<details>
<summary><b>🔴 Connection Issues</b></summary>

```
Error: "could not connect to server"
```
**Solutions:**
- ✅ Check database credentials
- ✅ Verify host/port accessibility  
- ✅ Ensure SSL mode for cloud DBs
- ✅ Check firewall settings

</details>

<details>
<summary><b>🟡 Query Generation Issues</b></summary>

```
Error: "SQL query failed"
```
**Solutions:**
- ✅ Rephrase your question more clearly
- ✅ Check if tables/columns exist
- ✅ Verify data types match query expectations
- ✅ Try simpler queries first

</details>

<details>
<summary><b>🟠 Visualization Issues</b></summary>

```
Error: "No suitable data for chart"
```
**Solutions:**
- ✅ Ensure numeric columns for charts
- ✅ Check for null/empty data
- ✅ Verify date format for time series
- ✅ Try different query approaches

</details>

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** changes: `git commit -m 'Add amazing feature'`
4. **Push** to branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### 🎯 Areas for Contribution
- 🔌 Additional database connectors
- 📊 New visualization types
- 🤖 Improved AI prompts
- 🌐 Internationalization
- 🎨 UI/UX improvements

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **[LangChain](https://langchain.com/)** - SQL chain functionality
- **[Streamlit](https://streamlit.io/)** - Amazing web framework
- **[Plotly](https://plotly.com/)** - Interactive visualizations
- **[OpenRouter](https://openrouter.ai/)** - AI model access

---

## 📞 Support & Community

<div align="center">

[![GitHub Issues](https://img.shields.io/badge/Issues-GitHub-red?style=for-the-badge&logo=github)](https://github.com/yourusername/talk-to-database/issues)
[![Discussions](https://img.shields.io/badge/Discussions-GitHub-blue?style=for-the-badge&logo=github)](https://github.com/yourusername/talk-to-database/discussions)
[![Wiki](https://img.shields.io/badge/Wiki-Documentation-green?style=for-the-badge&logo=wikipedia)](https://github.com/yourusername/talk-to-database/wiki)

</div>

---

<div align="center">
  <h3>🌟 If this project helped you, please give it a star! 🌟</h3>
  
  <!-- Replace with footer animation -->
  <!-- ![Footer](./assets/footer.gif) -->
  
  <p><i>Made with ❤️ for the data community</i></p>
</div>

---

## 📈 Roadmap

- [ ] 🔌 Support for more databases (MongoDB, Redis)
- [ ] 🤖 Multiple AI model options
- [ ] 📱 Mobile-responsive design
- [ ] 🔄 Query history and favorites
- [ ] 📊 Advanced chart customization
- [ ] 🌍 Multi-language support
- [ ] 🔐 Enhanced security features
- [ ] ☁️ Cloud deployment templates

---

## 📊 Project Stats

<div align="center">
  
  ![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/talk-to-database)
  ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/yourusername/talk-to-database)
  ![GitHub code size](https://img.shields.io/github/languages/code-size/yourusername/talk-to-database)
  
</div>

<!-- GIF Creation Instructions:

TO CREATE WORKING GIFS FOR YOUR README:

1. Create an 'assets' folder in your repo root
2. Record these GIFs using tools like:
   - LICEcap (free, cross-platform)
   - Kap (macOS)
   - ScreenToGif (Windows)
   - OBS Studio (all platforms)

3. Recommended settings:
   - Resolution: 800x600 or 1024x768
   - Frame rate: 10-15 fps
   - Duration: 5-15 seconds
   - File size: Under 10MB each

4. Name your GIFs:
   - demo.gif (main application demo)
   - connect.gif (database connection process)
   - query.gif (asking questions and getting SQL)
   - charts.gif (automatic chart generation)
   - schema.gif (schema exploration)
   - examples.gif (multiple queries showcase)
   - quickstart.gif (app startup)
   - visualizations.gif (different chart types)
   - footer.gif (closing animation)

5. Upload to ./assets/ folder and uncomment the image lines above


https://github.com/user-attachments/assets/c580f022-bb74-418f-a621-c766e0ad5b8d


-->

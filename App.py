import streamlit as st

# --- App Configuration — No logo/avatar ---
st.set_page_config(
    page_title="Data Skills Hub",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Minimal Color Styling / Container Sim ---
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #0f0f0f;
        color: #f5f5f5;
    }
    .stButton>button {
        background-color: #262730;
        color: #f5f5f5;
        border: none;
        padding: 0.5rem 1rem;
        margin-top: 10px;
    }
    .st-radio label {
        color: #ddd !important;
    }
    .reportview-container .markdown-text-container {
        font-size: 1rem;
    }
    a {
        color: #ffd700;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📚 Learn with Ashwik")
choice = st.sidebar.radio("Select Topic", ["Home", "📈 Data Science", "📊 Data Analytics", "📑 MS Excel"])

# --- Custom Divider ---
def divider(title):
    st.markdown(f"""---\n#### {title}\n""")

# --- Home Page ---
def home():
    st.title("🎓 Data Skills Hub - Interactive Learning")
    st.markdown("""
Welcome to your personalized learning environment covering:

- 📈 **Data Science**
- 📊 **Data Analytics**
- 📑 **Microsoft Excel**

Built for beginners to intermediate learners with **real examples**, **video learning**, and **interactive quizzes**.
""")

    st.image(
        "https://images.unsplash.com/photo-1519389950473-47ba0277781c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
        caption="Empower your career with data skills.",
        use_container_width=True,
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Modules", "3")
    col2.metric("Code Examples", "30+")
    col3.metric("Viewers", "1,200+")

    divider("🌐 Quick Learning Videos")
    cols = st.columns(3)
    cols[0].video("https://www.youtube.com/watch?v=ua-CiDNNj30")  # DS
    cols[1].video("https://www.youtube.com/watch?v=9J9gkqFtyYg")   # Analytics
    cols[2].video("https://www.youtube.com/watch?v=8cG-VeN94Og")   # Excel

    divider("🤝 Connect with Me")
    st.markdown(f"""
I'm Ashwik Bire, and I created this learning hub to make data education accessible to everyone.

📇 Connect with me on [LinkedIn](https://linkedin.com/in/ashwik-bire-b2a000186)
""")

# --- Data Science Page ---
def data_science():
    st.title("📈 Data Science")
    st.markdown("Explore how data drives decisions, predictions, and innovation.")

    with st.expander("🚀 Overview & Tools"):
        st.markdown("""
- What is Data Science?
- Lifecycle: Data collection → Cleaning → Modeling → Evaluation
- Python, Pandas, NumPy, Matplotlib, Scikit-Learn
- Real-world use: AI in healthcare, risk modeling, targeted marketing
        """)

    col1, col2 = st.columns(2)
    col1.markdown("""
- **Python for DS**  
- **DataFrames & Series**  
- **Exploratory data viz**  
""")
    col2.markdown("""
- **ML algorithms**  
- **Supervised vs Unsupervised**  
- **Model scoring & tuning**  
""")

    with st.expander("💡 Simple ML Code Example"):
        st.code("""
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'exp': [1,2,3,4], 'salary': [40000, 45000, 50000, 60000]}
df = pd.DataFrame(data)
X, y = df[['exp']], df['salary']

model = LinearRegression().fit(X, y)
print("Prediction (5 yrs):", model.predict([[5]]))
        """, language="python")

    divider("🧠 Try a Quick Quiz")
    q = st.radio("Which is a supervised ML algorithm?", ["K-Means", "Linear Regression", "DBSCAN"])
    if st.button("Answer"):
        st.success("Correct ✅" if q == "Linear Regression" else "❌ That's not supervised.")

    divider("📥 Resources")
    st.markdown("""
- [Kaggle: Learn Python](https://www.kaggle.com/learn/python)  
- [DS Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)  
- [Download Cheatsheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)
    """)

# --- Data Analytics Page ---
def data_analytics():
    st.title("📊 Data Analytics")
    st.markdown("Understand the past, analyze the present, and forecast the future.")

    with st.expander("📌 Analytics Essentials"):
        st.markdown("""
- Four types: Descriptive, Diagnostic, Predictive, Prescriptive
- Tools: Excel, SQL, Python, Tableau
- Data Preparation: outliers, nulls, filters
        """)

    with st.container():
        col1, col2 = st.columns(2)
        col1.markdown("""
- 📂 Cleaning & Filtering  
- 📈 Aggregation patterns  
- 📊 Visualizations  
        """)
        col2.markdown("""
- 🧩 Pivot analysis  
- 🔢 SQL Queries  
- 📉 Trend decomposition  
        """)

    with st.expander("🧮 Sample: Product Sales Preview"):
        st.code("""
df = pd.read_csv("sales.csv")
top = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(5)
print(top)
        """)

    divider("🧠 Quiz Time")
    ans = st.radio("Which analytics is about **'Why did it happen?'**", ["Descriptive", "Diagnostic", "Predictive"])
    if st.button("Check", key="quiz2"):
        st.success("Correct ✔️" if ans == "Diagnostic" else "❌ Try again")

    divider("📦 Resource Picks")
    st.markdown("""
- [Analytics Vidhya Guide](https://www.analyticsvidhya.com/blog/2021/04/a-beginners-guide-to-data-analytics/)  
- [W3Schools SQL](https://www.w3schools.com/sql/)  
- [DataCamp Analyst Track](https://www.datacamp.com/tracks/data-analyst-with-python)  
""")

# --- Excel Page ---
def ms_excel():
    st.title("📑 MS Excel Mastery")
    st.markdown("The most powerful spreadsheet tool for analysts and business users.")

    with st.expander("📋 Excel Basics"):
        st.markdown("""
- Formulas: `SUM`, `AVERAGE`, `IF`, `AND`, `OR`
- Freezing, Sorting, Filtering
- Autofill, cell references
        """)
        st.video("https://www.youtube.com/watch?v=8cG-VeN94Og")

    with st.expander("📊 Advanced Excel Tools"):
        st.markdown("""
- Pivot Tables & Charts  
- **VLOOKUP** and **INDEX-MATCH**  
- Conditional formatting & Macros  
        """)
        st.video("https://www.youtube.com/watch?v=RZP_iO3Kg_M")

    divider("📝 Quick Quiz")
    exq = st.radio("What does `=VLOOKUP()` do?", ["Looks left", "Looks up vertically", "Sorts rows"])
    if st.button("Submit", key="excel_q"):
        st.success("✔️ Correct!" if exq == "Looks up vertically" else "❌ Nope!")

    divider("📥 Download Helper")
    st.markdown("[📄 Download Excel Cheatsheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")

# --- Page Routing Logic ---
if choice == "Home":
    home()
elif choice == "📈 Data Science":
    data_science()
elif choice == "📊 Data Analytics":
    data_analytics()
elif choice == "📑 MS Excel":
    ms_excel()

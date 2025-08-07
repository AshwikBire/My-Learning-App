import streamlit as st

# Global Config
st.set_page_config(
    page_title="Ultimate Learning App",
    page_icon=":mortar_board:",
    layout="wide"
)

# [OPTIONAL] Inject custom CSS for visual polish
st.markdown("""
    <style>
        .main {
            background-color: #f3f8fc;
        }
        h1, h2, h3 {
            color: #28527a;
        }
        .stButton > button {
            color: white;
            background: #3274d9;
        }
        .stRadio > div {
            background: #e8f0fe;
            padding: 5px;
            border-radius: 5px;
        }
        a {
            color: #1d5b99;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# LinkedIn
LINKEDIN_URL = "https://linkedin.com/in/ashwik-bire-b2a000186"

st.sidebar.title("📚 Learn Dashboard")
page = st.sidebar.radio("Navigate", ["Home", "Data Science", "Data Analytics", "MS Excel"])

# Separator
def section_separator(title=""):
    st.markdown(f"""<hr style="margin-top:40px; margin-bottom:20px">""", unsafe_allow_html=True)
    if title:
        st.subheader(title)

# --- Home Page ---
def show_home():
    st.title("🎓 Welcome to the Ultimate Learning App")
    st.markdown("""
        Learn **Data Science**, **Data Analytics**, and **MS Excel** in one powerful, friendly dashboard.
        Ideal for beginners and professionals alike.
    """)
    
    # Banner Image
    st.image(
        "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1200&q=80",
        caption="Unlock Your Data Skills!",
        use_container_width=True,
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Courses", "3")
    col2.metric("Hands-on Examples", "30+")
    col3.metric("Community Learners", "5,000+")

    section_separator("🎥 Featured YouTube Tutorials")
    v1, v2, v3 = st.columns(3)
    v1.video("https://www.youtube.com/watch?v=ua-CiDNNj30")  # Data Science
    v2.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")  # Data Analytics
    v3.video("https://www.youtube.com/watch?v=8cG-VeN94Og")  # Excel

    section_separator("📎 Connect")
    st.markdown(f"""
        Reach out for learning updates and insights:  
        👉 [Ashwik Bire on LinkedIn]({LINKEDIN_URL})
    """)
    
    section_separator("🚀 Get Started")
    st.write("Use the sidebar to explore topics. Each module offers video lessons, quizzes, hands-on examples, and downloadable resources.")

# --- Data Science Page ---
def show_data_science():
    st.title("📊 Data Science Learning Path")

    st.write("Data Science combines programming, statistics, and ML to build real-world insights and predictions.")

    with st.expander("📘 Introduction"):
        st.markdown("""
        - What is Data Science?  
        - Life-cycle: collect → clean → explore → model → deploy  
        - Tools: Python, pandas, NumPy, scikit-learn, matplotlib
        """)
        st.video("https://www.youtube.com/watch?v=ua-CiDNNj30")

    col1, col2 = st.columns(2)
    col1.markdown("""
    - Data manipulation with `pandas`  
    - Exploratory Data Analysis (EDA)  
    - Visualizing data with `matplotlib`, `seaborn`
    """)
    col2.markdown("""
    - Cleaning missing values  
    - Statistical understanding (mean, std, outliers)  
    - Intro to Machine Learning
    """)

    with st.expander("🤖 ML Walkthrough: Linear Regression"):
        st.code('''
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {'experience': [1,2,3,4,5], 'salary': [35000, 42000, 50000, 58000, 64000]}
df = pd.DataFrame(data)

X = df[['experience']]
y = df['salary']

model = LinearRegression().fit(X, y)
prediction = model.predict([[6]])

print(f"Predicted salary for 6 years: ₹{prediction[0]:,.0f}")
        ''', language="python")

    section_separator("🧠 Quick Quiz")
    q1 = st.radio("Which algorithm is used in supervised learning?", ["K-means", "Linear Regression", "Apriori"])
    if st.button("Submit Answer - DS"):
        if q1 == "Linear Regression":
            st.success("✅ Correct! Linear Regression is supervised.")
        else:
            st.warning("❌ Nope! Try again.")

    section_separator("📄 Resources")
    st.markdown("""
    - [📘 Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)  
    - [🧠 Kaggle DS Courses](https://www.kaggle.com/learn/data-science)  
    - [🧪 Scikit-learn Docs](https://scikit-learn.org/stable/)
    """)

# --- Data Analytics Page ---
def show_data_analytics():
    st.title("📈 Data Analytics Learning Path")
    st.markdown("Turn raw data into insights. Master analytics workflows with tools like SQL, Excel, and pandas.")

    with st.expander("📘 Core Concepts"):
        st.markdown("""
        - Descriptive vs Diagnostic vs Predictive Analytics  
        - Data cleanup: handling nulls, formatting  
        - Trend discovery and relationships  
        """)
        st.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")

    col1, col2 = st.columns(2)
    col1.markdown("""
    - Cleaning & filtering in Excel  
    - Positions using pivot tables  
    - SQL for analysts  
    """)
    col2.markdown("""
    - Building dashboards  
    - Groupby and visualization in Python  
    - Value-based storytelling  
    """)

    with st.expander("📊 Example: Sales Revenue Insights"):
        st.code('''
import pandas as pd

df = pd.read_csv("sales.csv")
df.dropna(inplace=True)
top_sales = df.groupby("region")["sales"].sum().sort_values(ascending=False)
print(top_sales)
        ''')

    section_separator("🧠 Quick Quiz")
    q2 = st.radio("Which analytics type predicts future outcomes?", ["Descriptive", "Diagnostic", "Predictive"])
    if st.button("Submit Answer - Analytics"):
        if q2 == "Predictive":
            st.success("✅ Correct! Predictive = forecasts.")
        else:
            st.warning("❌ Not quite. Try again.")

    section_separator("📄 Downloads")
    st.markdown("[📥 Analytics Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")

# --- Excel Page ---
def show_ms_excel():
    st.title("📊 MS Excel Mastery")

    st.write("Master Excel’s formulas, visualization, and automation tools to handle and analyze data efficiently.")

    col1, col2 = st.columns(2)
    col1.markdown("""
    - Basic functions: `SUM`, `IF`, `AVERAGE`, `TEXT`, `LEN`  
    - Formatting tricks  
    - Data cleanup workflows  
    """)
    col2.markdown("""
    - Pivot tables  
    - VLOOKUP, INDEX + MATCH  
    - Conditional formatting  
    """)

    with st.expander("📊 Create a Dashboard"):
        st.write("Combine pivot tables, charts, and slicers to build interactive dashboards for sales, staff, or KPIs.")
        st.video("https://www.youtube.com/watch?v=RZP_iO3Kg_M")

    section_separator("🧠 Quick Quiz")
    q3 = st.radio("Which function retrieves data horizontally?", ["VLOOKUP", "HLOOKUP", "INDEX", "IF"])
    if st.button("Submit Answer - Excel"):
        if q3 == "HLOOKUP":
            st.success("✅ That's right!")
        else:
            st.warning("❌ Oops! Hint: 'H' is for Horizontal.")

    section_separator("📄 Downloads")
    st.markdown("[📥 Excel Formula PDF](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")

# --- Routing ---
if page == "Home":
    show_home()
elif page == "Data Science":
    show_data_science()
elif page == "Data Analytics":
    show_data_analytics()
elif page == "MS Excel":
    show_ms_excel()

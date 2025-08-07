import streamlit as st

# LinkedIn Profile
LINKEDIN_URL = "https://linkedin.com/in/ashwik-bire-b2a000186"

# Streamlit page config (wide view is better for mobile/tablets)
st.set_page_config(
    page_title="📚 Data Learning App",
    page_icon="📊",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("📖 Topics")
page = st.sidebar.radio("Navigate", ["🏠 Home", "📊 Data Science", "📈 Data Analytics", "📑 MS Excel"])

def section_header(title):
    st.markdown(f"---\n### {title}\n")

# Home Page
def show_home():
    st.title("📚 Learn Data Science, Analytics & Excel")
    st.subheader("All-In-One Learning Companion ✨")

    st.markdown("""
    Welcome to your mobile-friendly learning hub covering:
    - 📊 **Data Science**
    - 📈 **Data Analytics**
    - 📑 **Microsoft Excel**

    Navigate through topics using the menu. Each comes with videos, quizzes, examples, and cheat sheets!
    """)

    st.image(
        "https://images.unsplash.com/photo-1601582583202-c4e6b5c5ca58?auto=format&fit=crop&w=1200&q=80",
        caption="Empower Your Data Journey 🚀",
        use_container_width=True
    )

    # Quick stats
    col1, col2, col3 = st.columns(3)
    col1.metric("Lessons", "50+")
    col2.metric("Tutorials", "30+")
    col3.metric("Quizzes", "10+")

    section_header("🎬 YouTube Learning Picks")
    yt1, yt2, yt3 = st.columns(3)
    yt1.video("https://www.youtube.com/watch?v=ua-CiDNNj30")  # DS
    yt2.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")   # Analytics
    yt3.video("https://www.youtube.com/watch?v=8cG-VeN94Og")   # Excel

    section_header("🔗 Connect")
    st.markdown(f"""
        **LinkedIn:** [Ashwik Bire]({LINKEDIN_URL})  
        Get access to projects, networks, and insights!
    """)

# Data Science Page
def show_data_science():
    st.title("📊 Data Science Learning")
    st.markdown("""
    Data Science uses Python, statistics, and ML to derive insights from data.
    """)

    with st.expander("📘 What You'll Learn"):
        st.markdown("""
        - 🧰 Tools: Python, Pandas, Numpy, Jupyter  
        - 📊 Data Cleaning & Analysis  
        - 📈 Visualizations (Matplotlib, Seaborn)  
        - 🤖 Machine Learning Algorithms  
        """)

    st.video("https://www.youtube.com/watch?v=Gv9_4yMHFhI")

    col1, col2 = st.columns(2)
    col1.markdown("""
    ### 📌 Python Essentials  
    - Variables, Lists, Dictionaries  
    - Functions & Loops  
    - Libraries Overview
    """)
    col2.markdown("""
    ### 📌 Machine Learning  
    - Supervised & Unsupervised  
    - Linear Regression, K-Means  
    - Model Evaluation
    """)

    with st.expander("💻 Code: Linear Regression Example"):
        st.code('''
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'exp': [1, 2, 3, 4], 'salary': [35000, 40000, 50000, 55000]}
df = pd.DataFrame(data)

X = df[['exp']]
y = df['salary']

model = LinearRegression()
model.fit(X, y)
pred = model.predict([[5]])
print(f"Est. Salary for 5 yrs exp: ${pred[0]:.2f}")
        ''', language='python')

    section_header("🧠 Quick Quiz")
    answer = st.radio("Which ML type uses labels?", ["Unsupervised", "Supervised", "Reinforcement"], key="ds_quiz")
    if st.button("Submit", key="ds_submit"):
        st.success("✅ Correct!") if answer == "Supervised" else st.error("❌ Try again")

    section_header("📁 Cheat Sheet")
    st.markdown("[Download: Data Science Basics](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")

# Data Analytics Page
def show_data_analytics():
    st.title("📈 Data Analytics Curriculum")

    st.markdown("""
    Learn to explore, clean, and visualize data for impactful decision-making.
    """)

    with st.expander("📘 What's Inside?"):
        st.markdown("""
        - 🧹 Data Cleaning (missing values, outliers)  
        - 📉 Descriptive vs Predictive Analytics  
        - 🎨 Visualization & Dashboards  
        - 🧪 SQL + Business Insights  
        """)

    st.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")

    col1, col2 = st.columns(2)
    col1.markdown("""
    ### 🔧 Tools
    - Excel  
    - SQL  
    - Tableau  
    """)
    col2.markdown("""
    ### 📊 Analytics Types
    - Descriptive  
    - Diagnostic  
    - Predictive  
    - Prescriptive  
    """)

    with st.expander("💻 Code: Analyzing Sales"):
        st.code('''
import pandas as pd
df = pd.read_csv("sales.csv")
df = df.dropna()
top = df.groupby('product')['revenue'].sum().nlargest(5)
print(top)
        ''', language="python")

    section_header("🧠 Quiz Time")
    q = st.radio("What analytics type forecasts future?", ["Descriptive", "Diagnostic", "Predictive"], key="da_q")
    if st.button("Submit", key="da_submit"):
        st.success("✅ Yes, Predictive it is!") if q == "Predictive" else st.error("❌ Nope")

    section_header("📁 Resource")
    st.markdown("[Download: Analytics Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")

# MS Excel Page
def show_ms_excel():
    st.title("📑 Excel Mastery Ground")
    st.markdown("""
    Build data skills in spreadsheet fundamentals, dashboards, and automation.
    """)

    with st.expander("💻 Learn Essentials"):
        st.markdown("""
        - ✅ SUM, AVERAGE, IF Functions  
        - 🔄 VLOOKUP, INDEX-MATCH  
        - 📈 Pivot Tables & Charts  
        - ⚙️ Macros Introduction  
        """)

    st.video("https://www.youtube.com/watch?v=8cG-VeN94Og")

    col1, col2 = st.columns(2)
    col1.markdown("""
    ### Shortcuts
    - Ctrl + Arrow (jump)  
    - Ctrl + T (table)  
    - Alt + E + S + V (Paste special)
    """)
    col2.markdown("""
    ### Tips
    - Use Named Ranges  
    - Use Form Control for dropdowns  
    - Always back up formulas
    """)

    section_header("📊 Quiz: Excel Basics")
    ans = st.radio("Which formula finds horizontal value?", ["VLOOKUP", "HLOOKUP", "INDEX"], key="exc_q")
    if st.button("Submit", key="exc_submit"):
        st.success("🎉 Correct!") if ans == "HLOOKUP" else st.error("⛔ Try again")

    section_header("📁 Resource")
    st.markdown("[Download: Excel Quick Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")

# Page Router
if page.startswith("🏠"):
    show_home()
elif page.startswith("📊"):
    show_data_science()
elif page.startswith("📈"):
    show_data_analytics()
elif page.startswith("📑"):
    show_ms_excel()

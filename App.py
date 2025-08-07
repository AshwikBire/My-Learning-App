import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# Get current page (defaults to 'home')
query_params = st.query_params
current_page = query_params.get("page", "home")

# Navigation Helper
def go_to(page):
    st.query_params.page = page


# ------------------- Pages -------------------

# -------- HOME --------
def page_home():
    st.title("📚 Learn Data Science, Analytics & Excel")
    st.subheader("All-in-One Learning Platform for Beginners & Professionals")

    st.image(
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1280&q=80",
        caption="🚀 Empower Your Career with Data Skills",
        use_container_width=True
    )

    st.markdown("### 🚀 Choose a Learning Path:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("📊 Data Science", on_click=lambda: go_to("data_science"))
    with col2:
        st.button("📈 Data Analytics", on_click=lambda: go_to("data_analytics"))
    with col3:
        st.button("📑 MS Excel", on_click=lambda: go_to("excel"))

    st.divider()

    st.subheader("🎥 Featured YouTube Tutorials")
    col_a, col_b, col_c = st.columns(3)
    col_a.video("https://www.youtube.com/watch?v=ua-CiDNNj30")  # DS video
    col_b.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")   # Analytics video
    col_c.video("https://www.youtube.com/watch?v=8cG-VeN94Og")   # Excel video

    st.divider()
    st.markdown("### 🔗 Connect with Ashwik Bire")
    st.markdown("[🔗 LinkedIn - Click here](https://linkedin.com/in/ashwik-bire-b2a000186)")


# -------- DATA SCIENCE --------
def page_data_science():
    st.title("📊 Data Science Learning")
    st.video("https://www.youtube.com/watch?v=Gv9_4yMHFhI")

    st.markdown("""
    Data Science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data.

    **Key learning areas include:**
    - 🐍 Python programming with libraries like Pandas and NumPy for data manipulation.
    - 📊 Data cleaning, exploratory data analysis, and effective visualization.
    - 🤖 Machine learning concepts, including supervised, unsupervised learning, and model evaluation.
    - ⚙️ Data Engineering fundamentals for building data pipelines.
    """)

    with st.expander("💡 Why Data Science?"):
        st.markdown("""
        Data-driven decisions are now at the core of successful organizations worldwide. Data Scientists transform raw data into actionable insights that drive innovation, optimize operations, and create competitive advantages.

        This course will help you understand the lifecycle of data science projects—from data collection and cleaning to model building and deployment.
        """)

    st.subheader("💡 Concepts Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
    • Python & Jupyter notebooks basics  
    • Data structures & data manipulation  
    • Data visualization with Matplotlib and Seaborn  
    • Introduction to statistics and probability  
    • Data wrangling techniques and handling missing data  
    """)
    col2.markdown("""
    • Machine learning workflows  
    • Regression, classification, clustering algorithms  
    • Model validation and hyperparameter tuning  
    • Ethics and responsible AI  
    • Introduction to Big Data tools (Spark, Hadoop overview)  
    """)

    with st.expander("📚 Read More: Core Python for Data Science"):
        st.markdown("""
        Python is the most popular language in data science because of its readability and vast ecosystem. Learning Python essentials—like lists, dictionaries, functions, and modules—is crucial for performing complex data operations efficiently.

        Libraries like Pandas provide powerful data structures and functions making data cleaning and analysis straightforward.
        """)

    with st.expander("📚 Read More: Data Visualization Best Practices"):
        st.markdown("""
        Effective data visualization communicates insights clearly and efficiently. Choosing the right chart and using color effectively can highlight key patterns and trends, aiding decision makers to understand data narratives better.

        Learn different types of plots such as histograms, scatter plots, box plots, and heatmaps.
        """)

    with st.expander("💻 Example: Linear Regression in Python"):
        st.code("""
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'Experience': [1,2,3,4,5], 'Salary': [45000, 50000, 60000, 65000, 70000]}
df = pd.DataFrame(data)

X = df[['Experience']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

predicted_salary = model.predict([[6]])
print(f'Predicted salary for 6 years experience: ${predicted_salary[0]:.2f}')
        """)

    with st.expander("📚 Read More: Machine Learning Workflow"):
        st.markdown("""
        The machine learning workflow involves collecting data, preprocessing, feature engineering, model selection, training, evaluation, and deployment.

        Understanding this pipeline lets you build reliable models and improve them iteratively.
        """)

    with st.expander("🧠 Quiz"):
        answer = st.radio("Which machine learning approach uses labeled training data?", ["Unsupervised", "Supervised", "Reinforcement"])
        if st.button("Submit", key="ds_quiz_submit"):
            if answer == "Supervised":
                st.success("✅ Correct! Supervised learning uses labeled data.")
            else:
                st.error("❌ Incorrect, try again.")

    st.markdown("📥 [Download Data Science Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))


# -------- DATA ANALYTICS --------
def page_data_analytics():
    st.title("📈 Data Analytics Curriculum")
    st.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")

    st.markdown("""
    Data Analytics involves examining data sets to uncover patterns, trends, and insights to support decision-making.

    **Focus areas include:**
    - Data cleaning and preparation to ensure high quality.
    - Data summarization and visualization for storytelling.
    - Use of SQL and BI tools like Power BI and Tableau for interactive dashboards.
    - Introduction to statistical inference for data-driven decisions.
    """)

    with st.expander("💡 Importance of Data Analytics"):
        st.markdown("""
        Analytics enables organizations to convert data into knowledge. Effective analytics supports business intelligence, operational efficiency, and competitive strategy.

        You'll learn how to transform raw data into actionable insights using modern tools and techniques.
        """)

    st.subheader("💡 Topics Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
    • Types of analytics: descriptive, diagnostic, predictive, prescriptive   
    • Exploratory data analysis (EDA) techniques  
    • Data visualization best practices  
    • SQL fundamentals for querying  
    • Data quality assessment and cleaning  
    """)
    col2.markdown("""
    • Building dashboards with Power BI/Tableau  
    • Python toolkits: Pandas for data handling, Matplotlib/Seaborn for plots  
    • Statistical concepts: sampling, hypothesis testing  
    • Communicating insights through storytelling  
    """)

    with st.expander("📚 Read More: Power BI Fundamentals"):
        st.markdown("""
        Power BI helps visualize and share insights through interactive reports. You will learn to connect to various data sources, transform data using Power Query, and create dashboards.

        Understanding how to interpret these dashboards is essential for data-driven decisions.
        """)

    with st.expander("💻 Example: Basic Sales Data Analysis in Python"):
        st.code("""
import pandas as pd

sales_df = pd.read_csv('sales_data.csv')
sales_df_clean = sales_df.dropna()
top_products = sales_df_clean.groupby('Product')['Revenue'].sum().nlargest(5)

print(top_products)
        """)

    with st.expander("🧠 Quiz: Analytics Basics"):
        q = st.radio("Which analytics type forecasts future outcomes?", ["Descriptive", "Predictive", "Diagnostic"])
        if st.button("Submit", key="da_quiz_submit"):
            if q == "Predictive":
                st.success("✅ Correct! Predictive analytics forecasts future events.")
            else:
                st.error("❌ Incorrect. Try again.")

    st.markdown("📥 [Download Data Analytics Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))


# -------- EXCEL --------
def page_excel():
    st.title("📑 Microsoft Excel Essentials")
    st.video("https://www.youtube.com/watch?v=8cG-VeN94Og")

    st.markdown("""
    Excel empowers you to organize, calculate, and visualize data effectively.

    Key learning outcomes:
    - Master formulas like SUM, AVERAGE, IF, VLOOKUP, and INDEX-MATCH.
    - Create PivotTables and PivotCharts for summarizing data.
    - Automate tasks and create custom functions using Macros and VBA.
    - Tips for spreadsheet management and collaboration.
    """)

    with st.expander("💡 Why Excel is Important"):
        st.markdown("""
        Excel remains one of the most widely used tools for data analysis across industries due to its flexibility and ease of use. Whether for financial modeling, reporting, or data visualization, proficiency in Excel is invaluable.

        Through this course, you'll gain skills to use Excel as a powerful analytics tool.
        """)

    st.subheader("🔑 Key Features Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
    • Cell referencing and formulas  
    • Lookup functions: VLOOKUP & INDEX-MATCH  
    • Data validation and conditional formatting  
    • Working with tables and structured references  
    """)
    col2.markdown("""
    • PivotTables and slicers  
    • Charts and dashboards  
    • Introduction to Macros and VBA scripting  
    • Collaboration tools and workbook sharing  
    """)

    with st.expander("📚 Read More: PivotTables Explained"):
        st.markdown("""
        PivotTables help summarize large datasets with drag-and-drop ease. You learn to aggregate data by categories, filter, and analyze trends quickly.

        This feature amplifies Excel’s power in transforming raw data into meaningful summaries.
        """)

    with st.expander("🧠 Quiz: Excel Basics"):
        ans = st.radio("Which function is used for horizontal lookup?", ["VLOOKUP", "HLOOKUP", "INDEX"])
        if st.button("Submit", key="excel_quiz_submit"):
            if ans == "HLOOKUP":
                st.success("✅ Correct! HLOOKUP searches rows horizontally.")
            else:
                st.error("❌ Incorrect, try again.")

    st.markdown("📥 [Download Excel Cheat Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))


# --------------- PAGE ROUTING ---------------
if current_page == "home":
    page_home()
elif current_page == "data_science":
    page_data_science()
elif current_page == "data_analytics":
    page_data_analytics()
elif current_page == "excel":
    page_excel()
else:
    st.error("Page not found. Click below to return.")
    st.button("Home", on_click=lambda: go_to("home"))

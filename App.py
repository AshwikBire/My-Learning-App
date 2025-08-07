import streamlit as st

# LinkedIn profile link
LINKEDIN_URL = "https://linkedin.com/in/ashwik-bire-b2a000186"

# Configure page
st.set_page_config(page_title="Ultimate Learning App", page_icon=":mortar_board:", layout="wide")

# Sidebar Navigation
st.sidebar.title("Learn Dashboard")
page = st.sidebar.radio("Navigate", ["Home", "Data Science", "Data Analytics", "MS Excel", "About Me"])

def section_separator(text=""):
    st.markdown(f"---\n### {text}\n")

# ----- Home Page -----
def show_home():
    st.title("Welcome to the Ultimate Learning App :mortar_board:")
    st.write(
        """
        An interactive platform to learn:
        - **Data Science**
        - **Data Analytics**
        - **MS Excel**

        🎯 Designed for beginners to intermediate learners, with practical examples, quizzes, videos, and resources.
        """
    )
    st.image(
        "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1200&q=80",
        caption="Unlock Your Data Skills!",
        use_container_width=True,
    )
    col1, col2, col3 = st.columns(3)
    col1.metric("Lessons", "50+")
    col2.metric("Code Examples", "30+")
    col3.metric("Quizzes", "10+")
    section_separator("Getting Started")
    st.markdown(
        """
        Use the sidebar to explore topics. Take quizzes to test yourself and watch videos for deeper understanding.
        Download cheat sheets to keep handy.
        """
    )


# ----- Data Science Page -----
def show_data_science():
    st.title("Data Science Learning Path :bar_chart:")
    st.write("Data Science combines programming, statistics, and ML to extract insights and build predictive models.")

    with st.expander("📘 Introduction to Data Science"):
        st.markdown(
            """
            - What is Data Science?  
            - Data lifecycle: collection, cleaning, exploration, modeling, evaluation  
            - Tools: Python, Pandas, NumPy, Matplotlib, Scikit-learn  
            - Industry use cases: healthcare, finance, marketing, more  
            """
        )
        st.video("https://www.youtube.com/watch?v=ua-CiDNNj30")  # Intro video

    st.subheader("Core Topics")
    col1, col2 = st.columns(2)
    col1.markdown(
        """
        - Python essentials for DS: data types, functions, libraries  
        - Data manipulation with Pandas: filtering, grouping, aggregation  
        - Data visualization techniques using Matplotlib and Seaborn  
        """
    )
    col2.markdown(
        """
        - Statistical concepts: probability, distributions, hypothesis testing  
        - Machine learning basics: supervised and unsupervised learning  
        - Model evaluation metrics and avoiding overfitting  
        """
    )

    with st.expander("🤖 Machine Learning Fundamentals"):
        st.markdown(
            """
            - Supervised vs Unsupervised Learning  
            - Key algorithms: Linear Regression, Logistic Regression, Decision Trees, K-Means  
            - Evaluation metrics: accuracy, precision, recall, F1-score  
            """
        )
        st.video("https://www.youtube.com/watch?v=Gv9_4yMHFhI")  # ML basics video

    with st.expander("💻 Hands-on: Simple Linear Regression Example"):
        st.markdown("Predict salary based on years of experience using sklearn.")
        st.code(
            '''
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {'experience': [1,2,3,4,5], 'salary': [45000, 50000, 60000, 65000, 70000]}
df = pd.DataFrame(data)
X = df[['experience']]
y = df['salary']

model = LinearRegression()
model.fit(X, y)

predicted = model.predict([[6]])
print(f"Predicted salary: ${predicted[0]:.2f}")

plt.scatter(df['experience'], df['salary'], color='blue')
plt.plot(df['experience'], model.predict(X), color='red')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Experience')
plt.show()
            ''',
            language="python",
        )

    section_separator("Quiz: Test Your Knowledge")
    quiz_question = "What type of learning uses labeled data?"
    options = ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning"]
    answer = st.radio(quiz_question, options)
    if st.button("Submit Answer"):
        if answer == "Supervised Learning":
            st.success("Correct! Supervised learning uses labeled data.")
        else:
            st.error("Incorrect, please try again.")

    section_separator("Downloadable Cheat Sheet")
    st.markdown(
        "[Download Data Science Cheat Sheet (PDF)](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)"
    )

    section_separator("Recommended Resources")
    st.markdown(
        """
        - [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)  
        - [Kaggle Data Science Courses](https://www.kaggle.com/learn/data-science)  
        - [Coursera ML by Andrew Ng](https://www.coursera.org/learn/machine-learning)  
        """
    )


# ----- Data Analytics Page -----
def show_data_analytics():
    st.title("Data Analytics Learning Path :bar_chart:")
    st.write("Analyze data to extract actionable insights and support decision-making.")

    with st.expander("🔎 Analytics Fundamentals"):
        st.markdown(
            """
            - Types: Descriptive, Diagnostic, Predictive, Prescriptive Analytics  
            - Data cleaning, validation, and handling missing values  
            - Identifying trends, patterns, and outliers  
            """
        )
        st.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")  # Analytics intro

    st.subheader("Tools & Techniques")
    col1, col2 = st.columns(2)
    col1.markdown(
        """
        - Excel pivot tables and charts  
        - SQL basics for querying  
        - Tableau and Power BI introduction  
        """
    )
    col2.markdown(
        """
        - Data visualization best practices  
        - Using Pandas and Matplotlib for analytics in Python  
        """
    )

    with st.expander("📊 Example: Sales Data Analysis"):
        st.write(
            """
            Project outline:
            1. Load sales CSV data into Pandas  
            2. Clean and filter for top products  
            3. Create charts to visualize trends  
            """
        )
        st.code(
            '''
import pandas as pd

sales_df = pd.read_csv("sales_data.csv")
sales_df = sales_df.dropna()
top_products = sales_df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(10)
print(top_products)
# Visualization here
            ''',
            language="python",
        )

    section_separator("Quiz: Data Analytics Basics")
    quiz_question = "Which type of analytics focuses on predicting future events?"
    options = ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"]
    answer = st.radio(quiz_question, options, key="analytics_quiz")
    if st.button("Submit Answer", key="analytics_submit"):
        if answer == "Predictive":
            st.success("Correct! Predictive analytics forecasts future trends.")
        else:
            st.error("Incorrect, try again.")

    section_separator("Downloadable Resources")
    st.markdown(
        "[Data Analytics Cheat Sheet PDF](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)"
    )

    section_separator("Recommended Resources")
    st.markdown(
        """
        - [DataCamp Analytics Track](https://www.datacamp.com/tracks/data-analyst-with-python)  
        - [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)  
        - [Tableau Training Videos](https://www.tableau.com/learn/training)  
        """
    )


# ----- MS Excel Page -----
def show_ms_excel():
    st.title("Master Microsoft Excel :computer:")
    st.write("Excel is a versatile tool for data entry, analysis, visualization, and automation.")

    with st.expander("📄 Excel Basics"):
        st.markdown(
            """
            - Cells, rows, columns, and ranges  
            - SUM, AVERAGE, IF, CONCATENATE formulas  
            - Formatting, sorting, filtering data  
            """
        )
        st.video("https://www.youtube.com/watch?v=8cG-VeN94Og")  # Excel basics video

    with st.expander("⚙️ Advanced Excel Functions"):
        st.markdown(
            """
            - VLOOKUP, HLOOKUP, INDEX-MATCH  
            - Pivot tables and charts  
            - Conditional formatting and macros introduction  
            """
        )
        st.video("https://www.youtube.com/watch?v=RZP_iO3Kg_M")  # Excel advanced video

    with st.expander("📊 Example: Create a Sales Dashboard"):
        st.markdown(
            """
            Use pivot tables, slicers, and charts to create interactive dashboards filtering by region/time.
            """
        )
    
    col1, col2 = st.columns(2)
    col1.markdown(
        """
        **Efficiency Tips**  
        - Keyboard shortcuts  
        - Format Painter  
        - Named ranges  
        """
    )
    col2.markdown(
        """
        **Best Practices**  
        - Document complex formulas  
        - Use data validation  
        - Regular backups  
        """
    )

    section_separator("Quiz: Excel Formulas")
    quiz_question = "Which formula is used to look up a value horizontally?"
    options = ["VLOOKUP", "HLOOKUP", "INDEX", "MATCH"]
    answer = st.radio(quiz_question, options, key="excel_quiz")
    if st.button("Submit Answer", key="excel_submit"):
        if answer == "HLOOKUP":
            st.success("Correct! HLOOKUP looks up values horizontally.")
        else:
            st.error("Incorrect, please try again.")

    section_separator("Downloadable Resources")
    st.markdown(
        "[Excel Cheat Sheet PDF](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)"
    )

    section_separator("Recommended Resources")
    st.markdown(
        """
        - [Excel Easy Tutorials](https://www.excel-easy.com/)  
        - [Microsoft Excel Help](https://support.microsoft.com/en-us/excel)  
        - [Chandoo.org Excel Training](https://chandoo.org/wp/excel-school/)  
        """
    )


# ----- About Me Page -----
def show_about_me():
    st.title("About Me - Ashwik Bire :wave:")
    st.image(
        'https://media-exp1.licdn.com/dms/image/C5603AQF2VaANkGzA4w/profile-displayphoto-shrink_200_200/0/1617010101937?e=2147483647&v=beta&t=example',
        width=150,
        use_container_width=False
    )
    st.markdown(
        """
        Hi, I'm **Ashwik Bire**, passionate about data science and analytics education.  
        I focus on making complex topics approachable through hands-on learning.  
        """
    )
    st.markdown(f"### Connect with me on [LinkedIn]({LINKEDIN_URL}) :link:")
    st.write(
        """
        Reach out for mentorship, collaborations, or questions related to data science, analytics, or Excel.
        """
    )


# Page routing
if page == "Home":
    show_home()
elif page == "Data Science":
    show_data_science()
elif page == "Data Analytics":
    show_data_analytics()
elif page == "MS Excel":
    show_ms_excel()
elif page == "About Me":
    show_about_me()

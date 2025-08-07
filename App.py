import streamlit as st

# LinkedIn profile link
LINKEDIN_URL = "https://linkedin.com/in/ashwik-bire-b2a000186"

# Configure page
st.set_page_config(page_title="Ultimate Learning App", page_icon=":mortar_board:", layout="wide")

# Sidebar Navigation
st.sidebar.title("Learn Dashboard")
page = st.sidebar.radio("Navigate", ["Home", "Data Science", "Data Analytics", "MS Excel", "About Me"])

# Helper to display horizontal separator with text
def section_separator(text=""):
    st.markdown(f"---\n### {text}\n")

# Home Page
def show_home():
    st.title("Welcome to the Ultimate Learning App :mortar_board:")
    st.write(
        """
        This interactive learning platform covers comprehensive materials on:
        - **Data Science**
        - **Data Analytics**
        - **MS Excel**
        
        🎯 Designed for beginners to intermediate learners aiming to build skills with practical examples.
        
        Use the sidebar menu to navigate between different topics.
        """
    )
    st.image(
        "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1200&q=80",
        caption="Unlock Your Data Skills!",
        use_container_width=True,
    )
    # Quick stats or learning highlights - use columns
    col1, col2, col3 = st.columns(3)
    col1.metric("Lessons", "40+")
    col2.metric("Code Examples", "25+")
    col3.metric("Projects", "5+")
    section_separator("Getting Started")
    st.markdown(
        """
        This app will guide you through fundamentals and beyond, with examples and exercises.
        Explore the Data Science, Data Analytics, and MS Excel sections to dive in.
        """
    )

# Data Science Page
def show_data_science():
    st.title("Data Science Learning Path :bar_chart:")

    st.write(
        """
        Data Science blends programming, stats, and ML to extract insights and build predictive models.
        """
    )
    
    # Introduction
    with st.expander("📘 Introduction to Data Science"):
        st.markdown(
            """
            - What is Data Science?  
            - Lifecycle: Data collection, cleaning, exploration, modeling, evaluation.
            - Tools: Python, Jupyter, Pandas, NumPy, Matplotlib, Scikit-learn.
            - Use cases in industries like healthcare, finance, marketing.
            """
        )
    
    # Detailed topics with columns
    st.subheader("Core Topics Covered")
    col1, col2 = st.columns(2)
    col1.markdown(
        """
        - **Python Essentials for DS**  
          Data structures, functions, libraries.

        - **Data Manipulation with Pandas**  
          Series, DataFrames, filtering, grouping, aggregation.
        """
    )
    col2.markdown(
        """
        - **Data Visualization**  
          Matplotlib, Seaborn basics, plots, customization.

        - **Statistical Concepts**  
          Probability, distributions, hypothesis testing.
        """
    )
    
    # Machine Learning basics
    with st.expander("🤖 Machine Learning Fundamentals"):
        st.markdown(
            """
            - Supervised vs Unsupervised Learning  
            - Common algorithms: Linear Regression, Logistic Regression, Decision Trees, K-Means.  
            - Model evaluation: Accuracy, Precision, Recall, F1-score.  
            - Overfitting, Underfitting concepts.  
            """
        )
    
    # Hands-on example
    with st.expander("💻 Hands-on: Simple Linear Regression Example"):
        st.markdown(
            """
            We will predict salary based on years of experience using sklearn.
            """
        )
        st.code(
            '''
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset
data = {'experience': [1,2,3,4,5], 'salary': [45000, 50000, 60000, 65000, 70000]}
df = pd.DataFrame(data)

X = df[['experience']]
y = df['salary']

# Model training
model = LinearRegression()
model.fit(X, y)

# Prediction for 6 years experience
predicted = model.predict([[6]])
print(f"Predicted salary: ${predicted[0]:.2f}")

# Visualization
plt.scatter(df['experience'], df['salary'], color='blue')
plt.plot(df['experience'], model.predict(X), color='red')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Experience')
plt.show()
            ''',
            language="python",
        )
    
    # Recommended resources
    section_separator("Recommended Resources")
    st.markdown(
        """
        - [Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
        - [Kaggle Data Science Courses](https://www.kaggle.com/learn/data-science)
        - [Coursera Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning)
        """
    )

# Data Analytics Page
def show_data_analytics():
    st.title("Data Analytics Learning Path :bar_chart:")

    st.write(
        """
        Data Analytics focuses on processing and analyzing datasets to extract actionable insights.
        """
    )
    
    # Fundamentals
    with st.expander("🔎 Analytics Fundamentals"):
        st.markdown(
            """
            - Descriptive, Diagnostic, Predictive, Prescriptive Analytics  
            - Data cleaning, validation, handling missing data  
            - Identifying trends, outliers, and patterns  
            """
        )

    # Tools and Techniques
    st.subheader("Tools & Techniques")
    col1, col2 = st.columns(2)
    col1.markdown(
        """
        - Excel Pivot Tables & Charts  
        - SQL Querying Basics  
        - Tableau and Power BI Overview  
        """
    )
    col2.markdown(
        """
        - Data visualization best practices  
        - Using Python libraries like Pandas and Matplotlib for analytics  
        """
    )

    # Example project
    with st.expander("📊 Example: Sales Data Analysis"):
        st.write(
            """
            Here’s a simplistic outline of a sales data analytics project:
            1. Load sales CSV data into Pandas.
            2. Clean and filter data for top performing products.
            3. Create relevant charts and insights for decision making.
            """
        )
        st.code(
            '''
import pandas as pd

# Load dataset
sales_df = pd.read_csv("sales_data.csv")

# Data Cleaning
sales_df = sales_df.dropna()
top_products = sales_df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(10)

print(top_products)
# Visualization and reporting goes here
            ''',
            language="python",
        )
        
    # Additional Resources
    section_separator("Recommended Resources")
    st.markdown(
        """
        - [DataCamp Data Analytics Track](https://www.datacamp.com/tracks/data-analyst-with-python)
        - [SQL Tutorial](https://www.w3schools.com/sql/)
        - [Tableau Free Training Videos](https://www.tableau.com/learn/training)
        """
    )

# MS Excel Page
def show_ms_excel():
    st.title("Master Microsoft Excel :computer:")

    st.write(
        """
        Excel is a versatile tool for data entry, analysis, visualization, and automation.
        """
    )
    
    # Basics
    with st.expander("📄 Excel Basics"):
        st.markdown(
            """
            - Understanding cells, rows, columns, and ranges  
            - Common formulas: SUM, AVERAGE, IF, CONCATENATE  
            - Cell formatting, data sorting, filtering  
            """
        )

    # Advanced formulas and features
    with st.expander("⚙️ Advanced Excel Functions"):
        st.markdown(
            """
            - Lookup functions: VLOOKUP, HLOOKUP, INDEX-MATCH  
            - Pivot tables and dynamic charts  
            - Conditional formatting to highlight data  
            - Introduction to Macros and VBA scripting basics  
            """
        )

    # Practical example
    with st.expander("📊 Example: Build a Sales Dashboard"):
        st.markdown(
            """
            Combine pivot tables, slicers, and charts to create interactive data dashboards.
            Use slicers to filter sales by regions or time periods for dynamic insights.
            """
        )
    
    # Excel tips with columns for clarity
    col1, col2 = st.columns(2)
    col1.markdown(
        """
        **Tips for Efficiency:**  
        - Use keyboard shortcuts  
        - Format Painter  
        - Named ranges  
        """
    )
    col2.markdown(
        """
        **Best Practices:**  
        - Document complex formulas  
        - Use data validation  
        - Backup your workbook regularly  
        """
    )

    # Additional resources
    section_separator("Recommended Resources")
    st.markdown(
        """
        - [Excel Easy Tutorials](https://www.excel-easy.com/)  
        - [Microsoft Excel Help & Learning](https://support.microsoft.com/en-us/excel)  
        - [Chandoo.org Excel Training](https://chandoo.org/wp/excel-school/)  
        """
    )

# About Me Page
def show_about_me():
    st.title("About Me - Ashwik Bire :wave:")
    st.image(
        'https://media-exp1.licdn.com/dms/image/C5603AQF2VaANkGzA4w/profile-displayphoto-shrink_200_200/0/1617010101937?e=2147483647&v=beta&t=example',
        width=150,
        use_container_width=False  # optional for profile image, image fits well by default
    )
    st.markdown(
        """
        Hi, I'm **Ashwik Bire**, a passionate data scientist and analytics enthusiast dedicated to empowering others
        through knowledge and hands-on learning.  
        
        I specialize in making complex topics accessible and practical.
        """
    )
    st.markdown(f"### Connect with me on [LinkedIn]({LINKEDIN_URL}) :link:")
    st.write(
        """
        Feel free to reach out for collaborations, mentorship, or queries related to data science and analytics.
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

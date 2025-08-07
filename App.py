import streamlit as st

# LinkedIn profile link
LINKEDIN_URL = "https://linkedin.com/in/ashwik-bire-b2a000186"

# App Title and icon
st.set_page_config(page_title="Learn Data Science & Analytics", page_icon=":bar_chart:", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Science", "Data Analytics", "MS Excel", "About Me"])

def show_home():
    st.title("Welcome to the Ultimate Learning App")
    st.markdown("""
    This app provides curated learning materials for:
    - **Data Science**
    - **Data Analytics**
    - **MS Excel**

    Use the sidebar to navigate through different topics.
    """)
    st.image("https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=60",
             caption="Learn and grow your skills!", use_column_width=True)

def show_data_science():
    st.title("Data Science Learning Materials")
    st.markdown("""
    Data Science is the field of using data analysis, machine learning, statistics, and programming
    to extract insights and build models.
    """)
    with st.expander("Introduction to Data Science"):
        st.write("""
        - Understand the data science process.
        - Learn key Python libraries: NumPy, pandas, matplotlib, scikit-learn.
        - Explore datasets and basic statistics.
        """)
    with st.expander("Machine Learning Basics"):
        st.write("""
        - Supervised vs unsupervised learning.
        - Algorithms like linear regression, decision trees.
        - Building and evaluating models.
        """)
    with st.expander("Hands-on Coding Example"):
        st.code('''
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {'experience': [1,2,3,4,5], 'salary': [45000, 50000, 60000, 65000, 70000]}
df = pd.DataFrame(data)

X = df[['experience']]
y = df['salary']

model = LinearRegression()
model.fit(X, y)
predicted = model.predict([[6]])
print(f"Predicted salary for 6 years experience: ${predicted[0]:.2f}")
        ''', language='python')

def show_data_analytics():
    st.title("Data Analytics Learning Materials")
    st.markdown("""
    Data Analytics focuses on analyzing data to find meaningful patterns and support decision-making.
    """)
    with st.expander("Data Analytics Fundamentals"):
        st.write("""
        - Types of analytics: descriptive, diagnostic, predictive, prescriptive.
        - Data cleaning and preparation.
        - Visualization basics.
        """)
    with st.expander("Popular Tools & Techniques"):
        st.write("""
        - Excel pivot tables, charts.
        - SQL querying basics.
        - Introduction to Tableau and Power BI.
        """)
    with st.expander("Example: Analyzing Sales Data"):
        st.code('''
# Pseudocode example
# 1. Load sales data
# 2. Clean and filter top performing products
# 3. Create visual summaries and insights
        ''')

def show_ms_excel():
    st.title("Master MS Excel")
    st.markdown("""
    Excel is a powerful tool for data organization, analysis, and visualization.
    """)
    with st.expander("Excel Basics"):
        st.write("""
        - Understand cells, ranges, formulas.
        - Use essential functions like SUM, AVERAGE, IF.
        - Formatting and data validation.
        """)
    with st.expander("Advanced Functions"):
        st.write("""
        - VLOOKUP, INDEX-MATCH
        - Pivot tables and charts
        - Conditional formatting and macros intro
        """)
    with st.expander("Example: Create Sales Dashboard"):
        st.write("Combine pivot tables, charts, and slicers to build interactive dashboards.")

def show_about_me():
    st.title("About Me - Ashwik Bire")
    st.markdown("""
    Hi, I am Ashwik Bire, passionate about data science, analytics, and empowering learners.
    Connect with me on LinkedIn for more updates and projects.
    """)
    st.markdown(f"[LinkedIn Profile]({LINKEDIN_URL})")
    st.image('https://media-exp1.licdn.com/dms/image/C5603AQF2VaANkGzA4w/profile-displayphoto-shrink_200_200/0/1617010101937?e=2147483647&v=beta&t=example', width=150)
    st.write("Feel free to reach out!")

# Route the pages
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

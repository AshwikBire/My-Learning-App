import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# Get current page (defaults to 'home')
query_params = st.query_params
current_page = query_params.get("page", "home")

# Navigation Helper
def go_to(page):
    st.query_params.page = page

def section_header(title):
    st.markdown(f"<h2 style='color:#005B96; border-bottom: 2px solid #005B96; padding-bottom:8px;'>{title}</h2>", unsafe_allow_html=True)

def card_button(label, key, callback):
    """Render a big button with card-like style."""
    style = """
        <style>
        .stButton>button {
            background-color: #0078D4;
            color: white;
            height: 4rem;
            width: 100%;
            border-radius: 8px;
            font-size: 1.2rem;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #005A9E;
            color: #E1EFFE;
        }
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)
    st.button(label, key=key, on_click=callback)

def box_highlight(content):
    st.markdown(f"""
    <div style="background-color:#E6F0FA; padding:10px 15px; border-radius:10px; margin-bottom:15px;">
    {content}
    </div>
    """, unsafe_allow_html=True)


# ------------------- Pages -------------------

# -------- HOME --------
def page_home():
    section_header("Welcome to Data Science & Analytics with Ashwik Bire")

    st.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)

    st.markdown("<p style='font-size:1.1rem;'>Select a learning path from the options below to get started. Each path includes detailed tutorials, quizzes, and resources.</p>", unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5, gap="large")
    with col1:
        card_button("Data Science", "btn_ds", lambda: go_to("data_science"))
    with col2:
        card_button("Data Analytics", "btn_da", lambda: go_to("data_analytics"))
    with col3:
        card_button("Microsoft Excel", "btn_excel", lambda: go_to("excel"))
    with col4:
        card_button("Power BI", "btn_pbi", lambda: go_to("power_bi"))
    with col5:
        card_button("Artificial Intelligence", "btn_ai", lambda: go_to("ai"))

    st.divider()

    section_header("Featured Tutorials")

    col_a, col_b, col_c, col_d, col_e = st.columns(5, gap="medium")
    col_a.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")
    col_b.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")
    col_c.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")
    col_d.video("https://www.youtube.com/watch?v=AGrl-H87pRU")
    col_e.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")

    st.divider()

    st.markdown("<p style='font-size:1.1rem; font-weight:bold;'>Connect with Ashwik Bire on <a href='https://linkedin.com/in/ashwik-bire-b2a000186' target='_blank' style='color:#0078D4;'>LinkedIn</a> for updates and mentorship.</p>", unsafe_allow_html=True)

# -------- DATA SCIENCE --------
def page_data_science():
    section_header("Data Science Learning")

    st.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")

    intro_text = """
    <p style='font-size:1.1rem;'>Data Science unlocks insights from complex data by using statistics, programming, and algorithms. Key pathways in this domain include data cleaning, visualization, machine learning, and data engineering.</p>
    """
    st.markdown(intro_text, unsafe_allow_html=True)

    with st.expander("Why Data Science?"):
        st.markdown("""
        Data science enables data-driven decision-making, powering innovation and competitive advantages worldwide.
        Understand how data is collected, cleaned, analyzed, and modeled in real-world applications.
        """)

    st.subheader("Concepts Covered")
    col1, col2 = st.columns(2, gap="large")
    col1.markdown("""
    - Python & Jupyter basics  
    - Data manipulation with Pandas  
    - Data visualization (Matplotlib, Seaborn)  
    - Intro to statistics & probability  
    - Data wrangling & cleaning  
    """)
    col2.markdown("""
    - Machine Learning fundamentals  
    - Regression, classification, clustering  
    - Model validation and tuning  
    - Ethics in AI & data science  
    - Big Data tools overview  
    """)

    with st.expander("Read More: Core Python for Data Science"):
        st.markdown("""
        Python is popular for data science due to its simplicity and powerful libraries. Master lists, dictionaries, and Pandas functions for effective data operations.
        """)

    with st.expander("Read More: Data Visualization Best Practices"):
        st.markdown("""
        Visualizing data helps communicate findings. Learn to choose the right chart, colors, and annotations to convey your insights clearly.
        """)

    with st.expander("Example: Linear Regression in Python"):
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

    with st.expander("Read More: Machine Learning Workflow"):
        st.markdown("""
        Explore the complete ML workflow: data preprocessing, model selection, training, evaluation, and deployment for real-world results.
        """)

    box_highlight("<b>Quiz:</b> Which machine learning approach uses labeled training data?")
    answer = st.radio("", ["Unsupervised", "Supervised", "Reinforcement"], key="ds_quiz", horizontal=True)
    if st.button("Submit Answer", key="ds_submit"):
        if answer == "Supervised":
            st.success("Correct! Supervised learning uses labeled data.")
        else:
            st.error("Incorrect, please try again.")

    st.markdown("[Download Data Science Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")

    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)


# -------- DATA ANALYTICS --------
def page_data_analytics():
    section_header("Data Analytics Curriculum")
    st.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")

    intro_text = """
    <p style='font-size:1.1rem;'>Data Analytics transforms raw information into actionable insights through cleaning, visualization, and summarization using SQL, Python, and BI tools.</p>
    """
    st.markdown(intro_text, unsafe_allow_html=True)

    with st.expander("Importance of Data Analytics"):
        st.markdown("""
        Data analytics drives smarter business decisions by uncovering trends, quality issues, and forecasting.
        """)

    st.subheader("Topics Covered")
    col1, col2 = st.columns(2, gap="large")
    col1.markdown("""
    - Descriptive, diagnostic, predictive, prescriptive analytics  
    - Exploratory data analysis (EDA)  
    - Data visualization best practices  
    - SQL querying fundamentals  
    - Data quality and cleaning  
    """)
    col2.markdown("""
    - Power BI/Tableau dashboards  
    - Python (Pandas, Seaborn) tools  
    - Statistical inference basics  
    - Data storytelling and presentation  
    """)

    with st.expander("Read More: Power BI Fundamentals"):
        st.markdown("""
        Power BI simplifies connections to diverse data, allowing transformation, modeling, and interactive report generation.
        """)

    with st.expander("Example: Sales Data Analysis Code"):
        st.code("""
import pandas as pd

sales_df = pd.read_csv('sales_data.csv')
sales_df_clean = sales_df.dropna()
top_products = sales_df_clean.groupby('Product')['Revenue'].sum().nlargest(5)

print(top_products)
        """)

    box_highlight("<b>Quiz:</b> Which analytics type forecasts future outcomes?")
    q = st.radio("", ["Descriptive", "Predictive", "Diagnostic"], key="da_quiz", horizontal=True)
    if st.button("Submit Answer", key="da_submit"):
        if q == "Predictive":
            st.success("Correct! Predictive analytics forecasts future events.")
        else:
            st.error("Incorrect, please try again.")

    st.markdown("[Download Data Analytics Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")

    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)


# -------- EXCEL --------
def page_excel():
    section_header("Microsoft Excel Essentials")
    st.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")

    intro_text = """
    <p style='font-size:1.1rem;'>Excel allows you to organize, calculate, and visualize data with formulas, PivotTables, charts, and automation tools.</p>
    """
    st.markdown(intro_text, unsafe_allow_html=True)

    with st.expander("Why Excel is Important"):
        st.markdown("""
        Excel is ubiquitous in business analytics, finance, and reporting, making mastery highly valuable.
        """)

    st.subheader("Key Features Covered")
    col1, col2 = st.columns(2, gap="large")
    col1.markdown("""
    - Cell referencing and formulas  
    - Lookup functions: VLOOKUP & INDEX-MATCH  
    - Data validation and conditional formatting  
    - Tables and structured references  
    """)
    col2.markdown("""
    - PivotTables and slicers  
    - Charts and dashboards  
    - Macros and VBA scripting basics  
    - Collaboration and sharing  
    """)

    with st.expander("Read More: PivotTables Explained"):
        st.markdown("""
        PivotTables let you dynamically summarize and explore large datasets with interactive filtering and grouping.
        """)

    box_highlight("<b>Quiz:</b> Which function is used for horizontal lookup?")
    ans = st.radio("", ["VLOOKUP", "HLOOKUP", "INDEX"], key="excel_quiz", horizontal=True)
    if st.button("Submit Answer", key="excel_submit"):
        if ans == "HLOOKUP":
            st.success("Correct! HLOOKUP searches horizontally across rows.")
        else:
            st.error("Incorrect, please try again.")

    st.markdown("[Download Excel Cheat Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")

    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)


# -------- POWER BI --------
def page_power_bi():
    section_header("Microsoft Power BI Fundamentals")
    st.video("https://www.youtube.com/watch?v=AGrl-H87pRU")

    intro_text = """
    <p style='font-size:1.1rem;'>Power BI enables interactive data visualizations and business intelligence capabilities with ease, suitable for users at all levels.</p>
    """
    st.markdown(intro_text, unsafe_allow_html=True)

    with st.expander("Why Learn Power BI?"):
        st.markdown("""
        Power BI bridges the gap between data and business insights by simplifying report creation, sharing, and collaboration.
        """)

    st.subheader("Key Features Covered")
    col1, col2 = st.columns(2, gap="large")
    col1.markdown("""
    - Power BI Desktop overview  
    - Connecting to multiple data sources  
    - Data transformation with Power Query  
    - Creating and customizing visuals  
    """)
    col2.markdown("""
    - Using DAX for analytics calculations  
    - Designing interactive dashboards  
    - Publishing and sharing reports  
    - Collaboration features  
    """)

    with st.expander("Read More: Introduction to Power Query"):
        st.markdown("""
        Power Query allows easy data import and transformation from diverse sources without complex coding.
        """)

    box_highlight("<b>Quiz:</b> Which Power BI component hosts reports for sharing?")
    ans = st.radio("", ["Power BI Desktop", "Power BI Service", "Power Query"], key="pbi_quiz", horizontal=True)
    if st.button("Submit Answer", key="pbi_submit"):
        if ans == "Power BI Service":
            st.success("Correct! Power BI Service is the cloud platform for sharing reports.")
        else:
            st.error("Incorrect, please try again.")

    st.markdown("[Download Power BI Guide](https://docs.microsoft.com/en-us/power-bi/guided-learning/power-bi-learning-guide)")

    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)


# -------- ARTIFICIAL INTELLIGENCE --------
def page_ai():
    section_header("Artificial Intelligence Fundamentals")
    st.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")

    intro_text = """
    <p style='font-size:1.1rem;'>Artificial Intelligence (AI) enables machines to perform tasks that typically require human intelligence, including problem-solving, perception, and decision-making.</p>
    """
    st.markdown(intro_text, unsafe_allow_html=True)

    with st.expander("Why Learn AI?"):
        st.markdown("""
        AI is revolutionizing industries by automating processes and enhancing decision-making. This course provides a foundation in AI concepts and practical applications.
        """)

    st.subheader("Topics Covered")
    st.markdown("""
    - History and foundations of AI  
    - Machine Learning: supervised, unsupervised, reinforcement learning  
    - Neural networks and deep learning basics  
    - Natural Language Processing fundamentals  
    - AI ethics and societal considerations  
    """)

    with st.expander("Read More: Neural Networks Explained"):
        st.markdown("""
        Neural networks, inspired by biological brains, form the backbone of many AI applications. Understanding their layers and training mechanisms is key to mastering deep learning.
        """)

    box_highlight("<b>Quiz:</b> Which AI technique learns from labeled datasets?")
    ans = st.radio("", ["Reinforcement Learning", "Unsupervised Learning", "Supervised Learning"], key="ai_quiz", horizontal=True)
    if st.button("Submit Answer", key="ai_submit"):
        if ans == "Supervised Learning":
            st.success("Correct! Supervised learning requires labeled data.")
        else:
            st.error("Incorrect, please try again.")

    st.markdown("[Download AI Fundamentals Guide](https://ai.google/education/)")

    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)


# --------------- PAGE ROUTING ---------------
if current_page == "home":
    page_home()
elif current_page == "data_science":
    page_data_science()
elif current_page == "data_analytics":
    page_data_analytics()
elif current_page == "excel":
    page_excel()
elif current_page == "power_bi":
    page_power_bi()
elif current_page == "ai":
    page_ai()
else:
    st.error("Page not found. Click below to return.")
    st.button("Back to Home", on_click=lambda: go_to("home"))

import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# Custom CSS for dark translucent dev-style look and advanced button UI
custom_css = """
<style>
    /* Background with subtle cubes pattern and dark translucent overlay */
    .stApp {
        background: 
          linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)),
          url('https://www.transparenttextures.com/patterns/cubes.png');
        background-repeat: repeat;
        background-size: 80px 80px;
        color: #c8d6e5;
    }

    /* Content boxes transparency and rounded corners */
    .css-1d391kg, .css-1d391kg {
        background-color: rgba(24,25,29,0.75) !important;
        border-radius: 12px !important;
    }

    /* Heading colors */
    h1, h2, h3, h4 {
        color: #81ecec !important;
    }

    /* Styled links */
    a { 
        color: #00cec9 !important; 
        text-decoration: underline; 
    }

    /* Advanced styled large navigation buttons */
    .nav-button > button {
        background-color: #0984e3 !important;
        color: white !important;
        border-radius: 15px !important;
        font-size: 1.4rem !important;
        font-weight: 700;
        padding: 1.2rem 1rem !important;
        width: 100%;
        box-shadow: 0 4px 15px 0 #00cec955;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }
    .nav-button > button:hover {
        background-color: #74b9ff !important;
        color: #2d3436 !important;
        box-shadow: 0 8px 30px 0 #00cec997;
    }
    .nav-button > button:focus {
        outline: none !important;
        box-shadow: 0 0 0 3px #55efc4 !important;
    }

    /* Radio buttons and inputs style */
    div[role="radiogroup"] > label {
        color: #dfe6e9 !important;
    }

    /* Expander header style */
    .streamlit-expanderHeader {
        background-color: rgba(12,13,17,0.6) !important;
        border-radius: 8px !important;
        color: #55efc4 !important;
        font-weight: 600 !important;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Get current page (defaults to 'home')
query_params = st.query_params
current_page = query_params.get("page", "home")

# Navigation Helper
def go_to(page):
    st.query_params.page = page

def section_header(title):
    st.markdown(f"<h2 style='color:#81ecec; border-bottom: 2px solid #00cec9; padding-bottom:8px;'>{title}</h2>", unsafe_allow_html=True)

def board_button(label, key, callback):
    """Render a large full-width card-style button for navigation."""
    container = st.container()
    with container:
        st.markdown(
            f"""
            <div class="nav-button">
                <button type="button" onclick="()">{label}</button>
            </div>
            """, unsafe_allow_html=True
        )
        # Use a real Streamlit button overlaid for actual click listener with same label appearance but invisible
        # This is a hack to get styled button and functional Streamlit button
        clicked = st.button(label, key=key, on_click=callback)
    return clicked

# Implementation note: Streamlit doesn't allow fully custom buttons with click handlers outside normal buttons.
# So we style normal buttons. We'll just use normal buttons but with CSS class styling via container usage.
# For this, inject class on the button directly via markdown hack not fully feasible.
# Instead, style all buttons in the .nav-button class and put Streamlit buttons inside their own columns.

# We'll style each button inside a column with class NavButton applied.
# So for real usability and consistent styling, buttons are created inside columns with the CSS applied for class nav-button.

# We'll implement below by placing buttons inside columns and applying CSS styles for .stButton>button selector
# (already done above), and use column-based layout with large width buttons.

# ------------------- Pages -------------------

# -------- HOME --------
def page_home():
    section_header("Welcome to Data Science & Analytics with Ashwik Bire")

    st.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)

    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Select a learning path from the options below to get started. Each path includes detailed tutorials, quizzes, and resources.</p>", unsafe_allow_html=True)

    cols = st.columns(5, gap="large")
    pages = [
        ("Data Science", "data_science"),
        ("Data Analytics", "data_analytics"),
        ("Microsoft Excel", "excel"),
        ("Power BI", "power_bi"),
        ("Artificial Intelligence", "ai")
    ]
    for col, (label, page_key) in zip(cols, pages):
        with col:
            st.button(label, key=f"btn_{page_key}", on_click=lambda p=page_key: go_to(p), help=f"Go to {label} page", use_container_width=True)

    st.divider()
    section_header("Featured Tutorials")

    col_a, col_b, col_c, col_d, col_e = st.columns(5, gap="medium")
    col_a.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")
    col_b.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")
    col_c.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")
    col_d.video("https://www.youtube.com/watch?v=AGrl-H87pRU")
    col_e.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")

    st.divider()
    st.markdown("<p style='font-size:1.1rem; font-weight:bold; color:#55efc4;'>Connect with Ashwik Bire on <a href='https://linkedin.com/in/ashwik-bire-b2a000186' target='_blank' style='color:#00cec9;'>LinkedIn</a> for updates and mentorship.</p>", unsafe_allow_html=True)


# -------- DATA SCIENCE --------
def page_data_science():
    section_header("Data Science Learning")

    st.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")

    st.markdown("""
    <p style='font-size:1.1rem; color:#dfe6e9;'>Data Science unlocks insights from complex data by using statistics, programming, and algorithms. Key pathways include data cleaning, visualization, machine learning, and data engineering.</p>
    """, unsafe_allow_html=True)

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
        Python is the most popular language in data science because of its readability and powerful libraries. Master lists, dictionaries, and Pandas functions for effective data operations.
        """)

    with st.expander("Read More: Data Visualization Best Practices"):
        st.markdown("""
        Visualizing data helps communicate findings clearly. Learn chart choices, colors, and annotations for impactful storytelling.
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
        Learn full ML pipeline: preprocessing, model training, evaluation, and deployment.
        """)

    quiz_question = "<b>Quiz:</b> Which machine learning approach uses labeled training data?"
    st.markdown(quiz_question, unsafe_allow_html=True)
    answer = st.radio("", ["Unsupervised", "Supervised", "Reinforcement"], key="ds_quiz", horizontal=True)
    if st.button("Submit Answer", key="ds_submit"):
        if answer == "Supervised":
            st.success("Correct! Supervised learning uses labeled data.")
        else:
            st.error("Incorrect, try again.")

    st.markdown("[Download Data Science Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")

    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)


# -------- DATA ANALYTICS --------
def page_data_analytics():
    section_header("Data Analytics Curriculum")
    st.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")

    st.markdown("""
    <p style='font-size:1.1rem; color:#dfe6e9;'>Data Analytics transforms raw information into actionable insights through cleaning, visualization, and summarization using SQL, Python, and BI tools.</p>
    """, unsafe_allow_html=True)

    with st.expander("Importance of Data Analytics"):
        st.markdown("""
        Data analytics drives smarter business decisions by uncovering trends and forecasting.
        """)

    st.subheader("Topics Covered")
    col1, col2 = st.columns(2, gap="large")
    col1.markdown("""
    - Descriptive, diagnostic, predictive, prescriptive analytics  
    - Exploratory data analysis (EDA)  
    - Data visualization best practices  
    - SQL fundamentals  
    - Data quality and cleaning  
    """)
    col2.markdown("""
    - Power BI and Tableau dashboards  
    - Python tools (Pandas, Seaborn)  
    - Stats inference fundamentals  
    - Data storytelling presentation  
    """)

    with st.expander("Read More: Power BI Fundamentals"):
        st.markdown("""
        Power BI transforms and visualizes data for interactive business analysis.
        """)

    with st.expander("Example: Sales Data Analysis Code"):
        st.code("""
import pandas as pd

sales_df = pd.read_csv('sales_data.csv')
sales_df_clean = sales_df.dropna()
top_products = sales_df_clean.groupby('Product')['Revenue'].sum().nlargest(5)

print(top_products)
        """)

    quiz_label = "<b>Quiz:</b> Which analytics type forecasts future outcomes?"
    st.markdown(quiz_label, unsafe_allow_html=True)
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

    st.markdown("""
    <p style='font-size:1.1rem; color:#dfe6e9;'>Excel lets you analyze and visualize data with formulas, PivotTables, charts, and more.</p>
    """, unsafe_allow_html=True)

    st.subheader("Key Features Covered")
    col1, col2 = st.columns(2, gap="large")
    col1.markdown("""
    - Formulas, referencing  
    - Lookup functions: VLOOKUP & INDEX-MATCH  
    - Validation and formatting  
    """)
    col2.markdown("""
    - PivotTables and slicers  
    - Charts and dashboards  
    - Macros and VBA basics  
    - Sharing features  
    """)

    with st.expander("Read More: PivotTables Explained"):
        st.markdown("""
        PivotTables provide interactive ways to summarize large data quickly.
        """)

    quiz_label = "<b>Quiz:</b> Which Excel function is used for horizontal lookup?"
    st.markdown(quiz_label, unsafe_allow_html=True)
    ans = st.radio("", ["VLOOKUP", "HLOOKUP", "INDEX"], key="excel_quiz", horizontal=True)
    if st.button("Submit Answer", key="excel_submit"):
        if ans == "HLOOKUP":
            st.success("Correct! HLOOKUP searches horizontally in rows.")
        else:
            st.error("Incorrect, please try again.")

    st.markdown("[Download Excel Cheat Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")

    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)


# -------- POWER BI --------
def page_power_bi():
    section_header("Microsoft Power BI Fundamentals")
    st.video("https://www.youtube.com/watch?v=AGrl-H87pRU")

    st.markdown("""
    <p style='font-size:1.1rem; color:#dfe6e9;'>Power BI provides interactive business analytics and data visualizations, connecting multiple data sources easily.</p>
    """, unsafe_allow_html=True)

    with st.expander("Why Learn Power BI?"):
        st.markdown("""
        Power BI simplifies report creation, sharing, and data-driven collaboration.
        """)

    st.subheader("Key Features Covered")
    col1, col2 = st.columns(2, gap="large")
    col1.markdown("""
    - Power BI Desktop overview  
    - Connecting and preparing data  
    - Creating visuals  
    - Power Query for data transformation  
    """)
    col2.markdown("""
    - DAX language basics  
    - Dashboard design  
    - Publishing and sharing reports  
    - Collaboration features  
    """)

    with st.expander("Read More: Introduction to Power Query"):
        st.markdown("""
        Power Query simplifies data import, cleaning, and reshaping without code.
        """)

    quiz_label = "<b>Quiz:</b> Which Power BI component hosts reports for sharing?"
    st.markdown(quiz_label, unsafe_allow_html=True)
    ans = st.radio("", ["Power BI Desktop", "Power BI Service", "Power Query"], key="pbi_quiz", horizontal=True)
    if st.button("Submit Answer", key="pbi_submit"):
        if ans == "Power BI Service":
            st.success("Correct! Power BI Service hosts reports for collaboration.")
        else:
            st.error("Incorrect, please try again.")

    st.markdown("[Download Power BI Guide](https://docs.microsoft.com/en-us/power-bi/guided-learning/power-bi-learning-guide)")

    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)


# -------- AI PAGE --------
def page_ai():
    section_header("Artificial Intelligence Fundamentals")
    st.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")

    st.markdown("""
    <p style='font-size:1.1rem; color:#dfe6e9;'>AI enables machines to simulate intelligent human behavior, solving complex problems across industries.</p>
    """, unsafe_allow_html=True)

    st.subheader("Topics Covered")
    st.markdown("""
    - AI concepts and history  
    - Machine learning algorithms  
    - Neural networks and deep learning basics  
    - Natural Language Processing  
    - AI ethics and impact  
    """)

    with st.expander("Read More: Neural Networks Explained"):
        st.markdown("""
        Neural networks, inspired by brain biology, power many AI applications today.
        """)

    quiz_label = "<b>Quiz:</b> Which AI technique learns from labeled datasets?"
    st.markdown(quiz_label, unsafe_allow_html=True)
    ans = st.radio("", ["Reinforcement Learning", "Unsupervised Learning", "Supervised Learning"], key="ai_quiz", horizontal=True)
    if st.button("Submit Answer", key="ai_submit"):
        if ans == "Supervised Learning":
            st.success("Correct! Supervised learning uses labeled data.")
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

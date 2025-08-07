import streamlit as st
import time

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# Custom CSS for dark translucent background and developer style
custom_css = """
<style>
    /* Dark translucent overlay background */
    .stApp {
        background: 
            linear-gradient(
                rgba(0, 0, 0, 0.85), 
                rgba(0, 0, 0, 0.85)
            ),
            url('https://www.transparenttextures.com/patterns/cubes.png');
        background-repeat: repeat;
        background-size: 80px 80px;
        color: #c8d6e5; 
        transition: opacity 0.6s ease-in-out;
    }
    /* Content box styling */
    .css-1d391kg, .css-1d391kg {
        background-color: rgba(24, 25, 29, 0.75) !important;
        border-radius: 12px !important;
    }
    /* Headings */
    h1, h2, h3, h4 {
        color: #81ecec !important;
    }
    /* Links */
    a {
        color: #00cec9 !important;
        text-decoration: underline;
    }
    /* Buttons */
    .stButton>button {
        background-color: #0984e3 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: background-color 0.3s ease;
        box-shadow: 0 0 8px #00cec9;
    }
    .stButton>button:hover {
        background-color: #74b9ff !important;
        color: #2d3436 !important;
        box-shadow: 0 0 12px #55efc4;
    }
    /* Radio groups */
    div[role="radiogroup"] > label {
        color: #dfe6e9 !important;
    }
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: rgba(12, 13, 17, 0.6) !important;
        border-radius: 8px !important;
        color: #55efc4 !important;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Get current page (defaults to 'home')
query_params = st.query_params
current_page = query_params.get("page", "home")

# Navigation Helper with simulated animated transition
def go_to(page):
    # Show loading spinner to simulate transition
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("<h3 style='color:#00cec9;'>Loading...</h3>", unsafe_allow_html=True)
        with st.spinner(text="Preparing the page..."):
            time.sleep(0.6)  # animation delay
    placeholder.empty()
    st.experimental_set_query_params(page=page)

def fade_in_container(render_function):
    """Simulate fade-in effect by displaying content."""
    container = st.empty()
    # Display nothing to simulate starting hidden state
    container.markdown("")
    # Render the actual content after a short delay
    time.sleep(0.2)
    container.empty()
    render_function(container)

def section_header(title, container=None):
    html = f"<h2 style='color:#81ecec; border-bottom: 2px solid #00cec9; padding-bottom:8px;'>{title}</h2>"
    if container:
        container.markdown(html, unsafe_allow_html=True)
    else:
        st.markdown(html, unsafe_allow_html=True)

def card_button(label, key, callback, container=None):
    style = """
        <style>
        .stButton>button {
            background-color: #0984e3 !important;
            color: white !important;
            height: 4rem;
            width: 100%;
            border-radius: 8px !important;
            font-size: 1.2rem;
            font-weight: 600;
            transition: background-color 0.3s ease;
            box-shadow: 0 0 8px #00cec9;
        }
        .stButton>button:hover {
            background-color: #74b9ff !important;
            color: #2d3436 !important;
            box-shadow: 0 0 12px #55efc4;
        }
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)
    if container:
        with container:
            st.button(label, key=key, on_click=callback)
    else:
        st.button(label, key=key, on_click=callback)

def box_highlight(content, container=None):
    html = f"""
    <div style="background-color: rgba(0, 188, 212, 0.15); padding:10px 15px; border-radius:10px; margin-bottom:15px; box-shadow: 0 0 8px #00cec9;">
    {content}
    </div>
    """
    if container:
        container.markdown(html, unsafe_allow_html=True)
    else:
        st.markdown(html, unsafe_allow_html=True)

# ------------------- Pages -------------------

# -------- HOME --------
def page_home():
    container = st.container()
    section_header("Welcome to Data Science & Analytics with Ashwik Bire", container)
    container.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)
    container.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Select a learning path below. Each includes tutorials, quizzes, and resources.</p>", unsafe_allow_html=True)

    cols = container.columns(5, gap="large")
    card_button("Data Science", "btn_ds", lambda: go_to("data_science"), cols[0])
    card_button("Data Analytics", "btn_da", lambda: go_to("data_analytics"), cols[1])
    card_button("Microsoft Excel", "btn_excel", lambda: go_to("excel"), cols[2])
    card_button("Power BI", "btn_pbi", lambda: go_to("power_bi"), cols[3])
    card_button("Artificial Intelligence", "btn_ai", lambda: go_to("ai"), cols[4])

    container.divider()
    section_header("Featured Tutorials", container)

    vids = [
        "https://www.youtube.com/watch?v=IBnLsKOhpyU",
        "https://www.youtube.com/watch?v=DsI1vG-kXR8",
        "https://www.youtube.com/watch?v=7ny5ljw6NbI",
        "https://www.youtube.com/watch?v=AGrl-H87pRU",
        "https://www.youtube.com/watch?v=2ePf9rue1Ao"
    ]
    vid_cols = container.columns(5, gap="medium")
    for idx, url in enumerate(vids):
        vid_cols[idx].video(url)

    container.divider()
    container.markdown("<p style='font-size:1.1rem; font-weight:bold; color:#55efc4;'>Connect with Ashwik Bire on <a href='https://linkedin.com/in/ashwik-bire-b2a000186' target='_blank' style='color:#00cec9;'>LinkedIn</a> for updates and mentorship.</p>", unsafe_allow_html=True)

# -------- DATA SCIENCE --------
def page_data_science():
    container = st.container()
    section_header("Data Science Learning", container)
    container.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")

    intro_text = """
    <p style='font-size:1.1rem; color:#dfe6e9;'>Data Science unlocks insights from complex data using statistics, programming, and algorithms. It covers data cleaning, visualization, machine learning, and engineering.</p>
    """
    container.markdown(intro_text, unsafe_allow_html=True)

    with container.expander("Why Data Science?"):
        st.markdown("""
        Data science enables data-driven decision-making, powering innovation and competitive advantages worldwide.
        Understand data collection, cleaning, analysis, and modeling in real-world contexts.
        """)

    container.subheader("Concepts Covered")
    col1, col2 = container.columns(2, gap="large")
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

    with container.expander("Read More: Core Python for Data Science"):
        st.markdown("""
        Python is favored in data science for readability & vast libraries. Learn lists, dictionaries, and Pandas for data operations.
        """)

    with container.expander("Read More: Data Visualization Best Practices"):
        st.markdown("""
        Visualization effectively communicates insights. Learn chart choices, colors, annotations, to tell your data story.
        """)

    with container.expander("Example: Linear Regression in Python"):
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

    with container.expander("Read More: Machine Learning Workflow"):
        st.markdown("""
        Learn full ML pipeline: data preprocessing, model training, evaluation, and deployment for production-ready models.
        """)

    box_highlight("<b>Quiz:</b> Which machine learning approach uses labeled training data?")
    answer = container.radio("", ["Unsupervised", "Supervised", "Reinforcement"], key="ds_quiz", horizontal=True)
    if container.button("Submit Answer", key="ds_submit"):
        if answer == "Supervised":
            st.success("Correct! Supervised learning uses labeled data.")
        else:
            st.error("Incorrect, try again.")

    container.markdown("[Download Data Science Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")

    container.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# -------- DATA ANALYTICS --------
def page_data_analytics():
    container = st.container()
    section_header("Data Analytics Curriculum", container)
    container.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")

    intro_text = """
    <p style='font-size:1.1rem; color:#dfe6e9;'>Data Analytics transforms raw data into actionable insights using SQL, Python, and BI tools through cleaning and visualization.</p>
    """
    container.markdown(intro_text, unsafe_allow_html=True)

    with container.expander("Importance of Data Analytics"):
        st.markdown("""
        Analytics supports smarter business decisions by uncovering trends and forecasting.
        """)

    container.subheader("Topics Covered")
    col1, col2 = container.columns(2, gap="large")
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
    - Statistical inference basics  
    - Data storytelling  
    """)

    with container.expander("Read More: Power BI Fundamentals"):
        st.markdown("""
        Power BI makes data connection, transformation, modeling, and reporting easier than ever.
        """)

    with container.expander("Example: Sales Data Analysis Code"):
        st.code("""
import pandas as pd

sales_df = pd.read_csv('sales_data.csv')
sales_df_clean = sales_df.dropna()
top_products = sales_df_clean.groupby('Product')['Revenue'].sum().nlargest(5)

print(top_products)
        """)

    box_highlight("<b>Quiz:</b> Which analytics type forecasts future outcomes?")
    q = container.radio("", ["Descriptive", "Predictive", "Diagnostic"], key="da_quiz", horizontal=True)
    if container.button("Submit Answer", key="da_submit"):
        if q == "Predictive":
            st.success("Correct! Predictive analytics forecasts future events.")
        else:
            st.error("Incorrect, try again.")

    container.markdown("[Download Data Analytics Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")

    container.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# -------- EXCEL --------
def page_excel():
    container = st.container()
    section_header("Microsoft Excel Essentials", container)
    container.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")

    intro_text = """
    <p style='font-size:1.1rem; color:#dfe6e9;'>Excel offers powerful organizational, calculation, and visualization features with formulas, PivotTables, charts, and macros.</p>
    """
    container.markdown(intro_text, unsafe_allow_html=True)

    with container.expander("Why Excel is Important"):
        st.markdown("""
        Excel is critical in finance, analytics, and reporting. Mastering it can significantly boost your professional skills.
        """)

    container.subheader("Key Features Covered")
    col1, col2 = container.columns(2, gap="large")
    col1.markdown("""
    - Cell referencing and formulas  
    - Lookup functions: VLOOKUP & INDEX-MATCH  
    - Data validation & conditional formatting  
    - Tables and structured references  
    """)
    col2.markdown("""
    - PivotTables and slicers  
    - Charts and dashboards  
    - Macros and VBA basics  
    - Collaboration & sharing features  
    """)

    with container.expander("Read More: PivotTables Explained"):
        st.markdown("""
        PivotTables allow dynamic summary and data exploration through filtering and grouping.
        """)

    box_highlight("<b>Quiz:</b> Which function is used for horizontal lookup?")
    ans = container.radio("", ["VLOOKUP", "HLOOKUP", "INDEX"], key="excel_quiz", horizontal=True)
    if container.button("Submit Answer", key="excel_submit"):
        if ans == "HLOOKUP":
            st.success("Correct! HLOOKUP searches horizontally.")
        else:
            st.error("Incorrect, try again.")

    container.markdown("[Download Excel Cheat Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")

    container.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# -------- POWER BI --------
def page_power_bi():
    container = st.container()
    section_header("Microsoft Power BI Fundamentals", container)
    container.video("https://www.youtube.com/watch?v=AGrl-H87pRU")

    intro_text = """
    <p style='font-size:1.1rem; color:#dfe6e9;'>Power BI is a leading business intelligence tool providing rich data visualization and collaboration capabilities.</p>
    """
    container.markdown(intro_text, unsafe_allow_html=True)

    with container.expander("Why Learn Power BI?"):
        st.markdown("""
        Power BI enables quick, interactive report creation and sharing across organizations.
        """)

    container.subheader("Key Features Covered")
    col1, col2 = container.columns(2, gap="large")
    col1.markdown("""
    - Power BI Desktop overview  
    - Connecting to diverse data sources  
    - Data preparation with Power Query  
    - Visuals creation & customization  
    """)
    col2.markdown("""
    - DAX for calculations  
    - Designing interactive dashboards  
    - Publishing & sharing reports  
    - Team collaboration features  
    """)

    with container.expander("Read More: Introduction to Power Query"):
        st.markdown("""
        Learn how Power Query simplifies data import and transformation processes.
        """)

    box_highlight("<b>Quiz:</b> Which Power BI component is used to share reports?")
    ans = container.radio("", ["Power BI Desktop", "Power BI Service", "Power Query"], key="pbi_quiz", horizontal=True)
    if container.button("Submit Answer", key="pbi_submit"):
        if ans == "Power BI Service":
            st.success("Correct! Power BI Service hosts shared reports.")
        else:
            st.error("Incorrect, try again.")

    container.markdown("[Download Power BI Guide](https://docs.microsoft.com/en-us/power-bi/guided-learning/power-bi-learning-guide)")

    container.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# -------- ARTIFICIAL INTELLIGENCE --------
def page_ai():
    container = st.container()
    section_header("Artificial Intelligence Fundamentals", container)
    container.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")

    intro_text = """
    <p style='font-size:1.1rem; color:#dfe6e9;'>AI enables machines to simulate intelligent human behavior for applications like robotics, vision, and language processing.</p>
    """
    container.markdown(intro_text, unsafe_allow_html=True)

    with container.expander("Why Learn AI?"):
        st.markdown("""
        AI revolutionizes automation and decision-making. This course covers foundations and practical applications.
        """)

    container.subheader("Topics Covered")
    container.markdown("""
    - AI history & concepts  
    - Machine Learning types: supervised, unsupervised, reinforcement  
    - Neural networks & deep learning basics  
    - Natural Language Processing fundamentals  
    - AI ethics & social impact  
    """)

    with container.expander("Read More: Neural Networks Explained"):
        st.markdown("""
        Neural networks mimic brain structures to enable deep learning and pattern recognition.
        """)

    box_highlight("<b>Quiz:</b> Which AI technique learns from labeled data?")
    ans = container.radio("", ["Reinforcement Learning", "Unsupervised Learning", "Supervised Learning"], key="ai_quiz", horizontal=True)
    if container.button("Submit Answer", key="ai_submit"):
        if ans == "Supervised Learning":
            st.success("Correct! Supervised learning uses labeled data.")
        else:
            st.error("Incorrect, try again.")

    container.markdown("[Download AI Fundamentals Guide](https://ai.google/education/)")

    container.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

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

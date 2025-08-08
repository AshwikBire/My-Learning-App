import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# Custom CSS for dark translucent dev-style look
custom_css = """
<style>
    .stApp {
        background: 
            linear-gradient(rgba(0, 0, 0, 0.85), rgba(0,0,0,0.85)),
            url('https://www.transparenttextures.com/patterns/cubes.png');
        background-repeat: repeat;
        background-size: 80px 80px;
        color: #c8d6e5;
    }
    .css-1d391kg, .css-1d391kg {
        background-color: rgba(24,25,29,0.75) !important;
        border-radius: 12px !important;
    }
    h1, h2, h3, h4 {
        color: #81ecec !important;
    }
    a { color: #00cec9 !important; text-decoration: underline; }
    .stButton>button {
        background-color: #0984e3 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #74b9ff !important;
        color: #2d3436 !important;
    }
    .streamlit-expanderHeader {
        background-color: rgba(12,13,17,0.6) !important;
        border-radius: 8px !important;
        color: #55efc4 !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Get current page (defaults to 'home')
query_params = st.query_params
current_page = query_params.get("page", "home")

def go_to(page):
    st.query_params.page = page

def section_header(title):
    st.markdown(f"<h2 style='color:#81ecec; border-bottom:2px solid #00cec9; padding-bottom:6px;'>{title}</h2>", unsafe_allow_html=True)

def card_button(label, key, callback):
    st.button(label, key=key, on_click=callback)

def box_highlight(content):
    st.markdown(f"<div style='background-color:rgba(0,188,212,0.15);padding:10px 15px;border-radius:10px;margin-bottom:15px;box-shadow:0 0 8px #00cec9'>{content}</div>", unsafe_allow_html=True)

# -------- HOME --------
def page_home():
    section_header("Welcome to Data Science & Analytics with Ashwik Bire")
    st.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Select a learning path or view all materials below.</p>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6 = st.columns(6, gap="large")
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
    with col6:
        card_button("Learning Material", "btn_material", lambda: go_to("material"))
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

# -------- LEARNING MATERIAL PAGE --------
def page_material():
    section_header("Complete Learning Materials Library")
    st.markdown("""
    <p style='font-size:1.12rem;color:#dfe6e9;'>A central hub of downloadable guides, recommended books, video courses, and reading lists for all disciplines. Explore, download, and bookmark your favorites.</p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📝 Downloadable Guides & Cheat Sheets")
    st.markdown("""
- 📥 [Data Science Cheat Sheet PDF](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)
- 📥 [Data Analytics Quick Reference](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)
- 📥 [Excel Functions & Shortcuts PDF](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)
- 📥 [Power BI Learning Guide (Microsoft)](https://docs.microsoft.com/en-us/power-bi/guided-learning/power-bi-learning-guide)
- 📥 [AI Fundamentals Guide (Google)](https://ai.google/education/)
    """)

    st.markdown("---")
    st.subheader("📚 Books & Further Reading")
    with st.expander("Data Science"):
        st.markdown("""
- *Python Data Science Handbook* — Jake VanderPlas ([Read Online](https://jakevdp.github.io/PythonDataScienceHandbook/))
- *Hands-On Machine Learning with Scikit-Learn, Keras, & TensorFlow* — Aurélien Géron
- *Storytelling With Data* — Cole Nussbaumer Knaflic
        """)
    with st.expander("Analytics & BI"):
        st.markdown("""
- *Data Analytics Made Accessible* — A. Maheshwari
- *Data Visualization: A Practical Intro* — Kieran Healy
- *The Big Book of Dashboards* — Steve Wexler
        """)
    with st.expander("Excel"):
        st.markdown("""
- *Excel Bible* — John Walkenbach
- *Excel Power Programming with VBA* — Michael Alexander
- *Excel Dashboards and Reports* — Michael Alexander & John Walkenbach
        """)
    with st.expander("Power BI"):
        st.markdown("""
- *Mastering Microsoft Power BI* — Brett Powell
- *Power BI for the Excel Analyst* — Wyn Hopkins
        """)
    with st.expander("Artificial Intelligence"):
        st.markdown("""
- *Artificial Intelligence: A Guide to Intelligent Systems* — Michael Negnevitsky
- *Deep Learning* — Ian Goodfellow, Yoshua Bengio, and Aaron Courville ([Free Online](https://www.deeplearningbook.org/))
- *Make Your Own Neural Network* — Tariq Rashid
        """)

    st.markdown("---")
    st.subheader("📰 Top Blogs & MOOC Portals")
    st.markdown("""
- [Microsoft Learn](https://learn.microsoft.com/)
- [Kaggle Learn](https://www.kaggle.com/learn)
- [Google AI Blog](https://ai.googleblog.com/)
- [Towards Data Science](https://towardsdatascience.com/)
- [DataCamp Community](https://www.datacamp.com/community)
- [Analytics Vidhya](https://www.analyticsvidhya.com/)
- [Chandoo (Excel)](https://chandoo.org/wp/)
    """)

    st.markdown("---")
    st.subheader("🎬 Recommended Playlists")
    st.markdown("""
- [Data Science Full Courses](https://www.youtube.com/playlist?list=PLF797E961509B4EB5)
- [Power BI Training](https://www.youtube.com/playlist?list=PL1N57mwBHtN0JFoWOGou-6BjdQY7fjalY)
- [Python for Everybody - Coursera](https://www.youtube.com/playlist?list=PLl_Xou7GtCi6VPp8FDiirp-1oMujyFgRO)
    """)
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# -------- DATA SCIENCE PAGE --------
def page_data_science():
    section_header("Data Science Learning")
    st.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Data Science unlocks insights from complex data using statistics, programming, and algorithms.</p>", unsafe_allow_html=True)
    with st.expander("Why Data Science?"):
        st.markdown("Data science enables data-driven decision-making and innovation in real-world applications.")
    st.subheader("Concepts Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""- Python & Jupyter basics  
- Data manipulation with Pandas  
- Data viz (Matplotlib, Seaborn)  
- Intro to statistics & probability  
- Data wrangling/cleaning""")
    col2.markdown("""- Machine Learning fundamentals  
- Regression, classification, clustering  
- Model validation  
- Ethics in data science  
- Big Data tools overview""")
    with st.expander("Read More: Core Python for Data Science"):
        st.markdown("Python's clean syntax and huge ecosystem make it ideal for data manipulation and analysis.")
    with st.expander("Example: Linear Regression in Python"):
        st.code("""
import pandas as pd
from sklearn.linear_model import LinearRegression
data = {'Experience':[1,2,3,4,5], 'Salary':[45000,50000,60000,65000,70000]}
df = pd.DataFrame(data)
model=LinearRegression(); model.fit(df[['Experience']], df['Salary'])
print(model.predict([[6]]))
        """)
    box_highlight("<b>Quiz:</b> Which learning approach uses labeled data?")
    answer = st.radio("", ["Unsupervised", "Supervised", "Reinforcement"], key="ds_quiz", horizontal=True)
    if st.button("Submit Answer", key="ds_submit"):
        if answer == "Supervised":
            st.success("Correct! Supervised learning uses labeled data.")
        else:
            st.error("Incorrect, please try again.")
    st.markdown("[Download Data Science Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# -------- DATA ANALYTICS PAGE --------
def page_data_analytics():
    section_header("Data Analytics Curriculum")
    st.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Data Analytics transforms info into insights using SQL, Python, and BI tools.</p>", unsafe_allow_html=True)
    with st.expander("Importance of Data Analytics"):
        st.markdown("Analytics enables smarter business decisions by uncovering trends and forecasting.")
    st.subheader("Topics Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""- Descriptive, diagnostic, predictive, prescriptive analytics  
- Data visualization  
- SQL fundamentals  
- Data quality""")
    col2.markdown("""- BI dashboards (Power BI, Tableau)  
- Python tools (Pandas, Seaborn)  
- Stats inference fundamentals  
- Data storytelling presentation""")
    with st.expander("Read More: Power BI Fundamentals"):
        st.markdown("Power BI transforms and visualizes data for interactive business analysis.")
    with st.expander("Example: Sales Data Analysis Code"):
        st.code("""
import pandas as pd
sales_df = pd.read_csv('sales_data.csv')
sales_df_clean = sales_df.dropna()
print(sales_df_clean.groupby('Product')['Revenue'].sum().nlargest(5))
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

# -------- EXCEL PAGE --------
def page_excel():
    section_header("Microsoft Excel Essentials")
    st.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Excel lets you analyze and visualize data with formulas, PivotTables, and more.</p>", unsafe_allow_html=True)
    st.subheader("Key Features Covered")
    col1, col2 = st.columns(2)
    col1.markdown("- Formulas, referencing\n- Lookup functions (VLOOKUP, INDEX-MATCH)\n- Validation and formatting")
    col2.markdown("- PivotTables, charts\n- Macros and VBA\n- Sharing and collaboration")
    with st.expander("Read More: PivotTables Explained"):
        st.markdown("PivotTables allow interactive and dynamic summary tables for data exploration.")
    box_highlight("<b>Quiz:</b> Which Excel function is for horizontal lookup?")
    ans = st.radio("", ["VLOOKUP", "HLOOKUP", "INDEX"], key="excel_quiz", horizontal=True)
    if st.button("Submit Answer", key="excel_submit"):
        if ans == "HLOOKUP":
            st.success("Correct! HLOOKUP searches horizontally in rows.")
        else:
            st.error("Incorrect, please try again.")
    st.markdown("[Download Excel Cheat Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# -------- POWER BI PAGE --------
def page_power_bi():
    section_header("Microsoft Power BI Fundamentals")
    st.video("https://www.youtube.com/watch?v=AGrl-H87pRU")
    st.markdown("<p style='font-size:1.1rem;color:#dfe6e9;'>Power BI enables interactive data visualizations and business intelligence, connecting to many data sources seamlessly.</p>", unsafe_allow_html=True)
    st.subheader("Key Features Covered")
    col1, col2 = st.columns(2)
    col1.markdown("- Desktop interface\n- Data source connections\n- Power Query for shaping data\n- Custom visuals")
    col2.markdown("- DAX analytics\n- Dashboards\n- Cloud reporting\n- Collaboration tools")
    with st.expander("Read More: Power Query"):
        st.markdown("Power Query offers powerful, low-code ETL and fast data prep for BI projects.")
    box_highlight("<b>Quiz:</b> Which Power BI component hosts reports for sharing?")
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
    st.markdown("<p style='font-size:1.1rem;color:#dfe6e9;'>AI allows machines to solve complex problems and simulate human thinking.</p>", unsafe_allow_html=True)
    st.subheader("Topics Covered")
    st.markdown("- AI concepts, history\n- Machine learning\n- Deep learning basics\n- NLP fundamentals\n- Ethics and impact")
    with st.expander("Read More: Neural Networks Explained"):
        st.markdown("Neural networks are the backbone of most modern deep learning solutions.")
    box_highlight("<b>Quiz:</b> Which AI type learns from labeled data?")
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
elif current_page == "material":
    page_material()
else:
    st.error("Page not found. Click below to return.")
    st.button("Back to Home", on_click=lambda: go_to("home"))

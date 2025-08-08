import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
.stApp {
    background: 
        linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
        url('https://www.transparenttextures.com/patterns/cubes.png');
    background-repeat: repeat;
    background-size: 80px 80px;
    color: #c8d6e5;
}
h1, h2, h3, h4 { color: #81ecec !important; }
a { color: #00cec9 !important; text-decoration: underline; }
.stButton>button {
    background-color: #0984e3 !important;
    color: white !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
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
""", unsafe_allow_html=True)

# --- Routing Params ---
query_params = st.query_params
current_page = query_params.get("page", "home")

def go_to(page):
    st.query_params.page = page

def section_header(title):
    st.markdown(f"<h2 style='color:#81ecec; border-bottom:2px solid #00cec9; padding-bottom:6px;'>{title}</h2>", unsafe_allow_html=True)

def box_highlight(content):
    st.markdown(f"<div style='background-color:rgba(0,188,212,0.15);padding:10px 15px;border-radius:10px;margin-bottom:15px;box-shadow:0 0 8px #00cec9'>{content}</div>", unsafe_allow_html=True)

# --- HOME PAGE ---
def page_home():
    section_header("Welcome to Data Science & Analytics with Ashwik Bire")
    st.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Select a learning path or view all materials below.</p>", unsafe_allow_html=True)

    # Navigation Cards
    labels = ["Data Science", "Data Analytics", "Microsoft Excel", "Power BI", "Artificial Intelligence", "Learning Material"]
    pages = ["data_science", "data_analytics", "excel", "power_bi", "ai", "material"]
    cols = st.columns(6, gap="large")
    for i in range(6):
        with cols[i]:
            st.button(labels[i], key=f"btn_{i}", on_click=lambda p=pages[i]: go_to(p))

    st.divider()
    section_header("Featured Tutorials")
    video_links = [
        "https://www.youtube.com/watch?v=IBnLsKOhpyU",
        "https://www.youtube.com/watch?v=DsI1vG-kXR8",
        "https://www.youtube.com/watch?v=7ny5ljw6NbI",
        "https://www.youtube.com/watch?v=AGrl-H87pRU",
        "https://www.youtube.com/watch?v=2ePf9rue1Ao"
    ]
    cols_videos = st.columns(5, gap="medium")
    for i, link in enumerate(video_links):
        cols_videos[i].video(link)

    st.markdown("""
    <p style='font-size:1.1rem; font-weight:bold; color:#55efc4;'>
    Connect with Ashwik Bire on <a href='https://linkedin.com/in/ashwik-bire-b2a000186' target='_blank'>LinkedIn</a> for updates and mentorship.
    </p>
    """, unsafe_allow_html=True)

# --- DATA SCIENCE PAGE ---
def page_data_science():
    section_header("Data Science Learning")
    st.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Data Science unlocks insights from complex data using statistics, programming, and algorithms.</p>", unsafe_allow_html=True)

    with st.expander("Why Data Science?"):
        st.markdown("Data science enables data-driven decision-making and innovation in real-world applications.")

    # Topics
    st.subheader("Concepts Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""- Python & Jupyter basics  
- Data manipulation with Pandas  
- Data viz (Matplotlib, Seaborn)  
- Statistics & Probability  
- Data cleaning/wrangling""")
    col2.markdown("""- ML fundamentals  
- Regression, Classification  
- Model validation  
- Big Data tools  
- Ethics in data""")

    with st.expander("Example: Linear Regression Code"):
        st.code("""
import pandas as pd
from sklearn.linear_model import LinearRegression
data = {'Experience':[1,2,3,4,5], 'Salary':[45000,50000,60000,65000,70000]}
df = pd.DataFrame(data)
model=LinearRegression(); model.fit(df[['Experience']], df['Salary'])
print(model.predict([[6]]))
        """)

    box_highlight("<b>Quiz:</b> Which learning approach uses labeled data?")
    ans = st.radio("", ["Unsupervised", "Supervised", "Reinforcement"], key="ds_quiz", horizontal=True)
    if st.button("Submit Answer", key="ds_submit"):
        st.success("Correct! Supervised learning uses labeled data.") if ans == "Supervised" else st.error("Incorrect. Try again.")

    st.markdown("[Download Data Science Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --- ANALYTICS PAGE ---
def page_data_analytics():
    section_header("Data Analytics Curriculum")
    st.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Data Analytics transforms info into insights using SQL, Python, and BI tools.</p>", unsafe_allow_html=True)

    with st.expander("Why Analytics?"):
        st.markdown("Analytics drives informed strategic decisions across industries.")

    st.subheader("Topics Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""- Descriptive, diagnostic, predictive  
- SQL basics  
- Visualization  
- Data quality""")
    col2.markdown("""- BI dashboards  
- Python (Pandas, Seaborn)  
- Statistical inference  
- Storytelling""")

    with st.expander("Example: Sales Analysis"):
        st.code("""
import pandas as pd
sales_df = pd.read_csv('sales_data.csv')
sales_df_clean = sales_df.dropna()
print(sales_df_clean.groupby('Product')['Revenue'].sum().nlargest(5))
        """)

    box_highlight("<b>Quiz:</b> Which analytics type forecasts future outcomes?")
    qa = st.radio("", ["Descriptive", "Predictive", "Diagnostic"], key="da_quiz", horizontal=True)
    if st.button("Submit Answer", key="da_submit"):
        st.success("Yes! Predictive analytics forecasts.") if qa == "Predictive" else st.error("Try again!")

    st.markdown("[Download Analytics Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --- EXCEL PAGE ---
def page_excel():
    section_header("Microsoft Excel Essentials")
    st.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Excel empowers cleaning, analysis and insights with functions and smart UI.</p>", unsafe_allow_html=True)

    st.subheader("Key Features Covered")
    c1, c2 = st.columns(2)
    c1.markdown("- Formulas, VLOOKUP, INDEX-MATCH, validation")
    c2.markdown("- PivotTables, charts, VBA, collaboration")

    with st.expander("Understanding PivotTables"):
        st.markdown("PivotTables summarize data and enhance visual trends detection instantly.")

    box_highlight("📘 Quiz: Which Excel function performs a horizontal lookup?")
    qx = st.radio("", ["VLOOKUP", "HLOOKUP", "INDEX"], key="excel_quiz", horizontal=True)
    if st.button("Submit Answer", key="excel_submit"):
        st.success("Correct, HLOOKUP works across rows.") if qx == "HLOOKUP" else st.error("Not quite. Try again.")

    st.markdown("[Download Excel Cheat Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --- POWER BI PAGE ---
def page_power_bi():
    section_header("Power BI Fundamentals")
    st.video("https://www.youtube.com/watch?v=AGrl-H87pRU")
    st.markdown("<p style='font-size:1.1rem;'>Power BI enables advanced visual storytelling through real-time dashboards across data scales.</p>", unsafe_allow_html=True)

    st.subheader("What You'll Learn")
    left, right = st.columns(2)
    left.markdown("- Desktop & interface\n- Data sourcing\n- Custom visuals & shaping")
    right.markdown("- DAX analytics\n- Cloud publishing\n- Collaboration tools")

    with st.expander("Power BI: Power Query Basics"):
        st.markdown("Power Query provides ETL (Extract, Transform, Load) simplicity with GUI controls.")

    box_highlight("📘 Quiz: Which component hosts published dashboards?")
    pc = st.radio("", ["Power BI Desktop", "Power BI Service", "Power Query"], key="pbi_quiz", horizontal=True)
    if st.button("Submit Answer", key="pbi_submit"):
        st.success("Correct. Power BI Service enables sharing online.") if pc == "Power BI Service" else st.error("Nope. Try again.")

    st.markdown("[Download Power BI Guide](https://docs.microsoft.com/en-us/power-bi/guided-learning/power-bi-learning-guide)")
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --- AI PAGE ---
def page_ai():
    section_header("Artificial Intelligence Fundamentals")
    st.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")
    st.markdown("<p style='font-size:1.1rem;'>AI systems mimic intelligence via learning and decision-making algorithms.</p>", unsafe_allow_html=True)

    st.subheader("Topics Covered")
    st.markdown("- AI foundations\n- Machine Learning types\n- Intro to Deep Learning\n- NLP basics\n- Ethics")

    with st.expander("Neural Networks Explained"):
        st.markdown("NNs simulate layers of perception for classification, detection, & generation.")

    box_highlight("📘 Quiz: Which AI model learns from labeled data?")
    aq = st.radio("", ["Reinforcement Learning", "Unsupervised", "Supervised"], key="ai_quiz", horizontal=True)
    if st.button("Submit Answer", key="ai_submit"):
        st.success("Correct! Supervised = labeled datasets.") if aq == "Supervised" else st.error("Oops! Try again.")

    st.markdown("[Download AI Fundamentals Guide](https://ai.google/education/)")
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --- MATERIAL PAGE ---
def page_material():
    section_header("Complete Learning Materials Library")
    st.markdown("<p style='font-size:1.12rem;'>Guides, PDFs, books, blogs, and MOOC resources categorized by your learning goals.</p>", unsafe_allow_html=True)

    st.subheader("📝 Downloadable Guides & Cheat Sheets")
    st.markdown("""
- 📥 [Data Science](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)
- 📥 [Analytics](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)
- 📥 [Excel](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)
- 📥 [Power BI](https://docs.microsoft.com/en-us/power-bi/guided-learning/power-bi-learning-guide)
- 📥 [AI Guide](https://ai.google/education/)
    """)

    st.subheader("📚 Recommended Reading")
    for topic, books in {
        "Data Science": [
            "*Python Data Science Handbook*", "*Hands-On ML*", "*Storytelling with Data*"
        ],
        "Analytics & BI": [
            "*Data Analytics Made Accessible*", "*Data Visualization*", "*Big Book of Dashboards*"
        ],
        "Excel": [
            "*Excel Bible*", "*Power Programming with VBA*", "*Dashboards and Reports*"
        ],
        "Power BI": [
            "*Mastering Microsoft Power BI*", "*Power BI for Excel Analysts*"
        ],
        "AI": [
            "*AI: Guide to Intelligent Systems*", "*Deep Learning*", "*Make Your Own Neural Net*"
        ]
    }.items():
        with st.expander(topic):
            for book in books: st.markdown(f"- {book}")

    st.subheader("📰 Blogs & MOOCs")
    st.markdown("""
- [Microsoft Learn](https://learn.microsoft.com/)
- [Kaggle Learn](https://www.kaggle.com/learn)
- [Google AI Blog](https://ai.googleblog.com/)
- [Towards Data Science](https://towardsdatascience.com/)
- [Analytics Vidhya](https://www.analyticsvidhya.com/)
    """)

    st.subheader("🎬 YouTube Playlists")
    st.markdown("""
- [Python for Everybody](https://www.youtube.com/playlist?list=PLl_Xou7GtCi6VPp8FDiirp-1oMujyFgRO)
- [Power BI Basics](https://www.youtube.com/playlist?list=PL1N57mwBHtN0JFoWOGou-6BjdQY7fjalY)
    """)
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --- Router ---
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
    st.error("Page not found.")
    st.button("Back to Home", on_click=lambda: go_to("home"))


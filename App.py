import streamlit as st

# --- SETUP ---
st.set_page_config(
    page_title="Learning Hub by Ashwik Bire",
    layout="wide",
    page_icon="📘"
)

# --- DARK DEV STYLE CSS ---
st.markdown("""
<style>
/* Background + Developer Pattern */
.stApp {
    background: 
        linear-gradient(rgba(0, 0, 0, 0.92), rgba(0,0,0,0.92)),
        url('https://www.transparenttextures.com/patterns/cubes.png');
    background-size: 80px 80px;
    color: #dfe6e9;
}

/* Content box transparency and rounded corners */
.css-1d391kg, .css-1d391kg {
    background-color: rgba(24,25,29,0.75) !important;
    border-radius: 12px !important;
}

/* Headings */
h1, h2, h3, h4 {
    color: #81ecec;
}
a {
    color: #00cec9;
    font-weight: 600;
}

/* Navigation buttons styling */
.stButton > button {
    background-color: #0984e3 !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    font-weight: bold;
    font-size: 1.05rem;
    padding: 0.75rem 1.25rem;
    transition: 0.3s;
}
.stButton > button:hover {
    background-color: #74b9ff !important;
    color: #2c3e50 !important;
    box-shadow: 0 0 8px #00cec9;
}

/* Expander header style */
.streamlit-expanderHeader {
    background-color: rgba(255, 255, 255, 0.05) !important;
    border-radius: 6px !important;
    font-weight: 600;
}

/* Radio button label color */
div[role="radiogroup"] > label {
    color: #dfe6e9 !important;
}
</style>
""", unsafe_allow_html=True)

# --- URL Routing ---
query_params = st.query_params
current_page = query_params.get("page", "home")

# --- Navigation Helper ---
def go_to(page):
    st.query_params.page = page

def section_header(label):
    st.markdown(f"<h2 style='color:#81ecec; border-bottom:2px solid #00cec9; padding:0.4em 0'>{label}</h2>", unsafe_allow_html=True)

def box(content):
    st.markdown(
        f"<div style='background-color:rgba(0,188,212,0.1); padding:12px; border-radius:8px; margin:10px 0'>{content}</div>", 
        unsafe_allow_html=True
    )

# --- HOME PAGE ---
def page_home():
    section_header("📘 Welcome to the Learning Hub by Ashwik Bire")
    st.image("banner.png", use_container_width=True)
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Select a course below to begin your learning journey.</p>", unsafe_allow_html=True)

    cols = st.columns(6)
    pages = [
        ("Data Science", "data_science"),
        ("Analytics", "data_analytics"),
        ("Excel", "excel"),
        ("Power BI", "power_bi"),
        ("Artificial Intelligence", "ai"),
        ("Learning Material", "material"),
    ]
    for col, (label, page_key) in zip(cols, pages):
        with col:
            st.button(label, key=f"btn_{page_key}", on_click=lambda p=page_key: go_to(p), use_container_width=True)

    st.markdown("---")
    section_header("🎥 Featured Tutorials")
    vids = [
        "https://www.youtube.com/watch?v=IBnLsKOhpyU",
        "https://www.youtube.com/watch?v=DsI1vG-kXR8",
        "https://www.youtube.com/watch?v=7ny5ljw6NbI",
        "https://www.youtube.com/watch?v=AGrl-H87pRU",
        "https://www.youtube.com/watch?v=2ePf9rue1Ao",
    ]
    vid_cols = st.columns(5)
    for col, v in zip(vid_cols, vids):
        col.video(v)

    st.markdown("💬 **Connect on [LinkedIn](https://linkedin.com/in/ashwik-bire-b2a000186)** — for updates, tips, and mentorship.")

# --- LEARNING MATERIAL PAGE ---
def page_material():
    section_header("📚 Learning Materials")

    st.markdown("""
    <p style='font-size:1.12rem;color:#dfe6e9;'>A central hub of downloadable guides, recommended books, curated video courses, and further reading materials for all disciplines.</p>
    """, unsafe_allow_html=True)

    st.subheader("📥 Downloadable Guides & Cheat Sheets")
    st.markdown("""
- [Data Science Cheat Sheet (DataCamp PDF)](https://assets.datacamp.com/blog_assets/Data_Science_Cheat_Sheet_Python.pdf)  
- [Data Analytics Quick Reference](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)  
- [Excel Shortcuts & Formulas (ExcelJet PDF)](https://cdn.exceljet.net/sites/default/files/downloads/ExcelJet_Excel_cheat_sheet.pdf)  
- [Power BI Learning Guide (Microsoft)](https://learn.microsoft.com/en-us/power-bi/guided-learning/overview)  
- [AI Fundamentals Guide (Google)](https://ai.google/education/)  
""")

    st.subheader("📖 Recommended Books & Reading")
    with st.expander("💠 Data Science Books"):
        st.markdown("""
- *Python Data Science Handbook* — Jake VanderPlas ([Online](https://jakevdp.github.io/PythonDataScienceHandbook/))  
- *Hands-On Machine Learning* — Aurélien Géron  
- *Storytelling With Data* — Cole Nussbaumer Knaflic  
""")
    with st.expander("💠 Analytics & BI Books"):
        st.markdown("""
- *Data Analytics Made Accessible* — A. Maheshwari  
- *The Big Book of Dashboards* — Steve Wexler  
""")
    with st.expander("💠 Excel Books"):
        st.markdown("""
- *Excel Bible* — John Walkenbach  
- *Excel Power Programming with VBA* — Michael Alexander  
""")
    with st.expander("💠 Power BI Books"):
        st.markdown("""
- *Mastering Microsoft Power BI* — Brett Powell  
- *Power BI for the Excel Analyst* — Wyn Hopkins  
""")
    with st.expander("💠 Artificial Intelligence Books"):
        st.markdown("""
- *Deep Learning* — Goodfellow, Bengio, and Courville ([Free online](https://www.deeplearningbook.org/))  
- *Make Your Own Neural Network* — Tariq Rashid  
""")

    st.subheader("🌐 Top Official Learning Platforms & Blogs")
    st.markdown("""
- [Microsoft Learn](https://learn.microsoft.com/)  
- [Kaggle Learn](https://kaggle.com/learn)  
- [Google AI Blog](https://ai.googleblog.com/)  
- [Towards Data Science](https://towardsdatascience.com/)  
- [DataCamp Community](https://www.datacamp.com/community)  
- [Analytics Vidhya](https://www.analyticsvidhya.com/)  
- [Chandoo (Excel)](https://chandoo.org/wp/)  
""")

    st.subheader("🎬 Playlists & Free Courses")
    st.markdown("""
- [Data Science Full Courses](https://www.youtube.com/playlist?list=PLF797E961509B4EB5)  
- [Power BI Training Playlists](https://www.youtube.com/playlist?list=PL1N57mwBHtN0JFoWOGou-6BjdQY7fjalY)  
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)  
""")

    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --- Placeholder simplified pages for example (replace with full content from earlier) ---

def page_data_science():
    section_header("Data Science Learning")
    st.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")
    st.markdown("""
    Data Science unlocks insights from data by applying statistics, programming, and ML.
    """)
    # Additional content here ...
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

def page_data_analytics():
    section_header("Data Analytics Curriculum")
    st.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")
    st.markdown("""
    Explore data cleaning, visualization, and analytics with SQL, Python, and BI tools.
    """)
    # Additional content here ...
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

def page_excel():
    section_header("Microsoft Excel Essentials")
    st.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")
    st.markdown("""
    Master Excel formulas, PivotTables, charts, and automation.
    """)
    # Additional content here ...
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

def page_power_bi():
    section_header("Microsoft Power BI Fundamentals")
    st.video("https://www.youtube.com/watch?v=AGrl-H87pRU")
    st.markdown("""
    Learn to design interactive dashboards and reports with Power BI.
    """)
    # Additional content here ...
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

def page_ai():
    section_header("Artificial Intelligence Fundamentals")
    st.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")
    st.markdown("""
    Understand AI basics, including machine learning, neural networks, and NLP.
    """)
    # Additional content here ...
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --- PAGE ROUTING ---
pages = {
    "home": page_home,
    "data_science": page_data_science,
    "data_analytics": page_data_analytics,
    "excel": page_excel,
    "power_bi": page_power_bi,
    "ai": page_ai,
    "material": page_material,
}

pages.get(current_page, lambda: st.error("Page not found. Click below to return."))()
if current_page not in pages:
    st.button("Back to Home", on_click=lambda: go_to("home"))


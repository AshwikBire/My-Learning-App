import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Learning Hub by Ashwik Bire", layout="wide", page_icon="📘")

# --- DARK MODE CSS & BUTTON STYLE ---
st.markdown("""
<style>
/* Background and developer pattern */
.stApp {
    background: 
        linear-gradient(rgba(0, 0, 0, 0.92), rgba(0,0,0,0.92)),
        url("https://www.transparenttextures.com/patterns/cubes.png");
    background-size: 80px 80px;
    color: #dfe6e9;
}

/* Section Headers */
h1, h2, h3 {
    color: #81ecec !important;
}

/* Button container layout */
.nav-button > button {
    height: 90px;
    width: 100%;
    font-size: 1.15rem;
    font-weight: 700;
    border: none;
    border-radius: 16px;
    background-color: rgba(40, 40, 40, 0.85);
    color: #ffffff;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    transition: all 0.3s ease-in-out;
}
.nav-button > button:hover {
    background-color: rgba(80, 80, 80, 0.95);
    color: #00cec9;
    transform: translateY(-2px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.4);
}

/* Expander */
.streamlit-expanderHeader {
    background-color: rgba(255, 255, 255, 0.07) !important;
    border-radius: 6px;
    font-weight: 600;
}

/* Links */
a {
    color: #00cec9;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# --- Routing config ---
query_params = st.query_params
current_page = query_params.get("page", "home")

def go_to(page_name: str):
    st.query_params.page = page_name

# --- Helpers ---
def section_header(text):
    st.markdown(f"<h2 style='color:#81ecec; border-bottom:2px solid #00cec9'>{text}</h2>", unsafe_allow_html=True)

# --- HOME PAGE ---
def page_home():
    st.image("banner.png", use_container_width=True)
    section_header("📘 Welcome to the Learning Hub by Ashwik Bire")
    st.markdown("_Explore courses, resources, and video tutorials all in one place._")

    # Navigation buttons in columns
    labels = [
        ("📚 Learning Material", "material"),
        ("📊 Data Science", "data_science"),
        ("📈 Data Analytics", "data_analytics"),
        ("📑 Microsoft Excel", "excel"),
        ("📊 Power BI", "power_bi"),
        ("🤖 AI (Artificial Intelligence)", "ai"),
    ]
    btn_cols = st.columns(len(labels))
    for (label, route), col in zip(labels, btn_cols):
        with col:
            with st.container():
                st.markdown(f"""
                <div class="nav-button">
                    <button onclick="window.location.search='?page={route}'">{label}</button>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"{label}", key=route):
                    go_to(route)

    st.markdown("---")
    section_header("🎥 Featured Tutorials")
    videos = [
        "https://www.youtube.com/watch?v=IBnLsKOhpyU",
        "https://www.youtube.com/watch?v=DsI1vG-kXR8",
        "https://www.youtube.com/watch?v=7ny5ljw6NbI",
        "https://www.youtube.com/watch?v=AGrl-H87pRU",
        "https://www.youtube.com/watch?v=2ePf9rue1Ao",
    ]
    cols = st.columns(len(videos))
    for col, link in zip(cols, videos):
        col.video(link)

    st.markdown("---")
    st.markdown("💬 **Connect on [LinkedIn](https://linkedin.com/in/ashwik-bire-b2a000186)** — for updates and mentorship.")


# --- ICONIC PAGES: LEARNING MATERIAL ---
def page_material():
    section_header("📚 Learning Materials")
    st.markdown("Comprehensive resource center to support your learning journey:")

    st.markdown("### 📥 Downloadable Guides")
    st.markdown("""
- [Data Science Cheat Sheet (DataCamp)](https://assets.datacamp.com/blog_assets/Data_Science_Cheat_Sheet_Python.pdf)  
- [Analytics Quick Guide](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)  
- [Excel Formulas (ExcelJet)](https://cdn.exceljet.net/sites/default/files/downloads/ExcelJet_Excel_cheat_sheet.pdf)  
- [Power BI - Official Guide](https://learn.microsoft.com/en-us/power-bi/guided-learning/overview)  
- [Google AI Education](https://ai.google/education/)
""")

    st.markdown("### 📖 Books & References")
    with st.expander("📘 Data Science"):
        st.markdown("""
- *Python Data Science Handbook* ([Free](https://jakevdp.github.io/PythonDataScienceHandbook/))  
- *Hands-On Machine Learning* – A. Géron  
""")
    with st.expander("📘 Excel Mastery"):
        st.markdown("""
- *Excel Bible* – John Walkenbach  
- *Excel Dashboards and Reports* – Wiley  
""")
    with st.expander("📘 BI/Analytics"):
        st.markdown("""
- *The Big Book of Dashboards*  
- *Mastering Microsoft Power BI*  
""")
    with st.expander("📘 AI & ML"):
        st.markdown("""
- *Deep Learning* – Goodfellow et al. ([Book](https://www.deeplearningbook.org/))  
- *The Hundred-Page Machine Learning Book* – Andriy Burkov  
""")

    st.markdown("### ◀ Free Learning Platforms")
    st.markdown("""
- [Microsoft Learn](https://learn.microsoft.com/)  
- [Kaggle Learn](https://kaggle.com/learn)  
- [Google AI Hub](https://ai.google/education/)  
- [DataCamp Community](https://www.datacamp.com/community)  
- [Analytics Vidhya](https://www.analyticsvidhya.com/)  
""")

    st.markdown("### 🎬 Curated Playlists")
    st.markdown("""
- 📺 [Power BI Full Course](https://www.youtube.com/watch?v=AGrl-H87pRU)  
- 📺 [Excel for Beginners](https://www.youtube.com/watch?v=7ny5ljw6NbI)  
- 📺 [AI Full Course 10 Hrs](https://www.youtube.com/watch?v=2ePf9rue1Ao)  
""")
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --- PLACEHOLDER PAGES (use real content as needed) ---
def page_data_science():
    section_header("📊 Data Science")
    st.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")
    st.markdown("Learn Python, data wrangling, ML, and data storytelling...")
    st.button("Back to Home", on_click=lambda: go_to("home"))

def page_data_analytics():
    section_header("📈 Data Analytics")
    st.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")
    st.markdown("Explore EDA with SQL, BI tools, and Python...")
    st.button("Back to Home", on_click=lambda: go_to("home"))

def page_excel():
    section_header("📑 Microsoft Excel")
    st.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")
    st.markdown("Master Excel functions, dashboards, and data prep.")
    st.button("Back to Home", on_click=lambda: go_to("home"))

def page_power_bi():
    section_header("📊 Power BI")
    st.video("https://www.youtube.com/watch?v=AGrl-H87pRU")
    st.markdown("Learn how to build and publish live dashboards with Power BI.")
    st.button("Back to Home", on_click=lambda: go_to("home"))

def page_ai():
    section_header("🤖 Artificial Intelligence")
    st.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")
    st.markdown("Learn the foundations of AI, ML, and Deep Learning...")
    st.button("Back to Home", on_click=lambda: go_to("home"))

# --- PAGE ROUTER ---
pages = {
    "home": page_home,
    "material": page_material,
    "data_science": page_data_science,
    "data_analytics": page_data_analytics,
    "excel": page_excel,
    "power_bi": page_power_bi,
    "ai": page_ai
}
pages.get(current_page, page_home)()

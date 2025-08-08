import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# Custom CSS for dark translucent dev-style look and advanced button UI
st.markdown("""
<style>
    /* Background with developer pattern and dark overlay */
    .stApp {
        background: 
          linear-gradient(rgba(0, 0, 0, 0.92), rgba(0, 0, 0, 0.92)),
          url('https://www.transparenttextures.com/patterns/cubes.png');
        background-repeat: repeat;
        background-size: 80px 80px;
        color: #dfe6e9;
    }

    /* Content box transparency and rounding */
    .css-1d391kg, .css-1d391kg {
        background-color: rgba(24,25,29,0.75) !important;
        border-radius: 12px !important;
    }

    /* Headings color */
    h1, h2, h3, h4 {
        color: #81ecec !important;
    }

    /* Styled links */
    a { 
        color: #00cec9 !important; 
        font-weight: 600;
        text-decoration: underline;
    }

    /* Large, modern navigation buttons */
    .stButton > button {
        background-color: #0984e3 !important;
        color: white !important;
        border-radius: 15px !important;
        font-size: 1.4rem !important;
        font-weight: 700;
        padding: 1rem 1.25rem !important;
        width: 100% !important;
        box-shadow: 0 4px 15px 0 #00cec955;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #74b9ff !important;
        color: #2c3e50 !important;
        box-shadow: 0 8px 30px 0 #00cec997;
    }
    .stButton > button:focus {
        outline: none !important;
        box-shadow: 0 0 0 3px #55efc4 !important;
    }

    /* Expander header style */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        color: #55efc4 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- URL Routing ---
query_params = st.query_params
current_page = query_params.get("page", "home")

# --- Navigation Helper ---
def go_to(page):
    st.query_params.page = page

def section_header(title):
    st.markdown(f"<h2 style='color:#81ecec; border-bottom: 2px solid #00cec9; padding: 0.4em 0'>{title}</h2>", unsafe_allow_html=True)

def box_highlight(content):
    st.markdown(f"""
    <div style="background-color: rgba(0,188,212,0.15); padding:12px; border-radius:8px; margin-bottom:15px; box-shadow: 0 0 8px #00cec9;">
        {content}
    </div>
    """, unsafe_allow_html=True)

# -------- HOME --------
def page_home():
    section_header("📘 Welcome to the Learning Hub by Ashwik Bire")

    st.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)

    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Select a learning path from the options below to get started. Each path includes detailed tutorials, quizzes, and resources.</p>", unsafe_allow_html=True)

    cols = st.columns(6, gap="large")
    # Learning Material is first as requested
    page_buttons = [
        ("Learning Material", "material"),
        ("Data Science", "data_science"),
        ("Data Analytics", "data_analytics"),
        ("Microsoft Excel", "excel"),
        ("Power BI", "power_bi"),
        ("Artificial Intelligence", "ai")
    ]
    for col, (label, key) in zip(cols, page_buttons):
        with col:
            st.button(label, key=f"btn_{key}", on_click=lambda page=key: go_to(page))

    st.markdown("---")
    section_header("🎥 Featured Tutorials")
    vids = [
        "https://www.youtube.com/watch?v=IBnLsKOhpyU",
        "https://www.youtube.com/watch?v=DsI1vG-kXR8",
        "https://www.youtube.com/watch?v=7ny5ljw6NbI",
        "https://www.youtube.com/watch?v=AGrl-H87pRU",
        "https://www.youtube.com/watch?v=2ePf9rue1Ao"
    ]
    cols_vid = st.columns(5, gap="medium")
    for col, vid in zip(cols_vid, vids):
        col.video(vid)

    st.markdown("<p style='font-size:1.1rem; font-weight:bold; color:#55efc4;'>Connect with Ashwik Bire on <a href='https://linkedin.com/in/ashwik-bire-b2a000186' target='_blank' style='color:#00cec9;'>LinkedIn</a> for updates and mentorship.</p>", unsafe_allow_html=True)


# -------- LEARNING MATERIAL PAGE --------
def page_material():
    section_header("📚 Learning Materials")

    st.markdown("<p style='font-size:1.12rem; color:#dfe6e9;'>A central hub of downloadable guides, recommended books, video courses, and reading lists for all disciplines. Explore, download, and bookmark your favorites.</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📝 Downloadable Guides & Cheat Sheets")
    st.markdown("""
- 📥 [Data Science Cheat Sheet PDF (DataCamp)](https://assets.datacamp.com/blog_assets/Data_Science_Cheat_Sheet_Python.pdf)
- 📥 [Data Analytics Cheat Sheet (Analytics Vidhya)](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)
- 📥 [Excel Quick Reference (ExcelJet)](https://cdn.exceljet.net/sites/default/files/downloads/ExcelJet_Excel_cheat_sheet.pdf)
- 📥 [Power BI Learning Guide (Microsoft)](https://learn.microsoft.com/en-us/power-bi/guided-learning/overview)
- 📥 [AI Fundamentals Guide (Google)](https://ai.google/education/)
    """)

    st.markdown("---")
    st.subheader("📚 Books & Further Reading")
    with st.expander("Data Science"):
        st.markdown("""
- *Python Data Science Handbook* — Jake VanderPlas ([Link](https://jakevdp.github.io/PythonDataScienceHandbook/))
- *Hands-On Machine Learning with Scikit-Learn & TensorFlow* — Aurélien Géron
- *Storytelling With Data* — Cole Nussbaumer Knaflic
        """)
    with st.expander("Analytics & BI"):
        st.markdown("""
- *Data Analytics Made Accessible* — A. Maheshwari
- *The Big Book of Dashboards* — Steve Wexler et al.
- *Data Visualization: A Practical Introduction* — Kieran Healy
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
- *Deep Learning* — Ian Goodfellow et al. ([Online Book](https://www.deeplearningbook.org/))
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
- [Chandoo.org (Excel)](https://chandoo.org/wp/)
    """)

    st.markdown("---")
    st.subheader("🎬 Recommended Playlists")
    st.markdown("""
- [Data Science Full Courses](https://www.youtube.com/playlist?list=PLF797E961509B4EB5)
- [Power BI Training](https://www.youtube.com/playlist?list=PL1N57mwBHtN0JFoWOGou-6BjdQY7fjalY)
- [Python for Everybody - Coursera](https://www.youtube.com/playlist?list=PLl_Xou7GtCi6VPp8FDiirp-1oMujyFgRO)
    """)
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# For brevity, placeholders for other existing pages, remain here for integration:
def page_data_science():
    st.write("Full Data Science Page content here...")

def page_data_analytics():
    st.write("Full Data Analytics Page content here...")

def page_excel():
    st.write("Full Microsoft Excel Page content here...")

def page_power_bi():
    st.write("Full Power BI Page content here...")

def page_ai():
    st.write("Full Artificial Intelligence Page content here...")

# --- PAGE ROUTING ---
pages = {
    "home": page_home,
    "material": page_material,
    "data_science": page_data_science,
    "data_analytics": page_data_analytics,
    "excel": page_excel,
    "power_bi": page_power_bi,
    "ai": page_ai
}

pages.get(current_page, lambda: (
    st.error("Page not found."),
    st.button("Back to Home", on_click=lambda: go_to("home"))
))()

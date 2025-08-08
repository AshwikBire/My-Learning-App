import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub by Ashwik Bire", layout="wide", page_icon="📘")

# Custom CSS for dark translucent developer-style look and advanced button UI
st.markdown("""
<style>
    /* Background with subtle cubes pattern and dark translucent overlay */
    .stApp {
        background:
          linear-gradient(rgba(0, 0, 0, 0.92), rgba(0,0,0,0.92)),
          url('https://www.transparenttextures.com/patterns/cubes.png');
        background-size: 80px 80px;
        color: #dfe6e9;
    }
    /* Content box style */
    .css-1d391kg {
        background-color: rgba(24,25,29,0.75) !important;
        border-radius: 12px !important;
    }
    /* Headings color */
    h1, h2, h3, h4 {
        color: #81ecec !important;
    }
    /* Links */
    a { 
        color: #00cec9 !important; 
        font-weight: 600;
        text-decoration: underline;
    }
    /* Buttons */
    .stButton > button {
        background-color: #0984e3 !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: 700;
        font-size: 1.05rem;
        padding: 0.75rem 1.25rem;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        width: 100%;
        box-shadow: 0 2px 10px 0 #00cec9aa;
    }
    .stButton > button:hover {
        background-color: #74b9ff !important;
        color: #2c3e50 !important;
        box-shadow: 0 5px 20px 0 #00cec9cc;
    }
    /* Expander header style */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 6px !important;
        font-weight: 600;
        color: #55efc4 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Routing ---
query_params = st.query_params
current_page = query_params.get("page", "home")

# Navigation Helper
def go_to(page):
    st.query_params.page = page

def section_header(label):
    st.markdown(
        f"<h2 style='color:#81ecec; border-bottom:2px solid #00cec9; padding-bottom:8px;'>{label}</h2>", unsafe_allow_html=True
    )

def button_fullwidth(label, key, target):
    if st.button(label, key=key):
        go_to(target)

# -------- HOME PAGE --------
def page_home():
    section_header("📚 Welcome to the Learning Hub by Ashwik Bire")
    st.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)
    
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Use the buttons below to navigate through the courses and materials.</p>", unsafe_allow_html=True)

    cols = st.columns(6, gap="large")
    with cols[0]:
        button_fullwidth("📚 Learning Material", "btn_material", "material")
    with cols[1]:
        button_fullwidth("📊 Data Science", "btn_ds", "data_science")
    with cols[2]:
        button_fullwidth("📈 Data Analytics", "btn_da", "data_analytics")
    with cols[3]:
        button_fullwidth("📑 Microsoft Excel", "btn_excel", "excel")
    with cols[4]:
        button_fullwidth("📊 Power BI", "btn_pbi", "power_bi")
    with cols[5]:
        button_fullwidth("🤖 Artificial Intelligence", "btn_ai", "ai")

    st.markdown("---")
    section_header("🎥 Featured Tutorials")
    vids = [
        "https://www.youtube.com/watch?v=IBnLsKOhpyU",
        "https://www.youtube.com/watch?v=DsI1vG-kXR8",
        "https://www.youtube.com/watch?v=7ny5ljw6NbI",
        "https://www.youtube.com/watch?v=AGrl-H87pRU",
        "https://www.youtube.com/watch?v=2ePf9rue1Ao",
    ]
    columns = st.columns(5, gap="medium")
    for c, v in zip(columns, vids):
        c.video(v)

    st.markdown(
        "<p style='font-size:1.1rem; font-weight:bold; color:#55efc4;'>Connect with Ashwik Bire on "
        "<a href='https://linkedin.com/in/ashwik-bire-b2a000186' target='_blank' style='color:#00cec9;'>LinkedIn</a> for mentorship and updates.</p>",
        unsafe_allow_html=True,
    )


# -------- LEARNING MATERIAL PAGE --------
def page_material():
    section_header("📚 Learning Materials Library")
    st.markdown("<p style='font-size:1.12rem;color:#dfe6e9;'>Curated guides, cheat sheets, and recommended books across all topics.</p>", unsafe_allow_html=True)

    st.subheader("📝 Downloadable Resources")
    st.markdown("""
- ✔️ [Data Science Cheat Sheet (DataCamp PDF)](https://assets.datacamp.com/blog_assets/Data_Science_Cheat_Sheet_Python.pdf)
- ✔️ [Data Analytics Guide (Analytics Vidhya)](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)
- ✔️ [Excel Cheat Sheet (ExcelJet PDF)](https://cdn.exceljet.net/sites/default/files/downloads/ExcelJet_Excel_cheat_sheet.pdf)
- ✔️ [Power BI Learning Guide (Microsoft)](https://learn.microsoft.com/en-us/power-bi/guided-learning/overview)
- ✔️ [AI Education Resources (Google)](https://ai.google/education/)
    """)

    st.subheader("📚 Recommended Books and Reading")
    with st.expander("Data Science"):
        st.markdown("""
- *Python Data Science Handbook* — Jake VanderPlas ([Online](https://jakevdp.github.io/PythonDataScienceHandbook/))
- *Hands-On Machine Learning* — Aurélien Géron
- *Storytelling With Data* — Cole Nussbaumer Knaflic
        """)
    with st.expander("Data Analytics & BI"):
        st.markdown("""
- *Data Analytics Made Accessible* — A. Maheshwari
- *Data Visualization: A Practical Introduction* — Kieran Healy
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
- *Deep Learning* — Ian Goodfellow et al. ([Online Book](https://www.deeplearningbook.org/))
- *Make Your Own Neural Network* — Tariq Rashid
        """)

    st.subheader("🌎 Top Learning Portals & Blogs")
    st.markdown("""
- [Microsoft Learn](https://learn.microsoft.com/)
- [Kaggle Learn](https://www.kaggle.com/learn)
- [Google AI Blog](https://ai.googleblog.com/)
- [Towards Data Science](https://towardsdatascience.com/)
- [DataCamp Community](https://www.datacamp.com/community)
- [Analytics Vidhya](https://www.analyticsvidhya.com/)
- [Chandoo.org (Excel)](https://chandoo.org/wp/)
    """)

    st.subheader("🎬 Recommended Video Playlists")
    st.markdown("""
- [Data Science Full Courses Playlist](https://www.youtube.com/playlist?list=PLF797E961509B4EB5)
- [Power BI Tutorials Playlist](https://www.youtube.com/playlist?list=PL1N57mwBHtN0JFoWOGou-6BjdQY7fjalY)
- [Python for Everybody (Coursera Playlist)](https://www.youtube.com/playlist?list=PLl_Xou7GtCi6VPp8FDiirp-1oMujyFgRO)
    """)

    st.button("Back to Home", on_click=lambda: go_to("home"))

# -------- Placeholder pages: For brevity, just display page names.
def page_data_science():
    section_header("Data Science Learning")
    st.markdown("Full Data Science content will appear here.")

def page_data_analytics():
    section_header("Data Analytics Curriculum")
    st.markdown("Full Data Analytics content will appear here.")

def page_excel():
    section_header("Microsoft Excel Essentials")
    st.markdown("Full Microsoft Excel course content will appear here.")

def page_power_bi():
    section_header("Microsoft Power BI Fundamentals")
    st.markdown("Full Power BI course content will appear here.")

def page_ai():
    section_header("Artificial Intelligence Fundamentals")
    st.markdown("Full Artificial Intelligence course content will appear here.")


# --- PAGE ROUTING ---
pages = {
    "home": page_home,
    "material": page_material,
    "data_science": page_data_science,
    "data_analytics": page_data_analytics,
    "excel": page_excel,
    "power_bi": page_power_bi,
    "ai": page_ai,
}

pages.get(current_page, lambda: st.error("Page not found. Click below to return."))()
if current_page not in pages:
    st.button("Back to Home", on_click=lambda: go_to("home"))

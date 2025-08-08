import streamlit as st

# ------------------ PAGE SETUP --------------------
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# ------------------ DARK DEV STYLE CSS -------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: 
        linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.9)),
        url('https://www.transparenttextures.com/patterns/cubes.png');
    background-repeat: repeat;
    background-size: 80px 80px;
    color: #dfe6e9;
    font-family: 'Segoe UI', sans-serif;
}

/* Buttons in grid cards */
.custom-card {
    background-color: rgba(255,255,255,0.06);
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    text-align: center;
    transition: all 0.3s ease;
    cursor: pointer;
    margin-bottom: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}
.custom-card:hover {
    background-color: rgba(0,123,255,0.2);
    transform: scale(1.02);
}

/* Header styling */
h1, h2, h3 {
    color: #81ecec !important;
}
a {
    color: #00cec9 !important;
    text-decoration: underline;
    font-weight: bold;
}
.linear-title {
    font-size:1.5rem;
    font-weight:700;
    color:#00cec9;
    letter-spacing: 0.5px;
}

/* LinkedIn */
.linkedin {
    color: #55efc4;
    font-size: 1.05rem;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)


# ------------------ PAGE NAVIGATION --------------------
query_params = st.query_params
current_page = query_params.get("page", "home")
def go_to(page):
    st.query_params.page = page


# ------------------ UI HELPERs -------------------------
def tile(label, icon, page_name):
    col = st.container()
    with col:
        st.markdown(f"""
            <div class='custom-card' onclick="window.location.href='?page={page_name}'">
                <h3 style="margin-bottom: 10px;">{icon}</h3>
                <p class="linear-title">{label}</p>
            </div>
        """, unsafe_allow_html=True)

def section_header(text):
    st.markdown(f"<h2 class='linear-title'>{text}</h2>", unsafe_allow_html=True)


# ------------------ HOME PAGE -------------------------
def page_home():
    section_header("Ashwik Bire’s Learning Hub")
    st.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)

    st.markdown("### 📦 Select a learning path:")
    st.write("Explore dedicated content for each domain:")

    col1, col2, col3 = st.columns(3)
    with col1:
        tile("📚 Learning Materials", "📁", "material")
    with col2:
        tile("📊 Data Science", "📈", "data_science")
    with col3:
        tile("🧮 Data Analytics", "📉", "data_analytics")

    col4, col5, col6 = st.columns(3)
    with col4:
        tile("🧾 Microsoft Excel", "📊", "excel")
    with col5:
        tile("📊 Power BI", "📊", "power_bi")
    with col6:
        tile("🤖 Artificial Intelligence", "🤖", "ai")

    st.divider()
    section_header("📺 Featured Tutorials")
    col_a, col_b, col_c = st.columns(3)
    col_a.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")  # DS
    col_b.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")  # Excel
    col_c.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")  # AI

    st.markdown("### 👤 Connect with Ashwik Bire")
    st.markdown("""
    <p class='linkedin'>
        📎 <a href='https://linkedin.com/in/ashwik-bire-b2a000186' target='_blank'>LinkedIn Profile</a>
    </p>
    """, unsafe_allow_html=True)


# ------------------ LEARNING MATERIAL PAGE -------------------------
def page_material():
    section_header("🗂️ Learning Materials Library")
    st.markdown("""
Browse essential downloads, cheat sheets, reading lists, books and official course links.
    """)

    st.subheader("📥 Downloads & Cheat Sheets")
    st.markdown("""
- ✅ [Data Science PDF (DataCamp)](https://assets.datacamp.com/blog_assets/Data_Science_Cheat_Sheet_Python.pdf)
- ✅ [Analytics Guide (AV Cheat Sheet)](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)
- ✅ [Excel Guide](https://cdn.exceljet.net/sites/default/files/downloads/ExcelJet_Excel_cheat_sheet.pdf)
- ✅ [Power BI Learn Hub](https://learn.microsoft.com/en-us/power-bi/guided-learning/overview)
- ✅ [Google AI Education](https://ai.google/education/)
    """)

    st.subheader("📚 Book Picks & Reading")
    with st.expander("📘 Data Science"):
        st.markdown("- [Python DS Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)\n- [Hands-On ML - O'Reilly](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/)\n- [Storytelling with Data](https://www.storytellingwithdata.com/books)")

    with st.expander("📖 Data Analytics"):
        st.markdown("- [Data Analytics Made Accessible](https://www.academia.edu/41198364/Data_Analytics_Made_Accessible_pdf)\n- [Practical Data Visualization](https://socviz.co/)\n- [Dashboards Book](http://www.thebigbookofdashboards.com/)")

    with st.expander("📊 Excel & Power BI"):
        st.markdown("- [Excel Bible](https://www.wiley.com/en-us/Excel+Bible%2C+2021+Edition-p-9781119835246)\n- [Mastering Power BI](https://www.packtpub.com/product/mastering-microsoft-power-bi-second-edition/9781801810076)")

    with st.expander("🤖 Artificial Intelligence"):
        st.markdown("- [AI: Intelligent Systems](https://archive.org/details/artificialintell00negn_0)\n- [Deep Learning Book](https://www.deeplearningbook.org)\n- [Make Your Own Neural Network](https://www.makeyourownneuralnetwork.com)")

    st.subheader("🧭 Portals & MOOCs")
    st.markdown("""
- [Microsoft Learn](https://learn.microsoft.com/)
- [Kaggle Courses](https://www.kaggle.com/learn)
- [DataCamp](https://datacamp.com/)
- [Coursera](https://coursera.org/)
- [Google Crash Course](https://developers.google.com/machine-learning/crash-course)
    """)

    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)


# ------------------ PAGE ROUTER -------------------------
if current_page == "home":
    page_home()
elif current_page == "material":
    page_material()
# Placeholder - You can plug your fully developed `page_data_science()` and others here
elif current_page == "data_science":
    st.info("⚠️ Data Science page coming soon...")
elif current_page == "data_analytics":
    st.info("⚠️ Data Analytics page coming soon...")
elif current_page == "excel":
    st.info("📊 Excel content coming soon...")
elif current_page == "power_bi":
    st.info("📊 Power BI content coming soon...")
elif current_page == "ai":
    st.info("🤖 AI content coming soon...")
else:
    st.error("Page not found. Click below to return.")
    st.button("Back to Home", on_click=lambda: go_to("home"))

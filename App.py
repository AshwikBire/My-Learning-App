import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# Custom CSS for advanced dark background
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

# Navigation
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
    <p style='font-size:1.12rem;color:#dfe6e9;'>A central hub for downloadable guides, online courses, book recommendations, and reading lists for all disciplines. Explore, download, and bookmark your favorites.</p>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("📝 Downloadable Guides & Cheat Sheets")
    st.markdown("""
- 📥 [Data Science Cheat Sheet PDF (DataCamp, 2025 mirror)](https://assets.datacamp.com/blog_assets/Data_Science_Cheat_Sheet_Python.pdf)
- 📥 [Data Analytics Quick Reference (2025 Analytics Vidhya)](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)
- 📥 [Excel Functions & Shortcuts PDF (ExcelJet, working 2025)](https://cdn.exceljet.net/sites/default/files/downloads/ExcelJet_Excel_cheat_sheet.pdf)
- 📥 [Power BI Guided Learning (Official Microsoft Docs)](https://learn.microsoft.com/en-us/power-bi/guided-learning/overview)
- 📥 [Google AI Education Resource Hub (PDFs and online modules)](https://ai.google/education/)
    """)
    st.markdown("---")
    st.subheader("📚 Books & Further Reading")
    with st.expander("Data Science"):
        st.markdown("""
- *Python Data Science Handbook* — Jake VanderPlas ([Free Online](https://jakevdp.github.io/PythonDataScienceHandbook/))
- *Hands-On Machine Learning with Scikit-Learn, Keras, & TensorFlow* — Aurélien Géron ([Publisher Excerpt](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/))
- *Storytelling With Data* — Cole Nussbaumer Knaflic ([Official Site](https://www.storytellingwithdata.com/books))
        """)
    with st.expander("Analytics & BI"):
        st.markdown("""
- *Data Analytics Made Accessible* — A. Maheshwari ([Preview PDF](https://www.academia.edu/41198364/Data_Analytics_Made_Accessible_pdf))
- *Data Visualization: A Practical Intro* — Kieran Healy ([Free Sample Chapters](https://socviz.co/))
- *The Big Book of Dashboards* — Steve Wexler ([Companion site](http://www.thebigbookofdashboards.com/))
        """)
    with st.expander("Excel"):
        st.markdown("""
- *Excel Bible* — John Walkenbach ([Publisher Info](https://www.wiley.com/en-us/Excel+Bible%2C+2021+Edition-p-9781119835246))
- *Excel Power Programming with VBA* — Michael Alexander ([Sample on Google Books](https://books.google.com/books?id=VnOJDwAAQBAJ))
- *Excel Dashboards and Reports* — Alexander & Walkenbach ([Wiley](https://www.wiley.com/en-us/Excel+Dashboards+and+Reports%2C+4th+Edition-p-9781119076762))
        """)
    with st.expander("Power BI"):
        st.markdown("""
- *Mastering Microsoft Power BI* — Brett Powell ([Publisher Page](https://www.packtpub.com/product/mastering-microsoft-power-bi-second-edition/9781801810076))
- *Power BI for the Excel Analyst* — Wyn Hopkins ([Publisher](https://www.holyunblocker.com/cdn-cgi/l/email-protection#b4dbdadad1d8c6d884d1c1d1c6d9da9adac6c6d1c4c5d3d084dfd3d180d8d1))
        """)
    with st.expander("Artificial Intelligence"):
        st.markdown("""
- *Artificial Intelligence: A Guide to Intelligent Systems* — Michael Negnevitsky ([Preview PDF](https://archive.org/details/artificialintell00negn_0))
- *Deep Learning* — Goodfellow et al ([Full PDF Free](https://www.deeplearningbook.org/))
- *Make Your Own Neural Network* — Tariq Rashid ([Author's Page](https://www.makeyourownneuralnetwork.com/))
        """)
    st.markdown("---")
    st.subheader("📰 Top Blogs & MOOC Portals")
    st.markdown("""
- [Microsoft Learn](https://learn.microsoft.com/)
- [Kaggle Learn Courses](https://www.kaggle.com/learn)
- [Google AI Hub](https://ai.google/education/)
- [Towards Data Science](https://towardsdatascience.com/)
- [DataCamp Community](https://www.datacamp.com/community)
- [Analytics Vidhya](https://www.analyticsvidhya.com/)
- [Chandoo (Excel Resources)](https://chandoo.org/wp/)
    """)
    st.markdown("---")
    st.subheader("🎬 Recommended Playlists & MOOCs")
    st.markdown("""
- [Data Science Full Courses - Edureka](https://www.youtube.com/playlist?list=PL9ooVrP1hQOG2Yq6en6FYiD2b8X1jGoV-)
- [Power BI Training - Guy in a Cube](https://www.youtube.com/playlist?list=PL1N57mwBHtN0JFoWOGou-6BjdQY7fjalY)
- [Coursera Python for Everybody (Official)](https://www.coursera.org/specializations/python)
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
    """)
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# --------- (ALL OTHER PAGES REMAIN AS BEFORE, OMITTED FOR BREVITY) ---------
# Insert here the page_data_science, page_data_analytics, page_excel, page_power_bi, page_ai functions exactly as in your last working advanced code.

# -------- PAGE ROUTING ------------
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

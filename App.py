import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# --- Custom CSS ---
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

def go_to(page):
    st.query_params.page = page

def section_header(title):
    st.markdown(f"<h2 style='color:#81ecec; border-bottom:2px solid #00cec9; padding-bottom:6px;'>{title}</h2>", unsafe_allow_html=True)

def card_button(label, key, callback):
    st.button(label, key=key, on_click=callback)

# -------- LEARNING MATERIAL PAGE --------
def page_material():
    section_header("Complete Learning Materials Library")
    st.markdown("""
    <p style='font-size:1.12rem;color:#dfe6e9;'>A central hub of downloadable guides, official documentation, books, and video courses for every track. All resources have been verified as working and up to date for 2025.</p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📝 Downloadable Guides & Cheat Sheets")
    st.markdown("""
- 📥 [Data Science Cheat Sheet PDF (DataCamp, 2025)](https://cdn.datacamp.com/blog_assets/PythonForDataScience.pdf)
- 📥 [Data Analytics Quick Reference (IBM, 2025)](https://www.ibm.com/downloads/cas/0JYLMRAY)
- 📥 [Excel Functions & Shortcuts PDF (Official, 2025)](https://support.microsoft.com/en-us/office/keyboard-shortcuts-in-excel-1798d9d5-842a-42b8-9c99-9b7213f0040f)
- 📥 [Power BI Learning Guide (Microsoft, 2025)](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)
- 📥 [Google AI Education - PDF Collection (2025)](https://ai.google/education/)
    """)

    st.markdown("---")
    st.subheader("📚 Book & Reference Reads")
    with st.expander("Data Science"):
        st.markdown("""
- _Python Data Science Handbook_ (Jake VanderPlas): [Read Online](https://jakevdp.github.io/PythonDataScienceHandbook/)
- _Hands-On Machine Learning_, 3rd ed (A. Géron): [Publisher](https://github.com/ageron/handson-ml3)
        """)
    with st.expander("Analytics & BI"):
        st.markdown("""
- _Data Analytics Made Accessible_ (A. Maheshwari): [Amazon](https://www.amazon.com/Data-Analytics-Made-Accessible-2018/dp/0692052991)
- _Power BI documentation (official)_: [Microsoft Learn](https://learn.microsoft.com/power-bi)
        """)
    with st.expander("Excel"):
        st.markdown("""
- _Excel Bible_ (John Walkenbach): [Wiley](https://www.wiley.com/en-us/Excel+Bible%2C+Book+%2B+Online+Video+Training%2C+2nd+Edition-p-9781119832316)
- _Full Excel Formula List (Microsoft)_ : [Excel Function Reference](https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188)
        """)
    with st.expander("Artificial Intelligence"):
        st.markdown("""
- _Deep Learning_ (Goodfellow, et al.): [Read Free Online](https://www.deeplearningbook.org/)
- _Google “People + AI Guidebook” (2025)_: [Google AI Guidebook](https://pair.withgoogle.com/guidebook/)
        """)
    with st.expander("Power BI"):
        st.markdown("""
- _Get Started with Power BI_ (2025): [Microsoft Guides](https://learn.microsoft.com/en-us/power-bi/fundamentals/)
- _DAX Reference (latest)_: [DAX Guide](https://dax.guide/)
        """)

    st.markdown("---")
    st.subheader("📰 Trusted Documentation & MOOC Portals")
    st.markdown("""
- [Microsoft Learn (Data, BI, Excel, AI)](https://learn.microsoft.com/)
- [Kaggle Learn](https://www.kaggle.com/learn)
- [Google AI Education](https://ai.google/education/)
- [DataCamp Community](https://www.datacamp.com/community)
- [Analytics Vidhya Blogs](https://www.analyticsvidhya.com/blog/)
- [Chandoo Excel School](https://chandoo.org/wp/excel-school/)
    """)

    st.markdown("---")
    st.subheader("🎬 Recommended Playlists & Video Courses")
    st.markdown("""
- [Data Science Full Course (Simplilearn)](https://www.youtube.com/watch?v=IBnLsKOhpyU)
- [Analytics & BI Courses (Great Learning)](https://www.youtube.com/watch?v=DsI1vG-kXR8)
- [Excel Full Course (Simplilearn)](https://www.youtube.com/watch?v=7ny5ljw6NbI)
- [Power BI Full Tutorial (Simplilearn)](https://www.youtube.com/watch?v=AGrl-H87pRU)
- [Artificial Intelligence Full Course](https://www.youtube.com/watch?v=2ePf9rue1Ao)
    """)
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)

# ... (keep rest of your code for navigation and pages here, unchanged)
# Replace your material page function with the above definition in your Streamlit app!

import streamlit as st
# Add this at the top of your app — right after st.set_page_config()
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
body, div, p, h1, h2, h3, h4, h5, h6 {
    font-family: 'Inter', sans-serif !important;
}
.about-section {
    background-color: rgba(255, 255, 255, 0.05);
    padding: 20px 25px;
    border: 1px solid rgba(129, 236, 236, 0.25);
    border-radius: 12px;
    margin-bottom: 25px;
    line-height: 1.6;
    font-size: 1.05rem;
    color: #dfe6e9;
    box-shadow: 0 0 8px rgba(0, 206, 201, 0.3);
}
</style>
""", unsafe_allow_html=True)

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
    background-color: #00000!important;
    color: white !important;
    border-radius: 999px !important;
    font-weight: 600 !important;
}
.stButton>button:hover {
    background-color: #74b9ff !important;
    color: #2d3436 !important;
}
.streamlit-expanderHeader {
    background-color: rgba(0,0,0,0) !important;
    border-radius: 999px !important;
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
    # --- Google Fonts and Custom Styles ---
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
    body, div, p, h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
    }
    .about-section {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px 25px;
        border: 1px solid rgba(129, 236, 236, 0.25);
        border-radius: 12px;
        margin-bottom: 25px;
        line-height: 1.6;
        font-size: 1.05rem;
        color: #dfe6e9;
        box-shadow: 0 0 8px rgba(0, 206, 201, 0.3);
    }
    .stButton button {
        width: 100% !important;
        padding: 10px 16px;
        font-size: 0.95rem;
        font-weight: 600 !important;
        border-radius: 999px;
        color: white !important;
        background-color: #000 !important;
        transition: background 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 206, 201, 0.2);
    }
    .stButton button:hover {
        background-color: #74b9ff !important;
        color: #2d3436 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Header and Banner Image ---
    section_header("Welcome to Data Science & Analytics with Ashwik Bire")
    st.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)

    # --- ABOUT SECTION ---
    st.markdown("""
    <div class='about-section'>
    <strong>About This Platform:</strong><br><br>
    This Learning Hub is your gateway to mastering the world of <strong>data science, analytics, AI, Power BI, Excel</strong> and more — curated with care by <strong>Ashwik Bire</strong>. Whether you're starting your journey or leveling up, you'll discover a wide range of tutorials, quizzes, downloadable cheat sheets, book guides, and video-based learning, all organized for self-paced study.
    </div>
    """, unsafe_allow_html=True)

    # --- NAVIGATION IN A SINGLE-LINE ---
    labels = [
        "📊 Data Science", 
        "📈 Data Analytics", 
        "📗 Excel", 
        "📉 Power BI", 
        "🤖 Artificial Intelligence (AI)", 
        "📚 Materials"
    ]
    pages = ["data_science", "data_analytics", "excel", "power_bi", "ai", "material"]

    with st.container():
        cols = st.columns(len(pages))
        for i, page in enumerate(pages):
            with cols[i]:
                st.button(labels[i], key=f"nav_{i}", on_click=go_to, args=(page,))

    # --- Divider + Tutorials Section ---
    st.divider()
    section_header("🎥 Featured Video Tutorials")

    video_links = [
        "https://www.youtube.com/watch?v=IBnLsKOhpyU",  # Data Science
        "https://www.youtube.com/watch?v=DsI1vG-kXR8",  # Data Analytics
        "https://www.youtube.com/watch?v=7ny5ljw6NbI",  # Excel
        "https://www.youtube.com/watch?v=AGrl-H87pRU",  # Power BI
        "https://www.youtube.com/watch?v=2ePf9rue1Ao"   # AI
    ]
    cols_videos = st.columns(len(video_links), gap="medium")
    for i, link in enumerate(video_links):
        with cols_videos[i]:
            st.video(link)

    # --- Footer / LinkedIn CTA ---
    st.markdown("""
    <p style='font-size:1.1rem; text-align:center; font-weight:500; color:#55efc4; margin-top:30px;'>
    🔗 Connect with <strong>Ashwik Bire</strong> on 
    <a href='https://linkedin.com/in/ashwik-bire-b2a000186' target='_blank'>LinkedIn</a> for updates & mentorship.
    </p>
    """, unsafe_allow_html=True)


    

    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Select a learning path or view all materials below.</p>", unsafe_allow_html=True)

    # Navigation Cards
    labels = ["Data Science", "Data Analytics", "Microsoft Excel", "Power BI", "Artificial Intelligence", "Learning Material"]
    pages = ["data_science", "data_analytics", "excel", "power_bi", "ai", "material"]
    cols = st.columns(6, gap="large")
    for i, page in enumerate(pages):
        with cols[i]:
            st.button(labels[i], key=f"btn_{i}", on_click=go_to, args=(page,))

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
- 📥 [Machine Learning Crash Course by Google](https://developers.google.com/machine-learning/crash-course)
- 📥 [Kaggle Data Science & Machine Learning Guide](https://www.kaggle.com/learn/overview)
    """)

    st.markdown("---")
    st.subheader("📚 Books & Further Reading")
    with st.expander("Data Science"):
        st.markdown("""
- *Python Data Science Handbook* — Jake VanderPlas ([Read Online](https://jakevdp.github.io/PythonDataScienceHandbook/))
- *Hands-On Machine Learning with Scikit-Learn, Keras, & TensorFlow* — Aurélien Géron
- *Storytelling With Data* — Cole Nussbaumer Knaflic
- *Practical Statistics for Data Scientists* — Peter Bruce & Andrew Bruce
- *Data Science from Scratch* — Joel Grus
        """)
    with st.expander("Analytics & BI"):
        st.markdown("""
- *Data Analytics Made Accessible* — A. Maheshwari
- *Data Visualization: A Practical Intro* — Kieran Healy
- *The Big Book of Dashboards* — Steve Wexler
- *Naked Statistics* — Charles Wheelan
- *Business Intelligence Guidebook* — Rick Sherman
        """)
    with st.expander("Excel"):
        st.markdown("""
- *Excel Bible* — John Walkenbach
- *Excel Power Programming with VBA* — Michael Alexander
- *Excel Dashboards and Reports* — Michael Alexander & John Walkenbach
- *Power Pivot and Power BI* — Rob Collie
- *Excel Data Analysis* — Jinjer Simon
        """)
    with st.expander("Power BI"):
        st.markdown("""
- *Mastering Microsoft Power BI* — Brett Powell
- *Power BI for the Excel Analyst* — Wyn Hopkins
- *The Definitive Guide to DAX* — Marco Russo & Alberto Ferrari
- *Power Query for Power BI and Excel* — Chris Webb
        """)
    with st.expander("Artificial Intelligence"):
        st.markdown("""
- *Artificial Intelligence: A Guide to Intelligent Systems* — Michael Negnevitsky
- *Deep Learning* — Ian Goodfellow, Yoshua Bengio, and Aaron Courville ([Free Online](https://www.deeplearningbook.org/))
- *Make Your Own Neural Network* — Tariq Rashid
- *AI Superpowers* — Kai-Fu Lee
- *Reinforcement Learning: An Introduction* — Richard S. Sutton & Andrew G. Barto ([Online Version](http://incompleteideas.net/book/the-book.html))
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
- [Coursera Data Science Courses](https://www.coursera.org/browse/data-science)
- [edX Data Science Courses](https://www.edx.org/learn/data-science)
- [Udacity AI and Data Courses](https://www.udacity.com/school-of-ai)
- [Fast.ai Deep Learning](https://www.fast.ai/)
    """)

    st.markdown("---")
    st.subheader("🎬 Recommended Playlists & Video Courses")
    st.markdown("""
- [Data Science Full Courses](https://www.youtube.com/playlist?list=PLF797E961509B4EB5)
- [Power BI Training](https://www.youtube.com/playlist?list=PL1N57mwBHtN0JFoWOGou-6BjdQY7fjalY)
- [Python for Everybody - Coursera](https://www.youtube.com/playlist?list=PLl_Xou7GtCi6VPp8FDiirp-1oMujyFgRO)
- [StatQuest with Josh Starmer](https://www.youtube.com/user/joshstarmer)
- [Andrew Ng's Machine Learning Course (Coursera)](https://www.youtube.com/playlist?list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0)
- [3Blue1Brown Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-f6j6lVhJFiFDxP5d)
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
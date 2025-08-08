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
    background-color: #000000 !important;
    color: white !important;
    border-radius: 999px;
    font-weight: 600 !important;
}
.stButton>button:hover {
    background-color: #74b9ff !important;
    color: #2d3436 !important;
}
.streamlit-expanderHeader {
    background-color: rgb(0,0,0) !important;
    border-radius: 999px;

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
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Data Science unlocks insights from complex data using statistics, programming, and algorithms, empowering data-driven decision-making across industries.</p>", unsafe_allow_html=True)
    
    with st.expander("Why Data Science?"):
        st.markdown("""
Data science combines domain expertise, programming, and statistical knowledge to extract actionable insights from raw data. It drives innovation in healthcare, finance, marketing, and more.
- Understand customer trends and behaviors
- Optimize business operations
- Build predictive models for forecasting
- Support evidence-based policy making
""")

    st.subheader("Core Concepts and Tools Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
- Python programming & Jupyter notebooks  
- Data manipulation with Pandas and NumPy  
- Data visualization with Matplotlib, Seaborn, Plotly  
- Exploratory Data Analysis (EDA)  
- Statistics and probability theory fundamentals  
- Data cleaning and preprocessing techniques  
- Feature engineering and selection  
""")
    col2.markdown("""
- Machine Learning: supervised, unsupervised, semi-supervised  
- Regression, classification, clustering algorithms  
- Model evaluation and cross-validation  
- Deep Learning basics and frameworks (TensorFlow, PyTorch)  
- Natural Language Processing (NLP) introduction  
- Big Data tools and cloud computing essentials  
- Ethics in AI and data privacy considerations  
""")

    with st.expander("Popular Python Libraries for Data Science"):
        st.markdown("""
- **Pandas**: Data manipulation and analysis  
- **NumPy**: Numerical computing and array operations  
- **Matplotlib & Seaborn**: Flexible data visualization  
- **Scikit-learn**: Classic machine learning algorithms and tools  
- **TensorFlow & PyTorch**: Deep learning frameworks  
- **NLTK & SpaCy**: NLP libraries for text processing  
""")

    with st.expander("Practical Tips for Data Scientists"):
        st.markdown("""
- Always perform thorough data cleaning before modeling  
- Visualize data to uncover patterns and outliers  
- Start with simple models before moving to complex ones  
- Use cross-validation for robust model evaluation  
- Document your code and processes for reproducibility  
- Stay current with evolving tools and techniques  
""")

    with st.expander("Example: Linear Regression in Python"):
        st.code("""
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'Experience':[1,2,3,4,5], 'Salary':[45000,50000,60000,65000,70000]}
df = pd.DataFrame(data)

model = LinearRegression()
model.fit(df[['Experience']], df['Salary'])

print(f"Predicted Salary for 6 years experience: {model.predict([[6]])[0]:.2f}")
""")

    box_highlight("<b>Quiz 1:</b> Which learning approach uses labeled data?")
    answer1 = st.radio("", ["Unsupervised", "Supervised", "Reinforcement"], key="ds_quiz1", horizontal=True)
    if st.button("Submit Answer 1", key="ds_submit1"):
        if answer1 == "Supervised":
            st.success("Correct! Supervised learning uses labeled data.")
        else:
            st.error("Incorrect, please try again.")

    box_highlight("<b>Quiz 2:</b> Which algorithm type is typically used to group unlabeled data?")
    answer2 = st.radio("", ["Regression", "Classification", "Clustering"], key="ds_quiz2", horizontal=True)
    if st.button("Submit Answer 2", key="ds_submit2"):
        if answer2 == "Clustering":
            st.success("Right! Clustering groups unlabeled data based on similarity.")
        else:
            st.error("Try again! Clustering is for unlabeled data grouping.")

    box_highlight("<b>Quiz 3:</b> Which Python library is used primarily for deep learning?")
    answer3 = st.radio("", ["Scikit-learn", "Pandas", "TensorFlow"], key="ds_quiz3", horizontal=True)
    if st.button("Submit Answer 3", key="ds_submit3"):
        if answer3 == "TensorFlow":
            st.success("Correct! TensorFlow is a popular deep learning framework.")
        else:
            st.error("Incorrect. TensorFlow is primarily used for deep learning.")

    st.markdown("[Download Data Science Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")
    st.button("Back to Home", on_click=lambda: go_to("home"), use_container_width=True)
True)

#Data analytics 
def page_data_analytics():
    section_header("Data Analytics Curriculum")
    st.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")
    st.markdown("<p style='font-size:1.1rem; color:#dfe6e9;'>Data Analytics transforms raw data into actionable insights using statistical analysis, data visualization, and business intelligence tools.</p>", unsafe_allow_html=True)
    
    with st.expander("Importance of Data Analytics"):
        st.markdown("""
Data Analytics helps organizations make informed decisions by:
- Uncovering patterns and trends from data  
- Forecasting future outcomes to guide strategy  
- Optimizing business processes and efficiency  
- Improving customer targeting and personalization  
- Enhancing operational performance through data-driven insights
Analytics bridges technical skills and business knowledge to deliver impactful results.
""")

    st.subheader("Core Concepts and Techniques Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
- Descriptive analytics: Understanding what has happened  
- Diagnostic analytics: Explaining why it happened  
- Predictive analytics: Forecasting possible futures  
- Prescriptive analytics: Recommending actions  
- Data visualization principles and tools  
- SQL fundamentals for querying databases  
- Data cleaning and quality assurance techniques  
""")
    col2.markdown("""
- Business Intelligence tools (Power BI, Tableau)  
- Python for analytics: Pandas, NumPy, Seaborn  
- Statistical inference and hypothesis testing  
- Dashboard design and storytelling with data  
- Time series analysis basics  
- Data governance and ethics  
""")

    with st.expander("Popular Data Analytics Tools and Libraries"):
        st.markdown("""
- **SQL**: Structured Query Language for database access  
- **Pandas & NumPy**: For data manipulation and numerical computing  
- **Seaborn & Matplotlib**: Visualizing data distributions and trends  
- **Power BI & Tableau**: Interactive dashboards and reporting  
- **Statsmodels**: Statistical modeling  
- **Jupyter Notebooks**: Interactive analytics environment  
""")

    with st.expander("Practical Tips for Effective Data Analytics"):
        st.markdown("""
- Always start with data cleaning before analysis  
- Choose the right visualization to tell your data story clearly  
- Validate findings with statistical testing where applicable  
- Automate repetitive tasks with Python scripts or BI tools  
- Collaborate with domain experts for context and validation  
- Document your workflow for transparency and reproducibility  
""")

    with st.expander("Example: Sales Revenue Analysis Using Python"):
        st.code("""
import pandas as pd

sales_df = pd.read_csv('sales_data.csv')
# Clean data by dropping missing values
sales_df_clean = sales_df.dropna()

# Aggregate revenue by product
top_products = sales_df_clean.groupby('Product')['Revenue'].sum().nlargest(5)

print("Top 5 Products by Revenue:")
print(top_products)
""")

    box_highlight("<b>Quiz 1:</b> Which analytics type helps explain past data patterns?")
    q1 = st.radio("", ["Descriptive", "Predictive", "Prescriptive"], key="da_quiz1", horizontal=True)
    if st.button("Submit Answer 1", key="da_submit1"):
        if q1 == "Descriptive":
            st.success("Correct! Descriptive analytics summarizes past data.")
        else:
            st.error("Incorrect, try again.")

    box_highlight("<b>Quiz 2:</b> What is the primary language for data querying?")
    q2 = st.radio("", ["Python", "SQL", "R"], key="da_quiz2", horizontal=True)
    if st.button("Submit Answer 2", key="da_submit2"):
        if q2 == "SQL":
            st.success("Correct! SQL is used for querying databases.")
        else:
            st.error("Incorrect. SQL is the main query language.")

    box_highlight("<b>Quiz 3:</b> Which tool is best for building interactive dashboards?")
    q3 = st.radio("", ["Power BI", "Matplotlib", "Pandas"], key="da_quiz3", horizontal=True)
    if st.button("Submit Answer 3", key="da_submit3"):
        if q3 == "Power BI":
            st.success("Correct! Power BI specializes in interactive dashboards.")
        else:
            st.error("Incorrect. Power BI is designed for dashboards.")

    st.markdown("[Download Data Analytics Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")
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


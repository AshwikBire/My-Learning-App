import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Learning Hub", page_icon="📚", layout="wide")

# Get current page (defaults to 'home')
query_params = st.query_params
current_page = query_params.get("page", "home")

# Navigation Helper
def go_to(page):
    st.query_params.page = page


# ------------------- Pages -------------------

# -------- HOME --------
def page_home():
    st.title("📚 Learn Data Science, Analytics, Excel, Power BI, AI & Machine Learning")
    st.subheader("All-in-One Learning Platform for Beginners & Professionals")

    # Banner image from local repo
    st.image("banner.png", caption="Data Science & Analytics Course with Ashwik Bire", use_container_width=True)

    st.markdown("### 🚀 Choose a Learning Path:")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.button("📊 Data Science", on_click=lambda: go_to("data_science"))
    with col2:
        st.button("📈 Data Analytics", on_click=lambda: go_to("data_analytics"))
    with col3:
        st.button("📑 MS Excel", on_click=lambda: go_to("excel"))
    with col4:
        st.button("📊 Power BI", on_click=lambda: go_to("power_bi"))
    with col5:
        st.button("🤖 Artificial Intelligence", on_click=lambda: go_to("ai"))
    with col6:
        st.button("📚 Machine Learning", on_click=lambda: go_to("machine_learning"))

    st.divider()

    st.subheader("🎥 Featured YouTube Tutorials")
    col_a, col_b, col_c, col_d, col_e, col_f = st.columns(6)
    col_a.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")  # Data Science Full Course 2025
    col_b.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")  # Data Analytics 2025
    col_c.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")  # Excel Full Course 2025
    col_d.video("https://www.youtube.com/watch?v=AGrl-H87pRU")  # Power BI Full Tutorial
    col_e.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")  # AI Full Course for Beginners
    col_f.video("https://www.youtube.com/watch?v=Gv9_4yMHFhI")  # Machine Learning Full Course

    st.divider()
    st.markdown("### 🔗 Connect with Ashwik Bire")
    st.markdown("[🔗 LinkedIn - Click here](https://linkedin.com/in/ashwik-bire-b2a000186)")


# -------- DATA SCIENCE --------
def page_data_science():
    st.title("📊 Data Science Learning")
    st.video("https://www.youtube.com/watch?v=IBnLsKOhpyU")  # Updated full course Data Science video

    st.markdown("""
    Data Science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data.

    **Key learning areas include:**
    - 🐍 Python programming with libraries like Pandas and NumPy for data manipulation.
    - 📊 Data cleaning, exploratory data analysis, and effective visualization.
    - 🤖 Machine learning concepts, including supervised, unsupervised learning, and model evaluation.
    - ⚙️ Data Engineering fundamentals for building data pipelines.
    """)

    with st.expander("💡 Why Data Science?"):
        st.markdown("""
        Data-driven decisions are now at the core of successful organizations worldwide. Data Scientists transform raw data into actionable insights that drive innovation, optimize operations, and create competitive advantages.

        This course will help you understand the lifecycle of data science projects—from data collection and cleaning to model building and deployment.
        """)

    st.subheader("💡 Concepts Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
    • Python & Jupyter notebooks basics  
    • Data structures & data manipulation  
    • Data visualization with Matplotlib and Seaborn  
    • Introduction to statistics and probability  
    • Data wrangling techniques and handling missing data  
    """)
    col2.markdown("""
    • Machine learning workflows  
    • Regression, classification, clustering algorithms  
    • Model validation and hyperparameter tuning  
    • Ethics and responsible AI  
    • Introduction to Big Data tools (Spark, Hadoop overview)  
    """)

    with st.expander("📚 Read More: Core Python for Data Science"):
        st.markdown("""
        Python is the most popular language in data science because of its readability and vast ecosystem. Learning Python essentials—like lists, dictionaries, functions, and modules—is crucial for performing complex data operations efficiently.

        Libraries like Pandas provide powerful data structures and functions making data cleaning and analysis straightforward.
        """)

    with st.expander("📚 Read More: Data Visualization Best Practices"):
        st.markdown("""
        Effective data visualization communicates insights clearly and efficiently. Choosing the right chart and using color effectively can highlight key patterns and trends, aiding decision makers to understand data narratives better.

        Learn different types of plots such as histograms, scatter plots, box plots, and heatmaps.
        """)

    with st.expander("💻 Example: Linear Regression in Python"):
        st.code("""
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'Experience': [1,2,3,4,5], 'Salary': [45000, 50000, 60000, 65000, 70000]}
df = pd.DataFrame(data)

X = df[['Experience']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

predicted_salary = model.predict([[6]])
print(f'Predicted salary for 6 years experience: ${predicted_salary[0]:.2f}')
        """)

    with st.expander("📚 Read More: Machine Learning Workflow"):
        st.markdown("""
        The machine learning workflow involves collecting data, preprocessing, feature engineering, model selection, training, evaluation, and deployment.

        Understanding this pipeline lets you build reliable models and improve them iteratively.
        """)

    with st.expander("🧠 Quiz"):
        answer = st.radio("Which machine learning approach uses labeled training data?", ["Unsupervised", "Supervised", "Reinforcement"])
        if st.button("Submit", key="ds_quiz_submit"):
            if answer == "Supervised":
                st.success("✅ Correct! Supervised learning uses labeled data.")
            else:
                st.error("❌ Incorrect, try again.")

    st.markdown("📥 [Download Data Science Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))


# -------- DATA ANALYTICS --------
def page_data_analytics():
    st.title("📈 Data Analytics Curriculum")
    st.video("https://www.youtube.com/watch?v=DsI1vG-kXR8")  # Updated analytics resource video

    st.markdown("""
    Data Analytics involves examining data sets to uncover patterns, trends, and insights to support decision-making.

    **Focus areas include:**
    - Data cleaning and preparation to ensure high quality.
    - Data summarization and visualization for storytelling.
    - Use of SQL and BI tools like Power BI and Tableau for interactive dashboards.
    - Introduction to statistical inference for data-driven decisions.
    """)

    with st.expander("💡 Importance of Data Analytics"):
        st.markdown("""
        Analytics enables organizations to convert data into knowledge. Effective analytics supports business intelligence, operational efficiency, and competitive strategy.

        You'll learn how to transform raw data into actionable insights using modern tools and techniques.
        """)

    st.subheader("💡 Topics Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
    • Types of analytics: descriptive, diagnostic, predictive, prescriptive   
    • Exploratory data analysis (EDA) techniques  
    • Data visualization best practices  
    • SQL fundamentals for querying  
    • Data quality assessment and cleaning  
    """)
    col2.markdown("""
    • Building dashboards with Power BI/Tableau  
    • Python toolkits: Pandas for data handling, Matplotlib/Seaborn for plots  
    • Statistical concepts: sampling, hypothesis testing  
    • Communicating insights through storytelling  
    """)

    with st.expander("📚 Read More: Power BI Fundamentals"):
        st.markdown("""
        Power BI helps visualize and share insights through interactive reports. You will learn to connect to various data sources, transform data using Power Query, and create dashboards.

        Understanding how to interpret these dashboards is essential for data-driven decisions.
        """)

    with st.expander("💻 Example: Basic Sales Data Analysis in Python"):
        st.code("""
import pandas as pd

sales_df = pd.read_csv('sales_data.csv')
sales_df_clean = sales_df.dropna()
top_products = sales_df_clean.groupby('Product')['Revenue'].sum().nlargest(5)

print(top_products)
        """)

    with st.expander("🧠 Quiz: Analytics Basics"):
        q = st.radio("Which analytics type forecasts future outcomes?", ["Descriptive", "Predictive", "Diagnostic"])
        if st.button("Submit", key="da_quiz_submit"):
            if q == "Predictive":
                st.success("✅ Correct! Predictive analytics forecasts future events.")
            else:
                st.error("❌ Incorrect. Try again.")

    st.markdown("📥 [Download Data Analytics Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))


# -------- EXCEL --------
def page_excel():
    st.title("📑 Microsoft Excel Essentials")
    st.video("https://www.youtube.com/watch?v=7ny5ljw6NbI")  # Updated Excel Full Course

    st.markdown("""
    Excel empowers you to organize, calculate, and visualize data effectively.

    Key learning outcomes:
    - Master formulas like SUM, AVERAGE, IF, VLOOKUP, and INDEX-MATCH.
    - Create PivotTables and PivotCharts for summarizing data.
    - Automate tasks and create custom functions using Macros and VBA.
    - Tips for spreadsheet management and collaboration.
    """)

    with st.expander("💡 Why Excel is Important"):
        st.markdown("""
        Excel remains one of the most widely used tools for data analysis across industries due to its flexibility and ease of use. Whether for financial modeling, reporting, or data visualization, proficiency in Excel is invaluable.

        Through this course, you'll gain skills to use Excel as a powerful analytics tool.
        """)

    st.subheader("🔑 Key Features Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
    • Cell referencing and formulas  
    • Lookup functions: VLOOKUP & INDEX-MATCH  
    • Data validation and conditional formatting  
    • Working with tables and structured references  
    """)
    col2.markdown("""
    • PivotTables and slicers  
    • Charts and dashboards  
    • Introduction to Macros and VBA scripting  
    • Collaboration tools and workbook sharing  
    """)

    with st.expander("📚 Read More: PivotTables Explained"):
        st.markdown("""
        PivotTables help summarize large datasets with drag-and-drop ease. You learn to aggregate data by categories, filter, and analyze trends quickly.

        This feature amplifies Excel’s power in transforming raw data into meaningful summaries.
        """)

    with st.expander("🧠 Quiz: Excel Basics"):
        ans = st.radio("Which function is used for horizontal lookup?", ["VLOOKUP", "HLOOKUP", "INDEX"])
        if st.button("Submit", key="excel_quiz_submit"):
            if ans == "HLOOKUP":
                st.success("✅ Correct! HLOOKUP searches rows horizontally.")
            else:
                st.error("❌ Incorrect, try again.")

    st.markdown("📥 [Download Excel Cheat Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))


# -------- POWER BI --------
def page_power_bi():
    st.title("📊 Microsoft Power BI Fundamentals")
    st.video("https://www.youtube.com/watch?v=AGrl-H87pRU")

    st.markdown("""
    Microsoft Power BI is a powerful business analytics tool that enables you to visualize your data and share insights across your organization or embed them in an app or website.

    **Learning Objectives:**
    - Understand Power BI components: Desktop, Service, and Mobile.
    - Learn to import and transform data using Power Query.
    - Build interactive reports and dashboards.
    - Use DAX (Data Analysis Expressions) for advanced data calculations.
    - Share and collaborate on reports within your organization.
    """)

    with st.expander("💡 Why Learn Power BI?"):
        st.markdown("""
        Power BI is widely used in enterprises for its ease of use and powerful data visualization capabilities. It bridges the gap between raw data and actionable business insights, enabling fast and informed decisions.

        Mastering Power BI can significantly boost your career in business intelligence and analytics.
        """)

    st.subheader("🔍 Key Features Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
    • Power BI Desktop interface overview  
    • Connecting to data sources (Excel, SQL, web, etc.)  
    • Data transformation and cleansing with Power Query  
    • Creating visuals: charts, maps, tables  
    """)
    col2.markdown("""
    • Using DAX for calculated columns and measures  
    • Designing interactive dashboards  
    • Publishing reports to Power BI Service  
    • Collaboration and sharing features  
    """)

    with st.expander("📚 Read More: Introduction to Power Query"):
        st.markdown("""
        Power Query is a data connection technology that enables you to discover, connect, combine, and refine data across a wide variety of sources.

        Learning Power Query lets you prepare your data easily and efficiently for analysis.
        """)

    with st.expander("🧠 Quiz: Power BI Basics"):
        ans = st.radio("Which Power BI component hosts your reports for sharing?", ["Power BI Desktop", "Power BI Service", "Power Query"])
        if st.button("Submit", key="powerbi_quiz_submit"):
            if ans == "Power BI Service":
                st.success("✅ Correct! Power BI Service lets you share and collaborate on reports.")
            else:
                st.error("❌ Incorrect, please try again.")

    st.markdown("📥 [Download Power BI Learning Guide (PDF)](https://docs.microsoft.com/en-us/power-bi/guided-learning/power-bi-learning-guide)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))


# -------- ARTIFICIAL INTELLIGENCE --------
def page_ai():
    st.title("🤖 Artificial Intelligence (AI) Fundamentals")
    st.video("https://www.youtube.com/watch?v=2ePf9rue1Ao")  # AI Full Course for Beginners

    st.markdown("""
    Artificial Intelligence (AI) is the simulation of human intelligence in machines programmed to think and learn. It encompasses various fields such as machine learning, natural language processing, robotics, and computer vision.

    **Core learning objectives include:**
    - Understanding AI concepts and history.
    - Exploring machine learning and deep learning fundamentals.
    - Overview of neural networks and natural language processing.
    - Ethical considerations and real-world AI applications.
    """)

    with st.expander("💡 Why Learn AI?"):
        st.markdown("""
        AI is transforming industries by enabling automation, improving decision-making, and creating innovative products. Learning AI opens doors to cutting-edge technology roles and helps solve complex problems.

        This course introduces you to AI's foundational principles and its practical uses.
        """)

    st.subheader("📘 Topics Covered")
    st.markdown("""
    • History and evolution of AI  
    • Machine learning algorithms: supervised, unsupervised, reinforcement  
    • Fundamentals of neural networks and deep learning  
    • Natural language processing basics  
    • AI ethics, bias, and societal impact  
    """)

    with st.expander("📚 Read More: Neural Networks Explained"):
        st.markdown("""
        Neural networks are computing systems inspired by the human brain. They consist of interconnected nodes (neurons) that process data in layers, enabling deep learning models to recognize patterns and make decisions.

        Understanding their architecture helps grasp how AI systems learn from data.
        """)

    with st.expander("🧠 Quiz: AI Basics"):
        ans = st.radio("Which AI technique involves learning from labeled data?", ["Reinforcement Learning", "Unsupervised Learning", "Supervised Learning"])
        if st.button("Submit", key="ai_quiz_submit"):
            if ans == "Supervised Learning":
                st.success("✅ Correct! Supervised learning uses labeled data.")
            else:
                st.error("❌ Incorrect, please try again.")

    st.markdown("📥 [Download AI Fundamentals Guide (PDF)](https://ai.google/education/)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))


# -------- MACHINE LEARNING --------
def page_machine_learning():
    st.title("📚 Machine Learning Mastery")
    st.video("https://www.youtube.com/watch?v=Gv9_4yMHFhI")  # Machine Learning Full Course

    st.markdown("""
    Machine Learning (ML) is a subset of AI focused on building systems that learn and improve from experience without being explicitly programmed. ML drives many modern applications such as recommendation systems, fraud detection, and autonomous vehicles.

    **Core topics include:**
    - Types of ML: supervised, unsupervised, reinforcement learning.
    - Key algorithms: linear regression, decision trees, clustering, neural networks.
    - Model evaluation and hyperparameter tuning.
    - Feature engineering and data preprocessing.
    """)

    with st.expander("💡 Why Machine Learning?"):
        st.markdown("""
        Machine Learning enables predictive and prescriptive analytics that drive smart decision-making. Understanding ML concepts and algorithms equips you with skills highly demanded in data-driven industries.

        This section guides you through practical and theoretical foundations to build effective ML models.
        """)

    st.subheader("🔍 Topics Covered")
    col1, col2 = st.columns(2)
    col1.markdown("""
    • Supervised learning: regression, classification  
    • Unsupervised learning: clustering, dimensionality reduction  
    • Reinforcement learning basics  
    • Feature engineering and scaling techniques  
    """)
    col2.markdown("""
    • Model selection and evaluation metrics  
    • Cross-validation and hyperparameter tuning  
    • Neural networks and deep learning introduction  
    • Tools: scikit-learn, TensorFlow, Keras overview  
    """)

    with st.expander("💻 Example: Decision Tree Classification"):
        st.code("""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
        """)

    with st.expander("📚 Read More: Model Evaluation Metrics"):
        st.markdown("""
        Understanding evaluation metrics such as accuracy, precision, recall, F1-score, and ROC-AUC is crucial for assessing model performance and making improvements.

        Learn about confusion matrix and its importance in classification tasks.
        """)

    with st.expander("🧠 Quiz: Machine Learning Basics"):
        ans = st.radio("Which ML type learns patterns without labeled data?", ["Supervised", "Unsupervised", "Reinforcement"])
        if st.button("Submit", key="ml_quiz_submit"):
            if ans == "
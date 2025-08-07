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
    st.title("📚 Learn Data Science, Analytics & Excel")
    st.subheader("All-in-One Learning Platform for Beginners & Professionals")

    st.image(
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1280&q=80",
        caption="🚀 Empower Your Career with Data Skills",
        use_container_width=True
    )

    st.markdown("### 🚀 Choose a Learning Path:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("📊 Data Science", on_click=lambda: go_to("data_science"))
    with col2:
        st.button("📈 Data Analytics", on_click=lambda: go_to("data_analytics"))
    with col3:
        st.button("📑 MS Excel", on_click=lambda: go_to("excel"))

    st.divider()

    st.subheader("🎥 Featured YouTube Tutorials")
    col_a, col_b, col_c = st.columns(3)
    col_a.video("https://www.youtube.com/watch?v=ua-CiDNNj30")  # DS video
    col_b.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")   # Analytics video
    col_c.video("https://www.youtube.com/watch?v=8cG-VeN94Og")   # Excel video

    st.divider()
    st.markdown("### 🔗 Connect with Ashwik Bire")
    st.markdown("[🔗 LinkedIn - Click here](https://linkedin.com/in/ashwik-bire-b2a000186)")

# -------- DATA SCIENCE --------
def page_data_science():
    st.title("📊 Data Science Learning")
    st.video("https://www.youtube.com/watch?v=Gv9_4yMHFhI")

    st.markdown("""
    Build your foundation in:
    - 🐍 Python basics with Pandas/NumPy
    - 📊 Data cleaning and visualizations
    - 🧠 Machine learning with Scikit-learn
    """)

    st.subheader("💡 Concepts Covered")
    col1, col2 = st.columns(2)
    col1.markdown("• Python syntax\n• DataFrames\n• Data viz tools")
    col2.markdown("• Supervised vs Unsupervised\n• Model training\n• Accuracy metrics")

    with st.expander("💻 Example: Linear Regression"):
        st.code("""
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'exp': [1,2,3,4], 'salary': [30000, 35000, 40000, 45000]}
df = pd.DataFrame(data)
model = LinearRegression()
model.fit(df[['exp']], df['salary'])
print(model.predict([[5]]))  # Predict salary for 5 years
        """)

    with st.expander("🧠 Quiz"):
        answer = st.radio("Which ML type uses labeled data?", ["Unsupervised", "Supervised"])
        if st.button("Submit", key="ds_quiz_submit"):
            st.success("✅ Correct!") if answer == "Supervised" else st.error("❌ Nope, try again.")

    st.markdown("📥 [Download Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))

# -------- DATA ANALYTICS --------
def page_data_analytics():
    st.title("📈 Data Analytics Curriculum")
    st.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")

    st.markdown("""
    Learn how to:
    - Clean and explore structured data
    - Use SQL/Pandas for analysis
    - Build dashboards in Excel/Tableau
    """)

    st.subheader("💡 Topics Covered")
    col1, col2 = st.columns(2)
    col1.markdown("• Descriptive Analytics\n• Exploratory Data Analysis\n• Data Profiles")
    col2.markdown("• Predictive Analytics\n• SQL Queries\n• Data Cleaning")

    with st.expander("💻 Sample Code"):
        st.code("""
import pandas as pd
df = pd.read_csv("sales.csv")
df.dropna(inplace=True)
print(df.groupby("region")["revenue"].sum().nlargest(3))
        """)

    with st.expander("🧠 Quiz"):
        q = st.radio("Which type predicts trends?", ["Descriptive", "Predictive"])
        if st.button("Submit", key="da_quiz_submit"):
            st.success("✅ Great!") if q == "Predictive" else st.error("❌ Not quite.")

    st.markdown("📥 [Download Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))

# -------- EXCEL --------
def page_excel():
    st.title("📑 Excel Essentials")
    st.video("https://www.youtube.com/watch?v=8cG-VeN94Og")

    st.markdown("""
    Sharpen your spreadsheet skills:
    - Master formulas like SUM, IF, VLOOKUP
    - Analyze with pivot tables
    - Automate tasks using Macros
    """)

    st.subheader("💡 Key Features")
    col1, col2 = st.columns(2)
    col1.markdown("• Basic formulas (SUM, IF)\n• Sorting and filtering\n• Conditional formatting")
    col2.markdown("• Pivot tables\n• Charts\n• Macros/VBA basics")

    with st.expander("🧠 Quiz"):
        ans = st.radio("Which function looks horizontally?", ["VLOOKUP", "HLOOKUP"])
        if st.button("Submit", key="xl_quiz_submit"):
            st.success("✅ You're right!") if ans == "HLOOKUP" else st.error("❌ Try again.")

    st.markdown("📥 [Download Cheat Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")
    st.button("⬅️ Back to Home", on_click=lambda: go_to("home"))


# --------------- PAGE ROUTING ---------------
if current_page == "home":
    page_home()
elif current_page == "data_science":
    page_data_science()
elif current_page == "data_analytics":
    page_data_analytics()
elif current_page == "excel":
    page_excel()
else:
    st.error("Page not found. Click below to return.")
    st.button("Home", on_click=lambda: go_to("home"))

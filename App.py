import streamlit as st

# Configure page
st.set_page_config(page_title="Learning App", page_icon="📚", layout="wide")

# Helper to set navigation
def navigate_to(page_name):
    st.experimental_set_query_params(page=page_name)

# Get current route (from query parameters)
query_params = st.experimental_get_query_params()
current_page = query_params.get("page", ["home"])[0]  # default = "home"

# ---------- HOME PAGE ----------
def page_home():
    st.title("📚 Learn Data Science, Analytics & Excel")
    st.subheader("Your All-in-One Learning Platform")

    st.image(
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1280&q=80",
        use_container_width=True,
        caption="🎯 Master Skills in Tech, Step by Step",
    )

    # Buttons to navigate
    st.markdown("### Choose a Path:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("📊 Data Science", on_click=lambda: navigate_to("data_science"))
    with col2:
        st.button("📈 Data Analytics", on_click=lambda: navigate_to("data_analytics"))
    with col3:
        st.button("📑 MS Excel", on_click=lambda: navigate_to("excel"))

    # Videos
    st.markdown("---")
    st.subheader("🎥 Featured Tutorials")
    cols = st.columns(3)
    cols[0].video("https://www.youtube.com/watch?v=ua-CiDNNj30")  # DS
    cols[1].video("https://www.youtube.com/watch?v=9J9gkqFtyYg")   # Analytics
    cols[2].video("https://www.youtube.com/watch?v=8cG-VeN94Og")   # Excel

    # LinkedIn
    st.markdown("---")
    st.markdown("### 🤝 Connect with Ashwik Bire")
    st.markdown("[🔗 LinkedIn - Ashwik Bire](https://linkedin.com/in/ashwik-bire-b2a000186)")

# ---------- DATA SCIENCE PAGE ----------
def page_data_science():
    st.title("📊 Data Science Learning")

    st.video("https://www.youtube.com/watch?v=Gv9_4yMHFhI")

    st.markdown("""
    - Get started with Python, Numpy, Pandas  
    - Learn data cleaning, visualization  
    - Explore supervised & unsupervised ML  
    """)

    with st.expander("💻 Sample Code: Linear Regression"):
        st.code('''
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'exp': [1, 2, 3, 4], 'salary': [30000, 35000, 40000, 45000]}
df = pd.DataFrame(data)
X = df[['exp']]
y = df['salary']

model = LinearRegression()
model.fit(X, y)
print(model.predict([[5]]))
        ''')

    with st.expander("🧠 Quiz"):
        q = st.radio("What does supervised learning use?", ["Labeled data", "No labels"])
        if st.button("Submit", key="ds_q1"):
            st.success("✅ Correct!") if q == "Labeled data" else st.error("❌ Try Again")

    st.markdown("[📄 Download DS Cheat Sheet](https://www.datacamp.com/community/blog/download-data-science-cheat-sheet)")

    st.button("⬅️ Back to Home", on_click=lambda: navigate_to("home"))


# ---------- DATA ANALYTICS PAGE ----------
def page_data_analytics():
    st.title("📈 Data Analytics Mastery")
    st.video("https://www.youtube.com/watch?v=9J9gkqFtyYg")

    st.markdown("""
    - Clean and analyze large datasets  
    - Understand descriptive and predictive methods  
    - Use SQL, Excel, Python for insights  
    """)

    with st.expander("💻 Code Sample"):
        st.code('''
import pandas as pd
df = pd.read_csv("sales.csv")
df.dropna(inplace=True)
print(df.groupby("product")["revenue"].sum().nlargest(3))
        ''')

    with st.expander("🧠 Quiz"):
        q = st.radio("Which type predicts trends?", ["Descriptive", "Predictive"])
        if st.button("Submit", key="da_q1"):
            st.success("✅ Great!") if q == "Predictive" else st.error("Not quite.")

    st.markdown("[📄 Download Analytics Cheat Sheet](https://www.analyticsvidhya.com/wp-content/uploads/2020/03/Data-Analytics-Cheat-Sheet.pdf)")

    st.button("⬅️ Back to Home", on_click=lambda: navigate_to("home"))


# ---------- MS EXCEL PAGE ----------
def page_excel():
    st.title("📑 Excel for Data Users")
    st.video("https://www.youtube.com/watch?v=8cG-VeN94Og")

    st.markdown("""
    - Master formulas: SUM, IF, VLOOKUP  
    - Build pivot tables and charts  
    - Automate with simple macros  
    """)

    with st.expander("🧠 Quiz"):
        ans = st.radio("Which formula searches rows?", ["VLOOKUP", "HLOOKUP", "INDEX"])
        if st.button("Submit", key="excel_q1"):
            st.success("✅ Correct!") if ans == "HLOOKUP" else st.error("❌ Nope.")

    st.markdown("[📄 Download Excel Cheat Sheet](https://exceljet.net/sites/default/files/ExcelJet_Excel_Cheat_Sheet_PDF.pdf)")

    st.button("⬅️ Back to Home", on_click=lambda: navigate_to("home"))


# Render the active page
if current_page == "home":
    page_home()
elif current_page == "data_science":
    page_data_science()
elif current_page == "data_analytics":
    page_data_analytics()
elif current_page == "excel":
    page_excel()

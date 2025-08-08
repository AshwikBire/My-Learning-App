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
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Zoha | AI Fintech Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Dark CSS for a premium tech feel
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #00ffcc; font-family: 'Helvetica Neue', sans-serif; }
    h3 { color: #ffffff; }
    .project-card {
        background-color: #1e2630;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00ffcc;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_view_html=True)

# 2. Hero Section
st.title("🚀 Zoha | AI Fintech Engineer & Data Architect")
st.write("Building the bridge between intelligent logic and financial data. Ready for global remote operations.")
st.markdown("---")

# 3. Project Showcase
st.header("🧰 The Portfolio Suite")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="project-card">
        <h3>💰 TruePKR</h3>
        <p><b>Fintech Engine</b><br>A real-time currency exchange application designed to handle live API global market data fluctuations.</p>
    </div>
    """, unsafe_view_html=True)
    st.button("Launch TruePKR", key="truepkr_btn")

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>🧠 SpendWise AI</h3>
        <p><b>Financial Auditor</b><br>An automated business expense tracker featuring runway prediction math and anomaly detection logic.</p>
    </div>
    """, unsafe_view_html=True)
    st.button("Launch SpendWise AI", key="spendwise_btn")

with col3:
    st.markdown("""
    <div class="project-card">
        <h3>🩺 MediGuide AI</h3>
        <p><b>Healthcare Operations</b><br>An intelligent triage tool demonstrating advanced text orchestration and structured AI responses.</p>
    </div>
    """, unsafe_view_html=True)
    st.button("Launch MediGuide AI", key="mediguide_btn")

st.markdown("---")

# 4. The Edge / Value Proposition
st.header("🎯 Why Work With Me?")
st.write(
    "I specialize in rapid AI implementation. Instead of just writing syntax from memory, "
    "I architect systems by leveraging state-of-the-art AI tools to deliver fully functioning, "
    "production-ready data dashboards and automation workflows."
)

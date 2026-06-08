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
        margin-bottom: 15px;
        min-height: 180px;
    }
    .launch-link {
        display: inline-block;
        background-color: #00ffcc;
        color: #0e1117 !important;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
        margin-top: 10px;
        text-align: center;
    }
    .launch-link:hover {
        background-color: #00cc99;
    }
    </style>
""", unsafe_allow_html=True)

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
    <a class="launch-link" href="https://18-things-before-18-thy7s9fmiyugxatw8clyk5.streamlit.app/" target="_blank">Launch TruePKR ↗️</a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>🧠 SpendWise AI</h3>
        <p><b>Financial Auditor</b><br>An automated business expense tracker featuring runway prediction math and anomaly detection logic.</p>
    </div>
    <a class="launch-link" href="https://18-things-before-18-zqbufspxfh4doricggmbph.streamlit.app/" target="_blank">Launch SpendWise AI ↗️</a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="project-card">
        <h3>🩺 MediGuide AI</h3>
        <p><b>Healthcare Operations</b><br>An intelligent triage tool demonstrating advanced text orchestration and structured AI responses.</p>
    </div>
    <a class="launch-link" href="https://mediguide-ai-triage-ekuxqrgu6tskhebz5lmdmu.streamlit.app/" target="_blank">Launch MediGuide AI ↗️</a>
    """, unsafe_allow_html=True)

st.markdown("---")

# 4. The Edge / Value Proposition
st.header("🎯 Why Work With Me?")
st.write(
    "I specialize in rapid AI implementation. Instead of just writing syntax from memory, "
    "I architect systems by leveraging state-of-the-art AI tools to deliver fully functioning, "
    "production-ready data dashboards and automation workflows."
)

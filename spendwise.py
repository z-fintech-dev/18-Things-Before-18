import streamlit as st
import pandas as pd

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    div[data-testid="metric-container"] {
        background-color: #1f2937;
        border: 1px solid #374151;
        padding: 15px;
        border-radius: 10px;
        color: #ffffff;
    }
    .stDataFrame {
        border: 1px solid #374151;
        border-radius: 10px;
    }
   </style>
    """, unsafe_allow_html=True)
# --- CURRENCY LOGIC UPDATE ---
# Ensure PKR is the default and uses proper formatting
currency_options = {"PKR": "Rs.", "USD": "$", "GBP": "£"}
selected_currency = st.sidebar.selectbox("Select Currency", list(currency_options.keys()), index=0)
symbol = currency_options[selected_currency]

# 1. SETTINGS
st.set_page_config(page_title="SpendWise AI", layout="wide")
st.title("💰 SpendWise AI: Executive Financial Audit")

# 2. SIDEBAR UPLOADER
st.sidebar.header("Data Input")
uploaded_file = st.sidebar.file_uploader("Upload your transactions.csv", type=["csv", "txt"])

# 3. CURRENCY SELECTOR
currency_options = {"PKR": "Rs.", "USD": "$", "GBP": "£"}
selected_currency = st.sidebar.selectbox("Select Currency", list(currency_options.keys()))
symbol = currency_options[selected_currency]

# 4. MAIN LOGIC (Only runs if file is uploaded)
if uploaded_file is not None:
    # Read the file
    df = pd.read_csv(uploaded_file)
    
    # Clean the data
    df['Amount'] = pd.to_numeric(df['Amount'])
    
    # Calculations
    total_spent = df[df['Amount'] > 0]['Amount'].sum()
    total_income = abs(df[df['Amount'] < 0]['Amount'].sum())
    net_balance = total_income - total_spent

    # Display Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"{symbol} {total_income:,.2f}")
    col2.metric("Total Expenses", f"{symbol} {total_spent:,.2f}")
    col3.metric("Net Balance", f"{symbol} {net_balance:,.2f}")

    st.markdown("---")

    st.markdown("---")
    st.subheader("🚨 Financial Health Audit: Anomalous Spending")
    st.markdown("---")
    st.subheader("📅 Financial Runway Predictor")

    # 1. Calculate Daily Burn Rate (Total Expenses / number of days in the data)
    num_days = (pd.to_datetime(df['Date']).max() - pd.to_datetime(df['Date']).min()).days + 1
    daily_burn_rate = total_spent / num_days

    if daily_burn_rate > 0:
        days_left = net_balance / daily_burn_rate
        
        if days_left > 0:
            st.info(f"Your average daily spend is **{symbol}{daily_burn_rate:,.2f}**.")
            st.metric("Estimated Days of Runway", f"{int(days_left)} Days")
        else:
            st.error("⚠️ ALERT: Your net balance is zero or negative. Immediate budget adjustment required.")
    else:
        st.success("No expenses recorded yet. Your runway is infinite!")

    # 1. Calculate the average of all POSITIVE expenses
    expenses_only = df[df['Amount'] > 0]['Amount']
    avg_expense = expenses_only.mean()

    # 2. Define a 'Red Flag' threshold (e.g., 3x the average)
    threshold = avg_expense * 3

    # 3. Use that LAMBDA we talked about to tag transactions
    df['Audit_Status'] = df['Amount'].apply(
        lambda x: "🚩 RED FLAG: High Spend" if x > threshold else "✅ Normal"
    )

    # 4. Display only the Red Flags to the Executive
    red_flags = df[df['Audit_Status'].str.contains("🚩")]
    
    if not red_flags.empty:
        st.warning(f"Audit detected transactions exceeding the threshold of {symbol}{threshold:,.2f}")
        st.dataframe(red_flags, use_container_width=True)
    else:
        st.success("No anomalous spending detected in this period.")
    # Show Data Table
    st.subheader("📊 Recent Transactions")
    st.dataframe(df, use_container_width=True)

else:
    # This shows if no file is uploaded yet
    st.info("👋 Welcome! Please upload your 'transactions.csv' file in the sidebar to begin.")

import streamlit as st
import pandas as pd

# 1. PAGE CONFIG (Must be first!)
st.set_page_config(page_title="SpendWise AI", layout="wide")

# 2. CUSTOM STYLING
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    div[data-testid="metric-container"] {
        background-color: #1f2937;
        border: 1px solid #374151;
        padding: 15px;
        border-radius: 10px;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR CONTROLS
st.sidebar.header("Data Input")
uploaded_file = st.sidebar.file_uploader("Upload your transactions.csv", type=["csv", "txt"])

currency_options = {"PKR": "Rs.", "USD": "$", "GBP": "£"}
selected_currency = st.sidebar.selectbox("Select Currency", list(currency_options.keys()))
symbol = currency_options[selected_currency]

# 4. MAIN INTERFACE
st.title("💰 SpendWise AI: Executive Financial Audit")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Clean up column names to avoid matching issues due to hidden spaces
    df.columns = df.columns.str.strip()
    
    # Ensure Amount is numeric
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
    
    # Standardizing calculation (Assuming Positive = Expense for your current logic template)
    total_spent = df[df['Amount'] > 0]['Amount'].sum()
    total_income = abs(df[df['Amount'] < 0]['Amount'].sum())
    net_balance = total_income - total_spent

    # Metrics Row
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"{symbol} {total_income:,.2f}")
    col2.metric("Total Expenses", f"{symbol} {total_spent:,.2f}")
    col3.metric("Net Balance", f"{symbol} {net_balance:,.2f}")

    st.markdown("---")

    # Runway Predictor Section (With safety fallbacks for Date/Timestamp)
    st.subheader("📅 Financial Runway Predictor")
    
    # Find whatever date column exists
    date_col = None
    for col in ['Date', 'Timestamp', 'date', 'timestamp']:
        if col in df.columns:
            date_col = col
            break
            
    if date_col:
        try:
            num_days = (pd.to_datetime(df[date_col]).max() - pd.to_datetime(df[date_col]).min()).days + 1
            if num_days <= 0: num_days = 1
        except:
            num_days = 30 # Default fallback if dates fail to parse
    else:
        num_days = 30 # Default fallback if no date column exists at all
        st.caption("ℹ️ No date column found. Defaulting calculations over a 30-day timeline simulation.")

    daily_burn_rate = total_spent / num_days

    if daily_burn_rate > 0:
        days_left = net_balance / daily_burn_rate
        if days_left > 0:
            st.info(f"Your average daily spend is **{symbol}{daily_burn_rate:,.2f}** (Calculated over {num_days} days).")
            st.metric("Estimated Days of Runway", f"{int(days_left)} Days")
        else:
            st.error("⚠️ ALERT: Your net balance is zero or negative. Immediate budget adjustment required.")
    else:
        st.success("No expenses recorded yet. Your runway is infinite!")

    # Anomalous Spending Section
    st.markdown("---")
    st.subheader("🚨 Financial Health Audit: Anomalous Spending")
    
    expenses_only = df[df['Amount'] > 0]['Amount']
    if not expenses_only.empty:
        avg_expense = expenses_only.mean()
        threshold = avg_expense * 3
        
        df['Audit_Status'] = df['Amount'].apply(
            lambda x: "🚩 RED FLAG: High Spend" if x > threshold else "✅ Normal"
        )

        red_flags = df[df['Audit_Status'].str.contains("🚩")]
        if not red_flags.empty:
            st.warning(f"Audit detected transactions exceeding the threshold of {symbol}{threshold:,.2f}")
            st.dataframe(red_flags, use_container_width=True)
        else:
            st.success("No anomalous spending detected in this period.")

    # Full Transaction Table
    st.markdown("---")
    st.subheader("📊 Recent Transactions")
    st.dataframe(df, use_container_width=True)

else:
    st.info("👋 Welcome! Please upload your 'transactions.csv' file in the sidebar to begin.")

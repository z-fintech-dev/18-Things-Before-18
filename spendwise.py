import streamlit as st
import pandas as pd

# 1. SETTINGS
st.set_page_config(page_title="SpendWise AI", layout="wide")
st.title("💰 SpendWise AI: Executive Financial Audit")

# 2. SIDEBAR UPLOADER
st.sidebar.header("Data Input")
uploaded_file = st.sidebar.file_uploader("Upload your transactions.csv", type="csv")

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

    # Show Data Table
    st.subheader("📊 Recent Transactions")
    st.dataframe(df, use_container_width=True)

else:
    # This shows if no file is uploaded yet
    st.info("👋 Welcome! Please upload your 'transactions.csv' file in the sidebar to begin.")

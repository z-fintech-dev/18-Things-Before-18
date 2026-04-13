import streamlit as st
import pandas as pd
from datetime import datetime

# 1. SETTINGS & SETUP
st.set_page_config(page_title="SpendWise AI", layout="wide")
st.title("💰 SpendWise AI: Executive Financial Audit")

# 2. CURRENCY SELECTOR (The "International" touch)
currency_options = {"PKR": "Rs.", "USD": "$", "GBP": "£"}
selected_currency = st.sidebar.selectbox("Select Currency", list(currency_options.keys()))
symbol = currency_options[selected_currency]

# Instead of just loading a file, let's allow an upload
uploaded_file = st.sidebar.file_uploader("Upload your transactions.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # ... move all your analysis logic inside this 'if' block
else:
    st.info("Please upload a CSV file to begin the audit.")
    st.stop() # Stops the app until a file is provided
    
    # 4. DATA ANALYSIS (The "Fintech" Brain)
    total_spent = df[df['Amount'] > 0]['Amount'].sum()
    total_income = abs(df[df['Amount'] < 0]['Amount'].sum())
    net_balance = total_income - total_spent

    # 5. THE TOP METRICS
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"{symbol} {total_income:,.2f}")
    col2.metric("Total Expenses", f"{symbol} {total_spent:,.2f}")
    col3.metric("Net Balance", f"{symbol} {net_balance:,.2f}")

    st.markdown("---")

    # 6. SHOW THE DATA TABLE
    st.subheader("📊 Recent Transactions")
    st.dataframe(df, use_container_width=True)

except FileNotFoundError:
    st.error("Error: 'transactions.csv' not found. Please ensure the file is in the same folder.")

import streamlit as st # The engine for TruePKR
import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="TruePKR", page_icon="💶")
st.title("TruePKR: The Freelancer's Reality Check")

# 2. Sidebar for Inputs
st.sidebar.header("Transfer Details")
currency = st.sidebar.selectbox("Select Currency", ["USD ($)", "EUR (€)"])
amount = st.sidebar.number_input("Amount Received", min_value=0.0, value=1000.0)

# Set default market rates based on currency selection
default_rate = 280.0 if "USD" in currency else 310.0
market_rate = st.sidebar.number_input("Google/Market Rate (PKR)", min_value=0.0, value=default_rate)

# 3. User Preferences
st.sidebar.divider()
is_pseb = st.sidebar.checkbox("I am PSEB Registered (0.25% Tax)")
provider = st.sidebar.selectbox("Which Bank/App are you using?", 
                               ["SadaPay/NayaPay", "Standard Chartered", "Meezan/HBL", "Payoneer (to Bank)"])

# 4. Logic - Setting the "Resistance" based on Provider
if provider == "SadaPay/NayaPay":
    spread_pct = 0.012  # 1.2%
elif provider == "Standard Chartered":
    spread_pct = 0.015  # 1.5%
elif provider == "Payoneer (to Bank)":
    spread_pct = 0.030  # 3.0% (Includes middleman fee)
else:
    spread_pct = 0.022  # 2.2% for others

# 5. Calculations
gross_pkr = amount * market_rate
bank_cut = gross_pkr * spread_pct
tax_rate = 0.0025 if is_pseb else 0.01
fbr_tax = gross_pkr * tax_rate
final_take_home = gross_pkr - bank_cut - fbr_tax

# 6. The "Beautiful Receipt" Output (With Safety Guard)
st.divider()
st.subheader("📝 Your Digital Receipt")

if gross_pkr > 0:
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Gross Amount ({currency}):**")
        st.write(f"Bank/App Loss ({provider}):")
        st.write(f"Government Tax (FBR):")
        st.success(f"### **Net in Pocket:**")

    with col2:
        st.write(f"Rs. {gross_pkr:,.0f}")
        st.write(f"- Rs. {bank_cut:,.0f}")
        st.write(f"- Rs. {fbr_tax:,.0f}")
        st.success(f"### **Rs. {final_take_home:,.0f}**")

    st.warning(f"💡 You lost **Rs. {bank_cut + fbr_tax:,.0f}** in fees. That's about {((bank_cut+fbr_tax)/gross_pkr)*100:.1f}% of your hard work!")
else:
    st.info("Please enter an amount greater than 0 in the sidebar to see your breakdown.")

# 7. Credit Tag
st.caption("Created by Zoha (z-fintech-dev) | Project #1: TruePKR")


    

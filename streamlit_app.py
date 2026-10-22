# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Ryan Fang")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "* Fun Tab"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: Volume Chart
with tabs[3]:
    st.subheader(f"Something New")
    st.write("See how much money you would have made investing in Microsoft!")

    # Prepare the stock data
    stock = df.copy()
    stock["Date"] = pd.to_datetime(stock["Date"])
    stock = stock.sort_values("Date")

    # Let users choose their investment amount
    investment = st.slider("How much would you invest ($)?", 100, 10000, 1000, 100)

    # Let users choose when they bought the stock
    start_date = st.selectbox("Choose your purchase date:", stock["Date"])

    # Calculate investment performance
    selected = stock[stock["Date"] >= start_date].copy()
    purchase_price = selected["Close"].iloc[0]
    current_price = selected["Close"].iloc[-1]

    shares = investment / purchase_price
    final_value = shares * current_price
    profit = final_value - investment
    return_pct = (profit / investment) * 100

    # Display the results
    st.metric("Initial Investment", f"${investment:,.2f}")
    st.metric("Current Value", f"${final_value:,.2f}",
              delta=f"${profit:,.2f} ({return_pct:+.2f}%)")

    # Plot investment value over time
    selected["Investment Value"] = shares * selected["Close"]
    st.subheader("📈 Your Investment Over Time")
    st.line_chart(selected.set_index("Date")["Investment Value"])

    st.caption("Based on historical closing prices. Assumes fractional shares and excludes dividends and fees.")


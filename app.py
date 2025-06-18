# app.py

import streamlit as st
import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("📈 Stock Price Trend Predictor")

# User input: Stock Symbol
symbol = st.text_input("Enter Stock Symbol (e.g. RELIANCE.NS, AAPL):")

if st.button("Predict Trend"):
    try:
        # Fetch data
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="60d", interval="1d").reset_index()
        df = df[['Date', 'Close']].tail(30)

        if df.empty:
            st.error("Invalid symbol or no recent data. Try again.")
        else:
            df['Day_Index'] = range(1, len(df)+1)
            X = df['Day_Index'].values.reshape(-1, 1)
            y = df['Close'].values

            # Train model
            model = LinearRegression()
            model.fit(X, y)

            next_day = np.array([[X[-1][0] + 1]])
            predicted_price = model.predict(next_day)
            today_price = y[-1]

            # Show prediction
            st.subheader(f"Predicted Next Day Closing Price: {predicted_price[0]:.2f}")

            if predicted_price[0] > today_price:
                st.success("Trend: 📈 Likely UP")
            else:
                st.warning("Trend: 📉 Likely DOWN")

            # Plot
            fig, ax = plt.subplots()
            ax.plot(X, y, label='Actual Prices', marker='o')
            ax.plot(X, model.predict(X), label='Trend Line', color='red')
            ax.scatter(next_day, predicted_price, color='green', s=100, label='Predicted Next Day')
            ax.set_xlabel('Day Index')
            ax.set_ylabel('Closing Price')
            ax.set_title('Closing Price & Predicted Trend')
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")

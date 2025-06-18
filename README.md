📈 Stock Price Trend Predictor
An AI-powered web app that predicts whether a stock's price is likely to go up or down tomorrow based on the last 30 trading days of data.
Built with Python, yfinance, scikit-learn, Matplotlib, and Streamlit — fully open source and beginner-friendly.

What this app does:
✅ Fetches the latest 30 trading days of daily closing prices for any valid stock symbol (e.g. AAPL, RELIANCE.NS).
✅ Trains a simple Linear Regression model to learn the price trend over those days.
✅ Predicts the next day’s closing price using the trained model.
✅ Compares the predicted price to today’s price to decide:
“Likely Up 📈” or “Likely Down 📉”.
✅ Visualizes:

1️⃣ The actual past prices

2️⃣ The fitted trend line

3️⃣ The predicted next day’s price on the same plot.

✅ Runs as an interactive web app — just enter a stock symbol and click Predict Trend.

How it works (under the hood):
Here’s exactly what happens step-by-step when a user types a symbol and clicks Predict Trend:

1️⃣ User Input:

The app asks for a valid stock ticker (example: AAPL for Apple Inc, RELIANCE.NS for Reliance Industries on NSE India).

2️⃣ Fetch Live Data:

Uses the yfinance Python library to pull the last 60 calendar days of daily stock prices.

Selects the most recent 30 trading days (weekends/holidays are skipped automatically).

3️⃣ Prepare Data for ML:

Creates a new numeric index: Day_Index = 1, 2, 3, ..., 30.

Uses Day_Index as the input feature (X) and Close price as the target (y).

4️⃣ Train the Model:

Trains a LinearRegression model (scikit-learn) to fit a best-fit line:
y=m⋅X+b

5️⃣ Predict Next Day:

Predicts the closing price for Day_Index + 1 (tomorrow).

Compares it with today’s price to decide the trend.

6️⃣ Show Result:

Displays the predicted price rounded to two decimals.

Shows Trend: Likely UP 📈 or Likely DOWN 📉.

7️⃣ Plot Graph:

Plots the actual closing prices as a blue line.

Plots the model’s fitted trend line in red.

Highlights the predicted next point as a big green dot.

Makes it easy to visually check how well the trend line fits the real data.


Tech Stack:
Tool	              Purpose
Python 3	          Main programming language
yfinance	          Fetches live historical stock data
scikit-learn	      Linear Regression model
Matplotlib	        Data visualization
Streamlit	          Turns Python code into an interactive web app

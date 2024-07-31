from flask import Flask, jsonify, render_template
import yfinance as yf
import requests_html
from yahoo_fin import stock_info

# Get the top gainers of the day
day_gainers = stock_info.get_day_gainers()
print("Day Gainers:")
print(day_gainers)

# Get the top losers of the day
day_losers = stock_info.get_day_losers()
print("\nDay Losers:")
print(day_losers)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/day_gainers')
def day_gainers():
    gainers = stock_info.get_day_gainers().head(10)
    gainers = gainers[['Symbol', 'Name', 'Price (Intraday)', 'Change', 'Volume']]
    return jsonify(gainers.to_dict(orient='records'))

@app.route('/day_losers')
def day_losers():
    losers = stock_info.get_day_losers().head(10)
    losers = losers[['Symbol', 'Name', 'Price (Intraday)', 'Change', 'Volume']]
    return jsonify(losers.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
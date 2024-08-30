import datetime
import time
import yfinance as yf
from plyer import notification

def fetch_and_notify():
    rvnl = yf.Ticker("RVNL.NS")  # Ensure to use the correct ticker symbol (".NS" for NSE in India)
    
    try:
        # Fetch the latest stock data
        data = rvnl.history(period="1d")
        
        # Check if the data is fetched correctly
        if not data.empty:
            current_price = data['Close'].iloc[-1]
            day_low = data['Low'].iloc[-1]
            day_high = data['High'].iloc[-1]
            
            # Send notification
            notification.notify(
                title="RVNL Data - {}".format(datetime.date.today().strftime('%Y-%m-%d')),
                message="Current Price = {:.2f} \nDay Low = {:.2f} \nDay High = {:.2f}".format(
                    current_price,
                    day_low,
                    day_high
                ),
                app_name="RVNL",
                app_icon="F:/VS_CODING/Advance_PYTHON/Python Project/Images/Stock.ico",
                timeout=5
            )
        else:
            print("No data fetched for RVNL.")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

# Main loop to fetch data and notify every 30 seconds
while True:
    fetch_and_notify()
    time.sleep(30)

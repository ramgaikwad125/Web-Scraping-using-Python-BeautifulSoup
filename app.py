# ----------------------
#  Import Statments
# ----------------------
from flask import Flask, Response
from datetime import datetime
from NSE_webscraping import get_expiry_from_option_chain
from NSE_webscraping import get_strike_price_from_option_chain
import main
from main import get_data

# import main
app = Flask(__name__)

# ------------------------------------
# create the button to download csv
# ------------------------------------


@app.route("/")
def hello():
    return '''
        <html><body>
        Hello download today's Option Chain from NSE. <a href="/get_data"> Download.</a>
        </body></html>
        '''
# ------------------------
#   scrap the data
# ------------------------
@app.route("/get_data")
def main_function():
    today_date = datetime.today().strftime('%Y-%m-%d')
    data = get_data()
    # print(data.head(3))
    data.to_csv('results/NSE_'+today_date+'.csv')
    # return this data file
    return Response(print('Downloade Complete for', today_date, 'NSE Option Chain data'))


app.run(port=9001, debug=True)

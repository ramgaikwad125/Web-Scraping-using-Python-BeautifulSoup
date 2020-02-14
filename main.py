#--------------------------
# Import the Statments
#--------------------------
import pandas as pd
import requests
from bs4 import BeautifulSoup
from NSE_webscraping import get_strike_price_from_option_chain,strike_group_def
from NSE_webscraping import get_expiry_from_option_chain,expiration_group_def


#----------------------
#  Get NIFTY50 data
#----------------------
nifty50_url = "https://trendlyne.com/equity/DIV/NIFTY50/1887/nifty-50-dividend-yield/"
page = requests.get(nifty50_url)
soup = BeautifulSoup(page.content, 'html.parser')
nifty50_div = soup.title.string[61:66]
try:
    nifty50_close_price = soup.find_all("span", class_="tile-current-price pr05r LpriceCP LpriceNP positive")[0].string[17:25]
except:
    nifty50_close_price = soup.find_all("span", class_="tile-current-price pr05r LpriceCP LpriceNP negative")[0].string[17:25]
print('Nifty50 Dividend:',nifty50_div)
print('Nifty50 Close Price:',nifty50_close_price)


#------------------------
# Get BANKNIFTY data
#------------------------
banknifty_url = "https://trendlyne.com/equity/PE/NIFTYBANK/1898/nifty-bank-price-to-earning-ratios/"
page = requests.get(banknifty_url)
soup = BeautifulSoup(page.content, 'html.parser')
banknifty_div = soup.find_all("div", class_="cen tlv2-cmain")[2].string[16:21]
try:
    banknifty_close_price = soup.find_all("span", class_="tile-current-price pr05r LpriceCP LpriceNP positive")[0].string[17:25]
except:
    banknifty_close_price = soup.find_all("span", class_="tile-current-price pr05r LpriceCP LpriceNP negative")[0].string[17:25]
print('BankNifty Dividend:',banknifty_div)
print('BankNifty Close Price:',banknifty_close_price)


#-----------------------
# get Interest Rate
#-----------------------
repo_rate = "https://www.rbi.org.in/home.aspx"
page = requests.get(repo_rate)
soup = BeautifulSoup(page.content, 'html.parser')
repo_rate = soup.find_all("td")[7].string[45:49]
print(repo_rate)

def get_data():
        expdate = get_expiry_from_option_chain('NIFTY')
        print(expdate)

        symbol_list = ['NIFTY','BANKNIFTY']
        print(symbol_list)


        appended_data = []
        for symbol_i in symbol_list:
                for expdate_i in expdate:
                        data1 = get_strike_price_from_option_chain(symbol_i,expdate_i)
                        print(symbol_i,expdate_i)
                        appended_data.append(data1)


        appended_DATA = pd.DataFrame()
        for i in range((len(appended_data)-2)):
                DATA = pd.DataFrame(appended_data[i])
                appended_DATA = appended_DATA.append(DATA)

        # reset index of dataset
        appended_DATA = appended_DATA.reset_index(drop=True) 
        
        ## Rename the variables
        appended_DATA = appended_DATA[['date','ticker','expiry_date','str_price',
                                        'bid_price_put','ask_price_put','net_chng_put','iv_put','vol_put']]

        appended_DATA = appended_DATA.rename(columns={'date': 'quote_date', 'ticker':'symbol','expiry_date':'expiration',
                                'str_price':'strike','bid_price_put':'bid_1545','ask_price_put':'ask_1545',
                                'net_chng_put':'net_change','iv_put':'implied_volatility_1545','vol_put':'volume'}, index=str)
        appended_DATA = appended_DATA.replace(to_replace=r'^-$', value=0, regex=True).reset_index()
        
        underlying_bid_1545 = pd.Series([])
        Dividend = pd.Series([]) 

        ## running a for loop and asigning some values to series 
        ## Intrest Rate and Underlying bid value
        for i in range(len(appended_DATA)): 
                if appended_DATA["symbol"][i] == "NIFTY":
                        underlying_bid_1545[i] = nifty50_close_price
                        Dividend[i] = nifty50_div
                else: 
                        underlying_bid_1545[i] = banknifty_close_price
                        Dividend[i] = banknifty_div

        appended_DATA.insert(2, "underlying_bid_1545", underlying_bid_1545)
        appended_DATA.insert(2, "Dividend", Dividend)
        appended_DATA['Interest_rate'] = repo_rate
        appended_DATA['quote_date'] = pd.to_datetime(appended_DATA.quote_date,format = '%Y-%m-%d')
        appended_DATA['expiration'] = pd.to_datetime(appended_DATA.expiration,format = '%d%b%Y')
        appended_DATA = appended_DATA.fillna(0)

        appended_DATA = expiration_group_def(appended_DATA)
        appended_DATA = strike_group_def(appended_DATA)
        appended_DATA['bid_1545'] = pd.to_numeric(appended_DATA['bid_1545'], errors='coerce')
        appended_DATA['ask_1545'] = pd.to_numeric(appended_DATA['ask_1545'], errors='coerce')
        appended_DATA['volume'] = pd.to_numeric(appended_DATA['volume'], errors='coerce')
        appended_DATA = appended_DATA.drop(['index'], axis=1)
        return appended_DATA
        

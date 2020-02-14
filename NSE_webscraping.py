
#--------------------------
#    import statements
#-------------------------
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date

#-----------------------------------------------------------------
# Get all get possible expiry date details for the given script
#-----------------------------------------------------------------

def get_expiry_from_option_chain (symbol):

    # Base url page for the symbole with default expiry date
    Base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=-"

    # Load the page and sent to HTML parse
    page = requests.get(Base_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Locate where expiry date details are available
    locate_expiry_point = soup.find(id="date")
    # Convert as rows based on tag option
    expiry_rows = locate_expiry_point.find_all('option')

    index = 0
    expiry_list = []
    for each_row in expiry_rows:
        # skip first row as it does not have value
        if index <= 0:
            index = index + 1
            continue
        index = index + 1
        # Remove HTML tag and save to list
        expiry_list.append(BeautifulSoup(str(each_row), 'html.parser').get_text())
    
    expiry_list = list(expiry_list)
    # print(expiry_list)
    return expiry_list # return list



def get_strike_price_from_option_chain(symbol, expdate):
    
    Base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=" + expdate

    page = requests.get(Base_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table_cls_2 = soup.find(id="octable")
    req_row = table_cls_2.find_all('tr')
    
    chart_call = []
    oi_call = []
    chng_oi_call = []
    vol_call = []
    iv_call = []
    ltp_call = []
    net_chng_call = []
    bid_qty_call = []
    bid_price_call = []
    ask_qty_call = []
    ask_price_call = []
    str_price = []
    bid_qty_put = []
    bid_price_put = []
    ask_price_put = []
    ask_qty_put = []
    net_chng_put = []
    ltp_put = []
    iv_put = []
    vol_put = []
    chng_oi_put = []
    oi_put = []
    chart_put = []
    

    for row_number, tr_nos in enumerate(req_row):

        # This ensures that we use only the rows with values
        if row_number <= 1 or row_number == len(req_row) - 1:
            continue

        td_columns = tr_nos.find_all('td')
        
        chart_call_list = BeautifulSoup(str(td_columns[0]), 'html.parser').get_text()
        oi_call_list = BeautifulSoup(str(td_columns[1]), 'html.parser').get_text()
        chng_oi_call_list = BeautifulSoup(str(td_columns[2]), 'html.parser').get_text()
        vol_call_list = BeautifulSoup(str(td_columns[3]), 'html.parser').get_text()
        iv_call_list = BeautifulSoup(str(td_columns[4]), 'html.parser').get_text()
        ltp_call_list = BeautifulSoup(str(td_columns[5]), 'html.parser').get_text()
        net_chng_call_list = BeautifulSoup(str(td_columns[6]), 'html.parser').get_text()
        bid_qty_call_list = BeautifulSoup(str(td_columns[7]), 'html.parser').get_text()
        bid_price_call_list = BeautifulSoup(str(td_columns[8]), 'html.parser').get_text()
        ask_qty_call_list = BeautifulSoup(str(td_columns[9]), 'html.parser').get_text()
        ask_price_call_list = BeautifulSoup(str(td_columns[10]), 'html.parser').get_text()
        str_price_list = BeautifulSoup(str(td_columns[11]), 'html.parser').get_text()
        bid_qty_put_list = BeautifulSoup(str(td_columns[12]), 'html.parser').get_text()
        bid_price_put_list = BeautifulSoup(str(td_columns[13]), 'html.parser').get_text()
        ask_price_put_list = BeautifulSoup(str(td_columns[14]), 'html.parser').get_text()
        ask_qty_put_list = BeautifulSoup(str(td_columns[15]), 'html.parser').get_text()
        net_chng_put_list = BeautifulSoup(str(td_columns[16]), 'html.parser').get_text()
        ltp_put_list = BeautifulSoup(str(td_columns[17]), 'html.parser').get_text()
        iv_put_list = BeautifulSoup(str(td_columns[18]), 'html.parser').get_text()
        vol_put_list = BeautifulSoup(str(td_columns[19]), 'html.parser').get_text()
        chng_oi_put_list = BeautifulSoup(str(td_columns[20]), 'html.parser').get_text()
        oi_put_list = BeautifulSoup(str(td_columns[21]), 'html.parser').get_text()
        chart_put_list = BeautifulSoup(str(td_columns[22]), 'html.parser').get_text()

        
        chart_call.append(chart_call_list)
        oi_call.append(oi_call_list)
        chng_oi_call.append(chng_oi_call_list)
        vol_call.append(vol_call_list)
        iv_call.append(iv_call_list)
        ltp_call.append(ltp_call_list)
        net_chng_call.append(net_chng_call_list)
        bid_qty_call.append(bid_qty_call_list)
        bid_price_call.append(bid_price_call_list)
        ask_qty_call.append(ask_qty_call_list)
        ask_price_call.append(ask_price_call_list)
        str_price.append(str_price_list)
        bid_qty_put.append(bid_qty_put_list)
        bid_price_put.append(bid_price_put_list)
        ask_price_put.append(ask_price_put_list)
        ask_qty_put.append(ask_qty_put_list)
        net_chng_put.append(net_chng_put_list)
        ltp_put.append(ltp_put_list)
        iv_put.append(iv_put_list)
        vol_put.append(vol_put_list)
        chng_oi_put.append(chng_oi_put_list)
        oi_put.append(oi_put_list)
        chart_put.append(chart_put_list)
        
    data = {'date':date.today(),
            'ticker':symbol,
            'expiry_date':expdate,
            'chart_call':chart_call,
            'oi_call':oi_call,
            'chng_oi_call':chng_oi_call,
            'vol_call':vol_call,
            'iv_call':iv_call,
#             'ltp_call':ltp_call,
            'net_chng_call':net_chng_call,
            'bid_qty_call':bid_qty_call,
            'bid_price_call':bid_price_call,
            'ask_qty_call':ask_qty_call,
            'ask_price_call':ask_price_call,
            'str_price':str_price,
            'bid_qty_put':bid_qty_put,
            'bid_price_put':bid_price_put,
            'ask_price_put':ask_price_put,
            'ask_qty_put':ask_qty_put,
            'net_chng_put':net_chng_put,
#             'ltp_put':ltp_put,
            'iv_put':iv_put,
            'vol_put':vol_put,
            'chng_oi_put':chng_oi_put,
            'oi_put':oi_put,
            'chart_put':chart_put}
    
    data = pd.DataFrame.from_dict(data)
    
    return data


def expiration_group_def(appended_data):
    appended_data['date_diff'] = (appended_data['expiration'] - appended_data['quote_date']).astype('timedelta64[D]')

    # bins Creations for expiration_group
    # print('Labeling expiration_group ... ')
    bins_duration = [-float("inf"), 7, 14, 30, 60, 90, 180, 365, 547, 730, float("inf")] # Upto the number of days
    labels_duration = ['0_week','1_week', '2_week', '1_month', '2_month', '3_month', '6_month', '1_year', '1.5_year', '2_year']
    cat_duration = pd.cut(appended_data['date_diff'], bins=bins_duration, labels=labels_duration)
    Cat_duration = cat_duration.to_frame(name='expiration_group')
    Duration_encoded = pd.concat([appended_data, Cat_duration], axis=1)
    return Duration_encoded

def strike_group_def(appended_data):
    # Strike Encoding
    appended_data['Strike_diff'] = (1 - np.float64(appended_data['strike']) / np.float64(appended_data['underlying_bid_1545']))

    # bins Creations for Strike_group
    # print('Labeling Strike_group ...')
    bins_strike =[-float("inf"),-.70,-.60,-.50, -.40, -.30, -.20, -.10, 0, .10, .20, .30, .40, .50, .60, .70, 0.80, float("inf")]
    labels_strike = ['minus_other','minus_70','minus_60','minus_50', 'minus_40', 'minus_30', 'minus_20', 'minus_10', 'mid_point', 'plus_10', 'plus_20','plus_30', 'plus_40', 'plus_50', 'plus_60', 'plus_70','plus_other']
    cat_strike = pd.cut(appended_data['Strike_diff'], bins=bins_strike, labels=labels_strike)
    Cat_strike = cat_strike.to_frame(name='Strike_group')
    strike_encoded = pd.concat([appended_data, Cat_strike], axis=1)
    return strike_encoded



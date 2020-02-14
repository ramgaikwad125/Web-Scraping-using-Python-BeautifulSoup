from flask import Flask, jsonify, Response, json, request, render_template
from flask_restful import Resource
from datetime import time, datetime, timedelta
import pandas_market_calendars as mcal
import subprocess
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime 
import pymongo
from pymongo import MongoClient
import json
import dateutil.parser
import http.client as http 
import json
import schedule # use to make schedule of getting data 
import pandas_market_calendars as mcal
from ftplib import FTP
from pandas_datareader.data import DataReader as dr
import os
from zipfile import ZipFile
import zipfile
import re
import csv
pd.set_option('display.max_rows', 2000)
from NSE_webscraping import get_expiry_from_option_chain,get_strike_price_from_option_chain
import main
from main import get_data

# import main
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <html><body>
        Hello. <a href="/get_data">Get today's Option Chain Data from NSE.</a>
        </body></html>
        '''

@app.route("/get_data")
def main_function():
        today_date = datetime.today().strftime('%Y-%m-%d')
        data = get_data()
        data.to_csv('Results/NSE_'+today_date+'.csv')
        # client = MongoClient('localhost', 27017)
        # db = client.NSEData
        # Data = appended_DATA.to_dict('records')
        # db.OptionsData.insert_many(Data, ordered=True)

        # with open("./Results/NSE_May.csv") as fp:
        #         csv = fp.read()
        # return Response(
        #                 csv,
        #                 mimetype="text/csv",
        #                 headers={"Content-disposition":
        #                 "attachment; filename=NSE_May.csv"})
        return Response(print('Downloade Complete for',today_date,'NSE Option Chain data'))

 
app.run(port=5001,debug=True)


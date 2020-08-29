import json
import requests
from common import logging
from bs4 import BeautifulSoup

def update_database():
	logging("Updating database.")
	url_twse = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=20200828&type=ALLBUT0999"
	res = requests.post(url_twse,)
	soup =  bs(res.text, 'html.parser')
	smt = json.loads(soup.text)
	return smt

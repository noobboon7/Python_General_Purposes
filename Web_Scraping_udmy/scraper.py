import requests
import bs4 

result = requests.get("https://www.marketbeat.com/dividends/monthly-dividend-payers/")

print(result.text)
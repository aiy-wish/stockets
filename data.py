import requests
import pandas as pd

API_TOKEN = 'c30qrliad3i9gms63qk0'

import requests
r = requests.get(f'https://finnhub.io/api/v1/stock/symbol?exchange=US&token={API_TOKEN}')
json_file = r.json()

#print(json_file[]['displaySymbol'])

tickers = []
names = []
#dictionary = {}
for elem in json_file:
    #dictionary[elem['displaySymbol']] = elem['description'].title()
    tickers.append(elem['displaySymbol'])
    names.append(elem['description'].title())

d1 = {'ticker': tickers, 'name':names}
df = pd.DataFrame(d1)

d2 = {'stock': df['ticker'] + ', ' + df['name']}
df = pd.DataFrame(d2)
df = df.sort_values(by=['stock'])
df = df.reset_index(drop=True)
#print(df)

def print_stuff():
    #file = open("dict.txt", "w")
    #file. write("%s = %s\n" %("dictionary", dictionary))
    #file. close()

    file = open("tickers.txt", "w")
    file. write("%s = %s\n" %("tickers", tickers))
    file. close()

    file = open("name.txt", "w")
    file. write("%s = %s\n" %("names", names))
    file. close()

    file = open("dataframe.txt", "w")
    file. write("%s = %s\n" %("df", df))
    file. close()

print_stuff()


'''
r = requests.get(f'https://finnhub.io/api/v1/stock/symbol?exchange=US&token={API_TOKEN}')
json_file = r.json()
try:
    tickers = json_file['displaySymbol']
    print(tickers)
except:
  print("An exception occurred")
'''

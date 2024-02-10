import yfinance as yf
import csv
import pandas as pd
df=pd.read_csv("./csvs/nifty_50.csv")
df2 = pd.read_csv("./csvs/list_of_variables.csv")
symbols = df['symbol'].tolist()
symbols = [str(i)+".NS" for i in symbols]
keys_list = df2['values'].tolist()
to_train = './csvs/train_nifty_50.csv'
fil = open(to_train, 'w')
w = csv.writer(fil)
w.writerow(keys_list)

def get_live_quote(symbol):
    stock = yf.Ticker(symbol)
    quote = stock.info
    return quote

print(keys_list)
def get_all_data(stock):

    q = get_live_quote(str(stock))
    with open(to_train, 'a') as file:
        writer = csv.DictWriter(file,fieldnames=keys_list)
        data_to_write = {header: q.get(header, "") for header in keys_list}
        writer.writerow(data_to_write)

for i in symbols:
    get_all_data(i)


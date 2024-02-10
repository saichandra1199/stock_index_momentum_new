# factor=1.0/sum(d.values())
# normalised_d = {k: v*factor for k, v in d.items() }
# 
# result = dict([a, float(x.replace(",",""))] for a, x in d.items())

# d={'a':-20, 'b':10,'c':40,'d':-30}
# print(sum([abs(i) for i in list(d.values())]))

# def normalize(d, target=1.0):
#    raw = sum([abs(i) for i in list(d.values())])
#    factor = target/raw
#    return {key:value*factor for key,value in d.items()}

# res = normalize(d)
# print(res)
# import datetime
# curr_time = (str(datetime.datetime.now())).split(".")[0]
# print(curr_time)

import yfinance as yf

def get_live_quote(symbol):
    stock = yf.Ticker(symbol)
    quote = stock.info
    return quote

q = get_live_quote("INFY.NS")

for k,v in q.items():
    print(k,"-----",v)
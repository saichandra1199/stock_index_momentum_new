import yfinance as yf
import csv

trade_values = []
symbols = {'ADANIENT.NS': 0, 'ADANIPORTS.NS': 0, 'APOLLOHOSP.NS': 0, 'ASIANPAINT.NS': 0, 'AXISBANK.NS': 0, 'BAJAJ-AUTO.NS': 0, 'BAJFINANCE.NS': 0, 'BAJAJFINSV.NS': 0, 'BPCL.NS': 0, 'BHARTIARTL.NS': 0, 'BRITANNIA.NS': 0, 'CIPLA.NS': 0, 'COALINDIA.NS': 0, 'DIVISLAB.NS': 0, 'DRREDDY.NS': 0, 'EICHERMOT.NS': 0, 'GRASIM.NS': 0, 'HCLTECH.NS': 0, 'HDFCBANK.NS': 0, 'HDFCLIFE.NS': 0, 'HEROMOTOCO.NS': 0, 'HINDALCO.NS': 0, 'HINDUNILVR.NS': 0, 'ICICIBANK.NS': 0, 'INDUSINDBK.NS': 0, 'INFY.NS': 0, 'ITC.NS': 0, 'JSWSTEEL.NS': 0, 'KOTAKBANK.NS': 0, 'LT.NS': 0, 'LTIM.NS': 0, 'M&M.NS': 0, 'MARUTI.NS': 0, 'NESTLEIND.NS': 0, 'NTPC.NS': 0, 'ONGC.NS': 0, 'POWERGRID.NS': 0, 'RELIANCE.NS': 0, 'SBILIFE.NS': 0, 'SBIN.NS': 0, 'SUNPHARMA.NS': 0, 'TATAMOTORS.NS': 0, 'TATASTEEL.NS': 0, 'TCS.NS': 0, 'TATACONSUM.NS': 0, 'TECHM.NS': 0, 'TITAN.NS': 0, 'ULTRACEMCO.NS': 0, 'UPL.NS': 0, 'WIPRO.NS': 0}
fil = open('nifty_oi.csv', 'a')
writer = csv.writer(fil)

def get_live_quote(symbol):
    stock = yf.Ticker(symbol)
    quote = stock.info
    return quote

def normalize(d):
   raw = sum([abs(i) for i in list(d.values())])
   factor = 1.0/raw
   return {key:value*factor for key,value in d.items()}

def trade_nifty(symbols):

    final_result = [] ;  p_change = {}
    for k,v in symbols.items():
        data = get_live_quote(str(k))
        print(str(k.split(".")[0]),end ="\r")
        symbols[str(k)] = data['volume']
        change = ((data['currentPrice']-data['open'])/data['open'])*100
        p_change[str(k)] = float(change)

    symbols_norm =normalize(symbols)
    p_change_norm= normalize(p_change)

    for (k1,v1), (k2,v2) in zip(symbols_norm.items(), p_change_norm.items()):
        if k1==k2:
            result = v1*float(v2)
            final_result.append(result)
  
    return sum(final_result)

while(1):
    value = trade_nifty(symbols)
    print("ratio value : ",value)
    trade_values.append(value)
    writer.writerow(value)


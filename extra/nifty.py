import csv,sched, time ,datetime
import yfinance as yf

curr_time = (str(datetime.datetime.now()).split(" ")[1]).split(".")[0]
fil = open('nifty_'+curr_time+'.csv', 'a')
writer = csv.writer(fil)
trade_dict = {'i':0}
time_gap = 30

symbols = {'ADANIENT.NS': 0, 'ADANIPORTS.NS': 0, 'APOLLOHOSP.NS': 0, 'ASIANPAINT.NS': 0, 'AXISBANK.NS': 0, 'BAJAJ-AUTO.NS': 0, 'BAJFINANCE.NS': 0, 'BAJAJFINSV.NS': 0, 'BPCL.NS': 0, 'BHARTIARTL.NS': 0, 'BRITANNIA.NS': 0, 'CIPLA.NS': 0, 'COALINDIA.NS': 0, 'DIVISLAB.NS': 0, 'DRREDDY.NS': 0, 'EICHERMOT.NS': 0, 'GRASIM.NS': 0, 'HCLTECH.NS': 0, 'HDFCBANK.NS': 0, 'HDFCLIFE.NS': 0, 'HEROMOTOCO.NS': 0, 'HINDALCO.NS': 0, 'HINDUNILVR.NS': 0, 'ICICIBANK.NS': 0, 'INDUSINDBK.NS': 0, 'INFY.NS': 0, 'ITC.NS': 0, 'JSWSTEEL.NS': 0, 'KOTAKBANK.NS': 0, 'LT.NS': 0, 'LTIM.NS': 0, 'M&M.NS': 0, 'MARUTI.NS': 0, 'NESTLEIND.NS': 0, 'NTPC.NS': 0, 'ONGC.NS': 0, 'POWERGRID.NS': 0, 'RELIANCE.NS': 0, 'SBILIFE.NS': 0, 'SBIN.NS': 0, 'SUNPHARMA.NS': 0, 'TATAMOTORS.NS': 0, 'TATASTEEL.NS': 0, 'TCS.NS': 0, 'TATACONSUM.NS': 0, 'TECHM.NS': 0, 'TITAN.NS': 0, 'ULTRACEMCO.NS': 0, 'UPL.NS': 0, 'WIPRO.NS': 0}

def get_live_quote(symbol):
    stock = yf.Ticker(symbol)
    quote = stock.info
    return quote

def normalize(d):
   raw = sum([abs(i) for i in list(d.values())])
   factor = 1.0/raw
   return {key:value*factor for key,value in d.items()}

def trade_nifty(symbols):

    final_result = [] ; final_v2={} ; p_change = {} ; pos= [] ; neg= []
    # print('Started................')
    for k,v in symbols.items():
        data = get_live_quote(str(k))
        print(str(k.split(".")[0]),end ="\r")
        symbols[str(k)] = data['volume']
        change = ((data['currentPrice']-data['open'])/data['open'])*100
        p_change[str(k)] = float(change)

    # symbols = dict([a, float(x.replace(",",""))] for a, x in symbols.items())
    symbols_norm =normalize(symbols)
    p_change_norm= normalize(p_change)

    for (k1,v1), (k2,v2) in zip(symbols_norm.items(), p_change_norm.items()):
        # print(k1,"#",v1,"#",v2)
        if k1==k2:
            result = v1*float(v2)
            final_result.append(result)
            final_v2[str(k1)] = float(v2)

    final_norm = normalize(final_v2)
    
    for i in list(final_norm.values()):
        if float(i)<0:
            neg.append(float(i))
        else:
            pos.append(float(i))

    return sum(final_result),pos,neg

def main(my_scheduler):

    try:
        my_scheduler.enter((time_gap)-0.5,0.5, main, (my_scheduler,))
        value,pos,neg = trade_nifty(symbols)
        ratio = sum(pos) + sum(neg)

        if abs(ratio)-abs(trade_dict['i'])>=0.15 or abs(ratio)-abs(trade_dict['i'])<=-0.15:
            print(" @@@@@@@@@@@@@@ Entry/Exit triggered @@@@@@@@@@@@@@")
            entry =["call" if ratio > trade_dict['i'] else "put"]
            # n = notify2.Notification(entry[0])
            print("{} {} {} {} {} {} {} {} {}".format(u'\u25B2',len(pos),u'\u25BC',len(neg),u'\u2192',round(ratio,4),round(trade_dict['i'],4),entry[0],"\U0001F600"))
            trade_dict['i'] = ratio

        print("{} {} {} {} {} {} ({})".format(u'\u25B2',len(pos),u'\u25BC',len(neg),u'\u2192',round(ratio,4),round(trade_dict['i'],4)))
        writer.writerow([ratio])
    except:
        pass
    
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(1,1, main, (my_scheduler,))
my_scheduler.run()

'''https://www.nseindia.com/all-reports-derivatives'''

import pandas as pd 
import sys
resl=[]
path = './csvs/web_fno_oi/'
s = pd.read_csv(path+'fao_participant_oi_{}2023.csv'.format(sys.argv[1]))

# (call long + put short)-(call short + put long)
c = (int(s['Unnamed: 5'][1])+ int(s['Unnamed: 8'][1]))- (int(s['Unnamed: 6'][1])+ int(s['Unnamed: 7'][1]))
d = (int(s['Unnamed: 5'][2])+ int(s['Unnamed: 8'][2]))- (int(s['Unnamed: 6'][2])+ int(s['Unnamed: 7'][2]))
f = (int(s['Unnamed: 5'][3])+ int(s['Unnamed: 8'][3]))- (int(s['Unnamed: 6'][3])+ int(s['Unnamed: 7'][3]))
p = (int(s['Unnamed: 5'][4])+ int(s['Unnamed: 8'][4]))- (int(s['Unnamed: 6'][4])+ int(s['Unnamed: 7'][4]))
long = int(s['Unnamed: 5'][5])
short = int(s['Unnamed: 8'][5])


resl.extend([c,d,f,p])
result = resl[1]+resl[2]+resl[3]
res = [abs(ele) for ele in resl]
ratio = round(res[0]/sum(res) , 3)*2

def normalize(l):
   raw = sum([abs(i) for i in l])
   factor = 1.0/raw
   return [round(value*factor,3) for value in l]

norm_resl = normalize(resl)
print(norm_resl)
#print("Calls : ",int(long/pow(10,4)))
#print("Puts  : ",int(short/pow(10,4)))

if result>0:
    print('Bullish ==> {} && {}'.format(int(abs(sum([i for i in resl if i>0])/pow(10,3))),ratio))
else:
    print('Bearish ==> -{} && {}'.format(int(abs(sum([i for i in resl if i<0])/pow(10,3))),ratio))


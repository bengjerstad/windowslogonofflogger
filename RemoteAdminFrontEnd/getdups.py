import requests
import json
import pandas as pd
from datetime import date
from datetime import datetime
from dateutil import parser

r = requests.get('http://10.24.25.130:8000/get_dup')
newtxt = json.loads(r.text)

#s  = pandas.Series(newtxt,index=newtxt.keys())
df = pd.DataFrame(newtxt)
df = df.transpose()
#print(df)
dt=[]
for idx,x in enumerate(df['time']):
	newx = x.replace("_"," ")
	dt.append(parser.parse(newx))
	#print(dt)
print(df.columns.values)
del df['time']
df['date time'] = pd.Series(dt)

print(df)

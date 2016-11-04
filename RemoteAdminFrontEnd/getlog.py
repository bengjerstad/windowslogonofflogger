import requests
import json
import pandas as pd
from datetime import date
from datetime import datetime
from dateutil import parser
import sys

args = sys.argv

r = requests.get('http://10.24.25.130:8000/get_log?username='+args[1]+'&compname=all')
newtxt = json.loads(r.text)
if (newtxt=={}): 
	print("Returned nothing.");
else:
	#s  = pandas.Series(newtxt,index=newtxt.keys())
	df = pd.DataFrame(newtxt)
	df = df.transpose()
	#print(df)
	dt=[]
	for idx,x in enumerate(df['time']):
		newx = x.replace("_"," ")
		#print(newx)
		dt.append(parser.parse(newx))
		

	print(df.columns.values)
	del df['time']
	df['date time'] = dt

	print(df)

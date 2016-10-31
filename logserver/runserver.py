import hug
import json
import sqlite3
import pandas as pd
conn = sqlite3.connect('users.db')
c = conn.cursor()

@hug.get(examples='username=bgjerstad&compname=011acboe&stat=on&time=2016-10-20_0229 PM')
@hug.local()
def log_this(username: hug.types.text, compname: hug.types.text,stat: hug.types.text,time: hug.types.text,  hug_timer=3):
	data = {'username':'{0}'.format(username),'compname':'{0}'.format(compname),'stat':'{0}'.format(stat),'time':'{0}'.format(time)}
	data2 = (username,compname,stat,time)
	try:
		c.execute("INSERT INTO users VALUES "+str(data2))
	except sqlite3.OperationalError:
		makedb()
		c.execute("INSERT INTO users VALUES "+str(data2))
	conn.commit()
	return data

@hug.get(examples='username=bgjerstad&compname=011acboe')
@hug.local()
def get_log(username: hug.types.text, compname: hug.types.text,hug_timer=3):
	data2 = (username,compname)
	print(data2)
	c = conn.cursor()
	logs = {}
	dbkeys = ['username','compname','stat','time']
	if(data2==('all','all')):
		where = "1"
	if(data2[0]=='all' and data2[1]!='all'):
		where = "compname=' "+compname+" '"
	if(data2[1]=='all' and data2[0]!='all'):
		where = "username = ' "+username+" '"
	if(data2[1]!='all' and data2[0]!='all'):
		where = "username=' "+username+" ' AND compname=' "+compname+" '"
	try:
		dbout = c.execute("SELECT * FROM users WHERE "+where)
	except sqlite3.OperationalError:
		makedb()
		dbout = c.execute("SELECT * FROM users WHERE "+where)
	for idx,row in enumerate(dbout):
		logs[idx] = dict(zip(dbkeys,row))
	return logs

@hug.get(examples='')
@hug.local()
def get_dup(hug_timer=3):
	logs = {}
	dbkeys = ['compname','time','stat']
	#exclustion list
	exlist = [' star ',' tneurohr ']
	#get a list of all of the users
	userlist = []
	try:
		dbout = c.execute("SELECT DISTINCT username FROM users WHERE 1")
	except sqlite3.OperationalError:
		makedb()
		dbout = c.execute("SELECT DISTINCT username FROM users WHERE 1")
	for idx,row in enumerate(dbout):
		if not(row[0] in exlist):
			userlist.append(row[0])
	#for each user:
	# check if user has loged on twice but not logged off.
	for idx,user in enumerate(userlist):
		dbout = c.execute("SELECT compname,time,stat FROM users WHERE username='"+user+"'")
		dbout = dbout.fetchall()
		logcnt = len(dbout)	
		if(logcnt > 1):
			last = ''
			for row in dbout:
				if(row[2]==last):
					#print(user,row)
					thisis = user+row[1]
					logs[thisis] = dict(zip(dbkeys,row))
				last = row[2]
	return logs

@hug.get(examples='action=clear')
@hug.local()
def db(action: hug.types.text, hug_timer=3):
	#drop the table then recreate it.
	c.execute("DROP TABLE users")
	c.execute('''Create Table users (username text,compname text,stat text,time text)''')
	conn.commit()
	return 1

def makedb():
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute('''Create Table users (username text,compname text,stat text,time text)''')
	conn.commit()


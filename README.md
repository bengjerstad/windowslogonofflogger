# windowslogonofflogger
Project to log logons and logoffs of windows users to detect if a password has been compromised. 

This project is broken up into 2 parts:

1. Client script to gather info and send an HTTP request to the server.
The client script is a batch file that gets username, IPaddress, computername date and time 
the script calls a javascript file to send the gathered info in a HTTP request to the server. 

2. A server to log the HTTP request and get back the data.
The server is a hug server: http://www.hug.rest/ 
the hug server exposes a RESTFUL API and allows the logging and data analysis to take place in python. 
The python code pushes and pulls from a sqlite3 database file. 

Setup/Install
Set up server:
1. Install python and hug on a server.
2. Copy server files to the server.
  I copied the files to my user folder at /home/admin
3. Run the makedb.py script to write the database file.
4. run and test:
  hug -f 'home/admin/myapiwithdb.py'

Set up login scripts for windows domain.
1. Add the scripts to the login and logoff of grouppolicy
(https://technet.microsoft.com/en-us/library/cc770908(v=ws.11).aspx)
2. run and test

I had to make a change to the logon and logoff script because the batch file was not finding wget.js
I used:
\\[domain]\SysVol\anderson.ketsds.net\Policies\[sid]\User\Scripts\Logon\wget.js
instead of wget.js

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

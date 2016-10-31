# windowslogonofflogger
Project to log logons and logoffs of windows users to detect if a password has been compromised. 

This project is broken up into 3 parts:

1. Client script to gather info and send an HTTP request to the server.
The client script is a batch file that gets username, IPaddress, computername date and time 
the script calls a javascript file to send the gathered info in a HTTP request to the server. 

2. A server to log the HTTP request and get back the data.
The server is a hug server: http://www.hug.rest/ 
The hug server exposes a RESTFUL API and allows the logging and data analysis to take place in python3. 
The python code pushes and pulls from a sqlite3 database file. 

3. A front end to get the data from the server to the admin. 

Setup/Install
Set up server:

1. Install dependencies on server
  * python3
  * hug
    ```
    pip3 install hug --upgrade

    ```
  * sqlite
  * pandas
2. Copy server files to the server.
  I copied the files to my user folder at /home/admin
3. Run the makedb.py script to write the database file.
4. Run and test:

  Run:
  ```
  hug -f 'home/admin/myapiwithdb.py'
  
  ```
  Test:
  
  To test logging, open up a browser and enter:
  
  http://10.24.25.130:8000/log_this?username=bgjerstad&compname=011acboe&stat=on&time=2016-10-20_0229 PM
  
  To test getting the logs out of the server, in the browser enter:
  
  http://10.24.25.130:8000/get_log?username=bgjerstad&compname=011acboe
  
 
Set up login scripts for windows domain:

1. Add the scripts to the login and logoff of grouppolicy
 (https://technet.microsoft.com/en-us/library/cc770908(v=ws.11).aspx)
2. Run and test

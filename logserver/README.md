### Set up server:
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
3. Run and test:

  Run:
  ```
  hug -f 'home/admin/myapiwithdb.py'
  
  ```
  Test:
  
  To test logging, open up a browser and enter:
  
  http://[SERVER_IPADDRESS]:8000/log_this?username=bgjerstad&compname=011acboe&stat=on&time=2016-10-20_0229PM
  
  To test getting the logs out of the server, in the browser enter:
  
  http://[SERVER_IPADDRESS]:8000/get_log?username=bgjerstad&compname=011acboe
  
 
 ### Functions

Full definiton at: windowslogonofflogger/logserver/APIdefinition.md

log_this: to be used by scripts to log data into the database

get_log: to retrive all or parts of the log

get_dup: to get a list of users who have logged in at multiple computers. 

db: allows for clearing the database

ex_this: create a list of names to ingore in the get_dup function. 

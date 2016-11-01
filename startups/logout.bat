@echo off
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)

cscript /nologo %~dp0/wget.js "http://10.24.25.130:8000/log_this?username="+%USERNAME%+"&compname="+%computername%+"&stat=off&time="+%mydate%_%mytime%

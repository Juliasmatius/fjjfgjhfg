import requests
url = 'https://raw.githubusercontent.com/Juliasmatius/fjjfgjhfg/main/main.py'
r = requests.get(url, allow_redirects=True)
open('c:/julinjutut/main.py', 'wb').write(r.content)
import time
import random
import os
while True:
	timewait = random.randint(300, 900)
	print("Time seconds "+str(timewait))
	print("Time minutes "+str(timewait / 60))
	jsselect = round(random.randint(1, 9) / 3)
	print("Jumpscare num : "+str(jsselect))
	os.system("timeout /t "+str(timewait)+"")
	
	if jsselect < 1:
		os.system('start /d "%ProgramFiles(x86)%\Windows Media Player" wmplayer.exe "c:/jumpscarer/jump1.mp4"')
		time.sleep(33)
		os.system("taskkill /F /IM wmplayer.exe")
	if jsselect == 2:
		os.system('start /d "%ProgramFiles(x86)%\Windows Media Player" wmplayer.exe "c:/jumpscarer/jump2.mp4"')
		time.sleep(2)
		os.system("taskkill /F /IM wmplayer.exe")
	if jsselect == 3:
		os.system('start /d "%ProgramFiles(x86)%\Windows Media Player" wmplayer.exe "c:/jumpscarer/jump3.mp4"')
		time.sleep(2)
		os.system("taskkill /F /IM wmplayer.exe")

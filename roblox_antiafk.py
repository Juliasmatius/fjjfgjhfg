import keyboard
import time
import os
import winshell
os.system("xcopy /s %cd%\roblox_antiafk.py c:/roblox_antiafk.py")
desktop = winshell.desktop()
path = os.path.join(desktop, "Julin jutut.lnk")
target = r"c:/roblox_antiafk.py"
wDir = r"c:/"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.save()	
direction = 1
os.system("timeout 10")
totaltimes = 0
while True:
	times = 20
	if direction == 0:
		direction = 1
		while times > 0:
			keyboard.press_and_release('w')
			time.sleep(0.5)
			times = times - 1
			print(times)
			totaltimes = totaltimes + 1
		direction = 1
	if direction == 1:
			direction = 0
			while times > 0:
				keyboard.press_and_release('s')
				time.sleep(0.5)
				times = times - 1
				print(times)
				totaltimes = totaltimes + 1
			direction = 0
	print("direction")
	print(direction)
	print("Total times")
	print(totaltimes)

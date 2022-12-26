import os
import winshell
from win32com.client import Dispatch
def roblox_antiafk():
	os.system("python3 c:/julinjutut/roblox_antiafk.py")
def update():
	print("Updating...")
	os.system('python3 c:/julinjutut/update.py')
def createshortcut():
	desktop = winshell.desktop()
	path = os.path.join(desktop, "Julin jutut.lnk")
	target = r"c:/julinjutut/update.py"
	wDir = r"c:/julinjutut"
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(path)
	shortcut.Targetpath = target
	shortcut.WorkingDirectory = wDir
	shortcut.save()	
	start()
def start():
	print("Welcome")
	print("1. Update")
	print("2. Create a shortcut to desktop")
	print("3. Exit")
	print("4. Roblox Anti-AFK")
	selection = input("Selection : ")
	if selection == "4":
		roblox_antiafk()
	if selection == "1":
		update()
	else:
		if selection == "2":
			createshortcut()
		else:
			if selection == "3":
				exit()
			else:
				print("Invalid selection")
				start()
start()

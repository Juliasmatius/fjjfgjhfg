import os
def update():
	print("Updating...")
	os.system('start "Updating... " python3 c:/julinjutut/update.py')
def start():
	print("Welcome")
	print("1. Update")
	print("2. Exit")
	selection = input("Selection : ")
	if selection == "1":
		update()
	else:
		if selection == "2":
			exit()
		else:
			print("Invalid selection")
			start()
start()
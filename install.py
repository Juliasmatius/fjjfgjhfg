
def start():
	shure = input("Are you shure you want to install? [Y/N]")
	if shure == "N":
		exit()
	if shure == "Y":
		print("OK")
	print("Invalid")
	start()
start()

from getpass import getpass

def checker(username, password):
	if (username == 'Arnulfo') and (password == 'arnulfo118'):
		print("User Logged in")
		print( (username == 'Arnulfo') and (password == 'arnulfo118') )
	else:
		print("Wrong credentials")
		login()

def login():
	username = input("Enter username.. ")
	password = getpass("Enter password.. ")
	checker(username, password)
login()

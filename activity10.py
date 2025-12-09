from getpass import getpass
username = 'arnulfo'
password = 'arnulfo123'
 
user = input("USERNAME --> ")
passw = getpass("PASSWORD --> ")

if (user == username) and (passw == password) :		 	 	 	 
    print ("Logged in")
else:
    print ("Wrong Credentials")

#Small script for creating users from an Excel file.

#Imports necesary modules.
import pexpect as px
import pandas as pd

#Reads the file without headers or index.
file = pd.read_excel("Names_mod.xls", header=0, index=0)

#Funktion for removing unnecasary parts from the cell containing the phonenumber.
def phoneSplit(phone):
	nums = file.at[col, 3]
	nums = nums.strip('Tel: ')
	return nums

#Function for creating new users.
#Expects and replys on the interactive command "adduser".
def newUser():
	child = px.spawn("adduser " + str(username)) 
	child.expect('.*password: ')
	child.sendline(str(passwd)) 
	child.expect('.*password: ')
	child.sendline(str(passwd)) 
	child.expect('\r\n')
	child.expect('\r\n')
	child.expect(':*')
	child.sendline(str(name))
	child.expect(':*')
	child.sendline(str(room))
	child.expect(':*')
	child.sendline('')
	child.expect(':*')
	child.sendline(str(phone))
	child.expect(':*')
	child.sendline('Na')
	child.expect('\r\n')
	child.sendline('y')
	child.sendline('')

#Itererates the document, declaring variables with values from the correct cell.
#Calls the function for sanitizing the phonenumber from invalid data.
#Calls the function for adding new users. 
for col, row in file.iterrows():
	username = file.at[col, 5]
	passwd = file.at[col, 6]
	name = file.at[col, 0]
	room = file.at[col, 2]
	phone = phoneSplit(file.at[col, 3])
	newUser()
	print("Creates: user: " + str(username) + " passwd: " + 
		str(passwd) + " name: " + str(name) + " Nums: " + str(phone))
	
print ("Users have been created!")

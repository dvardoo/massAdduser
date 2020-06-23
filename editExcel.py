#Small script for manipulation of an excel file.

#Imports necessary libraries.
import pandas 
import random
import string

#Reads the original file.
file = pandas.read_excel("names.xls", header=None)

#Function for randomizing 4 letters as a username.
def user():
	chars = "".join([random.choice(string.ascii_lowercase) for i in range(4)])
	return chars

#Function for randomizing a password
#Choses 4 random words from the list and merges.
def passwd():
	#Only an example of wordlist, real scenario should use a more extensive wordlist.
	wordList = ["quotation","momentum","eavesdrop","fat","appetite","calendar",
	"horseshoe","sickness","redundancy","reason","lover","sight","lump","bomber",
	"trolley","poll","assertive","harvest","defeat","balance","inhabitant",
	"operational","invasion","fragment","hospitality","screen","other",
	"acquisition","thesis","bank","conservative","romantic","prestige",
	"celebration","bee","shareholder",]
	
	#Joins 4 of the words from list as a variable.
	randWord = ''.join(random.choice(wordList) + random.choice(wordList)
		+ random.choice(wordList) + random.choice(wordList))
	return randWord #Returns the variable

#Loops the Excel file, adding username and password. 
for name, row in file.iterrows():
	file.at[name, 5] = user() + str(name) 
	file.at[name, 6] = passwd() 
	file.to_excel("Names_mod.xls") 
	
print(file)

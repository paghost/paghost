#! /usr/bin/python

#Import Passwords 

# import passwords from all lists and 

from os import system, name
import glob

# open files and link to variables to append texts

let2txt = open("let2.txt", "a")
let3txt = open("let3.txt", "a")
let4txt = open("let4.txt", "a")
let5txt = open("let5.txt", "a")
let6txt = open("let6.txt", "a")
let7txt = open("let7.txt", "a")
let8txt = open("let8.txt", "a")
let9txt = open("let9.txt", "a")
let10txt = open("let10.txt", "a")
let11txt = open("let11.txt", "a")
let12txt = open("let12.txt", "a")
let13txt = open("let13.txt", "a")
let14txt = open("let14.txt", "a")
overtxt = open("over.txt", "a")


# findlength

def findlength(each1):
	count = 0
	for i in each1:
		count += 1
	return count

# Convert wordlists to list variables?? fuck

def floodvars(wls):
	for each in wls:
		length = findlength(each)
		
		if length == 2:
		  let2txt.writelines(each)
		elif length == 3:
		  let3txt.writelines(each)
		elif length == 4:
		  let4txt.writelines(each)
		elif length == 5:
		  let5txt.writelines(each)
		elif length == 6:
		  let6txt.writelines(each)
		elif length == 7:
		  let7txt.writelines(each)
		elif length == 8:
		  let8txt.writelines(each)
		elif length == 9:
		  let9txt.writelines(each)
		elif length == 10:
		  let10txt.writelines(each)
		elif length == 11:
		  let11txt.writelines(each)
		elif length == 12:
		  let12txt.writelines(each)
		elif length == 13:
		  let13txt.writelines(each)
		elif length == 14:
		  let14txt.writelines(each)
		else:
		  overtxt.writelines(each)

# Open wordlist and convert .txt to a string variable 
myfiles = []

for each_file in glob.glob("/wls/*.*"):   

	myfiles.append(each_file)
	wlsfile = open(each_file, "r")
	print ('Importing ',each_file)
	floodvars(wlsfile)
	

# What ppl see when they start the program :)

system('clear')

print ('\n')

print ("                             PWD HAX               Jan 15, 2022\n\n\n\n\n")


print ('2 Letter Words  = ',len(let2))
print ('3 Letter Words  = ',len(let3))
print ('4 Letter Words  = ',len(let4))
print ('5 Letter Words  = ',len(let5))
print ('6 Letter Words  = ',len(let6))
print ('7 Letter Words  = ',len(let7))
print ('8 Letter Words  = ',len(let8))
print ('9 Letter Words  = ',len(let9))
print ('10 Letter Words = ',len(let10))
print ('11 Letter Words = ',len(let11))
print ('12 Letter Words = ',len(let12))
print ('13 Letter Words = ',len(let13))
print ('14 Letter Words = ',len(let14))
print ('Over 14 Letters = ',len(over))
print ('')
print ('Total Words = ')




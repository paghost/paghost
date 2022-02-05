#! /usr/bin/python

from os import system, name
import glob


# Declare all list variables

let1 = ['a']
let2 = ['aa']
let3 = ['aaa']
let4 = ['aaaa']
let5 = ['aaaaa']
let6 = ['aaaaaa']
let7 = ['aaaaaaa']
let8 = ['aaaaaaaa']
let9 = ['aaaaaaaaa']
let10 = ['aaaaaaaaaa']
let11 = ['aaaaaaaaaaa']
let12 = ['aaaaaaaaaaaa']
let13 = ['aaaaaaaaaaaaa']
let14 = ['aaaaaaaaaaaaaa']
over = ['abababababababa']



# Convert wordlists to list variables?? fuck

def floodvars(wls):
	for each in wls.readlines():
		each = each.rstrip('\n')
		if len(each) == 1:
	  	  let1.append(each.lower())
		elif len(each) == 2:
		  let2.append(each.lower())
		elif len(each) == 3:
		  let3.append(each.lower())
		elif len(each) == 4:
		  let4.append(each.lower())
		elif len(each) == 5:
		  let5.append(each.lower())
		elif len(each) == 6:
		  let6.append(each.lower())
		elif len(each) == 7:
		  let7.append(each.lower())
		elif len(each) == 8:
		  let8.append(each.lower())
		elif len(each) == 9:
		  let9.append(each.lower())
		elif len(each) == 10:
		  let10.append(each.lower())
		elif len(each) == 11:
		  let11.append(each.lower())
		elif len(each) == 12:
		  let12.append(each.lower())
		elif len(each) == 13:
		  let13.append(each.lower())
		elif len(each) == 14:
		  let14.append(each.lower())
		else:
		  over.append(each.lower())

# Open wordlist and convert .txt to a string variable 
myfiles = []


for each_file in glob.glob("*.txt"):   

	myfiles.append(each_file)
	wlsfile = open(each_file, "r")
	print ('Importing ',each_file)
	floodvars(wlsfile)
	
# What ppl see when they start the program :)
def startprogram():
	system('clear')
	print ('\n')
	print ("                                            PWD HAX               Feb 4th, 2022\n\n\n\n\n")
	print ('\n') 
	print ('\n')
	print ('\n')



# Sequence Variables
def seqvars():
	for each in range(len(let1)):
		for each2 in range(len(let2)):
		 	for each3 in range(len(let3)):
				print(let1[each] + let2[each2] + let3[each3])


startprogram()


seqvars()


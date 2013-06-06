#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
#*************************************

#REMINDER: OPEN THIS FILE IN IDLE

#You're almost at the end of Task 1!
#Hopefully, this has so far been a recap of programming skills you already know in another language.
#If not, please make sure you have done the optional programming exercises in the 'Playing around with Python' sections to reinforce your learning.

#Now that you know the basics, we will start combining several concepts to create even more powerful programs.

#============= Looping over lists ==================

#What if you have a list of items and for each item you want to do something? Python is able to do this very quickly and much more easily than Java.
#Imagine if the list had 100 items, 3 items or no items. The logic is the same and can be done in one line in Python. 

items = ['Milk', 'Bread', 'Cheese'] #Define a list of strings

for item in items: #'item 'is the name of the current String item of the list that the loop is on, you can name it anything
	print item 

#This loop prints out every item in the list. 
#This is a very powerful tool in Python and shows how you can simply loop through an array/list

#======================= Play around with Python a bit  =================================
#	
#	Create a new file in this folder called loopLists.py
#	Inside it, define a list of Strings of your 5 favourite movies.
#	Now, loop over the list. For each item in the list, print out "Movie: " plus the movies name.
#	Can you figure out how to outprint Movie 1: <Movie 1's name>
#	Movie 2: ... etc?
#	HINT: Google would be needed for this one!
#
#==================================================================================================


#============= Writing while loops ==================

#A while loop is more advanced than a for loop. Instead of specifiying how many times you want it to run in advance, 
#The while loop will continue to execute until the condition is no longer true.
#You have to set up a while loop carefully because you may create an infinite loop if the condition cannot become false in the execution of the while loop!

i = 9
while i < 10:
   i = i + 1
   
#The loop will only execute once because the condition while i < 10 is not true after you have added 1 to i

#Infinite while loops:
# i = 10
# while i < 14
#    print "I can see infinity"
#This will loop forever becaise the condition i < 14 will always be true because you never change i in the while loop -> be careful!

#While loops are useful for validation. What if you want a user to keep inputting things until he gets something right?
#While the user has not entered the correct thing...execute some code. This will be useful in the upcoming tasks.

#======================= Play around with Python a bit  =================================
#	
#	Create a new file in this folder called whileNot.py
#	In your program, type 'import random' in the top line.
#	Then, type num = random.randint(1,5) 
#	Everytime your program is run, num will be assigned a random integer from 1 to 5.
#	Now, get a users input and cast it to an int. Store it in a variable numGuess.
#	While numGuess is not equal to num, give the user another guess!
#	Under the while loop, type a print statement to outprint "You guessed correctly!"
#	Run your program a few times - how many tries does it take you to get it right? 
#	Extend your program to make it even harder for the user to guess the right answer.
#
#==================================================================================================


#============= Comparing Strings and else if else statements ==================  
#We can have more complicated logical structures. We can chain up multiple if statements.
#elif stands for else if. If the first condition isn't satisfied, it will check the 2nd, then the third, then if none of the top are true, it will have to execute the else.
 
name = "John"
if name == "Mary": #First check
	print "Hello"
elif name == "Peter": #If first check fails then another check
	print "Parker"
else:                 #If all the checks above fails
	print "Ok :(" 
	
#You can of course only have an if statement or an if statement with as many elif's as you want or just an if-else. You cannot just have an elif or else.


#============= The difference between assigning things to variables and checking if a variable has a certain value ==================  
	
#Note that name = "John" means you are assigning the string John to name. 
#name == "Mary" means 'check if the String stored in the variable name equals "Mary" . 

# Don't confuse = and ==  ********* NB ************

#============== Nesting (Slightly more advanced though processes) ===================

if name == "A":
		if name =="B":
			print "It isnt possible for this code to execute, how can the variable name be two things at once?"
else:
	print "Your name isnt A but I cant automatically assume from that that it isnt B" 
	
#Think about this one logically! Note the indentation carefully. You have an if within an if else. 

#You can also have a for within a for loop (a nested for), a while within a while -> anything you want really! 


#============== Conditionals revisited ==================

if name == "A" or name =="B":
	print "Your name is either A or B but I dont know for sure which!"
elif name =="A" and name =="B":
	print "This code will never execute because name cant be both the string A and B at the same tiem"
	
#or is the symbol for 'OR' and and is the symbol for 'AND' which match up to logic. 
#Think about how two nested if statements is similar logic to one if statement with an AND condition! 

#======================= Play around with Python a bit (OPTIONAL) =================================
#	
# 	Write a new program, andOr.py.
#	The program should take an integer as input, and a random integer from 1 to 10.
#	Only using one if condition, have the program output "True" when the users integer is bigger than the random integer
#	and also even
#
#==================================================================================================

#======================= Play around with Python a bit (OPTIONAL) =================================
#	
# 	Write a new program, listsTwo.py
#	The program should take an integer as input. It should then allow the user to input as many Strings as the number into a list of Strings.
#	For example, if the user enters 3, the program should program them three seperate times for a String.
#	Once this is working, extend your program so that a user can only enter a String that isn't already in the list.
#	Think about how this can be done most efficently. 
#
#==================================================================================================

#======================= Play around with Python a bit (OPTIONAL) =================================
#	
#	Write a new program named TomRiaz.py and save it in this folder.
#	The program should take in a users name.  Only if his name is "Riaz" OR "Tom" will it execute a for loop asking 
#	for some the user to add items to a list (similar to the above optional exercise). 
#	If the user's name was "Tom" it will print the list of all the items the user entered, if it was "Riaz" it will not print the list. 
#	This is because Riaz just tells Tom what to buy, Tom needs to see the list at the end of the program!
#	Try thinking about the logic behind if statements , OR , AND and how you can do just about anything if you use the right combition of these at the right time!
#
#==================================================================================================

# ********************* CHECKPOINT. THE EXAMPLE CODE FOR TASK 1 IS NOW COMPLETE  *****************************************
#Nesting can be very confusing. Try your best to understand! You can complete Task 1 and move on to Task 2 and more Python techniques without understanding nesting techniques fully.
#Please read how to run python files below as there are two options to do so -> Hopefully you have done some of the optional exercises by now and already know how to do this!


#Now, time to write your first simple Python program in order to move on to Task 2 and even more exciting Python techniques:

#*************** TASK 1, THE COMPULSORY AND FINAL TASK FOR THIS SECTION OF INTRODUCTORY PYTHON ****************
#	Write a python program that takes in a user input as a String. While the String is not "John", add every string entered to a list until "John" is entered. Then outprint the list. 
#	 This program basically stores all incorrectly entered strings in a list where "John" is the only correct string. Save this as John.py in this folder.
#	 Example input : "Riaz", "Tom", "John"
#    Output: ['Riaz','Tom']
# 	 AFTER YOU COMPLETE THIS TASK, MAKE SURE John.py IS IN YOUR DROPBOX FOLDER FOR ONE OF OUR TEACHERS TO CHECK IT AND GIVE YOU TASK 2 ******************

#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
#*************************************

#REMINDER: OPEN THIS FILE IN IDLE.

#Congrats! You've made it to Task 3.
#You've learnt the basics of programming - variables, data types, if statements, casting and loops.
#These basics are the core of all programming languages - in fact - they are all you need!
#It has been scientifically proven that anything and everything that can be possibly computed, can be computed with just these tools!

#Just like with basic tools out ancestors used (such as stone hammers/bone daggers), we have moved on to make advanced tools such as Jet Engines, Skyscrapers and planes..
#The most basic tools of computation are those you have learnt.
#Any language, or method that can in some way encode or carry out what you have learnt is known as TURING COMPLETE.
#This is named after the famous Computer Scientist - Alan Turing. Alan Turing came up with the Theory of Computation - which proves that anything can be computed with
#the simple methods and tools you have used.

#Sounds crazy right? It isn't. When people study 'Computer Science', this is the core theme of the science. Why not read up about it and Turing a bit?
#You may also be interested in knowing that the human DNA has been proven to be Turing-Complete. This means that any kind of computation is possible within our bodies -
#and even that Python has the same computational power as our own bodies.

#So why bother with learning more programming tools? Imagine having to compute everything using reactions of DNA in test tubes!
#From here on, any programming tools you learn are just for CONVENIENCE. They help make a programmers life much easier. But THEORETICALLY speaking, you don't even need them!


#============= Working with lists/arrays ==================

#You have learnt about Strings, Ints and Float variables. But you can also have LISTS.
#You can have a LIST of Strings, Ints or Floats. But not a list of a combination of these.
#Lists and list operations are always specified by square brackets []. 

#Here we define a list of 3 strings. So this is a String list

stringList = ['John', 'Mary', 'Harry'] #Python knows that anything defined in [] is an array (Java) which in Python is known as a list. There are 3 String items in this list.

#We can dive into a list and get any element.
#In all programming languages, the first element of a list is at 0. The second is at 1 etc. 

print stringList[0] #prints 0th element of list, John

print stringList[1:2] #prints everything from the 1st to the 2nd element of list, NOT Including the 2nd element. so only prints the item in th 1th position which is Mary

print stringList[0:] #prints everything from the 0th position to the end ie the entire list

print stringList #A faster way to print the entire list 

stringList[2] = "Tom" #We can replace the 3rd element of the list with a new String. 'Harry' will be lost.

print stringList #To see that the list has changed

stringList.append("Mary") #We can add to the end of a list like this. This is important! We don't want to lose what is already on the list -> the safest bet is to just put new things on the end!

print len(stringList) #Will print the total number of items in the list, currently 4


#**** EXTRA INFORMATION ****
#NB. LISTS are not totally like java ARRAYS. They do NOT have a fixed limit you have to set at the start! (Don't worry if you dont know about this)
#They can dynamically resize, as you append items they just grow with no problem. As you remove, the same can happen with no errors.
#You can start of with an empty list A = [] . Then go A.append("Hi") and A will now be ['Hi']. That's really painless compared to Java!
#This is because Python 'Lists' are a more advanced 'Data Structure' than 'Arrays' in other languages --> But that's a more advanced topic!


#======================= Play around with Python a bit =================================
#
#	You've now learnt about if statements, for loops, and lists. That's a lot and those are really the bread and butter of Python.
#	Try write another simple program, called listMe.py , that takes in one user input (as a String) and then adds it to the end of a list. 
#	So our list will have one item like ['Input']
#	See if you can extend the program so that the user enters an integer lets call that interget n. 
#	Then using a for loop, the user gets to add n items to a list. Print the list out at the end to see if its working 
# 	and run it a few times by yourself with differnet input to check if it's working correctly - it's all about practice!
#
#	An example run of the above program is
#	Enter a number: 3                -> First raw_input
#	Enter an item: Dog               -> Start of for loop asking for items to put into list
#	Enter an item: Cat               -> 2nd run of for loop
#	Enter an item: Harry             -> 3rd and last run of for loop
#	Your list is: ['Dog','Cat','Hary'] -> the output of the list that has had the three Strings above appended to it
#
#	From the problem description I hope you can logically see that a program like this will use: 
# 	- raw_input to get user input , casting to cast this input from a String to an int int(raw_input("Enter your number"))  , a for loop to loop that number of times, 
#	 and a list to append new Strings from a second raw_input INSIDE the for loop!
#	It is helpful to think like this before starting to write a program. 
#
# 	Remember you can define a for loop by going:
#	rangeEnd = 10
#   for i in range(1, rangeEnd):
#		print i 
#
#   In programming, you should be able to stick in a variable anywhere you like! 
#	Think of the possibilities and many different ways to create the same program!
#
#==================================================================================================

# ********************* CHECKPOINT. Please make sure you understand LISTS, FOR LOOPS, IF STATEMENTS, VARIABLES, and GETTING INPUT  *****************************************
#If you do not by this point, then you should go back and try complete the optional tasks above. 
#If you still feel some things are not clear, please read the attached AdditionalReading.pdf, or create a new file in your Dropbox folder called 'Help.txt' and write what you need help with.
#Remember you can visit www.rmoola.com/advice.html for all the ways you can get help from us and our tutors are always standing by monitoring your Dropbox folder.

#As a new programmer, the above may take you a while to get your head around - rather take the time to learn the fundementals now than rush ahead!
#Remember that ALL programming languages have these 'structures' (if statements, for loops, lists etc). So if you can learn them now, they will apply to all other languages.


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

for item in items:
	print item 

#This loop prints out every item in the list. 
#This is a very powerful tool in Python and shows how you can simply loop through an array/list

#======================= Play around with Python a bit (OPTIONAL) =================================
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

#======================= Play around with Python a bit (OPTIONAL) =================================
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

#****************** END OF EXAMPLE CODE FOR TASK 3 ********************* #

#== Make sure you have read and understand all of this example.py file.
#== Now please complete the compulsory program for this Task as specified in the 'Instructions' pdf file in this folder ===
#== For this compulsory program you are required to create a file called John.py in this folder and complete a simple program ===
#== Make sure you create John.py in this folder so that one of our tutors can find it and mark it. ===


#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!

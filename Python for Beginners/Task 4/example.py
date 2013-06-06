#Welcome to the example file for your 4th.
#Now that you've completed the basic introduction to Python and completed a program correctly I am assuming you know how to create, run, edit python files correctly.
#I also hope you are able to google and use the python documents to find certain information out. This is a programmers greatest tool.
#Our teachers are of course still completely willing to help you!

#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
#*************************************


#This example.py will teach you how to create files with python, read from them, and define functions.
#You will need to use knowledge from Task 1 as these are the fundementals of programming and techniques found in Task 1 apply to almost every programming language -> So dont be afraid to refer back!

#======= Working with files in Python ===== #


#Python includes a built-in file type. The line below creates a new file 'object' named f that is linked to the example.txt file in this folder
f = file('example.txt', 'r+')
#This means f is open for reading. The first argument (example.txt.) is the filename and the second parameter is the
#mode, which can be 'r', 'w', or 'r+', among some others. r is for reading online, w is for writing online and r+ is for both. 
#Here we intend to read and write from example.txt

#The most common way to read from a file is simply to loop over the lines of the file:
f = open('example.txt', 'r+')


#Concatanting Strings
#You can add strings together to form a sentence
name = "Tim"
sentence = "My name is " + name

#You cannot add a string and a non string together, you must convert the non string if you want to do this
age = 12
sentence = "And my age is " + str(age)  #Casting int to String

#line stores each line of the text file in a list
for line in f:
	print "The first character of this line is: " + line[0] + "\n"
	print "The entire line is: " + line




f.close() #Always close files when done with them.


#======================= Play around with Python a bit (OPTIONAL TASK 1) ============================
#	Create a new python file in this folder called reader.py
#	There is already a textfile in this document called 'example.txt'. 
#   Write a very short program that creates a new file object called reader that opens the file 'example.txt' in r+ mode (should take 1 line)
#   Now that have you created the file object 'reader' add a line to your code under that that says 'print reader' 
# 	The textfile does not print out, rather you get a text outprint of something in <   >
#   This is because you printed out the OBJECT 'reader'. 'reader' is an object of the Python File class and objects and classes in Python work the same as they do in Java.
#   If you don't understand, don't worry, just understand that to print the contents of the file you have to type 'print reader.readlines()
#   Add 'print reader.readlines()' to your code and run it and you should see the contents of the file printed out!
#   When you see the output of 'print reader.readlines()' you may notice that each line is displayed in a LIST in the outprint (ie it has [   ] around it)
#   This is because Python automatically stores each line of the textfile in a list for you
#   Try adding 'print reader.readlines()[0]' to your code and now check the output. 
#   Do you understand what's happening? reader.readlines() returns a list. We automatically index to the first element in the list by adding [0] after readlines(). Then we print it out!
#   Its the same as working with lists in Task 1. When we had list = ['A','B']  print list[0] outprinted the first item of the lie - 'A'!
#==================================================================================================

#======== Writing to a file =========== #

ofile = open('output.txt', 'w') #We create a new file called output.txt (it doesn't exist yet) in write mode

name = raw_input("Enter your name: ");

ofile.write(name +"\n") #\n is the character to print a new line

#You must run this python file for the file 'output.txt' to be created with the output from this program in it :)

ofile.write("My name is on the line above in this text file.") #We write to the file again and the current contents of the file will not be overwritten! 

ofile.close() #Dont forget to close the file!


#======================= Play around with Python a bit (OPTIONAL TASK 2) ============================
# Let's try write a simple program that uses a while loop to print things to a text file.
# Remember in Task 1 you wrote a program that takes in names while the user hasnt entered 'John'?
# Remember how it stored all 'incorrect' names in a list?
# Let's take all those incorrect names and write them to a new txt file called 'IncorrectName.txt'.
# Copy and paste your code from John.py in Task 1 into this folder into a new python file called JohnWrite.py. Your Task 1 Folder may have been moved to the 'Completed Work' folder.
# At the end of your code, write the single line to create a new textfile in this folder called 'wrotenames.txt'. Don't know how to do this? Look at the section above -> we just told you how which python code creates a new file 'output.txt' in write mode :P
# Now loop through the list of incorrect names using a for loop. ie 'for name in names' if your list was saved in a variable called names.
# for each name, write the name to the text file!
# Remember to close your file afterwards!
#==================================================================================================



#==== Defining functions ====== #
# A function is like a java Method, its a block of defined code that is only run when you call it.
# This is a great way to reuse code and store logic that can be called from anywhere else in the program in just one line. 

def addone(x):
    return x+1

#This function takes in a variable x and adds one to it! We hope that x is an integer...
#Return means what you will get back if you go number = addone(5) , you'll get the int 6 which is 5+1
#We can call the input variable (here x) anything we want. Its just a name we give it so we know how to refer to it within the function (every indented under the def addone(x) line is 'within' the function)

num = 10

numPlusOne = addone(num)

print "10 plus 1 is equal to: " + str(numPlusOne)

#We can call the function multiple times in a loop:

for i in range(10):
    num = addone(num)  #Runs 10 times. 10 + 10 = 20!
	
print num


 
# === Importing outside modules ===
#Python has a huge number of modules that you must import to use. An example of this is the math module which has prebuilt in functions for you to use

import math #Imports the Math module. You do not need to install the Math module, it comes with Python but me specifically imported into a program that uses it.
 
number = 25
print "The square root of 25 is : " + str(math.sqrt(25))   #We are using the sqrt function of the math module

#Math.sqrt returns a FLOAT which is similar to a Java double (an Int only stores round numbers like 1, 2 ,3 , a double (java) or float (python) stores 1.2 , 2.3 ie real numbers)
#We must thus convert the result of math.sqrt(25) to a string before we will be able to print it out, since the print function only works on Strings 

square = math.pow(5,2) #the pow function will take the first argument (5) and put the second argument (2) as an exponent to the number. So we get 5^2 here which is 25.

print "5 squared is equal to: " + str(square)

#======================= Play around with Python a bit (OPTIONAL TASK 3) ============================
# Create a new python file in this folder called squareme.py 
# Inside in, import the math python math module right at the top
# Now define a simple function inside squareme called square, that takes in a variable called 'number'
# How to do this?  remember to define a function you type 'def functionname(nameOfVariableToTakeIn)
# Then indented under that what you want to do with the variable.
# Take the variable and apply the math.pow method to it
# So math.pow(number, 2) should return the squared number right? Print it out!
#==================================================================================================

 
#==== Indexing Strings ====
#Want to get the character of a particular string at a particular position?
 
word = "Hello"
print word[0] #Prints 'H'
print word[0:] #Prints 'Hello'
 
#A string can be indexed EXACTLY like a Python list because a string is basically a list of characters! 
 
print word [1:2] #Useful for string manipulation. Remember you can even index by variables as long as they are ints.
index = 2
print word [1:index] #Prints 'e'
 
 
 # ===== Defining multiline strings ==== 
longString = ''' This is a long string
 using triple quotes preserves everything inside it as a string
 even on diffrent lines and with different /n spacing. '''
 
 
 
 #===== End of example code ====

#'Now you should have all the tools you need to do Task 4. 
		
		
#== Task 4 ==
#Read example.py. Open it using Notepad++. This should help you understand more advanced Python. You are not required to read the entirety of AdditionalReading.pdf , it is purely for extra reference. 

#This example deals with using Python to read and write files and also how to define Python functions which are similar to Java methods.

#Now, create a python file called forgetful.py . Imagine your friend was very forgetful and always seemed to enter his email password incorrectly. You want to write a python program that takes all his incorrect password entries, stores it in a list, then records 
#all his incorrect password entries in a textfile called wrongpasswords.txt. 

#Example: your friends password is 'rusty'. But he enters 'rusty123', 'Rusty', 'rustless' before finally remembering his password is 'rusty' and entering it correctly.

#In this situation wrongpasswords.txt should read this exactly:
#Incorrect password 1: rusty123
#Incorrect password 2: Rusty
#Incorrect password 3: rustless
#Correct password entered on 4th entry.

#The program should ask the user for input by saying 'Please enter your password'. You can use code from the program you wrote in Task 1. The correct password will always be 'rusty' but the user can of course enter any String.
#Good luck!


#****** OPTIONAL CHALLENGE:  ********
#Edit your completed program so that the number of characters your friend gets wrong is also stored for each incorrect password. 

#In the same situation given above, wrongpasswords.txt should read this exactly:
#Incorrect password 1: rusty123 , wrong by 3 characters. 
#Incorrect password 2: Rusty , wrong by 1 characters. 
#Incorrect password 3: rustless , wrong by 4 characters. 
#Correct password entered on 4th entry.

#You should define a seprate function in your code, called countDifference, that takes in a String and returns an int. 
#Bonus points for people who can find and import python modules to help them do this task quicker -> surely someone has written a function for finding the difference between strings already?
#But maybe it's easier to write new logic for this than have to go and find our which module has such a function defined? Who knows!


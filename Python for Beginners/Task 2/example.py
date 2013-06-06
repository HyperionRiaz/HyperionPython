#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
#*************************************

#REMINDER: OPEN THIS FILE IN IDLE

#Congrats for making it to Task 2! You're well on your way to being a programmer.
#Let's explore some more complex programming ideas. If you feel you're struggling to keep up at any point - use your Task 1 code to refresh your knowledge.

#Inside the 'Example programs' folder you'll find example programs to help you understand concepts discussed below.
#Please open these files in IDLE, view the code, and run them to test your understanding.
#We strongly encourage that you complete all the 'Play around with Python' sections below.

#============= Casting ==================
#Sometimes you need to convert from one variable from one type to another. This is called 'casting'
#Remember when we talked about what would happen if you tried to add a String variable and an int variable?

number = 10
stringNumber = str(number) #Now stringNumber stores the string "10"

sentence = "A number divisible by two is " + stringNumber  #We're adding two Strings now so that's fine!

#OR we can cast and add things at the same time

sentenceTwo = "No people under the age of " + str(18)

age = int(raw_input("Enter your age")) #This is how you can convert a String input to an int. The variable age stores an Int. 

#Here we've applied the casting int() function to the output of the raw_input function. raw_input 'returns' a String variable, then we immediatly cast this to an Integer -> can you see this?
#It's like functions from mathematics y = 3(x). Don't worry if you don't know what that is!

#======================= Play around with Python a bit  ============================
#
#	Let's practice some casting.
#	Create a new file called 'cast.py'. Remember the tips from Task 1 to make sure you're not creating cast.py.txt (Turn extensions on in Windows)
#	Now write Python code to take the name of a users favourite restaurant and store it in a variable called favRest
#	Now, below this, write a statement to take in the users favourite restaurant. Use casting to store it in a variable called intFavNumber
#	Now print out both of these using two seperate print statements below what you have written. Be careful!
#	Now, once this is working, try cast favRest to an int. What happens? Add a comment in your code to explain why this is.
#
#==================================================================================================




#=============  Writing if statements ==================
#If statements are 'control structures' that can be used to add logic to your program. 
#They are really important. With if statements, we can check and control what's going on at any point in our program.
#Our programs can product different outputs with different inputs thanks to if statements.


if age >= 18:  #Note the colon! Don't forget it
	print "Youre over 18 and can come in"
else:
	print "Youre to young sorry"
	
#SYNTAX: Make sure you don't forget the : after the if and else command!
#SYNTAX: Indentation - make sure you don't forget this. More about this below.
	
#Your programs run from top to bottom. 
#If you insert the code snippet above into a program and you have defined age = 20 above the if statement, then you will get the output 'Youre over 18 and can come in'.
#If you did not define the variable 'age' above this code, then you will get an error because python runs from the top of the program to the bottom and doesn't know what 'age' means yet! 
#This is known as SEQUENTIAL programming. The program executes in a sequence from top to bottom of your ccode file. We will only work with sequential programs.

#Whatever is indented to the right of the 'if' will execute only if the condition specified (age bigger than or equal to 18) is TRUE
#Python finds out what is stored in the variable int and compares it with 18. It then either gets a TRUE or FALSE answer. If it is FALSE, whatever code is under 'else' will execute.

#Python uses indentation. You must indent code under an if statement to show it is 'within the if statement'
#Defintion of indentation: The placement of text farther to the right to separate it from surrounding text.

#if age > 12:
#	print "Hello"          ** NOTE THE TAB SPACE HERE, THE PRINT STATEMENT IS NOT AGAINST THE MARGIN BUT ONE TAB TO THE RIGHT **

#The tab is really important. your code will not run if you dont indent correctly. Python is all about indentation so if you're confused about this, please let us know!
#To insert the 'tab' space, hit the 'Tab' key on your keyboard. 
#Alternatively, after you type an if statement and hit 'enter' while in IDLE, your cursor will automatically be indented.


#======================= Play around with Python a bit  ============================
#
#	Let's practice an if-else statement and indentation.
#	Let's write a simple (and useful!) program to determine is a number is even or not.
#
#	Create a new file called 'if.py'. Remember the tips from Task 1 to make sure you're not creating cast.py.txt (Turn extensions on in Windows)
#	Now write Python code to take in a number a user enters. Store it in an integer variable called num, and make sure to use casting so that it's an int and not a String.
#	Now, a number is even if when dividing by 2 you get not remainder. For example, 3 divided by 2 is 1 remainder 1. So it is not even.
#	A command that checks a remainder is called MODULUS. In Python, you can do this with a % command. 
#	For example:
#	if num%2 == 0 :
#		<Do something>
#	
#	This means that if the number stored in variable num, modulus 2 has a remainder of 0, do whatever is indented under the if statement.
#	With this knowledge it should be easy to complete this program to output either 'The number you entered is even' or 'The number your entered is odd'.
#	Test your program with different numbers such as 3, 2, 8. Does it work?			
#
#==================================================================================================



#=============  Ways of comparing things ==================

#As a programmer, it's important to not forget the basic logical commands.
#We can check if values or values stored in variables are equal, smaller than one enough, different, etc.
#These work well with if statements to control what goes on in our programs.

num1 = 10
num2 = 20

if num1 >= num2: #The symbol for 'bigger than or equal to' is >=
	print "It's not possible that 10 is bigger than or equal to 20"
elif num1 <= num2: #The symbol for 'less than or equal to' is <=
	print "10 is less than or equal to 20" 
elif num1 != num2: #The symbol for 'not equal to' is !=
	print "This is also true since 10 isnt equal to 20, but the elif statement before comes first and is true so Python will execute that!"
elif num1==num2 : #The symbol for 'equal' is ==
	print "Will never execute this print statement..."
	
#Remember these 4 different ways of comparing variables!
#Additional ways: > can be used for 'bigger than' , < for 'smaller than' 

#'elif' stands for else if
#So the program will check the first part of the if statement (is num 1 bigger than or equal to num 2?) 
#If it is not, then it goes into the first 'elif' and checks if num1 is lessthan or equal to num2
#If it is not then the next...etc

#To have an elif you must have an if above it.
#To have an else you must have an if if. 
#You can't have an else without an if - think about it!
#You can have as many elif under an if, but only one else right at the bottom. It's like the failsafe!

#You can also compare STRINGS as follows:

myName = "Tom"

if myName == "Tom":
	print "Hey tom!"

#======================= Play around with Python a bit  ============================
#
# 	Let's practice comparing things and if statements.
#	As you can see, if-elseif-else statements can be used to VALIDATE things.
#	Remember casting? Remember that you can only cast a STRING to an INT if the String is something like "18". You can't convert "ABC" to an int or you'll get an error.
#	Let's write a program to demonstrate how an if else statement can be used to avoid this problem - ie to VALIDATE user input
#	Create a program called validate.py and save it in this folder.
#	Inside, write code to take in a String from a user. Ask the user for a number. Save it in a String variable called numStr.
#	ASSUME the user only ever enters "3" , "2" or "NO".
# 	We can cast "3" or "2" to an Integer, but not "NO".
#	Write an If, elseif, else statement to only cast numStr to a new variable, called numInt if it is either "3" or "2", else outprint "No can't be cast to an int'.
#	Did it work? Test your code with 3, 2 and No as inputs and comment the results.
# 	Now try other inputs - what happens?
#	
#==================================================================================================
	


#=============  Writing for loops ==================
#Programmers are lazy and sometimes they don't want to have to copy and paste the same statement many times.
#A for loop can specify patterns and repeat code.
#In this for loop below, the condition is that when the variable i (which is an integer) is in the range of 1 to 10 (ie either 1, 2, 3 ,4 ,5 ,6 ... or 10) , the code under
# the for loop will execute. range(1, 10) specifies that i = 1 in the first iteration of the loop. so 1 will be printed by this code. 
#Then the code will run again, this time with i=2, 2 will be printed out...etc until i=11. Now i is not in the range (1,10) so the code will stop executing.
#i is known as the index variable as it can tell you what 'iteration' the loop is on.

for i in range(1, 10):
	print i 

#This for loop prints the numbers 1 to 9. Again, note the indentation and the colon, just like in the if statement.

#You can use an if statement within a for loop!

for i in range (1,10):
	if i > 5:
		print i
		
#This will only print the numbers 6, 7, 8 and 9

#======================= Play around with Python a bit  ============================
#
#	Let's practice writing for loops.
#	Get user input and cast it to an int. Store it in a variable called num.
#	Now, if the number is bigger than 10, use a for loop to outprint it as many times as its value.
#	For example, if a user enters 11, the number 11 will be printed out 11 times.
#	If the user enters 6 or anything less than equal to 10, the program should outprint "Sorry, too small".
#
#	HINT: Use a for loop within an if statement.
#	HINT: You can use variables in range. ie, for i in range (1, num): 		
#
#==================================================================================================

#****************** END OF EXAMPLE CODE FOR TASK 2 ********************* #

#== Make sure you have read and understand all of the example.py file. 
#== Now please complete the compulsory program for this Task as specified in the 'Instructions' pdf file in this folder ===
#== For this compulsory program you are required to create a file called Control.py in this folder and complete a simply program ===
#== Make sure you create Control.py in this folder so that one of our tutors can find it and mark it. ===


#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
#*************************************
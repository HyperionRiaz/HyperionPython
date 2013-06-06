#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
#*************************************

#Welcome to example2.py. You may open this file in EITHER notepad++ or IDLE.
#I recommend that you open it in IDLE so that you can run it (by pressing F5) to view the output of the commands below.


#============= Errors when running Python files ==========

#Now that you've learnt how to run Python file, you should know about errors.
#There are different types of errors, and as a programmer you'll be sure to run into many.
#The process of resolving errors in code is known as 'debugging'.

#Any program you write must be EXACTLY correct. 
#All code is CASE SENSITIVE. This means that Print is not the same as print.
#If you enter an invalid Python command, mispell a command or misplace a puncutation mark - when trying to run your Python program, you will get a SYNTAX error.
#Syntax in programming is the way things are written.
#Errors appear in the Python shell when you try run a program and it fails.
#Be sure to read all errors carefully to discover what the problem is.
#Error reports in the Python shell will even tell you what line of your program had an error.
#Use the line numbers shown on the LEFT in Notepad++ to check that line of your code for an error.

#As a new programming, most of your errors will be Syntax errors. Double check everything you write!
#Be sure to close all quotes ( " ... ") , all brackets ( [ ] )!

#======================= Play around with Python a bit  ============================
#
#	Inside this Task 1 folder, there is a folder called 'Example programs'.
#	Open the file 'errors.py' in IDLE. 
#	Run the file in IDLE. Note the errors, fix them and get the program to run and finally outprint the message.
#
#==================================================================================================


#=============  How to print out things ==================
#If you declare things, you may want the person running your program to be able to see what's going on. This is know as program OUTPUT.
#The most common way to outprint things is to print them. 

number = 10

print number   #We defined number above so '10' will be printed to the output that a user running this program is looking at.

print "Printing a string" #You can also print strings, ints and floats directly without having to put them in a variable first

#A common SYNTAX error you could make above is by forgetting to add a closing " . Remember that all opening quotating marks (") require a closing one!

#=============  How to get input ==================
#Sometimes you want a user to enter something through the keyboard. The following command will show the text "Please Enter your name" in the output box of the program and the program will halt
#until the user enters something with their keyboard and presses ENTER.

name = raw_input("Enter your name") #This is a popup box like JOptionPane.showInputDialog in Java (don't worry if you don't know what that is). The variable 'name' stores what the user entered into the box as a String.

age = raw_input("Enter your age")

#A common SYNTAX error you could make above is by forgetting to add a closing ). Remember that all opening brackets ( , require a matching closing one!

#Learning how to program requires patience but most of all - PRACTICE.
#In the example code of our course, you'll find 'Playing around with Python' sections after key knowledge has been presented to you.
#These sections will help you get practice writing programs - they are all OPTIONAL, and only the final compulsory program of each task is required to move on.
#I highly recommend you complete all these optional tasks - you need all the practice you can get!
#Here's the first one: 


#======================= Play around with Python a bit  =================================
#
#	Now that you know how to output and input, why not write a simple program?
#	Create a file in this folder called 'inputOutput.py'. Make sure that the file type is actually .py. You can check this by opening a folder 
#	in Windows Explorer, going to the top left and clicking 'Organize'
#	Then click 'Folder and Search Options'. Then click the 'View' tab at the top then under the 'Advanced Settings' box, untick 'Hide Extensions for Known file Types'. 
#	Now right click in this folder and go New --> Text document. Call the file inputOutput.py (DELETE the .txt file 'extension'). 
#	The letters after a dot in a filename specifiy the type of file and how Windows deals with it. 
#	'py' after the dot means Windows knows this is a python file. 
#	Now right click your new inputOutput.py file and click 'Edit with Notepad++'
#	In the first line, type: name = raw_input("Enter your name")
#	In the second line, directly under the first line on the margin, type: print name
#   Note that your code must be against the margin of the page otherwise Python gets confused.
#
#	Now press the windows start button. Search for 'IDLE'. Open the program 'Python IDLE (GUI)' . In this program go to the top left, select file -> open. 
#	Navigate to this folder in the file browser and find 'inputOutput.py' and double click on it to open it in IDLE. 
#	Your code should open a nice python GUI (Graphical User Interface). You can press 'F5' and the code will run and your output will display in another window. 
#	Type your name into this window where it has asked 'Enter your name' and then hit enter. 
#	The program will then outprint your name which was automatically stored in the variable name which you specified it should print out
#	Congrats on creating your first persistant Python code! Using the tools you will learn after this, you can write complex, logical and useful programs. :)
#
#	You can now create programs using this method. Use can either code in IDLE or Notepad++. Coding in IDLE is simpler and faster.
#
#	Now, open your code in IDLE again. Reorder the statements you wrote (ie in the first line write print name)
#	Save the file (Ctrl+S), and try run it again (F5). What happens and why? Add some comments to your code to explain why this is.
#
#==================================================================================================

#======================= More on errors =================================
# Make sure you are very careful when spelling things. rawinput("Enter your name") will give you an error
# because the correct Python command is raw_input NOT rawinput or Raw_Input or raw_Input - you have to be precise when programming otherwise Python simply doesn't understand you!
# Also make sure all your code is against the left edge or margin of the IDLE programs page.
# Also make sure you declare variables before trying to use them! You can't say : print name  if you didn't tell Python what name is before that line!


#****************** END OF EXAMPLE CODE FOR TASK 1 ********************* #

#== Make sure you have read and understand all of the example.py and example2.py files in this folder 
#== Now please complete the compulsory program for this Task as specified in the 'Instructions' pdf file in this folder ===
#== For this compulsory program you are required to create a file called HelloWorld.py in this folder and complete a simple program ===
#== Make sure you create HelloWorld.py in this folder so that one of our tutors can find it and mark it. ===


#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
#*************************************

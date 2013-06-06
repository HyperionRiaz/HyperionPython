#This is a comment in python. Comments can be placed anywhere in Python code and the computer ignores them 
#- they are intended to be read by humans. Any line with a # in front of it is a comment.

# *** IF YOU DID NOT INSTALL NOTEPAD++ AND PYTHON (VERSION 2.7.3) ***
# *** PLEASE STOP READING THIS NOW, GO BACK AND OPEN THE WELCOME DOCUMENT, AND FOLLOW THE STEPS TO INSTALL BOTH OF THESE. ***

# Now that you have ensured that you installed Notepad++, PLEASE ENSURE YOU OPEN THIS FILE IN NOTEPAD++ otherwise you will not be able to read it.
# Right click this file --> Edit with Notepad++. Do not use Notepad on any other program to open this file for now.
# Once in Notepad++, click 'View' on the top toolbar and check 'Word Wrap'. 
# Things should be much easier to read now and comments will not go off your screen.

# Please read all the comments in this example file and all others. 

#========= Welcome to the Hyperion Python course ========= 

# Welcome to the Python programming course for people with no background in programming!
# This is the start of a course in programming. If you succesfully complete the few basic tasks, you'll be learning about exciting topics such as Artificial Intelligence.
# Python is one of the easiest languages to learn how to program. Programming takes patience and practice, and we hope to guide you through this with our course.

#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# If you do not have internet access, you can contact our lead tutor - Richard Morrow - on 083 611129 - if you are located in South Africa.
# Feel free to post any comments or feedback on our Facebook wall located at www.facebook.com/hyperiondev
# Visit www.rmoola.com/advice.html and www.hyperiondev.com for more information on getting assistance.
#*************************************


#========= Basic concept of programming ===
# Programmers write statements of code to create 'programs' - runnable files that do something.
# Code can be written in different programming LANGUAGES - Python, Java, C are examples of programming languages.
# This course is a programming course in the Python language. Hyperion has programming courses in other languages such as Java.

# We write commands, or code in the programming language Python and save these commands in a Python file (.py extension in Windows).
# You can then 'run' the Python file to make the code execute and the program execute the programs statements to produce an output or other effect determined by the statements.
# Information about how to 'run' Python files are given at the bottom of this file.
# But first lets get started on how to write some basic code in Python, and perform some basic operations.

#========= Reading Python code ===

#You're actually reading an example Python program right now.
#Comments in Python appear in GREEN if you have the file opened in notepad++. Keywords of the Python language appear in BLUE. 
#Python is VERY similar to Java and most programming languages have the same structure so if you learn one - you an learn more easily! It's not like learning human languages.
#Almost all programming languages share common SYNTAX, or the way the statements are written.

#========= Variables ===========
#A variable is a placeholder. 
#We use variables to store data in a program.

num = 2  #Assign the number 2 to the variable 'num'
num = 3  #Now 3 overwrites the 2 that was initially stored in num

#When coding Python, you can use call variables anything you want, but try using descriptive variable names.
myName = "Tom"      # A good variable name
variableOne = "Tom" #Not a good variable name, doesnt give a description of what would be stored inside it

#======================= Play around with Python a bit  ============================
#
#	At this point, why not play around with creating variables? Press the windows Start button, in the 'Search for programs and files' box, 
#	type 'Python (command line)' and you should see a program named exactly that pop up.
#	If this does not happen, your Python isn't installed on your system yet. Please download and install Python 2.7 
#	In the black box that appeared, type: name = "John"  
#	then press enter. Nothing happens but this Python program has remembered what you set the variable 'name' to.
#	To prove this type: print name 
#	and then hit enter. 'John' should be printed out by the program. 
#	If you close this black box, and open a new one and type: print name , you will get an error. This is because this is the Python 'Shell' and your variables aren't saved. 
#	We write python in text editors like Notepad++ or the IDLE Python GUI so that all our variable definitions and code are saved. We can then run these files as python programs. 
#	Keep the black box open and try out some commands as you read through this file. Try to add some numbers and variables as shown below.
#	 -> you are actually writing Python already, it's that simple!
#
#==================================================================================================




#========= Data types ===========

#You get different TYPES of variables : Strings, Ints and Floats . These different types are known as DATATYPES.
#Ints store integers (ie whole numbers). 
#String store text and you always use " " to denote Strings. do not use ' ' . Strings can have spaces in them. 
#Floats store real numbers (ie numbers with decimal points) so numbers such as 1.234 

aStringVariable = "ABC"
anIntVariable = 2

#You do not have to define variable types explicitly in Python like you do in Java
text = "Welcome"  #Python automatically knows the variable text is a String variable because you have "" around Welcome
number = 10 #Python knows number is an Int
numberStr = "10" #Watch out! Since you defined 10 within quotation marks, Python knows this is a String. It's not an integer even though we understand 10 is a number

#When writing programs, you'll have to decide what data types or variables you will need to do what you want your program to do.
#In most cases, it will be pretty obvious - want to store someones name? Use a String. Their age? Use an integer. 

#========= Arithmetic Operations ===========

#Additional and subtraction
one = 1
two = 2

answerAdd = one + two #the variable answerAdd now stores the integer 3
answerSubtract = two - one #The variable answerSubtract now stores the integer 1

#Multiplcation and division

answerDivide = one/two
answerMultiply = one*two
#Note the division and multiplication operations that are used in programming: / is used for divide and * for multiply

#Can you see how these statements could be used to create a calculator or even a simple program to do some kind of mathematics?

#========= Operations on different Data Types ===========

#Be careful! You can only perform certain arithmetic operations on variables of the same data type.
#EG: You can add two variables if they are both integers and the result will also be an interger as expected.
#If you add string objects they will be CONCATENATED. You cannot subtract, multiply or divide String variables - that's only for Ints or Floats. 

firstName = "Phil"
lastName =" Jones"

fullName = firstName + lastName #the variable fullName now stores the string "Phil Jones" , we have concatenated the two strings

#You can add as many strings or ints as you want in a statement, as long as they are all of the same datatype.

sentence = "Hello my name is : " + fullName         #We added the String "Hello my name is: " (which isnt stored in a variable) to the contents of the String variable fullName. 

#We'll discuss how to add variables of different datatypes later.


#=========== Running Python files =====================

#Now that you know how to write code, it's time to learn how to execute your code to see what the output is.
#Remember you're actually reading a Python file now. All the Python commands are the statements not seen in GREEN.
#Let's 'RUN' this Python file and take a look at what output it produces (if any).
#When you write Python code, you'll have to run it often to test that your programs are doing what you'd like them to do.

#There are three different ways to 'run' Python files.

# ======== OPTION 1: Run from IDLE Python GUI -- THE EASY WAY ========
#The easiest way to run Python files and this program is through a GUI (Graphical User Interface). 
#Please follow these steps to run this program:

#Simply go to  Windows Start and enter 'IDLE' into your windows search. Open the program 'IDLE (Python GUI)'
#If you can't find the IDLE program on your computer - you didn't install Python correct. Contact us for assistance.
#Go to the top left corner of this program and click --> File -- Open--> navigate to your Dropbox folder and open example.py.

#Now your code will open in the Python GUI IDLE. Press F5 on your keyboard to RUN the Python and the output will appear in a seperate python output (Python Shell) window!
#You can use this method to run ANY python file (file with a .py extension). 
#If there is an error in your code, the code won't run and the error will be printed out in the Python Shell windows.
#Another way to run Python files is to simply right click on this file (example.py) and select 'Open in IDLE'. You may or may not see this option.

#Errors are things like trying to add two variables that aren't the same data type, or using a variable that isn't declared! 
#(ie if you say num = num1+num2 and you haven't said what num1 and num2 above this statement!)
#We'll talk about errors more later.

#Let's put a line just below this comment that will print out the words 'Yay! You ran your first Python program!' when the file example1.py is run using IDLE.

print "Yay! You ran your first Python program!"

#Now when you follow the instructions above and open example1.py in the IDLE program and hit F5. 
#You should see "Yay! You ran your first Python program!" printed out in the Python Shell window!
#Whatever appears in the Shell window after running a program is known as the OUTPUT of a program.
#All the code above that aren't comments also ran, but just storing and declaring variables doesn't produce any output. 
#The Python Shell only shows the output of the program.

#I advise that you complete all tasks and open all example files in IDLE from now on.
#Perhaps create a shortcut to IDLE on your Desktop so that you can access it faster.
#Notepad++ can only be used to view the text of a code - you can't run the program from within Notepad++ unfortunately.


#======================= Play around with Python a bit  ============================
#
#	Now that you know how to run Python files, it is helpful to look at some example Python code.
#	Inside this Task 1 folder, there is a folder called 'Example programs'.
#	There are several example programs inside this folder.
#	Open each file using IDLE in the method explained above.
#	Take a look at the code to get a better idea of some of the concepts discussed above.
#	Run each file to see the output of each program.
#
#==================================================================================================







#The other two options are OPTIONAL. As long as you know how to use IDLE, you can complete our entire course.

# =========== Option 2: Use any GUI/IDE that you want.  -- ADVANCED ===========
#An IDE is a program like the IDLE Python GUI.
#You get many programs that let you run code within them.
#Some of these IDEs are more complicated than others.
#See http://wiki.python.org/moin/PythonEditors for a huge list of your options of different IDE's that you can run Python files from.

#=========== OPTION 3: Run from the windows command line (cmd)  -- THE HARD WAY =========== 
#Once you have set up Python to work from your command line, open cmd (Start --> run -- cmd), then navigate to this directory using the commands: 
#cd Dropbox
#cd <this folder name -> should be your firstname and first initial of surname eg RiazM) 
#python example.py
#This program should now run from your command line. If this does not work, Python is not set up correctly on your command line.
#You can email students@hyperiondev.com for help if you'd like to get this specific thing set up - though it is not required.

#==========================================================

#Play around with this program in IDLE. Try change statements and delete things, run the code and see what happens.
#Additional example of basic python can be found in AdditionalReading.pdf but you are not required to read the entire thing.

#*** NOW PLEASE ONLY CONTINUE TO READ THE example2.py FILE (OPEN IT IN IDLE), IF YOU MANAGED TO RUN THIS FILE SUCCESFULLY AND SAW THE OUTPUT USING IDLE ******
#*** If you were unable to run this file, you must let us know so that we can resolve your issues. ***





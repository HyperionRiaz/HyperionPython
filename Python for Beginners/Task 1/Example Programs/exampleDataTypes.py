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


#Let's look at some examples.
#I want to multiply three numbers together:

num1 = 2
num2 = 10
num3 = 20

result = num1*num2*num3

#Now I want to make a message to display the result.
#The message will have to be stored in a String variable, since it will contain text:

message = "The result of multiplying 2, 10 and 20 is " + str(result)

#The variable message now stores a String which contains the message.
#We use the function str(result) to convert the VALUE of result (which is an integer) to a String
#This is known as casting. We cast result to a String.

#Take a look at what message contains:

print message

#Run this program. Do you understand the output?
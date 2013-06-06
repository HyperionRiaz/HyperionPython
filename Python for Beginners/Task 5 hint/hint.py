counter = 0
myString = raw_input ("Enter String")


for item in range (0,len(myString)/3):
    print myString[counter:counter + 3]
    counter = counter + 3

    
    
#How to get the 'condons' (groups of 3) of any inputted String! 
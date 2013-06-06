#Welcome to Machine Learning in Python!
#We can now start talking about interesting topics now that you know basic python.

#********* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
#*************************************

#===== Python implementation of k-means =====

#We first import libraries for generating random numbers, and for reading comma separated value (".csv") files
from random import random,normalvariate,sample
import csv

#===== Reading the data =====
#We then read in data.csv. data.csv has 3 columns, and a header describing what each column is.
filename = raw_input("Enter a file name: ")
print "\nReading the data..."
with open(filename, 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #We don't want to include the header as a data row, so we pop it off the iterator
    header = datareader.next()
    #When we print the header, we see that it is read in as a list
    print header
    #Each data point will be a list with two elements (eg. [1.1, 2.3]).
    #We need to store our data as a list of lists (eg: [[1.1, 2.3],[1.8, 2.6],[0.9, 2.5]] is a list with three data points)
    #This line turns the iterator "datareader" into a list of data points, where [[float(elem[1]),float(elem[2])] ignores the
    #first column (which would have been elem[0]), only keeping the numeric data. "float()" converts the data from string type
    #to a "floating point number" which allows a decimal place, or just a "float" for short.
    data = [[float(elem[1]),float(elem[2])] for elem in datareader]
print "...Done"
    
#We can print the data to check that the form is correct
print "\nPrinting the data:"
print data

#===== Defining a distance function =====
#We need to define a distance function, that returns the distance between any two points
def distance(p1,p2):
        "Computes the distance between two points"
        return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

#data = [[random()+0.5,random()-0.5]  for i in range(500)]+[[random()-0.5,random()-0.5]  for i in range(1000)]+[[random()+0.5,random()+0.5]  for i in range(1000)]
#data = [[normalvariate(0,1)+2,normalvariate(0,1)-2]  for i in range(500)]+[[normalvariate(0,1)-2,normalvariate(0,1)-2]  for i in range(1000)]+[[normalvariate(0,1)+2,normalvariate(0,1)+2]  for i in range(1000)]


#===== Initialization =====
#We must decide how many clusters we will attempt to find
numMeans = int(raw_input("\nEnter the desired number of clusters: "))
#We initialize the means to be randomly selected points from our data. The list of means has the same
#"list of lists" structure as the list of data points, but it is much shorter
means = sample(data,numMeans)

#===== The algorithm =====
#K-Means is an algorithm that converges upon a solution with many iterations.
#Here we pick the number of iterations
iters = int(raw_input("\nEnter the number of cluster estimating iterations: "))
print "\nWatch the error get smaller:"
#The main algorithm loops starts here
for run in range(iters):
    #We need to build up new means each iteration, which we initialize to [0,0] here
    newMeans = [[0,0] for i in range(numMeans)]
    #We need to keep track of the number of points we allocate to each cluster, to use as a denominator to compute the means
    #We init these counters here
    meanCounters = [0 for i in range(numMeans)]
    #We also keep track of the total error (the sum of the minimum distances between the centres and each data point), initialized here
    totError = 0
    #For each data point
    for x in data:
        #===== Finding which cluster each point belongs to =====
        #We first need to find the cluster mean closest to each point
        closest_k = 0
        smallest_dis = 999999999
        #We iterate through each cluster mean...
        for k in enumerate(means):
            dis = distance(x,k[1])**2
            #...and keep track of which one is closest to the current data point
            if dis < smallest_dis:
                closest_k = k[0]
                smallest_dis = dis
        #Increment the total error
        totError = totError + smallest_dis
        #===== Updating the means  =====
        #We then update the new means by accumulating the sums of all the data points that "belong" to that center
        newMeans[closest_k][0] = newMeans[closest_k][0]+x[0]
        newMeans[closest_k][1] = newMeans[closest_k][1]+x[1]
        meanCounters[closest_k]=meanCounters[closest_k]+1
    #Then for each cluster mean, we divide by the number of points to go from a total to a mean
    for k in enumerate(newMeans):
        means[k[0]][0]=(k[1][0]/meanCounters[k[0]])
        means[k[0]][1]=(k[1][1]/meanCounters[k[0]])
    #We print the error each iteration to monitor the convergence
    print (totError)/len(data)

discard = raw_input("\nI hope you're happy with the convergence! Use more iterations next time if it hasn't converged. Press \"Enter\" to view the cluster details.")
#==== Interpreting the output ====
#Read in the csv file again, but this time take the country names instead of the numeric data
with open(filename, 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
    header = datareader.next()
    countrylist = [elem[0] for elem in datareader]

#Init a list of empty lists (one for each cluster), that we will populate with country names
countryLists = []
for k in range(len(means)):
    countryLists.append([])

#Loop through each data point, and assign the corresponding country name to that list
for x in range(len(countrylist)):
    #We first need to find the cluster mean closest to each point
    closest_k = 0
    smallest_dis = 999999
    #We iterate through each cluster mean...
    for k in enumerate(means):
        dis = distance(data[x],k[1])
        #...and keep track of which one is closest to the current data point
        if dis < smallest_dis:
            closest_k = k[0]
            smallest_dis = dis
    countryLists[closest_k].append(countrylist[x])
    
#Print out the cluster details, along with the country names
for k in range(len(means)):
    print "\nPrinting countries in cluster " + str(k+1) +":"
    print "Life expectancy: " + str(means[k][1])
    print "Birth rates (per 1000): " + str(means[k][0])
    print "Number of countries: " + str(meanCounters[k])
    print countryLists[k]
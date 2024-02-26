#
#
# @author John Michael Lott

import re

def testDrive(dist, fill, mpg):
    for i in range(len(dist)):              #Loop through to test each city for route
        tank = mpg * fill[i]                #Fill tank at start city
        tank -= dist[i]                     #travel to next city

        for j in range(len(dist)):          #Travel to following cities filling at each city
            if tank >=0:                    #if tank positive or 0 trip was successful
                curr = (i+1+j) % len(dist)  #increment current city index
                if curr == i:               #if successful loop back return index of start city
                    return curr             
                tank += (mpg * fill[curr])  #Fill tank at start city
                tank -= dist[curr]          #travel to next city
            else:                           #if no rounte found test next city
                break                 
    return -1                               #no route found, invalid set

userDist = input("Please enter a set of city distances (Ex [1,2,3,...]): ")
userFill = input("Please enter a set of gallon amounts for each of those cities: ")
userMPG = int(input("Please enter the car's mpg: "))

setDist = re.findall('\d+', userDist)  #extracts digits from user input
setDist = [int(i) for i in setDist]
setFill = re.findall('\d+', userFill)
setFill = [int(i) for i in setFill]

prefCity = testDrive(setDist, setFill, userMPG)     #run user input through algorithm

if prefCity == -1:
    print("Invalid set, no round trip possible.")
else:
    print("Preffered city is: ",prefCity)           #Display prefered city if exits
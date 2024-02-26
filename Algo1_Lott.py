#
#
# @author John Michael Lott

import re

def couplePairing(tSet):
    sLen = len(tSet)
    count = 0
    for i in range(0, sLen - 1, 2):
        nextVal = tSet[i] + (1 - (2 * (tSet[i] % 2)))      #stores the current values pair
        if tSet[i+1] != nextVal:        #if not paired search for pair
            if i == (sLen - 2):         #exit if indexed at last pair
                return -1
            for j in range(i+2, sLen):  #loop through remaining set for pair
                if nextVal == tSet[j]:  #if pair found do swap
                    swap = tSet[i+1]
                    tSet[i+1] = tSet[j]
                    tSet[j] = swap
                    count += 1          #increment swap count
                    break
                elif j == (sLen - 1):
                    return -1           #if pair not found exit, invalid set

    return count                        #return number of swaps



userInput = input("Please enter a set of numbers(Ex [1,2,3,...]): ")

userSet = re.findall('\d+', userInput)  #extracts digits from user input

userSet = [int(i) for i in userSet]

swapCount = couplePairing(userSet)      #run input through algorighm

if swapCount == -1:
    print("Pair(s) are missing from the set.")
else:
    print("Swap count: ",swapCount)     #Display swap count if found
#
#
# @author John Michael Lott

import re

def couplePairing(tSet):
    sLen = len(tSet)
    count = 0
    for i in range(0, sLen - 1, 2):
        nextVal = tSet[i] + (1 - (2 * (tSet[i] % 2)))      #stores the current values pair
        if tSet[i+1] != nextVal:
            if i == (sLen - 2):
                return -1
            for j in range(i+2, sLen):
                if nextVal == tSet[j]:
                    swap = tSet[i+1]
                    tSet[i+1] = tSet[j]
                    tSet[j] = swap
                    count += 1
                    break
                elif j == (sLen - 1):
                    return -1

    return count



userInput = input("Please enter a set of numbers(Ex [1,2,3,...]): ")

userSet = re.findall('\d+', userInput)  #extracts digits from user input

userSet = [int(i) for i in userSet]

swapCount = couplePairing(userSet)

if swapCount == -1:
    print("Pair(s) are missing from the set.")
else:
    print("Swap count: ",swapCount)
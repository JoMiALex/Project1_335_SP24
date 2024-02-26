# Project 1

> Name - John Michael Lott
>
> Email - jlott1004@csu.fullerton.edu
>
> Assignment - Project 1
>
> Github Link - https://github.com/JoMiALex/Project1_335_SP24

\* Contains Algorithm 1's & 2's:
    Pseudocode, Mathematical Analysis, How It Works
\*

## Algorithm 1
### Pseudocode

    PairCheckFunction(test set)
        count
        loop through even positions
            check and store needed value checking if above or below based on odd or even value

            


###  Complexity and Efficiency Class
    Proof by Step Count:
    T(n) = 2 + n/2 * (3 + (n-2)5)
         = 2 + n/2 * (5n - 7)
         = 2 + (5n^2-7)/2
         = (5n^2)/2 - 1/2
        Therefore, T(n) exists in O(n^2).
    

### How it Works
To run this algorithm type `py Algo1.py`




## Algorithm 2
### Pseudocode

    CityRunFunction(distanceSet, gasSet)
        Loop using each city as start
            Add range using gallons avalible times mpg
            Subtract distand to next city
            if range greater than 0
                Loop through the rest of the cities
                    Add range using gas available
                    Subtract distance
                    if negative exit loop

  
###  Complexity and Efficiency Class
    Proof by Step Count:
    T(n) = 
    
    Proof by Induction:
    1. 

    2. 

    3. 

    4. 

    5. Conclude
    Therefore, T(n) exists in O(n^2).

### How it Works
To run this algorithm type `py Algo2.py`
Will use the example provided in the Project 1 document. (Should return 4)

Next

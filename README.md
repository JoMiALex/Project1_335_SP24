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
            check for needed value in following indexes
            Once value found perform swap
            Otherwise exit with error
        return swap count upon successful pairing

            


###  Complexity and Efficiency Class
    Proof by Step Count:
    T(n) = 2 + n/2 * (3 + (n-2)5)
         = 2 + n/2 * (5n - 7)
         = 2 + (5n^2-7)/2
         = (5n^2)/2 - 1/2
        Therefore, T(n) exists in O(n^2).
    

### How it Works
To run this algorithm type `py Algo1_Lott.py`

Enter any even set of n numbers entirely containing corresponding pairs and the algorithm will return swaps needed to put together pairs.


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
    T(n) = n * (2 + n * 4)
         = n * (2 + 4n)
         = 4n^2 + 2n
         Therefore, T(n) exists in O(n^2).


### How it Works
To run this algorithm type `py Algo2_Lott.py`

Enter any corresponding set of values with an mpg. Algorithm will return the preferred city if one exists.

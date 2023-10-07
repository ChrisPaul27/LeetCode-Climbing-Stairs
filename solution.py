import math
class Solution(object):
    def climbStairs(self, n):
        out = 1
        j = 1
        i = n - 1
        while i >= j:
            out = out + math.factorial(i) / (math.factorial(i-j) * math.factorial(j))
            j = j + 1
            i = i - 1
        return out
#The first combination is given by a sum of all 1 (the number of 1 is equal to n)
#In the second step, I can start to use 2 as a step, so in this case I get n by a sum of n - 1 terms. So I have to calculate the possible displacements of 2 within n - 1 position (that is the binomial coefficient of n-1 over 1).
#In the third step, I can use two 2 as steps, this means that I will obtain n through a sum of n - 2 terms. So I have to calculate the possible shifts of 2 (this time two 2) inside n - 2 position (that is the binomial coefficient of n-2 over 2).
#The process continues as above, until i is above or equal to j (the number of 2 that I can use in order to get n).

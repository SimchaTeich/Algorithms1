#-------------------------------#
# Taken from lecture 1 slide 21 #
#-------------------------------#

from random import randint
from random import shuffle


def select(A, t):
    """
:   func finds recursivly the
:   t^th value of A if A was ordered
:
:   complex Good: pivot in the middle
:   every iteration: T(n) = {T(n/2) + O(n)}
:   ==> O(n)
:
:   complex Bad: pivot in the corner
:   every iteration: T(n) = {T(n-1) + O(n)}
:   ==> O(n^2)
:
:   param A: unsorted array
:   type A: array of integers
:   param t: index to find if A was ordered
:   type t: integer (start from 0)
    """
    # get a randomal pivot k
    k = A[randint(0, len(A) - 1)]
    
    S1 = [x for x in A if x < k]
    S2 = [x for x in A if x > k]
    
    if len(S1) == t:
        return k
    
    elif len(S1) > t:
        return select(S1, t)
    
    else:
        return select(S2, t - len(S1) - 1)


def main():
    # create an array
    arr = [i for i in range(1,100+1)]
    
    # shuffle it
    shuffle(arr)
    
    print(arr)

    # find the median.
    m = select(arr, len(arr)//2)
    print("Median is: " + str(m))


if __name__ == "__main__":
    main()    
    
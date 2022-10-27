#-----------------------------------#
# Taken from lecture 1 slides 22-23 #
#-----------------------------------#

from random import randint
from random import shuffle


def choose_good_pivot(A):
    """
:   exactly the same as function in slide 23.
:   the goal is to find the median by
:   median of medians.
    """
    # divide A into groups of size 5
    groups = [A[i:i + 5] for i in range(0, len(A), 5)]
    
    # sort each group
    for group in groups:
        group.sort()
    
    # be is the medians of the groups
    B = [g[len(g)//2] for g in groups]
    
    # return the median of medians
    return select(B, len(B)//2)


def select(A, t):
    """
:   func finds recursivly the
:   t^th value of A if A was ordered
:
:   complex: T(n) = {
:                      n < 50: c'*n
:                      n >= 50: c*n + T(n/5) + T((7/10)*n)
:                  }
:           ==> O(n)
:
:   param A: unsorted array
:   type A: array of integers
:   param t: index to find if A was ordered
:   type t: integer (start from 0)
    """
    if len(A) < 50:
        A.sort()
        return A[t]
    
    k = choose_good_pivot(A)
    
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
    arr = [i for i in range(1, 100+1)]
    
    # shuffle it
    shuffle(arr)
    
    print(arr)

    # find the median.
    m = select(arr, len(arr)//2)
    print("Median is: " + str(m))


if __name__ == "__main__":
    main()    
    
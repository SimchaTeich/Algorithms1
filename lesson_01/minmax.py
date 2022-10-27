from random import shuffle


def minMax(A, i, j):
    """
:   function finds recursivly the minimum
:   and the maximum of an array.
:
:   complex: T(n) = {
:                       n = 2: 1
:                       n > 2: 2T(n / 2) + 2
:                   }
:            ==> O(n)
:
:   param A: unsorted array
:   type A: numeric array
:   param i: index for start
:   type i: int
:   param j: index to end
:   type j: int
    """
    if j == i:
        return (A[i], A[i])
    
    if j == i + 1:
        if A[i] < A[j]:
            return (A[i], A[j])
        else:
            return (A[j], A[i])
        
    else:
        k = (i + j) // 2
        m1, M1 = minMax(A, i, k)
        m2, M2 = minMax(A, k + 1, j)
        return (min(m1, m2), max(M1, M2))


def main():

    # create an array
    arr = [i for i in range(1,100+1)]
    
    # shuffle it
    shuffle(arr)
    
    print(arr)
    
    # find minimum and maximum.
    m, M = minMax(arr, 0, len(arr) - 1)
    print("Min is: " + str(m))
    print("Max is: " + str(M))
    

if __name__ == "__main__":
    main()

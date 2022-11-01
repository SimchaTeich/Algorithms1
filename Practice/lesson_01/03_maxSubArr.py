#------------------------------------#
# Taken from practice 1 slides 15-16 #
#------------------------------------#


def maxCrossingSum(A, mid):
    """
:   finds the max sum from one from the
:   next sums: right of arr, left and middle.
:   
:   complex: O(n)
:
:   param A: array to check
:   type A: numeric array
:   param mid: index of the middle of A
:   type mid: int 
    """
    # create middle value if lenght is even.
    if len(A) % 2 == 0:
        A = A[:mid] + [0] + A[mid:]
        
    # calc the left side
    left_sum = min(A) - 1
    s = A[mid]
    for i in range(mid - 1, -1, -1):
        s += A[i]
        left_sum = max(s, left_sum)
        
    # calc the right side
    right_sum = min(A) - 1
    s = A[mid]
    for i in range(mid + 1, len(A)):
        s += A[i]
        right_sum = max(s, right_sum)
    
    # return the maximum of: left, right and middle.
    # the part of "-A[mid]" came from inclusion and rejection.
    return max(left_sum, right_sum, left_sum + right_sum - A[mid])


def maxSubArr(A):
    """
:   calc the max sum of sub array, recursivly.
:
:   complex: T(n) = {
:                       n = 1: 1
:                       n > 1: 2T(n/2) + c*n
:                   }
:                 ==> O(n*log(n))
:
:   param A: the array to find its max sum of sub array.
:   type A: numberic array.
    """

    if len(A) == 1:
        return A[0]
        
    mid = len(A) // 2
    
    # for left
    max_l = maxSubArr(A[:mid])
    
    # for right
    max_r = maxSubArr(A[mid:])
    
    # for middle
    max_m = maxCrossingSum(A, mid)
    
    return max(max_l, max_m, max_r)
    
    
def main():
    # array taken from slide 12 (answer: 43)
    arr1 = [13, -3, -25, 20, -3, -16, -23, 18,
           20, -7, 12, -5, -22, 15, -4, 7]
    
    # array taken from slide 14 (answer: 7)
    arr2 = [-2, -5, 6, -2, -3, 1, 5, -6]
    
    print("Arr 1 is: " + str(arr1))
    print("Max Sub Arr 1 is: " + str(maxSubArr(arr1)))
    print()
    print("Arr 2 is: " + str(arr2))
    print("Max Sub Arr 2 is: " + str(maxSubArr(arr2)))


if __name__ == "__main__":
    main()

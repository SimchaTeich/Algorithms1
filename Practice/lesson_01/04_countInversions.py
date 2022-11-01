#------------------------------------#
# Taken from practice 1 slides 18-25 #
#------------------------------------#


def countInMerge(A, l, m, r):
    """
:   merge same as merge-sort, but
:   with counting of inversions.
:   full explanetion appear in slide 22.
:   
:   complex: O(n)
:
:   param A: the full array
:   type A: numeric arr
:   param l: index for start part to check from left.
:   type l: int
:   param m: index of middle in the sub part of A to check.
:   type m: int
:   param r: index for end part to check from right.
:   type r: int
    """
    A1 = A[l:m+1]
    A2 = A[m+1:r+1]
    B = []
    count = 0
    i = 0
    j = 0
    
    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            B.append(A1[i])
            i += 1
        else:
            B.append(A2[j])
            j += 1
            
            # count pairs like <x,A2[j]>
            # when x is all values in A1[i:]
            count += (len(A1) - i)
    
    # append values that was left in A1    
    if i < len(A1):
        B += A1[i:]
    
    # append values that was left in A2
    if j < len(A2):
        B += A2[j:]
        
    # move all values from B back to A (because A stay the same address)
    for i in range(len(B)):
        A[l+i] = B[i]
    
    return count



def countInversion(A, l, r):
    """
:   calcs recursivly the number of inversions pairs in array.
:   full explanetion about who it works you can find in slide
:   18 - 25. read it and back to this function if you want :)
:
:   complex: T(n) = {
:                       n = 1: 1
:                       n > 1: 2T(n/2) + c*n
:                   }
:                 ==> O(n*log(n))
:
:   param A: array to sort and count inversions inside
:   type A: numeric array
:   param l: index of left side to work from it.
:   type l: int
:   param r: index of right side to work until it.
:   type r: int
    """
    count = 0
    c1 = 0
    c2 = 0
    c3 = 0
    
    if l < r:
        m = (l + r) // 2
        
        c1 = countInversion(A, l, m)
        
        c2 = countInversion(A, m + 1, r)
        
        c3 = countInMerge(A, l, m, r)
      
    return c1 + c2 + c3
    
    
def main():
    # array taken from slide 18 (answer: 3)
    arr1 = [2, 4, 1, 3, 5]
    print("arr1 before merge-sort: " + str(arr1))
    count1 = countInversion(arr1, 0, len(arr1) - 1)
    print("arr1 after merge-sort: " + str(arr1))
    print("number of inversions in arr1: " + str(count1))
    
    print()
    
    # array taken from slide 24 (answer: 11)
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    print("arr2 before merge-sort: " + str(arr2))
    count2 = countInversion(arr2, 0, len(arr2) - 1)
    print("arr2 after merge-sort: " + str(arr2))
    print("number of inversions in arr2: " + str(count2))


if __name__ == "__main__":
    main()

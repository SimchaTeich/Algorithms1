#------------------------------#
# Taken from lecture 4 slide 3 #
#------------------------------#


def regular_binomal(n, k):
    """
:   calcs the binomal number (n choose k)
:   according to the recursive identity:
:   (n choose k) == (n-1 choose k) + (n-1 choose k-1)
:
:   time complex: T(n, k) = T(n-1, k) + T(n-1,k-1)
:                         ==> (n choose k)
:                         and the biggest is (n choose n/2)
:                         ==> so it's aproximatly O((2^n)/sqrt(n))
:
:   param n: size of group to choose from it
:   type n: int
:   param k: who many member to choose from the group.
:   type k: int
    """
    if k == 0 or n == k:
        return 1
    
    if n < k:
        return 0
        
    return regular_binomal(n-1, k) + regular_binomal(n-1, k-1)


def dynamic_binomal(n, k):
    """
:   calcs the binomal number (n choose k)
:   by the dynamic programming way.
:
:   time complex: O(n^2)
:
:   param n: size of group to choose from it
:   type n: int
:   param k: who many member to choose from the group.
:   type k: int
    """
    # build matrix nXn
    values = [['.' for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(0,n+1):
        for j in range(0, i+1):
            if j == 0 or j == i:
                values[i][j] = 1
            
            else:
                values[i][j] = values[i-1][j-1] + values[i-1][j]
            
            if i == n and j == k:
                return values[i][j]
    

def main():
    print("calc with dynamic programing (30 choose 20) == ")
    print(dynamic_binomal(30, 20))
    
    
    print("calc with regular recursive (30 choose 20) == ")
    print(regular_binomal(30, 20))
    
    
    
if __name__ == "__main__":
    main()
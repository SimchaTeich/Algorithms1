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


def main():
    print(f"(5 choose 3) == ")
    print(regular_binomal(5, 3))
    
if __name__ == "__main__":
    main()
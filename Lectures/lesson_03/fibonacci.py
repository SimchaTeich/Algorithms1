#------------------------------#
# Taken from lecture 4 slide 2 #
#------------------------------#


def regular_fibonacci(n):
    """
:   the regular way to calc fibonacci
:   value for index n.
:
:   time complex: O(fi^n)
:
:   param n: index of fibonacci number to find its value.
:   type n: int
    """
    if n == 0 or n == 1:
        return n
        
    return regular_fibonacci(n-1) + regular_fibonacci(n-2)


def dynamic_fibonacci(n):
    """
:   finds the fibonacci value for index n
:   with dynamic programming.
:
:   time complex: O(n)
:
:   param n: index of fibonacci number to find its value.
:   type n: int
    """
    if n == 0 or n == 1:
        return n
    
    values = [0, 1]
    for i in range(n-1):
        values.append(values[-2] + values[-1])
    
    return values[-1]


def main():
    n = 0
    while True:
        print(f"the {n}'th fibonacci number by dynamic programming:")
        print(dynamic_fibonacci(n))
        print(f"the {n}'th fibonacci number by the regular way:")
        print(regular_fibonacci(n))
        print("----------")
        n += 1
 
if __name__ == "__main__":
    main()
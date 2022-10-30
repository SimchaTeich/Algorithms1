#-------------------------------#
# Taken from practice 1 slide 7 #
#-------------------------------#


def hanoi(diskettes_number, src, dst, helper):
    """
:   hanoi tower is famous quaestion in CS.
:   search this at google...
:   
:   complex: T(n) = {
:                       n = 1: 1
:                       n > 1: 2T(n-1) + 1
:                   }
:                 ==> O(2^n)
:
:   param diskettes_number: number of diskettes on src rod
:   type diskettes_number: int
:   param src: the name of src rod
:   type src: str
:   param dst: the name of dst rod
:   type dst: str
:   param helper: the name of the helper rod
:   type helper: str
    """
    if diskettes_number == 1:
        print(f"top diskette from {src} to {dst}")
    
    else:
        hanoi(diskettes_number - 1, src, helper, dst)
        print(f"top diskette from {src} to {dst}")
        hanoi(diskettes_number - 1, helper, dst, src)
    



def main():
    
    print("Hanoi Towers: A - is src, B - is dst, C- is helper")
    num = input("Enter number of diskettes to move from A to B: ")
    
    if not num.isnumeric():
        print("Sorry, try again to enter NUMBER at the next time.")
        print("Bye.")
        
    else:
        hanoi(int(num), "A", "B", "C")
    
    
    print("done.")
    
    
if __name__ == "__main__":
    main()
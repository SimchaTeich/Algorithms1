#----------------------#
# Taken from lecture 7 #
#----------------------#


LEFT = "LEFT"
SAME_LINE = "SAME_LINE"
RIGHT = "RIGHT"


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    def __str__(self):
        return f"({self._x}, {self._y})"
    
    def get_x(self):
        return self._x
        
    def get_y(self):
        return self._y


def determinant_2x2(matrix):
    """
:   calc determinant.
:   param matrix: square matrix 2x2
:   param type: list of list type double.
:   return: determinant.
:   rtype: double.
    """
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]


def determinant_3x3(matrix):
    return matrix[0][0] * determinant_2x2([matrix[1][1:], matrix[2][1:]]) -\
           matrix[0][1] * determinant_2x2([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]) +\
           matrix[0][2] * determinant_2x2([matrix[1][:-1], matrix[2][:-1]])


def direction(p1, p2, p3)-> int:
    """
:   return 1 for left
:   return 0 for same line
:   return -1 for right
    """
    matrix = [[         1,          1,          1],
              [p1.get_x(), p2.get_x(), p3.get_x()],
              [p1.get_y(), p2.get_y(), p3.get_y()]]
    
    
    d = determinant_3x3(matrix)
    if d > 0:
        return LEFT
    elif d == 0:
        return SAME_LINE
    else:
        return RIGHT


def main():

    # left (slide 9)
    print(direction(Point(1, 2), Point(7, 1), Point(4, 7)))
    
    # right (slide 21 after my change)
    print(direction(Point(0, 0), Point(0, 1), Point(1, 0)))
    
    # same line
    print(direction(Point(1, 1), Point(2, 2), Point(3, 3)))
    
if __name__ == "__main__":
    main()
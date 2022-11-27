#--------------------------------#
# ideas was taken from lecture 7 #
#--------------------------------#
from functools import reduce
from functools import cmp_to_key

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


class Board:
    def __init__(self, points):
        self._points = points
        self._point_with_min_y = self._find_point_min_y()
    
    
    def _determinant_2x2(self, matrix):
        """
    :   calc determinant.
    :   param matrix: square matrix 2x2
    :   param type: list of list type double.
    :   return: determinant.
    :   rtype: double.
        """
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    
    def _determinant_3x3(self, matrix):
        return matrix[0][0] * self._determinant_2x2([matrix[1][1:], matrix[2][1:]]) -\
            matrix[0][1] * self._determinant_2x2([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]) +\
            matrix[0][2] * self._determinant_2x2([matrix[1][:-1], matrix[2][:-1]])


    def _direction(self, p1, p2, p3):
        """
    :   return the direction according to the algo
    :   with determinant.
    :   param p1: the first point
    :   type p1: Point
    :   param p2: the second point
    :   type p2: Point
    :   param p3: the third point
    :   type p3: Point
    :   return: direction from p2 to p3
    :   rtype: str
        """
        matrix = [[       1,          1,          1],
                [p1.get_x(), p2.get_x(), p3.get_x()],
                [p1.get_y(), p2.get_y(), p3.get_y()]]
    
    
        d = self._determinant_3x3(matrix)
        if d > 0:
            return LEFT
        elif d == 0:
            return SAME_LINE
        else:
            return RIGHT
    
    
    def _find_point_min_y(self):
        """
    :   function finds the point with the
    :   minimum value of y coordinate.
    :   return: the point was described abouve.
    :   rtype: Point        
        """
        return reduce(lambda min_p, p: min_p if min_p.get_y() < p.get_y() else p, self._points, self._points[0])
    
    
    def _direction_comperator(self, p1, p2):
        """
    :   a comperator by direction of p1--->p--->p2
    :   param p1, p2: two points to compare
    :   type p1, p2: Point
        """
        direction = self._direction(p1, self._point_with_min_y, p2)
        
        if direction == LEFT:
            return -1
        elif direction == SAME_LINE:
            return 0
        else:
            return 1

            
    def _sort_points_by_angle(self):
        """
    :   sort the points by angle point with min y
    :   return: the sorted points where first
    :           point is with minimal y
    :   rtype: list of Point
        """
        points_without_p = list(filter(lambda p: p != self._point_with_min_y, self._points))
        points_without_p.sort(key = cmp_to_key(self._direction_comperator))        
        return [self._point_with_min_y] + points_without_p


    def convex_hull(self):
        points = self._sort_points_by_angle()
        
        stack = []
        stack.append(points[0])
        stack.append(points[1])
        
        for i in range(2, len(points)):
            while self._direction(stack[-2], stack[-1], points[i]) == LEFT:
                stack.pop(-1)
            
            stack.append(points[i])
        
        return stack
        
def main():
    
    q1 = Point(11, 2)
    q2 = Point(4, 10)
    q3 = Point(7, 18)
    q4 = Point(11, 10)
    q5 = Point(12, 14)
    q6 = Point(17, 15)
    q7 = Point(21, 20)
    q8 = Point(21, 14)
    q9 = Point(20, 10)
    q10 = Point(18, 6)
    q11 = Point(23, 4)
    
    board = Board([q11, q1, q10, q2, q9, q3, q8, q4, q7, q5, q6])
    
    c_h = board.convex_hull()
    for p in c_h:
        print(p)
    
if __name__ == "__main__":
    main()
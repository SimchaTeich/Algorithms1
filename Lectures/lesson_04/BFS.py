#------------------------------------------#
# BFS was taken from lecture 5 slide 9     #
# PRINT_PATH taken from lecture 5 slide 17 #
#------------------------------------------#
from os import system
from time import sleep


WHITE = 0
GRAY = 1
BLACK = 2


class Node:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._neighbors = []
        self._color = WHITE
        self._distance = None
        self._prev = None
    
    def __str__(self):
        return f"({self.get_x()}, {self.get_y()})"
    
    def get_x(self):
        return self._x
        
    def get_y(self):
        return self._y
    
    def get_distance(self):
        return self._distance
    
    def get_neighbors(self):
        return self._neighbors
    
    def get_color(self):
        return self._color
    
    def get_prev(self):
        return self._prev
    
    def add_neighbor(self, new_node):
        self._neighbors.append(new_node)
    
    def update_color(self):
       self._color += 1
    
    def set_distance(self, new_dist):
        self._distance = new_dist
    
    def set_prev(self, prev_node):
        self._prev = prev_node


class Board:
    def __init__(self, side, nodes_list):
        self._side = side
        self._board = [[None]*side for _ in range(side)]
        
        # init the board with nodes.
        for node in nodes_list:
            self._board[node.get_x()][node.get_y()] = node
            print(node.__repr__())
        
        
    def __str__(self):
        s = ""
        for i in range(self._side):
            for j in range(self._side):
                if self._board[i][j]:
                    s += str(self._board[i][j].get_color())
                    s += " "
                else:
                    s += "  "
            
            s += '\n'
        return s
    
    
    def print_level(self):
        system("cls")
        #print("#-----------------#")
        print(self)
        sleep(1)
    
    
    def BFS(self, s):
        """
:       The BFS algo same as slide 9
:       param s: strating node
:       type s: Node 
        """
        self.print_level()
    
        # init the start node
        s.update_color() # to gray
        s.set_distance(0)
        s.set_prev(None)
    
        self.print_level()
        
        Q = [s]
        while Q:
            u = Q.pop()
            for v in u.get_neighbors():
                if v.get_color() == WHITE:
                    v.update_color() # to gray
                    v.set_distance(u.get_distance() + 1)
                    v.set_prev(u)
                    Q.insert(0, v)
         
            u.update_color() # to black
            self.print_level()


    def print_path(self, s, v):
        """
:       print cordintas of path from s to v recursivly,
:       according to the PATH-TREE just after one BFS.
:       param s: node for start the path
:       type s: Node
:       param v: node for end the path
:       type v: Node
        """
        if s == v:
            print(v, "-->", end='') 
        elif v.get_prev() != None:
            self.print_path(s, v.get_prev())
            print(v, "-->", end='')
        else:
            print(f"No path from s:{s} to v:{v}!")

def main():
    
    # build the next undirected-graph:
    # V = {1, 2, 3, 4, 5}
    n1 = Node(1, 1)
    n2 = Node(2, 3)
    n3 = Node(3, 1)
    n4 = Node(4, 2)
    n5 = Node(4, 4)
    
    # E = {(1, 2), (1, 3), (2, 3), (3, 5), (4, 5)}
    n1.add_neighbor(n2)
    n1.add_neighbor(n3)
    n2.add_neighbor(n1)
    n2.add_neighbor(n3)
    n2.add_neighbor(n5)
    n3.add_neighbor(n1)
    n3.add_neighbor(n2)
    n4.add_neighbor(n5)
    n5.add_neighbor(n2)
    n5.add_neighbor(n4)
    
    # insert all nodes to matrix folow by coorinates
    board = Board(5, [n1, n2, n3, n4, n5])
    
    # run the BFS!
    board.BFS(n2)

    # find the path from n2 to n4.
    print(f"Path from {n2} to {n4}:")
    board.print_path(n2, n4)

if __name__ == "__main__":
    main()
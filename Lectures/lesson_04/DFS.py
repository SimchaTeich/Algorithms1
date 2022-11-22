#------------------------------------------#
# DFS was taken from lecture 6 slide 4     #
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
        self._d = None # discovery time
        self._f = None # finish time
        self._prev = None
    
    def __str__(self):
        return f"({self.get_x()}, {self.get_y()})"
    
    def get_x(self):
        return self._x
        
    def get_y(self):
        return self._y
    
    def get_d(self):
        return self._d
        
    def get_f(self):
        return self._f
    
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
    
    def set_d(self, discovery_time):
        self._d = discovery_time
        
    def set_f(self, finish_time):
        self._d = finish_time
        
    def set_prev(self, prev_node):
        self._prev = prev_node


class Board:
    time = 0

    def __init__(self, side, nodes_list):
        self._side = side
        self._board = [[None]*side for _ in range(side)]
        self._nodes = nodes_list
        
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
        print(self)
        sleep(1)
    
    
    def DFS_visit(self, u):
        """
:       The DFS_visit algo same as slide 4
        """
        u.update_color() # to gray
        self.print_level()
        Board.time += 1
        u.set_d = Board.time
        
        for v in u.get_neighbors():
            if v.get_color() == WHITE:
                v.set_prev(u)
                self.DFS_visit(v)
            
        u.update_color() # to black
        self.print_level()
        Board.time += 1
        u.set_f = Board.time
    
    
    def DFS(self):
        """
:       The DFS algo same as slide 4
        """
        self.print_level()
        
        for u in self._nodes:
            if u.get_color() == WHITE:
                self.DFS_visit(u)
        


    def print_path(self, s, v):
        """
:       print cordintas of path from s to v recursivly,
:       according to the PATH-TREE just after one DFS.
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
    
    # build the next directed-graph as in slide 5:
    # V = {1, 2, 3, 4, 5, 6}
    n1 = Node(1, 1)
    n2 = Node(1, 3)
    n3 = Node(1, 5)
    n4 = Node(3, 1)
    n5 = Node(3, 3)
    n6 = Node(3, 5)
    
    # E = {(1, 2), (1, 4), (2, 5), (3, 5), (3, 6), (4, 2), (5, 4), (6, 6)}
    n1.add_neighbor(n2)
    n1.add_neighbor(n4)
    n2.add_neighbor(n5)
    n3.add_neighbor(n5)
    n3.add_neighbor(n6)
    n4.add_neighbor(n2)
    n5.add_neighbor(n4)
    n6.add_neighbor(n6)
    
    # insert all nodes to matrix folow by coorinates
    board = Board(6, [n1, n2, n3, n4, n5, n6])
    
    # run the DFS!
    board.DFS()

if __name__ == "__main__":
    main()
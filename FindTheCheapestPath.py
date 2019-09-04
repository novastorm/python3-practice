'''
You should be familiar with the "Find the shortest path" problem. But what if moving to a neighboring coordinate counted not as 1 step but as N *steps? *

INSTRUCTIONS

Your task is to find the path through the field which has the lowest cost to go through.

As input you will receive:
1) a toll_map matrix (as variable t) which holds data about how expensive it is to go through the given field coordinates
2) a start coordinate (tuple) which holds information about your starting position
3) a finish coordinate (tuple) which holds information about the position you have to get to

As output you should return:
1) the directions list


EXAMPLE

INPUT:

toll_map  |  start  |  finish
          |         |
[         |         |
 [1,9,1], |  (0,0)  |  (0,2)
 [2,9,1], |         |
 [2,1,1], |         |
]         |         |



OUTPUT:

["down", "down", "right", "right", "up", "up"]
CLARIFICATIONS

1) the start and finish tuples have the (x, y) format which means start = (x_1, y_1) and finish = (x_2, y_2), start_pos = field[x_1][y_1] and finish_pos = field[x_2][y_2]
2) the total cost is increased after leaving the matrix coordinate, not entering it
3) the field will be rectangular, not necessarily a square
4) the field will always be of correct shape
5) the actual tests will check total_cost based on your returned directions list, not the directions themselves, so you shouldn't worry about having multiple possible solutions

'''
from heapq import *

def cheapest_path(t, start, finish):

    class Node:
        def __init__ (self, position, direction):
            self.position = position
            self.direction = direction
            
        def __repr__ (self):
            return str(self)
            
        def __str__ (self):
            return '{{{}, {}, {}}}'.format(self.position,self.direction, dist.get(self.position, float('inf')))
            
        def __lt__ (self, other):
            return dist[self.position] < dist.get(other.position, float('inf'))

    MIN_X = 0
    MIN_Y = 0
    MAX_X = len(t)
    MAX_Y = len(t[0])
    
    X = 0
    Y = 1
    
    NONE = 'none'
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    directions = {
      NONE: (0,0),
      UP: (-1,0),
      DOWN: (1,0),
      LEFT: (0,-1),
      RIGHT: (0, 1)
    }

    unvisited = []
    dist = {}
    prev = {}

    dist[start] = 0
    prev[start] = Node(None, NONE)
    heappush(unvisited, Node(start, NONE))
    
    while unvisited:
#         print()
        print()

        node = heappop(unvisited)
#         print("N: ", node)

        if node.position == finish:
            break
            
        nodePos = node.position
        routeCost = t[nodePos[X]][nodePos[Y]]

        neighbor = None
        for dir in [UP, DOWN, LEFT, RIGHT]:
            delta = directions[dir]
            (x, y) = tuple(map(sum, zip(node.position, delta)))
            if (x < MIN_X or x >= MAX_X or
                y < MIN_Y or y >= MAX_Y):
                continue
            neighbor = (x, y)
            newDistance = dist[nodePos] + routeCost
            if dist.get(neighbor, None) == None:
                dist[neighbor] = newDistance
                prev[neighbor] = Node(nodePos, dir)
                heappush(unvisited, Node(neighbor, dir))
        
#             print(neighbor, newDistance, dist.get(neighbor, float('inf')))
            if newDistance < dist.get(neighbor, float('inf')):
                dist[neighbor] = newDistance
                prev[neighbor] = Node(nodePos, dir)
                heappush(unvisited, Node(neighbor, dir))

#         print("D: ", dist)    
#         print("P: ", prev)


#         print("UV: ", unvisited)
#         heapify(unvisited)
#         print("UV: ", unvisited)
            
    path = []
    walker = finish
    while walker:
#         print("W: ", walker)
#         print("p[W]: ", prev[walker])
        dir = prev[walker].direction
        if dir != NONE:
            path.insert(0, dir)
        walker = prev[walker].position
    
    return path
        
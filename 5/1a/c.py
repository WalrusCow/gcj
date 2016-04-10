import sys
import math

class Graph():
    def __init__(self):
        self.vertices = []
        self.adj = []
        # Set of points in the boundary
        self.boundary = set()
        self.rightmost = None

    def get_rightmost(self):
        # Top-rightmost vertex
        self.rightmost = max(self.vertices)

    def add_vertex(self, point):
        self.vertices.append(point)
        newL = []
        for l in self.adj:
            # Default to attached to everything
            # TODO: Get angles between each vertex
            l.append(True)
            newL.append(True)
        self.adj.append(newL)

        # Get the new boundary
        self.get_rightmost()
        self.boundary = {self.rightmost}
        current = self.rightmost
        angle = -math.pi / 2
        for 

    def remove_vertex():
        # Remove most recently added vertex
        self.vertices.pop()
        for l in self.adj:
            l.pop()
        self.adj.pop()

def num_until_boundary(point, points):
    ''' Determine the number of points in "points" to remove until
    "point" lies on the boundary. '''

    # Begin with a single point
    g = Graph()
    g.add_vertex(point)

    for p in points:
        # Determine if adding "p" to g would put "point" off boundary
        g.add_vertex(p)
        if point not in g.boundary:
            g.remove_vertex()



def test():
    n = int(sys.stdin.readline())
    points = []
    for _ in range(n):
        points.append(tuple(map(int, sys.stdin.readline().strip().split())))

    for tree in points:
        # Determine number to cut down for this tree to be on the boundary

    # Adjacency matrix for the graph
    adj = [[True] * len(points) for _ in points]

    print('\n'.join(map(str,points)))
    return [x[0] for x in points]

def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test()
        print('Case #{}:\n{}'.format(i+1, '\n'.join(map(str, answer))))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)

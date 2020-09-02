# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# Search should return the path.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,astar,astar_multi,fast)
class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.objects = 0

    def inlist(head, node):
        new = True
        nodeprev = newNode.prev
        while(not nodeprev==None):
             if(nodeprev.val == newNode.val):
                new = False
             nodeprev = nodeprev.prev
        return new


def search(maze, searchMethod):
    return {
        "bfs": bfs,
        "astar": astar,
        "astar_corner": astar_corner,
        "astar_multi": astar_multi,
        "fast": fast,
    }.get(searchMethod)(maze)

def solve_maze(maze):

    obj_target = len(maze.getObjectives())
    print(obj_target, " objects")
    obj_curr = 0
    frontier = []
    node = Node(maze.getStart())
    frontier.append(node)
    closed =[]
    #check all the nodes / paths
    print("starting search")
    while(node.objects != obj_target):
    # #     ##first get a list of all possible new neighbors from current node
        frontier_new = []
        #current node being searched
        node = frontier[0]
        currNode = node.val
        new_values= maze.getNeighbors(currNode[0], currNode[1])

    #make new nodes if its new, new objective.
        for i in new_values:
            newNode = Node(i)
            newNode.prev = node
            frontier_new.append(newNode)
            newNode.objects = node.objects

            if maze.isObjective(newNode.val[0], newNode.val[1]):
                # new = True
                # nodeprev = newNode.prev
                # while(not nodeprev==None):
                #      if(nodeprev.val == newNode.val):
                #         new = False
                #         nodeprev = None
                #      else:
                #          nodeprev = nodeprev.prev
                # if(new):
                newNode.objects = newNode.objects +1
                print("objective found: ",newNode.val )
                if(newNode.objects == obj_target):
                    return newNode
                # #   Check if current node is an objective

        #pop node from queue

        ##check if they are a new node on the path
        # for i in frontier_new:
        #     new = True
        #     nodeprev = i.prev
        #     while(not nodeprev==None):
        #          if(nodeprev.val == i.val and nodeprev.objects == i.objects):
        #             new = False
        #             nodeprev = None
        #          else:
        #             nodeprev = nodeprev.prev
        #     if(new):
        #         frontier.append(i)
        for i in frontier_new:
             if (not i.val in closed):
                 frontier.append(i)

        closed.append(frontier.pop(0).val)
        node = frontier[0]


def bfs(maze):
    """
    Runs BFS for part 1 of the assignment.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """

    node = solve_maze(maze)
    path = []
    while(not node  == None ):
        path.append(node.val)
        node = node.prev
    path.reverse()
    print (path)
    return path


def astar(maze):
    """
    Runs A star for part 1 of the assignment.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    return []

def astar_corner(maze):
    """
    Runs A star for part 2 of the assignment in the case where there are four corner objectives.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
        """
    # TODO: Write your code here
    return []

def astar_multi(maze):
    """
    Runs A star for part 3 of the assignment in the case where there are
    multiple objectives.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    return []


def fast(maze):
    """
    Runs suboptimal search algorithm for part 4.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    return []

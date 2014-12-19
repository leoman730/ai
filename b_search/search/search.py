# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    # init
    path = []
    explored = set()

    rootNode = [problem.getStartState(), list()]

    from util import Stack
    nodeStack = Stack()

    from util import Stack
    nodeStack = Stack()

    nodeStack.push(rootNode);

    while not nodeStack.isEmpty():
        
        node = nodeStack.pop()
        state = node[0]
        path = node[1]
        
        explored.add(state)        

        if problem.isGoalState(node[0]):
            return path
        else:
            children = problem.getSuccessors(node[0])
            # reverse_children = children[::-1]
            # for child in reverse_children:
            for child in children:
                if child[0] not in explored:
                    child_path = list(path)
                    child_path.append(child[1])
                    nodeStack.push([child[0], child_path])



    raise Exception, 'No solutions found'



# def depthFirstSearch(problem):
#     """
#     Search the deepest nodes in the search tree first.

#     Your search algorithm needs to return a list of actions that reaches the
#     goal. Make sure to implement a graph search algorithm.

#     To get started, you might want to try some of these simple commands to
#     understand the search problem that is being passed in:

#     print "Start:", problem.getStartState()
#     print "Is the start a goal?", problem.isGoalState(problem.getStartState())
#     print "Start's successors:", problem.getSuccessors(problem.getStartState())
#     """
#     "*** YOUR CODE HERE ***"
    
#     fringe = []
#     explored = []
#     fringe.append((problem.getStartState(),'',0))
     
#     return DFSRecursive(fringe, problem, explored)

    

# def DFSRecursive(fringe, problem, explored):
#     node = fringe.pop()    
#     explored.append(node[0])
    
#     if problem.isGoalState(node[0]):
#         return []
#     for i in problem.getSuccessors(node[0]):
#         if i[0] not in explored:
#             fringe.append(i)
#             tmpPath = DFSRecursive(fringe, problem, explored)
#             if (tmpPath != None):
#                 tmpPath.insert(0,i[1])
#                 print tmpPath
#                 return tmpPath

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    explored = set()
    rootNode = [problem.getStartState(), list()]

    from util import Queue
    queueNode = Queue()

    queueNode.push(rootNode)


    while not queueNode.isEmpty():

        currentNode = queueNode.pop()
        currentState = currentNode[0]
        currentPath = currentNode[1]
        
        explored.add(currentState)

        if problem.isGoalState(currentState):
            return currentPath

        else:
            children = problem.getSuccessors(currentState)            

            for child in children:
                childState = child[0]
                
                # Converts a tuple into list.
                childPath = list(currentPath)

                childPath.append(child[1])
                
                if childState not in explored:
                    queueNode.push([child[0], childPath])


    raise Exception, 'No solutions found'



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

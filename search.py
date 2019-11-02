# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 74].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  

  """
  dfs=DFS()
  dfs.PushAndMarkExplored(Node(problem.getStartState(),None,None))
  while (dfs.StackNotEmpty()):
    current = dfs.Stack.pop()
    if problem.isGoalState(current.getState()):
      return current.getActionsFromStart()
    else:
      successors = problem.getSuccessors(current.getState())
      for item in successors:
              if dfs.NotVisited(item[0]):
                dfs.PushAndMarkExplored(Node(item[0],current,item[1]))
                 
  

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 74]"
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

class Node:
  def __init__(self, state, parent, action):
        self.state  = state
        self.parent = parent
        self.action = action
        
  def __str__(self):
        return "State: " + str(self.state) + "\n" + \
               "Parent: " + str(self.parent.state) + "\n" + \
               "Action: " + str(self.action) + "\n" 

  def getState(self):
        return self.state

  def getParent(self):
        return self.parent

  def getAction(self):
        return self.action
  def getActionsFromStart(self):
        actionList = []
        currNode = self
        while currNode.getAction() is not None:
            actionList.append(currNode.getAction())
            currNode = currNode.parent
        actionList.reverse()
        return actionList

class DFS:
   'DFS containg the entire data structure needed to perform deep first search'
   Stack = util.Stack()
   Visited = set()

   def StackNotEmpty(self):
     return not self.Stack.isEmpty()
    
   def PushAndMarkExplored(self,item):
     self.Stack.push(item)
     self.Visited.add(item.getState())

   def NotVisited(self,item):
     return not item in self.Visited
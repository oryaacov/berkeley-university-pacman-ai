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
  return bdFirstSearch(problem,BDFS(util.Stack()))
  

def breadthFirstSearch(problem):
  return bdFirstSearch(problem,BDFS(util.Queue()))
 

def bdFirstSearch(problem,searchAlg):
  searchAlg.PushAndMarkExplored(Node(problem.getStartState(),None,None))
  while (searchAlg.NotEmpty()):
    current = searchAlg.Pop()
    if problem.isGoalState(current.getState()):
      return current.getActionsFromStart()
    else:
      successors = problem.getSuccessors(current.getState())
      for item in successors:
              if searchAlg.NotVisited(item[0]):
                searchAlg.PushAndMarkExplored(Node(item[0],current,item[1]))

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



class BDFS:
   'BDFS containg the entire data structure needed to perform best/deep  first search'
   def  __init__(self,dataStructure):
     self.ds=dataStructure
   ds=None
   Visited = set()

   def NotEmpty(self):
     return not self.ds.isEmpty()
    
   def PushAndMarkExplored(self,item):
     self.ds.push(item)
     self.Visited.add(item.getState())

   def NotVisited(self,item):
     return not item in self.Visited    
  
   def Pop(self):
     return self.ds.pop()


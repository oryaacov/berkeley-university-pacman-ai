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
           

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

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
  return bdFirstSearch(problem,BDFS(dfs,None,None))
  

def breadthFirstSearch(problem):
  return bdFirstSearch(problem,BDFS(bfs,None,None))
 

def uniformCostSearch(problem):
  return bdFirstSearch(problem,BDFS(ucs,None,None))

 
def aStarSearch(problem, heuristic=nullHeuristic):
  return bdFirstSearch(problem,BDFS(astar, heuristic,problem))
    


DISTANCE_FROM_GOAL="distanceFromGoal"

def calculateH(problem,state,method):
  if (method==DISTANCE_FROM_GOAL):
   goalX=problem.goal[0]
   goalY=problem.goal[1]
   currX=state.state[0]
   currY=state.state[1]
   return abs(goalX-currX)+abs(goalY-currY)



def bdFirstSearch(problem,searchAlg):
  startState=problem.getStartState()
  searchAlg.SetCurrent(Node(startState,None,None))
  searchAlg.PushAndMarkExplored(Node(startState,None,None),None,problem)
  while (searchAlg.NotEmpty()):
    current = searchAlg.Pop()
    if problem.isGoalState(current.getState()):
      return current.getActionsFromStart()
    else:
      successors = problem.getSuccessors(current.state)
      for item in successors:
              position, direction, stepPrice = item
              if searchAlg.NotVisited(position):
                searchAlg.PushAndMarkExplored(Node(position,current,direction),stepPrice,problem)
  
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
        print len(actionList)
        return actionList


class BDFS:
   'BDFS containg the entire data structure needed to perform best/deep  first search'
   def  __init__(self,dsName,heuristic,problem):
     self.dsName=dsName
     self.heuristic=heuristic
     self.problem=problem
     if (self.dsName==dfs):
       self.frontier=util.Stack()
     elif (self.dsName==bfs):
       self.frontier=util.Queue()
     elif (self.dsName==ucs):
       self.frontier=util.PriorityQueue()
     elif (self.dsName==astar):
       self.frontier=util.PriorityQueueWithFunction(lambda func:heuristic(self.GetCurrent(),self.problem))

   heuristic=None
   frontier=None
   dsName=None
   explored = set()
   current = None
   problem=None
   position=None

   def GetHeuristicVars(self):
     return self.GetCurrent(),self.problem

   def NotEmpty(self):
     return not self.frontier.isEmpty()
    
   def PushAndMarkExplored(self,item,priority,problem):
     if (self.dsName==dfs or self.dsName==bfs):
       self.frontier.push(item)
     elif self.dsName==astar:
       self.frontier.push(item)
     else:
       self.frontier.push(item,priority)

     self.explored.add(item.getState())

   def NotVisited(self,item):
     return not item in self.explored    
  
   def SetCurrent(self,item):
     self.current=item

   def SetPosition(self,item):
     self.position=item

   def GetCurrent(self):
     if self.current==None:
       self.current= self.problem.getStartState()
     return self.current


   def GetPosition(self):
     return self.position


   def GetSearchType(self):
     return self.dsName

   def Pop(self):
     state = self.frontier.pop()
     self.SetCurrent(state)
     return state


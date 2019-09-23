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

from util import Stack, Queue


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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions

    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    initial_state = problem.getStartState()
    current_state = initial_state
    sucessors = []
    estados_visitados = []
    caminho = []

    Pilha = Stack()

    while problem.isGoalState(current_state) == False:
        Initial_Length = len(sucessors)
        for i in range(0, len(problem.getSuccessors(current_state))):
            sucessors.append(problem.getSuccessors(current_state)[i])

        for i in range(Initial_Length, len(sucessors)):
            Pilha.push(list(sucessors[i]))

        nao_visitado = False
        while nao_visitado == False:
            estado_testado = (Pilha.pop())
            if estado_testado[0] not in estados_visitados:
                current_state = estado_testado[0]
                caminho.append(estado_testado[1])
                nao_visitado = True
            else:
                nao_visitado = False

        estados_visitados.append(current_state)

    for i in range(len(estados_visitados) - 1, 1, -1):
        if not(abs(estados_visitados[i][0] - estados_visitados[i-1][0]) <= 1 and abs(estados_visitados[i][1] - estados_visitados[i-1][1]) <= 1 and (abs(estados_visitados[i][0] - estados_visitados[i-1][0]) + abs(estados_visitados[i][1] - estados_visitados[i-1][1])) <= 1):
            del estados_visitados[i-1]
            del caminho[i-1]

    for i in range(0, len(caminho)):
        if caminho[i] == "North":
            caminho[i] = n
        elif caminho[i] == "South":
            caminho[i] = s
        elif caminho[i] == "East":
            caminho[i] = e
        else:
            caminho[i] = w

    return caminho

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions

    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    initial_state = problem.getStartState()
    current_state = initial_state
    sucessors = []
    estados_visitados = []
    caminho = []

    Fila = Queue()

    while problem.isGoalState(current_state) == False:
        Initial_Length = len(sucessors)
        for i in range(0, len(problem.getSuccessors(current_state))):
            sucessors.append(problem.getSuccessors(current_state)[i])

        for i in range(Initial_Length, len(sucessors)):
            Fila.push(list(sucessors[i]))

        nao_visitado = False
        while nao_visitado == False:
            estado_testado = (Fila.pop())
            if estado_testado[0] not in estados_visitados:
                current_state = estado_testado[0]
                caminho.append(estado_testado[1])
                nao_visitado = True
            else:
                nao_visitado = False

        estados_visitados.append(current_state)

    print(estados_visitados)

    for i in range(len(estados_visitados) - 1, 1, -1):
        if not(abs(estados_visitados[i][0] - estados_visitados[i-1][0]) <= 1 and abs(estados_visitados[i][1] - estados_visitados[i-1][1]) <= 1 and (abs(estados_visitados[i][0] - estados_visitados[i-1][0]) + abs(estados_visitados[i][1] - estados_visitados[i-1][1])) <= 1):
            del estados_visitados[i-1]
            del caminho[i-1]

    for i in range(0, len(caminho)):
        if caminho[i] == "North":
            caminho[i] = n
        elif caminho[i] == "South":
            caminho[i] = s
        elif caminho[i] == "East":
            caminho[i] = e
        else:
            caminho[i] = w

    return []

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
        from game import Directions

    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    # Define o nodo como um conjunto contendo o estado inicial, o custo do caminho e a lista de passos percorridos
    estados = (problem.getStartState(),0,[])  
	# Cria a fila de prioridade 
    fila_de_prioridade = util.PriorityQueue()  
	# Insere o nodo e a prioridade definida na fila
    fila_de_prioridade.push(estados,problem)
    estados_visitados = []
    while True:
	    # Verifica se a fila estar vazia, se estiver encerrar a iteracao
	    if fila_de_prioridade.isEmpty(): 
	        return False
	    estado, custoMeta, caminho = fila_de_prioridade.pop() # Desempilha o estado, o custo, e o elemento com a maior prioridade da fila
	    if problem.isGoalState(estado):   # Verifica se estar no estado meta
		    return caminho   # Retorna o caminho do no inicial ate o estado
	    if estado not in estados_visitados:  
		    estados_visitados.append(estado) # Adiciona o nodo na lista de nodos explorados
		    sucessores = problem.getSuccessors(estado)
	    # Percorre os filhos do elemento desempilhado 
	    for sucessor, direcao, custoEstado in sucessores:
	        if sucessor not in estados_visitados:
		        custoCaminho = custoMeta + custoEstado
		        # Insere o filho do elemento desempilhado com o menor custo acumulado como prioridade para realizar a expansao
		        fila_de_prioridade.push((sucessor,custoCaminho,caminho+[direcao]), custoCaminho)
    
    for i in range(0, len(caminho)):
        if caminho[i] == "North":
            caminho[i] = n
        elif caminho[i] == "South":
            caminho[i] = s
        elif caminho[i] == "East":
            caminho[i] = e
        else:
            caminho[i] = w

    return caminho
    util.raiseNotDefined()
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

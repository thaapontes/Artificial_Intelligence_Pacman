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
from util import Stack, Queue, PriorityQueue


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
    pais = [] 
    caminho =[0]
    rota = []

    Fila = Queue()

    # print(problem.getSuccessors((3,1)))

    while problem.isGoalState(current_state) == False:
        Initial_Length = len(sucessors)
        for i in range(0, len(problem.getSuccessors(current_state))):
            sucessors.append(problem.getSuccessors(current_state)[i])
            caminho.append((problem.getSuccessors(current_state)[i][1]))
            pais.append(current_state)

        for i in range(Initial_Length, len(sucessors)):
            Fila.push(list(sucessors[i]))

        nao_visitado = False
        while nao_visitado == False:
            estado_testado = (Fila.pop())
            if estado_testado[0] not in estados_visitados:
                current_state = estado_testado[0]
                nao_visitado = True
            else:
                nao_visitado = False

        estados_visitados.append(current_state)

    past_state = current_state
    while current_state != initial_state:
        print(current_state)
        print(past_state)
        print("\n")
        for i in range(0, len(sucessors)):
            if sucessors[i][0] == current_state and past_state != pais [i]:
                rota.append(current_state)
                past_state = current_state
                current_state = pais[i]
    
    print("Rota: ")
    print(rota)

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
    caminho=[]
    # Estado inicial salva o estado inicial (posicao x,y), o custo do estado atual e o caminho percorrido ate o estado atual
    estado_inicial = (problem.getStartState(), 0, caminho)

    fila_prioridade = PriorityQueue()
    fila_prioridade.push(estado_inicial, 1)

    estados_visitados = []

    while not(fila_prioridade.isEmpty()):
        estado, custo_atual, caminho = fila_prioridade.pop()
        if problem.isGoalState(estado):
            return caminho
        if estado not in estados_visitados:
            estados_visitados.append(estado)
            sucessores = problem.getSuccessors(estado)
            for estado_sucessor, direcao, custo_sucessor in sucessores:
                if estado_sucessor not in estados_visitados:
                    # Calcula o custo acumulado, somando o custo atual e o custo do sucessor
                    custo_acumulado = custo_atual + custo_sucessor

                    # Coloca na fila de prioridade o estado sucessor, custo acumulado e o caminho, alem da prioridade, 
                    # que e tambem o custo acumulado (quanto menor o custo, maior a prioridade)
                    fila_prioridade.push((estado_sucessor, custo_acumulado, caminho+[direcao]), custo_acumulado)



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    caminho=[]
    # Estado inicial salva o estado inicial (posicao x,y), o custo do estado atual e o caminho percorrido ate o estado atual
    estado_inicial = (problem.getStartState(), 0 + heuristic(problem.getStartState(), problem), caminho)

    fila_prioridade = PriorityQueue()
    fila_prioridade.push(estado_inicial, 1)

    estados_visitados = []

    while not(fila_prioridade.isEmpty()):
        estado, custo_atual, caminho = fila_prioridade.pop()
        if problem.isGoalState(estado):
            return caminho
        if estado not in estados_visitados:
            estados_visitados.append(estado)
            sucessores = problem.getSuccessors(estado)
            for estado_sucessor, direcao, custo_sucessor in sucessores:
                if estado_sucessor not in estados_visitados:
                    # Calcula o custo acumulado, somando o custo atual, o custo do sucessor e a funcao heuristica
                    custo_acumulado = custo_atual + custo_sucessor + heuristic(estado_sucessor, problem)
                    if heuristic(estado, problem) <= (custo_sucessor + heuristic(estado_sucessor, problem)):
                        print("MONOTONICA E ADMISSIVEL")
                    else:
                        print("NAO")
                    # Coloca na fila de prioridade o estado sucessor, custo acumulado e o caminho, alem da prioridade, 
                    # que e tambem o custo acumulado (quanto menor o custo, maior a prioridade)
                    fila_prioridade.push((estado_sucessor, custo_acumulado, caminho+[direcao]), custo_acumulado)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

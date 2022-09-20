# 2da Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import practica1 as modulo_p1
import sys
import os

 
# funcion aux
def check_input(userInput):
    if (not isinstance(userInput, list)) or (not isinstance(userInput[0], list)) or (not all(isinstance(e, tuple) for e in userInput[1])):
        raise TypeError("Tipo inválido de argumento. Formato correcto: (['a', 'b', 'c'], [('a', 'b'), ('b', 'c')])")


# a
def graph_has_eulerian_circuit(graph):


    check_input(graph)

    # vale solo para grafos conexos
    if not modulo_p1.es_conexo(graph):
        return False

    # G tiene un circuito euleriano s.i.i. el grado de entrada de cade vertice es el mismo que el grado de salida
    # (es decir, todos los vert tienen grado par)
    
    for v in modulo_p1.cuenta_grado(graph).values():
        if (v % 2) != 0:
            return False
    return True



# funcion aux
def is_bridge(edge, degList):
    try:
        ret = (degList[edge[0]] <= 1) or (degList[edge[1]] <= 1)
        return ret 
    except Exception as e:
        print(f"Error: {e}")

 
# funcion aux     
def get_degree_list(V,E):

    degreeDict = {}

    for vertex in V:
        degreeDict[vertex] = 0
        for edge in E:
            degreeDict[vertex] += 1 if vertex in edge else 0

    return degreeDict

# b
def find_eulerian_circuit(graph):

    check_input(graph)

    if not graph_has_eulerian_circuit(graph):
        return None

    V = graph[0]
    E = graph[1]
    eulCircuit = []
    initVert = V[0]

    for e in E:

        if e[0] == initVert or e[1] == initVert:

            if e[0] == initVert:
                    vIn = e[0]
                    vOut = e[1]
            else:
                    vIn = e[1]
                    vOut = e[0]

            if not is_bridge(e, get_degree_list(V, E)):
                eulCircuit.append((vIn, vOut))
                E.remove(e)
                initVert = vOut

    while E != []:           
        for e in E:      
            if e[0] == initVert or e[1] == initVert:
                if e[0] == initVert:
                    vIn = e[0]
                    vOut = e[1]
                else:
                    vIn = e[1]
                    vOut = e[0]

                eulCircuit.append((vIn, vOut))
                E.remove(e)
                initVert = vOut

    return eulCircuit




def main():

    os.system('cls')

    grafotest = [['a', 'b', 'c'], [('a', 'b'), ('c', 'a'), ('b', 'c')]]
    grafotest2 =[['a', 'b', 'c', 'd'], [('a', 'b'), ('b', 'c'), ('c', 'd'), ('b', 'd')]]
    grafotest3 = [['a', 'b', 'c'], [('a', 'b'), ('b', 'c')]]
    grafotest4 = [['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('b', 'c'), ('c','a'), ('d', 'e'), ('e', 'f'), ('d', 'f')]]
    grafo_disconexo = [['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('b', 'c'), ('a', 'c'), ('e', 'd')]]
    grafo_euler = [['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'e'), ('c', 'f'), ('d', 'e'), ('e', 'f')]]
    grafo_euler2= [['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e'), ('c', 'f'), ('d', 'f')]]

    # grafo para testear
    grafo = grafo_euler


    title = "Teoria de grafos - PRACTICA 2"
    author = "Juan Ignacio Bertoni 6to info"

    print("-"*len(title))
    print(f"{title}\n\n{author}")
    print("-"*len(title))

    # grafo = modulo_p1.lee_grafo_stdin()

    print(f"\ngrafo: {grafo}\n")
    
    # a
    print("a) El grafo tiene un CE") if graph_has_eulerian_circuit(grafo) else print("El grafo no tiene un CE")
    
    # b
    print(f"\nb) Circuito euleriano encontrado: {find_eulerian_circuit(grafo)}\n")


if __name__ == '__main__':
    main()
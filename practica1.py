# 1ra Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos
import sys
import os

# a
def lee_grafo_stdin():
    vertices = []
    aristas = []
    card = int(input("a) Ingresar cardinal de V\n"))
    for vert in range(card):
        v = input(f"Vertice {vert+1}\n")
        vertices.append(v)
   
    finish = 0
    while (not finish):
        print(f"Ingresar arista, los vertices que posee son: {vertices}")
        ar = input("\n")
       
        if ar=="-1":
            finish = 1
            break
           
        vertSeparation = tuple(ar.split(' '))

        for v in vertSeparation:
            if v not in vertices:
                print(f"{v} no es un vertice del grafo, intentarlo de nuevo\n")
                exit(-1)
        if len(vertSeparation) != 2:
            print("Una arista debe estar compuesta de dos vertices\n")
            exit(-1)
       
        aristas.append(vertSeparation)
    
    g = [vertices, aristas]
    print(f"a) El grafo ingresado fue: {g}")
    return g
       

# b       
def cuenta_grado(grafo_lista):
 
    degreeDict = {}
    V = grafo_lista[0]
    E = grafo_lista[1]

    for vertex in V:
        degreeDict[vertex] = 0
        for edge in E:
            degreeDict[vertex] += 1 if vertex in edge else 0
    return degreeDict


# c
def lista_a_adyacencia(grafo_lista):
    V = grafo_lista[0]
    E = grafo_lista[1]

    # inicializar matriz
    matrAdyancencia = [[0 for _ in range(len(V))] for _ in range(len(V))] 

    i=0

    for vertex1 in V:
        j=0
        for vertex2 in V:
            # grafo simple
            if vertex1 != vertex2:
                for edge in E:
                    if vertex1 in edge and vertex2 in edge:
                        matrAdyancencia[i][j] = 1
            j+=1
        i+=1

    return matrAdyancencia



# funcion aux
def modif_list(v, componentes, E):

    componentes.append([v])

    for e in E:
        for componente in componentes:
            if e[0] in componente and e[1] not in componente:
                componente.append(e[1])
            elif e[1] in componente and e[0] not in componente:
                componente.append(e[0])
    return componentes

# d
def componentes_conexas(grafo):
    V = grafo[0]
    E = grafo[1]
    componentes = []

    for v in V:
        # entra a fun1 si el vertice no fue encontrado en ninguna componente actual
        if not(any(v in componente for componente in componentes)):
            componentes = modif_list(v, componentes, E)
    return componentes

# e
def es_conexo(grafo_lista): 
    return len(componentes_conexas(grafo_lista)) == 1;


#################### FIN EJERCICIO PRACTICA ####################

def main():

    os.system('cls')

    grafotest = [['a', 'b', 'c'], [('a', 'b'), ('a', 'c'), ('b', 'c')]]
    grafotest2 =[['a', 'b', 'c', 'd'], [('a', 'b'), ('b', 'c'), ('c', 'd'), ('b', 'd')]]
    grafotest3 = [['a', 'b', 'c'], [('a', 'b'), ('b', 'c')]]
    grafo_disconexo = [['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('b', 'c'), ('a', 'c'), ('e', 'd')]]

    # grafo para testear
    grafo = grafo_disconexo

    title = "Teoria de grafos - PRACTICA 1"
    author = "Juan Ignacio Bertoni 6to info"

    print("-"*len(title))
    print(f"{title}\n\n{author}")
    print("-"*len(title))
    
    # a
    # grafo = lee_grafo_stdin()
    print(f"\na) Grafo: {grafo}")

    # b
    d = cuenta_grado(grafo)
    print(f"\nb) Grado de los vertices: {d}") 

    m = lista_a_adyacencia(grafo)
    
    # c
    print("\nc) Matriz de adyacencia:")
    for fila in m:
        print(f"{fila}")

    # d
    print(f"\nd) Componentes conexas: {componentes_conexas(grafo)}\n")

    # e
    print("\ne) El grafo es conexo\n") if es_conexo(grafo) else print("e) El grafo no es conexo\n")

if __name__ == '__main__':
    main()
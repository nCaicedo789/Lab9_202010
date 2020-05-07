import config as cf
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime
from ADT import queue as q
from DataStructures import adjlist as ga
import math

def compareByKey (key, element):

    return  (key == element['key'] )

def depth_first_search(Graph, Mapa_de_marcar, node):
    valor={'nodo':node, 'stado':True, 'predecesor':None}
    map.put(Mapa_de_marcar,valor['nodo'],valor)
    list_ad=g.adjacents(Graph,node)
    for i in range (1,lt.size(list_ad)+1):
        li_node=lt.getElement(list_ad,i)
        if not map.contains(Mapa_de_marcar,li_node):
            record={'nodo':li_node, 'stado':True, 'predecesor':node}
            map.put(Mapa_de_marcar,record['nodo'],record)
            depth_first_search(Graph, Mapa_de_marcar, li_node)

def newBFS(graph, source):
    """
    Crea una busqueda BFS para un grafo y un vertice origen
    """
    prime = 11000
    search={'graph':graph, 's':source, 'visitedMap':None}
    search['visitedMap'] = map.newMap(prime, maptype='PROBING', comparefunction=compareByKey)
    map.put(search['visitedMap'],source, {'marked':True,'edgeTo':None,'nodo':source})
    bfs(search, source)
    return search

def bfs (search, source):
    queue = q.newQueue()
    q.enqueue(queue, source)
    while not (q.isEmpty(queue)):
        v = q.dequeue (queue)
        list_ad=g.adjacents(search['graph'],v)
        for i in range (1,(lt.size(list_ad)+1)):
            w=lt.getElement(list_ad,i)
            if map.get(search['visitedMap'],w) == None:
                map.put(search['visitedMap'],w, {'marked':True,'edgeTo':None,'nodo':w})
                q.enqueue(queue, w)

        # Loop v's adjacent vertices with w
        # If w has not visited 
        # Visit w 
        # Enqueue w


import config
from DataStructures import edge as e
from DataStructures import listiterator as it
from ADT import list as lt
from ADT import indexminpq as minpq
from ADT import map as map
from ADT import graph as g
from ADT import stack as stk
import math


def newDijkstra(graph, s):
    """
    Crea una busqueda Dijkstra para un digrafo y un vertice origen
    """
    prime = nextPrime (g.numVertex(graph) * 2)
    search = {'graph':graph, 's':s, 'visitedMap':None, 'minpq':None}
    search['visitedMap'] = map.newMap(numelements=prime, maptype='PROBING', comparefunction=graph['comparefunction'])
    vertices = g.vertices (graph)
    itvertices = it.newIterator (vertices)
    while (it.hasNext (itvertices)):
        vert =  it.next (itvertices)
        map.put (search['visitedMap'], vert, {'marked':False,'edgeTo':None,'distTo':math.inf})
    map.put(search['visitedMap'], s, {'marked':True,'edgeTo':None,'distTo':0})
    pq = minpq.newIndexMinPQ(g.numVertex(graph), comparenames)
    search['minpq'] = pq
    minpq.insert(search['minpq'], s, 0)
    while not minpq.isEmpty(search['minpq']):
        v = minpq.delMin(pq)
        if not g.containsVertex(graph,v):
            raise Exception("Vertex ["+v+"] is not in the graph")
        v_list=g.adjacentEdges(v)
        for i in range(1, lt.size(v_list)+1):
            enlace= lt.getElement(v_list,i)
            relax(search, enalace)
        # obtener los enlaces adjacentes de v
        # Iterar sobre la lista de enlaces
        # Relajar (relax) cada enlace
    return search


def relax(search, edge):
    v = e.either(edge)
    w = e.other(edge, v)
    visited_v = map.get(search['visitedMap'], v)['value']
    visited_w = map.get(search['visitedMap'], w)['value']
    if visited_w['distTo'] > (visited_v['distTo'] + e.weight(edge)):
        distToW = visited_v['distTo'] + e.weight(edge)
        map.put(search['visitedMap'], w, {'marked':True,'edgeTo':edge,'distTo':distToW})
        if minpq.contains(search['minpq'], w): 
            minpq.decreasePriority(search['minpq'], w, distToW)
        else:
            minpq.insert(search['minpq'], w, distToW)
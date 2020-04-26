import config
from DataStructures import edge as e
from DataStructures import listiterator as it
from DataStructures import mapMinPQ as mapq
from ADT import map as map
from ADT import graph as g
from ADT import stack as stk
import math


def comparenames (searchname, element):
    return (searchname == element['key'])

def newDijkstra(graph, s):
    """
    Crea una busqueda Dijkstra para un digrafo y un vertice origen s
    """
    prime = nextPrime (g.numVertex(graph) * 2)
    search = {'graph':graph, 's':s, 'visitedMap':None, 'mapq':None}
    search['visitedMap'] = map.newMap(numelements=prime, maptype='PROBING', comparefunction=graph['comparefunction'])
    map.put(search['visitedMap'], s, {'marked':True,'edgeTo':None,'distTo':0})
    pq = mapq.newMapMinPQ(g.numVertex(graph), comparenames)
    search['mapq'] = pq
    mapq.insert(search['mapq'], s, 0)
    while not mapq.isEmpty(search['mapq']):
        pass
        # Obtain the min vertex v from mapq
        # For each v's adjacent edge e
        #   relax e
    return search


def relax(search, edge):
    v = e.either(edge)
    w = e.other(edge, v)
    visited_v = map.get(search['visitedMap'], v)['value']
    visited_w = map.get(search['visitedMap'], w)
    if visited_w is None or (visited_w['value']['distTo'] > visited_v['distTo'] + e.weight(edge)):
        pass
        # Record w's dist as v's dist + edge's weight
        # Record edge as w's predecesor
        # If w in mapq
        #   decrease priority of w in pq
        # Else
        #   insert w, dist in mapq


def distTo(search, v):
    visited_v = map.get(search['visitedMap'], v)
    if visited_v==None:
        return float('inf')
    return visited_v['value']['distTo']

def hasPathTo(search, v):
    return map.get(search['visitedMap'], v) != None

def pathTo(search, v):
    if hasPathTo(search, v)==False:
        return None
    path = stk.newStack()
    while v != search['s']:
        visited_v = map.get(search['visitedMap'],v)['value']
        edge = visited_v['edgeTo']
        stk.push(path, edge)
        v = e.either(edge)
    return path

# Function to return the smallest  
# prime number greater than N 
# # This code is contributed by Sanjit_Prasad  

def isPrime(n):
    # Corner cases  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if(n % 2 == 0 or n % 3 == 0): 
        return False
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
    return True

def nextPrime(N): 
    # Base case  
    if (N <= 1): 
        return 2
    prime = N 
    found = False
    # Loop continuously until isPrime returns  
    # True for a number greater than n  
    while(not found): 
        prime = prime + 1
        if(isPrime(prime) == True): 
            found = True
    return prime 


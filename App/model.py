"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import Dfs_Bfs as dbs
from DataStructures import dijkstra as dj
from datetime import datetime

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    libgraph = g.newGraph(7235,compareByKey,directed=True)
    rgraph = g.newGraph(111353,compareByKey)
    prime = 111353 * 2
    marcas_dfs= map.newMap(11000, maptype='PROBING',comparefunction=compareByKey)
    path_dfs=lt.newList()
    catalog = {'librariesGraph':libgraph, 'delayGraph':rgraph, 'visitedMap':None, 'marcas_dfs':marcas_dfs, 'marcas_bfs':None, 'path_dfs':path_dfs}
    catalog['visitedMap'] = map.newMap(prime, maptype='PROBING',comparefunction=compareByKey)    
    return catalog


def addLibraryNode (catalog, row):
    """
    Adiciona un nodo para almacenar una biblioteca
    """
    if not g.containsVertex(catalog['librariesGraph'], row['SOURCE']):
        g.insertVertex (catalog['librariesGraph'], row['SOURCE'])
    if not g.containsVertex(catalog['librariesGraph'], row['DEST']):
        g.insertVertex (catalog['librariesGraph'], row['DEST'])
    if not g.containsVertex(catalog['delayGraph'], row['SOURCE']):
        g.insertVertex (catalog['delayGraph'], row['SOURCE'])
    if not g.containsVertex(catalog['delayGraph'], row['DEST']):
        g.insertVertex (catalog['delayGraph'], row['DEST'])

def addLibraryEdge  (catalog, row):
    """
    Adiciona un enlace entre bibliotecas
    """
    g.addEdge (catalog['librariesGraph'], row['SOURCE'], row['DEST'], float(row['ARRIVAL_DELAY']))
    g.addEdge (catalog['delayGraph'], row['SOURCE'], row['DEST'])


def countNodesEdges (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de bibliotecas
    """
    nodes = g.numVertex(catalog['librariesGraph'])
    edges = g.numEdges(catalog['librariesGraph'])

    return nodes,edges

def getShortestPath (catalog, source, dst):
    """
    Retorna el camino de menor costo entre vertice origen y destino, si existe 
    """
    search=dj.newDijkstra(catalogo['librariesGraph'],source)
    mapa= search['visitedMap']
    lista=lt.newList()
    camino= path(mapa,lista,source,dst)
    # ejecutar Dijkstra desde source
    # obtener el camino hasta dst
    # retornar el camino
    return camino

def path(mapa,lista, source, dst):
    if source == dst:
        return lista
    vertice= map.get(mapa, source)
    anterior= vertice['edgeTo']
    lt.addFirst(lista, anterior)
    path(mapa,lista,anterior,dst)
    
# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  


def depth_first_search(catalog,node):
    valor={'nodo':node, 'stado':True, 'predecesor':None}
    map.put(catalog['visitedMap'],valor['nodo'],valor)
    list_ad=g.adjacents(catalog['delayGraph'],node)
    for i in range (1,lt.size(list_ad)+1):
        li_node=lt.getElement(list_ad,i)
        if not map.contains(catalog['visitedMap'],li_node):
            record={'nodo':li_node, 'stado':True, 'predecesor':node}
            map.put(catalog['visitedMap'],record['nodo'],record)
            depth_first_search(catalog,li_node)

def countConnectedComponents (catalog):
    """
    Retorna la cantidad de componentes conectados del grafo de revisiones
    """
    counter=0
    list_nodes=g.vertices(catalog['delayGraph'])
    total= g.numVertex(catalog['delayGraph'])
    for i in range(1,lt.size(list_nodes)+1):
        node=lt.getElement(list_nodes,i)
        if not map.contains(catalog['visitedMap'],node):
            depth_first_search(catalog,node)
            counter+=1
        sub_total=map.size(catalog['visitedMap'])
        if sub_total==total:
            break
    return counter

def getPath (catalog, source, dst):
    """
    Retorna el camino, si existe, entre vertice origen y destino
    """
    mapa= catalog['marcas_dfs']
    grafo= catalog['reviewGraph']
    path= catalog['path_dfs']
    if dst==source:
        return path
    if map.size(mapa)==0:
        dbs.depth_first_search(grafo,mapa,source)

    nod_bus =map.get(mapa, dst)
    if nod_bus != None:
        new_node= nod_bus['predecesor']
        lt.addFirst(path,new_node)
        getPath(catalog,source,new_node)

    def carga_bfs(catalog, source):
    search= dbs.newBFS(catalog['reviewGraph'], source)
    catalog['marcas_bfs']= search['visitedMap']

def path_small(catalog, source, dst):

    mapa= catalog['marcas_bfs']
    path= catalog['path_bfs']
    if dst==source:
        return path
    if mapa == None:
        carga_bfs(catalog, source)
    nod_bus=map.get(mapa, dst) 
    if nod_bus != None:
        new_node= nod_bus['predecesor']
        lt.addFirst(path,new_node)
        path_small(catalog,source,new_node)
    else:
        return None
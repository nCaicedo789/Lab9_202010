Vytis Karanauskas 20191296
Nicolás Caicedo 201820789

1. ¿Cómo se utilizaron las estructuras de datos vistas en clase?
En este reto utilizamos grafos, mapas ordenados y listas. Se utilizo un grafo no dirigido para
resolver los primeros 3 requerimientos y en el req 4 utilizamos un grafo dirigido con peso.
Adicionalmente para la la implementación de bfs, dfs y dijkstra se utilizaron tablas de hash para tomar registro de los nodos visitados.
Utilizadon las tablas de hash se definieron los recoridos entre vertices, los cuales se cargaron en una lista simplemente encadena.

2. ¿Cuáles campos del archivo seleccionaron para definir los enlaces y nodos de los árboles, y como generaliza esta solución a otros tipos de problemas similares?
Como vertices tomamos los aeropuertos junto a la fecha y los enlaces entre estos eran los vuelos entre cada aeropueto. Para el requerimiento 4 se utilizo un grafo dirigido el
cual adiconalmente tenia como peso el tiempo de retraso de cada vuelo.
Esta implementacion se puede generalizar a otros problemas que involucre el viaje entre puntos especificos.

3. ¿Qué ventajas ofrecen los grafos sobre las estructuras de datos vistas anteriormente?
Los grafos permiten mostrar las conecciones entre elementos, lo cual es necesario para este problema. Las estructuras vistas anteriormente son utiles y algunas fuern utilizados,
pero por si estas no pueden mostrar relaciones entre elementos de manera concisa.

4. ¿En que escenarios recomendaría utilizar grafos dirigidos o no dirigidos?
Los grafos no dirigidos son mas pertinentes cuando el problema a resolver solo require las conecciones entre elementos. En cuanto a grafos dirigidos estos son pertinentes 
si el proble a resolver involucra movimiento de un elememto a otro, ya que uno puede ir de vertice A a B ó B a A.

5. ¿A qué conclusiones llegan a partir de analizar los resultados de complejidad temporal entre grafos dirigidos, no dirigidos y sus recorridos?
Los recoridos de grafos dirigidos tiene mayor complejidad temporal, por lo cual si el problema no require de su uso es mas pertinete usar grafos no dirigidos.
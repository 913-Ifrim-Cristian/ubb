import math

from exceptions import *
from random import randrange
from copy import deepcopy
from queue import Queue
from heapq import heappush, heappop
from math import inf


class Graph:

    def __init__(self, n=0, m=0):

        self.__vertices = set()
        self.__outbound_neighbours = dict()
        self.__inbound_neighbours = dict()
        self.__cost = dict()

        self._generate_graph(n, m)

    def _generate_graph(self, n, m):
        
        """
        Generates a random graph with n vertices and m edges
        """

        for vertex in range(n):
            self.add_vertex(vertex)

        for edge in range(m):
            first_vertex = randrange(n)
            second_vertex = randrange(n)

            while self.is_edge(first_vertex, second_vertex):
                first_vertex = randrange(n)
                second_vertex = randrange(n)

            self.add_edge(first_vertex, second_vertex, randrange(1000000))

    def vertices_iterator(self):
        """
        Returns an iterator to the set of vertices.
        """
        if len(self.__vertices) == 0:
            raise EdgeError("ERROR: The graph does not have any vertices!")

        for vertex in self.__vertices:
            yield vertex

    def outbound_neighbours_iterator(self, vertex):
        """
        Returns an iterator to the set of (outbound) neighbours of a vertex.
        """
        if not self.is_vertex(vertex):
            raise VertexError("ERROR: Invalid vertex.")

        for neighbour in self.__outbound_neighbours[vertex]:
            yield neighbour

    def inbound_neighbours_iterator(self, vertex):
        """
        Returns an iterator to the set of (inbound) neighbours of a vertex.
        """
        if not self.is_vertex(vertex):
            raise VertexError("ERROR: Invalid vertex.")

        for neighbour in self.__inbound_neighbours[vertex]:
            yield neighbour

    def edges_iterator(self):
        """
        Returns an iterator to the set of edges.
        """
        if len(self.__cost) == 0:
            raise EdgeError("ERROR: The graph does not have any edges!")

        for key, value in self.__cost.items():
            yield key[0], key[1], value

    def is_vertex(self, vertex):
        """
        Returns True if vertex belongs to the graph.
        """
        return vertex in self.__vertices

    def is_edge(self, first_vertex, second_vertex):
        """
        Returns True if the edge first_vertex-second_vertex belongs to the graph.
        """
        return first_vertex in self.__outbound_neighbours and second_vertex in self.__outbound_neighbours[first_vertex]

    def count_vertices(self):
        """
        Returns the number of vertices in the graph.
        """
        return len(self.__vertices)

    def count_edges(self):
        """
        Returns the number of edges in the graph.
        """
        return len(self.__cost)

    def in_degree(self, vertex):
        """
        Returns the number of edges with the endpoint vertex.
        """
        if vertex not in self.__inbound_neighbours:
            raise VertexError("ERROR: The specified vertex does not exist.")

        return len(self.__inbound_neighbours[vertex])

    def out_degree(self, vertex):
        """
        Returns the number of edges with the start point vertex.
        """
        if vertex not in self.__outbound_neighbours:
            raise VertexError("ERROR: The specified vertex does not exist.")

        return len(self.__outbound_neighbours[vertex])

    def get_edge_cost(self, first_vertex, second_vertex):
        """
        Returns the cost of an edge if it exists.
        """
        if (first_vertex, second_vertex) not in self.__cost:
            raise EdgeError("ERROR: The specified edge does not exist.")

        return self.__cost[(first_vertex, second_vertex)]

    def set_edge_cost(self, first_vertex, second_vertex, new_cost):
        """
        Sets the cost of an edge in the graph if it exists.
        """
        if (first_vertex, second_vertex) not in self.__cost:
            raise EdgeError("ERROR: The specified edge does not exist.")

        self.__cost[(first_vertex, second_vertex)] = new_cost

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        """
        if self.is_vertex(vertex):
            raise VertexError("ERROR: The specified vertex already exists.")

        self.__vertices.add(vertex)
        self.__outbound_neighbours[vertex] = set()
        self.__inbound_neighbours[vertex] = set()

    def add_edge(self, first_vertex, second_vertex, edge_cost=0):
        """
        Adds an edge to the graph.
        """
        if self.is_edge(first_vertex, second_vertex):
            raise EdgeError("ERROR: The specified edge already exists")

        if not self.is_vertex(first_vertex) or not self.is_vertex(second_vertex):
            raise EdgeError("ERROR: The vertices on the edge do not exist.")

        self.__outbound_neighbours[first_vertex].add(second_vertex)
        self.__inbound_neighbours[second_vertex].add(first_vertex)
        self.__cost[(first_vertex, second_vertex)] = edge_cost

    def remove_edge(self, first_vertex, second_vertex):
        """
        Removes an edge from the graph.
        """
        if not self.is_edge(first_vertex, second_vertex):
            raise EdgeError("ERROR: The specified edge does not exist.")

        del self.__cost[(first_vertex, second_vertex)]

        self.__outbound_neighbours[first_vertex].remove(second_vertex)
        self.__inbound_neighbours[second_vertex].remove(first_vertex)

    def remove_vertex(self, vertex):
        """
        Removes a vertex from the graph.
        """
        if not self.is_vertex(vertex):
            raise VertexError("ERROR: The specified vertex does not exit.")

        edges_to_remove_list = []
        for vtx in self.__outbound_neighbours[vertex]:
            edges_to_remove_list.append(vtx)

        for vtx in edges_to_remove_list:
            self.remove_edge(vertex, vtx)

        edges_to_remove_list = []
        for vtx in self.__inbound_neighbours[vertex]:
            edges_to_remove_list.append(vtx)

        for vtx in edges_to_remove_list:
            self.remove_edge(vtx, vertex)

        del self.__outbound_neighbours[vertex]
        del self.__inbound_neighbours[vertex]

        self.__vertices.remove(vertex)

    def copy(self):
        """
        Returns a deepcopy of the graph.
        """
        return deepcopy(self)

    def tarjan(self, vertex, sorted_list, fully_processed, in_process):
        """
        Function for sorting the graph topologically.
        :param vertex: the current vertex of the graph
        :param sorted_list: the list with the topological order
        :param fully_processed: vertices that are fully processed
        :param in_process: vertices that are in process
        :return: True if the vertex is valid, False otherwise
        """
        in_process.add(vertex)  # add to the set of processing vertices the current vertex
        for other_vertex in self.inbound_neighbours_iterator(vertex):  # process all inbound vertices of current vertex
            if other_vertex in in_process:
                return False
            elif other_vertex not in fully_processed:  # if one of the inbound neighbors of the current is not processed
                # process it and its inbound vertices
                ok = self.tarjan(other_vertex, sorted_list, fully_processed, in_process)
                if not ok:  # if we get to a vertex that is in process again we have a loop, so the graph is not a DAG
                    # we return False and the algorithm stops
                    return False
        in_process.remove(vertex)
        sorted_list.append(vertex)  # add the processed vertex to the topological sort
        fully_processed.add(vertex)  # add the processed vertex to the set of all the processed vertices
        return True

    def base_topo_sort(self):
        """
        Helper function for the topological sort.
        :return:the topological sort of the graph
        """
        sorted_list = []  # list for the topological sort
        fully_processed = set()  # set for all the processed vertices
        in_process = set()  # set for the vertices that are in process
        for vertex in self.vertices_iterator():  # go through all the vertices of the graph
            if vertex not in fully_processed:
                ok = self.tarjan(vertex, sorted_list, fully_processed, in_process)
                if not ok:  # the graph is not a DAG so we return None; it does not have a topological sort
                    sorted_list.clear()
                    return None
        return sorted_list

    def highest_cost_path(self, vertex_begin, vertex_end):
        """
        Function to compute the highest cost path from vertex begin to vertex end.
        :param vertex_begin: the beginning of the path
        :param vertex_end: the end of the path
        :return: the distance(cost) of the path and the dictionary of previous vertices
        """
        topological_order_list = self.base_topo_sort()  # get the topological sort
        dist = {}  # dictionary of costs from the source
        prev = {}  # dictionary that stores for each vertex the previous vertex from the path
        m_inf = float('-inf')
        for vertex in topological_order_list:  # initialize all the values of the dictionaries
            dist[vertex] = m_inf
            prev[vertex] = -1
        dist[vertex_begin] = 0

        for vertex in topological_order_list:  # go through all the vertices
            if vertex == vertex_end:  # stop the loop if we get to the end vertex
                break
            for other_vertex in self.outbound_neighbours_iterator(vertex):  # parse outbound neighbors of the current
                if dist[other_vertex] < dist[vertex] + self.__cost[(vertex, other_vertex)]:
                    # if the cost is greater update the dictionary
                    dist[other_vertex] = dist[vertex] + self.__cost[(vertex, other_vertex)]
                    prev[other_vertex] = vertex

        return dist[vertex_end], prev


def read_file(file_name):
    with open(file_name, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(n)
        for iterator in range(m):
            first_vertex, second_vertex, cost = map(int, file.readline().split())
            g.add_edge(first_vertex, second_vertex, cost)

    return g


def write_file(file_name, g):
    with open(file_name, "w") as file:
        file.write(f"{g.count_vertices()} {g.count_edges()}\n")
        for vertex in g.vertices_iterator():
            for neighbour in g.outbound_neighbours_iterator(vertex):
                file.write(f"{vertex} {neighbour} {g.get_edge_cost(vertex, neighbour)}\n")


def shortest_path(g, s, t):

    """
    Gets the shortest path from a starting vertex to a ending vertex of a given graph
    :param g: the given graph
    :param s: starting vertex
    :param t: ending vertex
    :return: the list representing the shortest path from starting vertex to ending vertex
    """

    prev = dict()
    prev[s] = None
    q = Queue()
    q.put(s)
    arrived = False
    while not q.empty() and not arrived:
        first = q.get()
        for neighbor in g.outbound_neighbours_iterator(first):
            if neighbor not in prev.keys():
                prev[neighbor] = first
                q.put(neighbor)

                if neighbor == t:
                    arrived = True
                    break
    path = []
    vertex = t
    path.append(t)
    if t not in prev.keys():
        raise ValueError(f"ERROR: There is no path between {s} and {t}.")

    while vertex != s:
        path.append(prev[vertex])
        vertex = prev[vertex]

    path.reverse()

    return path


def lowest_cost_walk(g, start_vertex, end_vertex):
    if not g.is_vertex(start_vertex) or not g.is_vertex(end_vertex):
        raise ValueError(f"ERROR: Invalid vertices!")

    distance = [inf for _ in g.vertices_iterator()]
    prev = [None for _ in g.vertices_iterator()]

    distance[start_vertex] = 0

    for _ in range(g.count_vertices() - 1):
        for u, v, c in g.edges_iterator():
            if distance[u] + c < distance[v]:
                distance[v] = distance[u] + c
                prev[v] = u

    for u, v, c in g.edges_iterator():
        if distance[u] + c < distance[v]:
            raise ValueError(f"Graph contains a negative-weight cycle")

    return distance, prev

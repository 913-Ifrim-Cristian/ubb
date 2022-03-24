from exceptions import *
from random import randrange
from copy import deepcopy

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
        for vertex in self.__vertices:
            yield vertex

    def outbound_neighbours_iterator(self, vertex):
        """
        Returns an iterator to the set of (outbound) neighbours of a vertex.
        """
        if not self.is_vertex(vertex):
            raise VertexError("Invalid vertex.")

        for neighbour in self.__outbound_neighbours[vertex]:
            yield neighbour

    def inbound_neighbours_iterator(self, vertex):
        """
        Returns an iterator to the set of (inbound) neighbours of a vertex.
        """
        if not self.is_vertex(vertex):
            raise VertexError("Invalid vertex.")

        for neighbour in self.__inbound_neighbours[vertex]:
            yield neighbour

    def edges_iterator(self):
        """
        Returns an iterator to the set of edges.
        """
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
            raise VertexError("The specified vertex does not exist.")

        return len(self.__inbound_neighbours[vertex])

    def out_degree(self, vertex):
        """
        Returns the number of edges with the start point vertex.
        """
        if vertex not in self.__outbound_neighbours:
            raise VertexError("The specified vertex does not exist.")

        return len(self.__outbound_neighbours[vertex])

    def get_edge_cost(self, first_vertex, second_vertex):
        """
        Returns the cost of an edge if it exists.
        """
        if (first_vertex, second_vertex) not in self.__cost:
            raise EdgeError("The specified edge does not exist.")

        return self.__cost[(first_vertex, second_vertex)]

    def set_edge_cost(self, first_vertex, second_vertex, new_cost):
        """
        Sets the cost of an edge in the graph if it exists.
        """
        if (first_vertex, second_vertex) not in self.__cost:
            raise EdgeError("The specified edge does not exist.")

        self.__cost[(first_vertex, second_vertex)] = new_cost

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        """
        if self.is_vertex(vertex):
            raise VertexError("Cannot add a vertex which already exists.")

        self.__vertices.add(vertex)
        self.__outbound_neighbours[vertex] = set()
        self.__inbound_neighbours[vertex] = set()

    def add_edge(self, first_vertex, second_vertex, edge_cost=0):
        """
        Adds an edge to the graph.
        """
        if self.is_edge(first_vertex, second_vertex):
            raise EdgeError("The specified edge already exists")

        if not self.is_vertex(first_vertex) or not self.is_vertex(second_vertex):
            raise EdgeError("The vertices on the edge do not exist.")

        self.__outbound_neighbours[first_vertex].add(second_vertex)
        self.__inbound_neighbours[second_vertex].add(first_vertex)
        self.__cost[(first_vertex, second_vertex)] = edge_cost

    def remove_edge(self, first_vertex, second_vertex):
        """
        Removes an edge from the graph.
        """
        if not self.is_edge(first_vertex, second_vertex):
            raise EdgeError("The specified edge does not exist.")

        del self.__cost[(first_vertex, second_vertex)]

        self.__outbound_neighbours[first_vertex].remove(second_vertex)
        self.__inbound_neighbours[second_vertex].remove(first_vertex)

    def remove_vertex(self, vertex):
        """
        Removes a vertex from the graph.
        """
        if not self.is_vertex(vertex):
            raise VertexError("Cannot remove a vertex which doesn't exist.")

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

from graph import *


class UI:
    def __init__(self):
        self.graph = Graph()

    def empty_graph(self):
        self.graph = Graph()
        print("SUCCESS: Graph created successfully!")

    def only_vertices_graph(self):
        n = int(input("Please enter the number of vertices: "))

        self.graph = Graph(n)
        print("SUCCESS: Graph created successfully!")

    def random_graph(self):
        n = int(input("Please enter the number of vertices: "))
        m = int(input("Please enter the number of edges: "))

        self.graph = Graph(n, m)
        print("SUCCESS: Graph created successfully!")

    def add_vertex(self):
        n = int(input("Please enter the number of the vertex you want to add: "))

        self.graph.add_vertex(n)
        print(f"SUCCESS: Vertex no. {n} added successfully!")

    def add_edge(self):
        first_vertex = int(input("Please enter the first vertex of the edge: "))
        second_vertex = int(input("Please enter the second vertex of the edge: "))
        cost = int(input("Please enter the cost of the edge: "))

        self.graph.add_edge(first_vertex, second_vertex, cost)
        print(f"SUCCESS: Edge: {first_vertex}->{second_vertex} added with cost: {cost} successfully!")

    def remove_vertex(self):
        n = int(input("Please enter the vertex you wish to remove: "))

        self.graph.remove_vertex(n)
        print(f"SUCCESS: Vertex {n} was successfully removed with all it's edges.")

    def remove_edge(self):
        first_vertex = int(input("Please enter the first vertex of the edge: "))
        second_vertex = int(input("Please enter the second vertex of the edge: "))

        self.graph.remove_edge(first_vertex, second_vertex)
        print(f"SUCCESS: Edge: {first_vertex}->{second_vertex} was successfully removed!")

    def change_edge(self):
        first_vertex = int(input("Please enter the first vertex of the edge: "))
        second_vertex = int(input("Please enter the second vertex of the edge: "))
        cost = int(input("Please enter the cost of the edge: "))

        self.graph.set_edge_cost(first_vertex, second_vertex, cost)
        print(f"SUCCESS: The cost of the Edge: {first_vertex}->{second_vertex} has been updated to: {cost}.")

    def print_edge(self):
        first = int(input("Please enter the first vertex of the edge: "))
        second = int(input("Please enter the second vertex of the edge: "))

        cost = self.graph.get_edge_cost(first, second)

        print(f"The cost of Edge: {first}->{second} is {cost}.")

    def in_degree(self):
        n = int(input("Please enter vertex for which you wish to find the in degree: "))

        print(f"The in degree of vertex: {n} is {self.graph.in_degree(n)}.")

    def out_degree(self):
        n = int(input("Please enter the vertex for which you wish to find the out degree: "))

        print(f"The in degree of vertex: {n} is {self.graph.out_degree(n)}.")

    def number_of_vertices(self):
        print(f"The number of vertices in the graph is: {self.graph.count_vertices()}.")

    def number_of_edges(self):
        print(f"The number of edges in the graph is: {self.graph.count_edges()}.")

    def is_vertex(self):
        n = int(input("Please enter the vertex: "))

        if self.graph.is_vertex(n):
            print(f"Vertex: {n} is in the graph.")
        else:
            print(f"Vertex {n} does not belong to the graph.")

    def is_edge(self):
        first = int(input("Please enter the first vertex of the edge: "))
        second = int(input("Please enter the second vertex of the edge: "))

        if self.graph.is_edge(first, second):
            print(f"Edge: {first}->{second} does exist.")
        else:
            print(f"Edge: {first}->{second} doesn't exist.")

    def print_vertex_list(self):
        for vertex in self.graph.vertices_iterator():
            print(vertex, end=", ")
        print()

    def print_outbound_neighbour_list(self):
        n = int(input("Please enter the vertex you wish to find the outbound neighbours for: "))

        found = False
        for vertex in self.graph.outbound_neighbours_iterator(n):
            print(vertex, end=", ")
            found = True

        if not found:
            print(f"ERROR: Vertex {n} has no neighbours.")

        print()

    def print_inbound_neighbour_list(self):
        n = int(input("Please enter the vertex you wish to find inbound neighbours for: "))

        found = False
        for vertex in self.graph.inbound_neighbours_iterator(n):
            print(vertex, end=", ")
            found = True

        if not found:
            print(f"ERROR: Vertex {n} has no inbound neighbours.")

        print()

    def print_edges(self):
        found = False
        for edge in self.graph.edges_iterator():
            print(f"Edge: {edge[0]}->{edge[1]} with the cost: {edge[2]}.")
            found = True

        if not found:
            print("ERROR: No edges in the graph.")

    def read_file(self):
        path = input("Type the file from which you wish to read: ")

        self.graph = read_file(path)

        print("SUCCESS: Graph successfully loaded.")

    def write_file(self):
        path = input("Type the file you wish to write to: ")

        write_file(path, self.graph)

        print("SUCCESS: Graph successfully saved to file.")

    def _print_menu(self):
        print("---------- GENERATE A GRAPH ----------")
        print("1. Generate an empty graph")
        print("2. Generate a graph with n vertices")
        print("3. Generate a graph with n vertices and m random edges")
        print("---------- MODIFY THE GRAPH ----------")
        print("4. Add a vertex")
        print("5. Add an edge")
        print("6. Remove a vertex")
        print("7. Remove an edge")
        print("8. Change the cost of an edge")
        print("---------- DETAILS OF THE GRAPH ----------")
        print("9. Print the cost of an edge")
        print("10. Print the in degree of a vertex")
        print("11. Print the out degree of a vertex")
        print("12. Print the number of vertices")
        print("13. Print the number of edges")
        print("14. Check whether a vertex belongs to the graph")
        print("15. Check whether an edge belongs to the graph")
        print("16. Print the list of vertices")
        print("17. Print the list of outbound neighbours of a vertex")
        print("18. Print the list of inbound neighbours of a vertex")
        print("19. Print the list of edges")
        print("---------- READ/WRITE A GRAPH ----------")
        print("20. Reads the graph from a file")
        print("21. Writes the graph to a file")
        print("---------- EXIT ----------")
        print("0. Exit")

    def start(self):
        commands_dict = {
            "1": self.empty_graph,
            "2": self.only_vertices_graph,
            "3": self.random_graph,
            "4": self.add_vertex,
            "5": self.add_edge,
            "6": self.remove_vertex,
            "7": self.remove_edge,
            "8": self.change_edge,
            "9": self.print_edge,
            "10": self.in_degree,
            "11": self.out_degree,
            "12": self.number_of_vertices,
            "13": self.number_of_edges,
            "14": self.is_vertex,
            "15": self.is_edge,
            "16": self.print_vertex_list,
            "17": self.print_outbound_neighbour_list,
            "18": self.print_inbound_neighbour_list,
            "19": self.print_edges,
            "20": self.read_file,
            "21": self.write_file
        }

        while True:
            self._print_menu()

            option = input(">>> ")
            if option == "0":
                break

            if option in commands_dict:
                try:
                    commands_dict[option]()
                except Exception as e:
                    print(e)

            else:
                print("ERROR: Invalid choice.")

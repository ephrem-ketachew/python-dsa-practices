class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            if v2 not in self.adj_list[v1] and v1 not in self.adj_list[v2]:
                self.adj_list[v1].append(v2)
                self.adj_list[v2].append(v1)
                return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            if v2 in self.adj_list[v1] and v1 in self.adj_list[v2]:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            
            # try:
            #     self.adj_list[v1].remove(v2)
            #     self.adj_list[v2].remove(v1)
            # except ValueError:
            #     pass
            
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for v in self.adj_list[vertex]:
                # self.remove_edge(v, vertex)
                if v in self.adj_list and vertex in self.adj_list[v]:
                    self.adj_list[v].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
            
my_graph = Graph()
my_graph.add('A')
my_graph.add('B')
my_graph.add('C')
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'C')
# my_graph.remove_edge('B', 'C')
my_graph.remove_vertex('C')
my_graph.print_graph()
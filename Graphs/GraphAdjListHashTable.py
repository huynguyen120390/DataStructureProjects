class Undirected_Graph_Adjlist_Hashtable:
    def __init__(self):
        self.graph = {}
        self.nodeNum = 0

    def add_vertex(self,node):
        if node not in self.graph:
            self.graph[node] = []
            self.nodeNum += 1
        else:
            raise "Conflict Node"
        

    def add_edge(self,node1,node2):
        if node1 not in self.graph: 
            raise f"No Node {node1} to connect"
        elif node2 not in self.graph:
            raise f"No Node {node2} to connect"
        else:
            if node2 in self.graph[node1]:
                raise "Conflict Edge"
            else:
                self.graph[node1].append(node2)
                self.graph[node2].append(node1)


    def display(self):
        for v in self.graph:
            print(f"{v} --> ",end="")
            for v2 in self.graph[v]:
                print(f"{v2} ",end="")
            print("")
        

    
if __name__ == "__main__":
    graph = Undirected_Graph_Adjlist_Hashtable()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,1)
    graph.add_edge(1,4)
    graph.add_edge
    graph.display()

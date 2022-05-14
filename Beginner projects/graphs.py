
#ways of representing
#Adjacency Matrix
#Adjacency List
#Graphs are used to solve many real-life problems. Graph theory is used to find shortest path in road or a network 3or more connection to be a cycle 1to 2 not cycle
#In mathematics, graph theory is the study of graphs,
#graphs contain cycles
#Few programming languages provide direct support for graphs as a data type
class graph:
   def __init__(self,edges):#its def innit becasue its a method
       self.edges = edges
       
        
#this graph has six nodes (A-F) and eight arcs.
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
print(graph)

#looks to complicated for to to code now 

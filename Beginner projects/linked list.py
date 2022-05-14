#Since the difference in memory usage between lists and linked lists is so insignificant, it’s better if you focus on their performance differences when it comes to time complexity.
#array only better if want to acces 1 element 
class node:
    def __init__(self,data=None,nextNode=None):#node on have 2 data data and pointer
        self.data = data
        self.nextNode = None#noe by default we update later
        
class linked_list:
    def __int__(self):
        self.head = None
        #The only information you need to store for a linked list is where the list starts

    def insert(self,data):
        node=node(data)
        if self.head is None:
            self.head = node
            return
#we could not code the head part seapreately but usally only really care about head
#keep track of head
        #part of ll

node1= linked_list()#only need provide 1 paramerter as second set to none
node1.head = node(10)

node2= node(20)#setting nodes data
node3= node(30)# unconnected nodes
node4= node(40)#Dont forget have to connect nodes once data set
node5= node(50)
node6= node(60)

node1.head.nextNode = node2# connecting nodes POINTERS
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
current = node2
while True:
    print (current.data, "-> ",end="")
    if current.nextNode is None:
        print ("None")
        break
    current = current.nextNode

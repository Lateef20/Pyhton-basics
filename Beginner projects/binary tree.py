#tree=! binary tree
#binary tree =! binary seach tree(AKA ordered binary tree)
#binary tree = no structure organisation
#binary search tree = Nodes children node should be: values of left child node lesser. Right child node values should be greater this allows for efficient fast sorting, searching a retrieving data.
#data in binary search tree will alwasys be larger to right of tree
#A tree whose elements have at most two children is called a binary tree.
#leaf node has no children always at/near bottom
#use an  famliy tree and tree analouge with children and leafs and root node and children nodes
#this need to code when making a tree:
#CREATE tree
#INSERT into tree #more needed to code in bst because need to set rules 
#DELETION from tree
#TRAVESERAL = access/visit each element in tree
#searching looking up paritcaulr item may or may not visit every node
#ually given array and asked to make inot bst . first array always root


#CREATE
#class for node add/initilisae with a value to node
class node():
    def __init__(self,data):#self because member of class
        self.data = data
        self.left = None
        self.right = None
        #NOT self.left = left because left and right not even defined yet
        #unlike linked list variable :next variable will be left and right
        #each node muse have Data Pointer to the left child Pointer to the right child
    def printtree(self):
        print(self.data)



#INSERT 
    def insert(self,data):
        if data == self.data:#if data already exist cannot add cannot have duplicate in bst
            return #dont need to add anything
        #this if statement stops dupicate values, i have seen some bst with duplicate values
        #this check should come after checking if empty or not  


        #first chek if there is data in the root node
        if self.data is None:
            self.data = data #if no data in root we set root here
            #if data there they we check child nodes
        else:
            if data < self.data: #less than on left. Convention to wrtie left node first
                if self.left is None: #know know its going to left we need to check if data already on left
                    self.left = node(data) #setting left child node
                else:
                    self.left.insert(data) #recurisvelkly continue to check left of tree. so now all left child sorted. if there was data we go to its left child and insert our value instead
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
            #data == value we want to inset . self.data == value in root node that we are comapring to 

#made more complicated becuase of checks we did could just be if left bigger condition then else
#why comparing node is self.data while new data is just data
            #each node muse have Data Pointer to the left child Pointer to the right child
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data),
        if self.right:
            self.right.printtree()

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:#if root node has to left child
                return str(lkpval)+" is not Found"
            return self.left.findval(lkpval)#else it does recurisve call 
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" is not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + " is found"
        
        #In-order Traversal
    def in_order(self):#no other data needed so just self
        #left
        res = []
        if self.left:
            res += self.left.in_order()
        #root 
        res.append(self.data)
        #right
        if self.right:
            res += self.right.in_order()
        return res
    def post_order(self):
        res = []
        if self.left:
            res += self.left.post_order()#recurise

        if self.right:
            res += self.right.post_order()

        res.append(self.data)
        return res
    def pre_order(self):
        res = []

        res.append(self.data)
        if self.left:
            res += self.left.post_order()#recurise

        if self.right:
            res += self.right.post_order()


        return res
root = node(10) #This becomes tree with only a root node.
root.insert(40)
root.insert(30)
root.insert(30)
root.insert(20)
root.printtree()
#print(root.findval(7))
#print(root.findval(40))
#TRAVESERAL depends on when root node vsited. leff always before right
#In-order Traversal In this traversal method, the left subtree is visited first, then the root and later the right sub-tree
#In-order traversal logic is implemented by creating an empty list
# Left -> Root -> Right

# Preorder traversal
# Root -> Left ->Right

#Post-order Traversal
# Left ->Right -> Root

print("Post order: ", root.post_order())
print("Per order: ",root.pre_order())
print("in order: ",root.in_order())
#sort why in order wrong

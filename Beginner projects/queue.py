# linear data structure FIFO
#can be implemennt as static or dynamic array

#2 implemtaion of linear queues in general as array or list
#list as item leave all items move one space so front queue always first elemnt
#with  a long queue his may require significant processing time
# with pointer and interger holding size of array and number of items currently in queue
#problem: when itme added removed space creaed at front which cannot be refilled until rear pointer to last element



#3 Implemenations for pyhton other lanugaes e.g java and c++ have 1 implemenation only
#Implementation using list
#List is a Python’s built-in data structure that can be used as a queue.
#Implementation using collections.deque #qeque = double ended queue
#Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container,
#list implemenation has downsided when using dynamic implementaion
#pyhton list versitle can bu used as stck queue and noraml list
#Implementation using queue.Queue



#Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
#Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
#Front: Get the front item from queue – Time Complexity : O(1)
#Rear: Get the last item from queue – Time Complexity : O(1)

#enqueue dequeue can be put/get =queue implementaion append/popleft (popleft when using double ended queue)  append/pop using list implemenation
#all for these implemented using function. so come after data using full stop


#im queue you cannot chose what element to remove from list?
#queue akways gives us next elemnent
#usefull when have multiple threads

import queue
#form queue import Queue#capital queue class is what we are looking for.insdie the queue module
q=queue.Queue()
q=queue.Queue(maxsize=5)
print(q.qsize())#itmes currenly in list
print(q.empty())#boolean 
print(q.full())#boolean
list1=[1,2,3,4,5]
for i in list1:
    q.put(i)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

#Cannot chose postion to get/pop will always be first item
#in Queue class queue object put and get only optional args is block and timepout(item, block=True, timeout=None) NO positional args
print("Empty: ",q.empty())#boolean
#dont know why when i try dequeue when no item in list i dont get error, program
#jsut does not finish running




#from collections import deque
#q=deque()
#q.append(10)
#q.append(100)
#q.append(1000)
#q.append(10000)
#print("Initial Queue is:",q)
#print(q.popleft())
#print(q.popleft())
#print("After Removing elements:",q)


from queue import PriorityQueue as ps
newq = ps()
#A tuple consists of a number of values separated by commas, for instance:
t=2,5
a=1,3
newq.put(t)
newq.put(a)
#what does higher priority mean they get dequeued first? Highest priorty at front/ highest priorty leaves first, no one want to be stuck in a list all day
print(newq.get())
#A typical pattern for entries is a tuple in the form: (priority_number, data).
#The lowest valued entries are retrieved first. lower = higher priority / closer to 1 higher prirty

#3 came deqeued first even though came in second becuase had hiher priority indicated by number closer to 1 . number was 1
#IMPLEMTED A PRIORTY QUEUE ALL BY MY SELF 

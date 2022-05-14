#First-In/Last-Out (FILO)
#empty()
#size()
#top() 
#push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
#pop() – Deletes the topmost element of the stack – Time Complexity: O(1

#3 method in pyhton same as queue methods
#list
#Collections.deque
#queue.LifoQueue #use but lifo makes it a staak
#singly linked list can also be used


#To start with the simpler one, you should never use list for any data structure that can be accessed by multiple threads. list is not thread-safe
#Okay, if you’re threading, you can’t use list for a stack and you probably don’t want to use deque for a stack, so how can you build a Python stack for a threaded program?
#The answer is in the queue module, queue.LifoQueue. 

#list may be familiar, but it should be avoided because it can potentially have memory reallocation issues
#uesd reverse a word and in browers
#IN STACK CAN ONLY AFFECT TOP ITEM 

from queue import LifoQueue
  
# Initializing a stack
stack = LifoQueue(maxsize=3)
  
# qsize() show the number of elements
# in the stack
print(stack.qsize())
  
# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')
  
print("Full: ", stack.full())
print("Size: ", stack.qsize())
  
# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
  
print("\nEmpty: ", stack.empty())

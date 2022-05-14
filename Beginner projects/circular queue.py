#Circular Queues are widely used and are often tested on job interviews.
#need head and rear pointer and number of element in queue
#Number of elements = Tail - Head. For instance, if Head = 2 and Tail = 5, then the number of elements will be 5 - 2 = 3
#all cirulcar queue implemented as class
#Initialize the queue, size of the queue (maxSize), head and tail pointers
#enqueue and de qeueue methods

class circular:
    def __init__(self.size):
        self.storage = [None]*size#using an array to implement
        self.head = 0
        self.tail = 0
        self

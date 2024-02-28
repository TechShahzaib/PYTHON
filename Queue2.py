import numpy as np
class Queue:
    def __init__(self):
        self.queue=np.zeros([8] , dtype=int)
        self.front=-1
        self.rear=-1
    def enqueue(self,data):
        if (self.rear==len(self.queue)-1 and self.front==0) :
            print("Queue is full") 
        if self.front==-1:
            self.front=self.rear=0
        elif self.rear==len(self.queue)-1:
            self.rear=0
        else:
            self.rear+=1
        self.queue[self.rear]=data
        print(self.queue[self.rear])
    def dequeue(self):
        if self.front==-1:
            print("Queue is empty")
        temp=self.queue[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        elif self.front==len(self.queue)-1:
            self.front=-1
        else:
            self.front+=1
        print("The removing value from the queue is",temp)

obj=Queue()
obj.enqueue(10)
obj.enqueue(26)
obj.enqueue(38)
obj.enqueue(43)
obj.enqueue(4)
obj.enqueue(7)
obj.enqueue(55)
obj.enqueue(66)
# obj.dequeue()


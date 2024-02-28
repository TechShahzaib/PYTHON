class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)
    # remove value from index 0 in front 

    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[-1]

q=Queue()
q.enqueue(1)   
q.enqueue(2) 
q.enqueue(3) 
q.enqueue(4)  

print("Front value:" ,q.front())
print("Rear value:" ,q.rear())

q.dequeue()
print("Front value:" ,q.front())
print("Rear value:" ,q.rear())


q.dequeue()
print("Front value:" ,q.front())
print("Rear value:" ,q.rear())
class Stack:
    def __init__(self):
        self.stackl=[]

    def push(self,data):
        self.stackl.append(data)

    def Pop(self):
        if len(self.stackl)==0:
            print("Stack is empty!")
        else:
            self.stackl.pop()

    def peek(self):
         if len(self.stackl)==0:
            print("Stack is empty!")
         else:    
           return self.stackl[-1] 

    def isempty(self):
        return len(self.stackl)==0
    def printstack(self):
        for i in self.stackl:
            print(i,end="  ")

# creating object
sk=Stack()
# sk.push(1)      
# sk.push(2)    
# sk.push(3) 
# sk.printstack()    
print(sk.peek())         
# sk.Pop()
# sk.Pop()
# sk.printstack() 
# print(sk.isempty())


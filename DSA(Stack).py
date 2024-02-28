import numpy as np
class Stack:
    def __init__(self):
        self.MyStack=np.zeros([10],dtype="int32")
        self.top=-1
    def Push(self,Item):
        if (self.top==len(self.MyStack)-1):
            print("The Stack is already full ")
        else:
            self.top+=1
            self.MyStack[self.top]=Item
            print(self.MyStack[self.top])
    def POP(self):
        if self.top==-1:
            print("The stack is  Empty")
        else:
            
            poppedItem=self.MyStack[self.top]
            # self.top=0
            self.MyStack[self.top]=0
            self.top-=1
            print( "The removing elements from Stack : ",poppedItem)
obj=Stack()
obj.Push(17)
obj.Push(27)
obj.Push(37)
obj.Push(47)
obj.POP()
obj.POP()
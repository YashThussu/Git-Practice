
class StackArr():

    def __init__(self):
        self.arr:list=[]
    
    def push(self,val):

        self.arr.append(val)
    
    def show(self):

        print(self.arr)
    
    def pop(self):

        print("Top item in the stack:",self.arr[-1])
        return self.arr.pop()
    
    def is_empty(self):

        if self.arr.__len__()==0:
            return 0
        
        else: return self.arr.__len__()

class Node:

    def __init__(self,value) -> None:
        
        self.value=value
        self.next=None

class LinkedList:

    def __init__(self):
        
        self.head=Node(None)
    

        


obj=StackArr()
n1=Node(10)
obj.push(10)
obj.show()
obj.push(20)
obj.pop()
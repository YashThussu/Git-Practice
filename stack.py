
class Stack():

    def __init__(self):
        self.arr:list=[]
    
    def push(self,val):

        self.arr.append(val)
    
    def show(self):

        print(self.arr)
    
    def pop(self):

        print("Top item in the stack:",self.arr[-1])
        return self.arr.pop()

        


obj=Stack()
obj.push(10)
obj.show()
obj.push(20)
obj.pop()
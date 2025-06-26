
class Stack():

    def __init__(self):
        self.arr:list=[]
    
    def push(self,val):

        self.arr.append(val)
    
    def show(self):

        print(self.arr)

        


obj=Stack()
obj.push(10)
obj.show()
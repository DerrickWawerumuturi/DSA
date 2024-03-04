class Dequeue: 
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == [] 
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
"""
Input Restricted Dequeue:
    where input is at a single end(I chose front)
"""   
class Input(Dequeue):
    def addFront(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()
"""
    Output Restricted Dequeue:
        where output is at a single end(I chose Rear)
"""    


class Output(Input):
    def addFront(self, item):
        self.items.insert(0, item)
    
    def addRear(self, item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop()
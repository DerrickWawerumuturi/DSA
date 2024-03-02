class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)


line = Queue()
line.enqueue("d")
line.enqueue("e")
line.enqueue("r")
line.enqueue("r")
line.enqueue("i")
line.enqueue("c")
line.enqueue("k")
line.display()
print(line.dequeue())
line.display()
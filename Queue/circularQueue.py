class CQueue:
    def __init__(self, k):
        self.k = k
        self.queue =  [None] * k
        self.head =  self.tail = -1


    def enqueue(self, data):
        if ((self.tail + 1) %  self.k == self.head):
            print("Queue is full")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
            print("list was empty")

        else:
            self.tail =  (self.tail + 1) %  self.k
            self.queue[self.tail] = data
            print("list had something")

    def dequeue(self):
        if (self.head == -1):
            print("queue is empty")
        elif (self.head ==  self.tail):
            self.head = -1
            self.tail = -1
            self.queue.pop(0)
        else:
            self.head = (self.head + 1) % self.k
            self.queue.pop(0)

    def printCqueue(self):
        if (self.head == -1):
            print("queue is empty")
        print(self.queue)
        

line1 = CQueue(6)
line1.enqueue(4)
line1.enqueue(3)
line1.enqueue(2)
line1.enqueue(7)
line1.enqueue(2)
line1.enqueue(1)
line1.enqueue(8)
#print(line1.queue)
line1.dequeue()
line1.printCqueue()
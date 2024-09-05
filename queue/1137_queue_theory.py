class MyCircularQueue(object):

    def __init__(self, k):
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = k
        self.queue = [None] * k

    def enQueue(self, value):
        if self.isFull():
            return False  # Return False if the queue is full

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False  # Return False if the queue is empty

        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1  # Return -1 if the queue is empty
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1  # Return -1 if the queue is empty
        return self.queue[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

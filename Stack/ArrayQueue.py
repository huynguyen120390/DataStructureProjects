class ArrayQueue:
    def __init__(self,limit):
        self.limit = limit
        self.length = 0
        self.queue = []


    def extend_limit(self,percent):
        self.limit = int((1+percent/100)*self.limit)
    

    def push(self,data): #O(1)
        if self.length < self.limit:
            self.queue.append(data)
            self.length += 1
        else:
            raise "QueueOverFlow"
        return data


    def pop(self): #O(n)
        if self.length > 0:
            data = self.queue[0]
            del self.queue[0]
            self.length -= 1
        else: 
            raise "QueueUnderFlow"
        return data


    def lookup(self,data):
        for i,v in enumerate(self.queue):
            if v == data:
                return i
        return - 1


    def peek(self):
        return self.queue[0]

    
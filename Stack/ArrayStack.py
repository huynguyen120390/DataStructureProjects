class Stack:
    def __init__(self):
        self.__limit = 10
        self.__length = 0
        self.__stack = []
    

    def extend_limit(self,percent):
        self.__limit = int((1 + percent/100)*self.__limit)
        

    def push(self,data): #O(1)
        if self.__length < self.__limit:
            self.__stack.append(data)
        else:
            raise "StackOverFlow"
        self.__length += 1
        return data


    def pop(self): #O(1)
        if self.__length > 0:
            data = self.__stack[self.__length - 1]
            del self.__stack[self.__length - 1]
        else:
            raise "StackUnderFlow"
        self.__length -= 1
        return data 


    def peek(self): #O(1)
        if self.__length > 0:
            return self.__stack[self.__length - 1]
        else:
            raise "StackUnderFlow"
    

    def lookup(self,data): #O(n)
        if self.__length > 0:
            for i,v in enumerate(self.__stack):
                if data == v:
                    return i
        else:
            raise "StackUnderFlow"
        return -1


    def import_array_into_stack(self,arr): #O(n), Theta(n)
        for i in arr:
            self.push(i)
        

    def empty_stack(self): #O(n) ,Theta(n)
        for _ in range(self.__length):
            self.pop()


    def display(self): 
        print(self.__stack)

    


if __name__ =='__main__':
    s = Stack()
    s.extend_limit(100)
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    s.import_array_into_stack(arr)
    i = s.lookup(3)
    s.display()
    print(s.peek())
    s.empty_stack()
    s.display()
    

    




        
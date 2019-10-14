from SinglyLinkedList import SinglyLinkedList
class LinkedListStack:
    def __init__(self,limit):
        self.limit = limit
        self.sll= SinglyLinkedList()
        self.length = 0

    def extend_limit(self,percent):
        self.limit = int((1+percent/100)*self.limit)
        
    def push(self,data): #
        self.sll.append(data)
        self.length += 1

    def pop(self):
        self.sll.delete(self.length - 1)
        self.length -= 1

    def display(self):
        self.sll.display()

    def lookup(self,data):
        return self.sll.lookup(data)

    def peek(self):
        return self.sll.head.data


if __name__ == "__main__":
    lls = LinkedListStack(10)
    lls.push(1)
    lls.push(2)
    lls.push(3)
    lls.push(4)
    lls.push(5)
    lls.pop()

    print(lls.display())
    print(lls.lookup(2))
    print(lls.peek())
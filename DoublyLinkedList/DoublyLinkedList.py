class DoublyLinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0


    def prepend(self,data):
        node = DoublyLinkedListNode(data)
        if(self.length == 0):
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
     

    def append(self,data):
        node = DoublyLinkedListNode(data)
        if (self.length == 0):
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1


    def insert(self,index, data):
        node = DoublyLinkedListNode(data)
        if (index < 0 or index > self.length):
            raise "OutBoundOfLinkedList"
        elif index == 0:
            self.prepend(data)
        elif index == self.length:
            self.append(data)
        else:
            curr = self.traverse_to_index(index)
            node.next = curr
            curr.prev.next = node
            node.prev = curr.prev
            curr.prev = node
            self.length += 1

    
    def delete(self,index):
        if(self.head == None):
            raise "EmptyList"
        elif(index == 0):
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev.next = None
                self.head.prev = None
        else:
            curr = self.traverse_to_index(index)
            if index == self.length - 1:
                self.tail = curr.prev
                curr.prev = None
                self.tail.next = None
            else:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.prev = None
                curr.next = None
        self.length -= 1


    def lookup(self,data):
        if self.head == None:
            raise "EmptyList"
        else:
            curr = self.head
            index = 0
            while curr != None :
                if curr.data == data:
                    return index
                else:
                    index += 1
                    curr = curr.next
            return -1        
    
            
    def traverse_to_index(self,index):
        if (index < 0 or index > self.length - 1):
            raise "OutBoundOfLinkedList"
        curr = self.head
        count = 0
        while(count < index):
            count += 1
            curr = curr.next
        return curr


    def display(self):
        arr = []
        if self.length != 0:
            curr = self.head
            while(curr!=None):
                arr.append(curr.data)
                curr = curr.next
        print(f"Length is {self.length} :")
        print(arr)

    


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.prepend(22)
    dll.prepend(33)
    dll.append(44)
    dll.insert(3,55)
    dll.display()
    dll.insert(3,65)
    dll.display()
    dll.insert(2,75)
    dll.display()
    dll.delete(0)
    dll.display()
    dll.delete(4)
    dll.display()
    dll.delete(1)
    dll.display()
    a = dll.lookup(22)
    b = dll.lookup(44)
    c = dll.lookup(65)
    assert a == 0, "Wrong"
    assert b == 1, "Wrong"
    assert c == 2, "Wrong"
    print(a,b,c)



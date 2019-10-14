
class OutOfBoundLinkedList(Exception):
    pass

class SinglyLinkedListNode:
    def __init__(self,data = None,next= None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self,data):
        self.prepend_node(SinglyLinkedListNode(data))

    def append(self,data):
        self.append_node(SinglyLinkedListNode(data))

    def prepend_node(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def append_node(self,node):
        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1    

    def insert_node_by_index(self,index,node):
        if self.head == None: #empty 
            self.head = node
        elif index == 0: #empty 
            self.prepend(node)
        elif index == self.length: #at end, expect one item beyond max length
            self.append(node)
        elif index > self.length or index < 0: #at end, expect beyond max length 
            raise OutOfBoundLinkedList
        else:
            curr = self.head 
            counter = 0
            while curr != None:
                curr = curr.next
                counter += 1
                if counter == index:
                    node.next = curr.next
                    curr.next = node


    def insert_data_by_index(self,index,data):
        node = SinglyLinkedListNode(data,None)
        self.insert_node_by_index(index,node)


    def delete(self,index):
        #Conds for existence
        value = -1 
        if self.length  < 1: # empty 
            return value
        elif index > self.length - 1: # expect beyond max length 
            return value 
        else:
            #Algor
            curr = self.head 
            counter = 0
            if index == 0: #index = 0 problem
                if self.length == 1:
                    self.head = None
                else:
                    self.head = self.head.next
            else: #stand-at-front approach with one cursor
                while curr != None: 
                    curr = curr.next
                    counter += 1
                    if counter == index - 1:
                        value = curr.next.data
                        if counter == self.length - 2:
                            curr.next = None 
                        else:
                            curr.next = curr.next.next
        
        return value

    def lookup(self,data):
        index = 0
        if self.length <= 0: # empty problem
            return -1
        else:
            curr = self.head
            if curr.data == data:
                index = 0
            else:
                while curr != None:
                    curr = curr.next
                    index += 1
                    if curr.data == data:
                        return index 
        

    def display(self):
        curr = self.head
        print("Length of {}".format(self.length))
        print('Head->',end = '')
        if self.length == 1: #or self.head.next == None
            print(curr.data)
        else:
            while curr != None: 
                print (str(curr.data) + '->',end ='')
                curr= curr.next
        print('None')

    def reverse(self):
        pass
        

if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.append(7)
    sll.append(8)
    sll.append(9)
    sll.append(7)
    sll.prepend(1)
    sll.append(83)
    sll.append(9)
    sll.display()
    index = sll.lookup(83)

    sll.insert_data_by_index(6,11)
    sll.display()
    sll.delete(0)
    
    print(index)
    sll.display()
    


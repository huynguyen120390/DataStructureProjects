class TreeNode:
    def __init__(self,data, id, left=None,right=None):
        self.data = data
        self.id = id
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        


    def insert(self,data):
        
        if self.root == None:
            newNode = TreeNode(data,0)
            self.root = newNode
        else:
            newNode = TreeNode(data,self.size + 1)
            curr = self.root
            while(1):
                if data <= curr.data:
                    if (curr.left == None):
                        curr.left = newNode
                        self.size += 1
                        break
                    else:
                        curr = curr.left
                elif data > curr.data:
                    if (curr.right == None):
                        curr.right = newNode
                        self.size += 1
                        break
                    else:
                        curr = curr.right



    def lookup(self,data,node):
        curr = node
        if curr == None:
            return False
        if curr.data == data:
            return True

        on_left = self.lookup(data,node.left)

        if on_left:
            return True
        else:
            on_right = self.lookup(data,node.right)
            if on_right:
                return True
            else:
                return False
        
    def remove(self,data):
        pass
            
    def display(self,node, direction):
        curr = node
        if curr == None:
            return curr
        else:
            
            if curr.left != None and curr.right == None:
                print(f'{direction} {curr.id}:{curr.data} -> L  {curr.left.id}:{curr.left.data}, R _:None ')
            elif curr.left == None and curr.left != None:
                print(f'{direction} {curr.id}:{curr.data} -> L _:None, R {curr.right.id}:{curr.right.data}')
            elif curr.left != None and curr.right != None:
                print(f'{direction} {curr.id}:{curr.data} -> L {curr.left.id}:{curr.left.data}, R {curr.right.id}:{curr.right.data}')
            else:
                print(f'{direction} {curr.id}:{curr.data} -> L _:None, R _:None')

        self.display(curr.left,'L')
        self.display(curr.right,'R')
        

        
            
        
            


if __name__ =='__main__':
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(-1)
    bst.insert(10)
    bst.insert(3)
    bst.insert(2)
    bst.remove(-1)
    print(bst.lookup(3,bst.root))
    bst.display(bst.root,'Root')
# # Binary Search Tree

# In[1]:


class Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None
        
class BSTree:
    def __init__(self, value = None):
        if(value == None):
            self.root = None
        else:
            self.root = Node(value)
        
    def insert(self, value):
        if(self.root == None):
            self.root = Node(value)
        else:
            parent = self.root
            child = self.root
            while(child):
                if(value < child.value):
                    parent = child
                    child = child.left
                elif(value > child.value):
                    parent = child
                    child = child.right
                elif(value == child.value):
                    child.count += 1
                    return
            if(child == None):
                if(child == parent.left):
                    parent.left = Node(value)
                else:
                    parent.right = Node(value)
                    
    def traversal(self, traversal_type):
        if(traversal_type == "preorder"):
            return self.preorder(self.root, "")
 
        elif(traversal_type == "inorder"):
            return self.inorder(self.root, "")
        
        elif(traversal_type == "postorder"):
            return self.postorder(self.root, "")
        
        else:
            print("Unsupported traversal type :", traversal_type)
            return False
        
    def preorder(self, start, traversal):
        if start:
            traversal += str(start.value)
            if(start.count>1):
                traversal += "("+str(start.count)+")"
            traversal += " "
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    
    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += str(start.value)
            if(start.count>1):
                traversal += "("+str(start.count)+")"
            traversal += " "
            traversal = self.inorder(start.right, traversal)
        return traversal
    
    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += str(start.value)
            if(start.count>1):
                traversal += "("+str(start.count)+")"
            traversal += " "
        return traversal
    
'''
       (20)
      /    \
     /      \
   (2)      (30[2])
   / \       /    
 (1) (10)  (25)
           /  \
         (22) (27)
 
'''
def main():
    my_tree = BSTree()
    my_tree.insert(20)
    my_tree.insert(2)
    my_tree.insert(10)
    my_tree.insert(1)
    my_tree.insert(30)
    my_tree.insert(25)
    my_tree.insert(27)
    my_tree.insert(22)
    my_tree.insert(30)
    
    print(my_tree.traversal("postorder"))
    print(my_tree.traversal("inorder"))
    print(my_tree.traversal("preorder"))
    
if __name__=="__main__":
    main()
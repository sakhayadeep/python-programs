#!/usr/bin/env python
# coding: utf-8

# # Binary tree traversal

# In[1]:


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
        
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
            traversal += (str(start.value) + " ")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    
    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder(start.right, traversal)
        return traversal
    
    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + " ")
        return traversal
    
'''
       (1)
      /   \
     /     \
   (2)     (3)
   / \     / \
 (4) (5) (6) (7)
 
preorder : 1 2 4 5 3 6 7
inorder  : 4 2 5 1 6 3 7
postorder: 4 5 2 6 7 3 1

'''
def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    
    print(tree.traversal("preorder"))
    print(tree.traversal("inorder"))
    print(tree.traversal("postorder"))
    
if __name__ == "__main__":
    main()

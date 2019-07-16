# # linked list 

# In[1]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value = None):
        self.first = None
        if(value != None):
            if(type(value) == int):
                self.first = Node(value)
            elif(type(value) == list and isinstance(n, int) for n in value):
                for i in value:
                    self.insert(i)
            else:
                print("please insert a integer or a list of integer")
        
    def insert(self, value):
        if(self.first == None):
            self.first = Node(value)
        else:
            temp = Node(value)
            previous_node = self.first
            next_node = self.first.next
            while(next_node):
                previous_node = next_node
                next_node = next_node.next
            previous_node.next = temp
        
    def delete(self, value):
        if(self.first == None):
            print("LinkedList is empty!!")
        elif(value == self.first.value):
            self.first = self.first.next
        else:
            previous_node = self.first
            next_node = self.first.next
            while(next_node):
                if(next_node.value == value):
                    previous_node.next = next_node.next
                    break
                else:
                    previous_node = next_node
                    next_node = next_node.next
            
            if(next_node == None):
                print(value, "not found!!")
    
    def display(self):
        if(self.first == None):
            print("LinkedList is empty")
        else:
            next_node = self.first
            items = ""
            while(next_node):
                items += str(next_node.value)+"->"
                next_node = next_node.next
                
            items += "None"
            print(items)

def main():
    ll = LinkedList([1,2,4])
    
    for i in range(2, 10):
        ll.insert(i)
        
    ll.delete(4)
    ll.delete(6)
    
    ll.display()

if __name__ == "__main__":
    main()
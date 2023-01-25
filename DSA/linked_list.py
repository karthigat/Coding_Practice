#Linked List
    #create
    #traverse

#create linked list
class HeadNode:
    """
        initialize head
    """
    def __init__(self):
        self.head= None 

    def display(self):
        nodes = []
        traverse_data = self.head
        while traverse_data is not None:
            nodes.append(traverse_data.data)
            traverse_data = traverse_data.next
        return nodes 

class Node:
    """
        initialize data and next
    """
    def __init__(self, data):
        self.data = data
        self.next = None


initialize = HeadNode()
initialize.head = Node('Apple') # initialize apple to head 
Node1 = Node('Orange') # pass orange to node
initialize.head.next = Node1 # assing 2nd node to head node's next
Node2 = Node('Grape')
Node1.next = Node2 # assign 3rd node to 2nd node's next
print(initialize.display())
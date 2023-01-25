#Linked List
    #create
    #traverse
    #insert at begining
    #insert at end
    #insert inbetween
    #remove

#create linked list
class HeadNode:
    """
        initialize head
    """
    def __init__(self):
        self.head= None 

    def atBegining(self, node):
        """
            insert at the begining of the node
        """
        new_head = node
        new_head.next = self.head
        self.head = new_head
    
    def atEnd(self ,node):
        """
            insert at the end of the node
        """
        if self.head.next is None: # if immediate next in 1st node is empty
            self.head.next = node
        at_end = self.head
        while(at_end.next): # if immediate next node is not empty
            at_end = at_end.next
        at_end.next = node

    def inBetween(self, mid_node, new_node):
        """
            insert inbetween the node
        """
        mid_traverse_data = self.head
        while mid_traverse_data.next is not None:
            if mid_traverse_data.data == mid_node:
                temp_next = mid_traverse_data.next 
                mid_traverse_data.next = Node(new_node) #assing the new data in between desired fruit
                mid_traverse_data.next.next = temp_next
            mid_traverse_data = mid_traverse_data.next
       
    def removeNode(self, remove_node):
        """
            remove the node
        """
        remove_node_next = self.head
        while remove_node_next.next is not None:
            if remove_node_next.next.data == remove_node:
                remove_node_next.next = remove_node_next.next.next #move the node in deleted next to prev node
            remove_node_next = remove_node_next.next 
            
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
initialize.atBegining(Node('Pineapple'))
print(initialize.display())
initialize.atEnd(Node('Watermelon'))
print(initialize.display())
initialize.inBetween('Apple','Kiwi')
print(initialize.display())
initialize.removeNode('Grape')
print(initialize.display())
import sys

sys.path.append('src')

from model.queue import PriorityQueue
from model.patient import Patient

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.value)
    
class BinaryTree:
    def __init__(self) -> None:
        self.root = None


    def print_tree(self, node, prefix="", is_left=True):
        if not node:
            print("Empty Tree")
            return
        if node.right:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

    def insert_node(self, node, value):

        if not node:
            return Node(value)

        else:
            custom_priority_queue = PriorityQueue()
            custom_priority_queue.enqueue(node)

            while not custom_priority_queue.is_empty():

                temporal_root_node = custom_priority_queue.dequeue()
                print('TEMPORAL ROOTNODE',temporal_root_node)
                if temporal_root_node.left is None:
                    if temporal_root_node.value.triage < value.triage:
                        temporal_root_node.left = Node(value)
                        return True
                    else:
                        print("ANA", value)
                        temporal_root_node.left = Node(value)
                        self.reassign_triage(temporal_root_node)

                custom_priority_queue.enqueue(temporal_root_node.left)


                if temporal_root_node.right is None:
                    if temporal_root_node.value.triage < value.triage:
                        temporal_root_node.right = Node(value)
                    else:
                        self.reassign_triage(temporal_root_node)

                    
                custom_priority_queue.enqueue(temporal_root_node.right)

    def reassign_triage(self,root_node):
        if not root_node:
            return
        if root_node.left.value.triage < root_node.value.triage:
            temporal_value = root_node.value
            root_node.value = root_node.left.value
            root_node.left.value = temporal_value
            self.reassign_triage(root_node)
            
        return root_node
        


    def check_heap_property(self):
        if not self.root:
            return
        
        if self.root.left.value.triage > self.root.value.triage:
            self.check_heap_property(self.root.left)
            self.check_heap_property(self.root.right)
        else:
            return False
        
        if self.root.right.value.triage > self.root.value.triage:
            self.check_heap_property(self.root.left)
            self.check_heap_property(self.root.right)

        else:
            return False
        return True
      
        
        

    def search_node(self, root_node, value):

        if not root_node:
            return False
        elif root_node.value == value:
            return True
        elif value < root_node.value:
            return self.search_node(root_node.left, value)
        else:
            return self.search_node(root_node.right, value)
        
    def delete_node(self, root_node, value):

        if root_node is None:
            return root_node
        
        if value < root_node.value:
            root_node.left = self.delete_node(root_node.left, value)
        elif value > root_node.value:
            root_node.right = self.delete_node(root_node.right, value)

        # Node to be deleted is found, and its a leaf node

        else:
            if root_node.left is None:
                return root_node.right
            elif root_node.right is None:
                return root_node.left
            temp = self.min_value_node(root_node.right)

            root_node.value = temp.value

            root_node.right = self.delete_node(root_node.right, temp.value)

        return root_node

    
    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

bt = BinaryTree()
root = Node(Patient('M', 'Juan', 20, 1))
bt.insert_node(root, Patient('F', 'Maria', 30, 2))
bt.insert_node(root, Patient('M', 'Pedro', 25, 2))
bt.insert_node(root, Patient('F', 'Ana', 35, 1))
print(bt.check_heap_property(),'AAAAAAAAAAAAAAAAAAAAAA')
bt.print_tree(root)
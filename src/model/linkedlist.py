class Node:

    __slots__ = 'value', 'next'

    def __init__(self, value):

        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
        
    def __init__(self) -> None:
        self.head = None
        self.tail = None
            
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next            
            
    def __str__(self) -> str:
        result = [str(x.value) for x in self]
        return ' '.join(result)
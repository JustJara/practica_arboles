'''
This module contains the implementation of a priority queue to store patients
'''

import sys

sys.path.append('src')

from model.patient import Patient
from model.linkedlist import LinkedList, Node

class Queue:

    def __init__(self) -> None:
        self.linked_list = LinkedList()

    def __str__(self) -> str:
        result = [str(x.value) for x in self.linked_list]
        return ' '.join(result)
    
    def is_empty(self) -> bool:
        return self.linked_list.head == None

    def enqueue(self, patient: Patient) -> None:
        new_node = Node(patient)

        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            new_node.next = None
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def dequeue(self) -> Patient:
        if self.is_empty():
            return None
        else:
            popped_node = self.linked_list.head

            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
            popped_node.next = None
            return popped_node

    
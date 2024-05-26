'''
This module contains the implementation of a priority queue to store patients
'''

import sys

sys.path.append('src')

from model.patient import Patient

class PriorityQueue:

    def __init__(self) -> None:
        self.list = []    

    def __str__(self):
        return ' '.join(map(str,self.list))
    
    def is_empty(self):
        return len(self.list) == 0

    def enqueue(self, node):
        self.list.append(node)

    def dequeue(self):

        if self.is_empty():
            return 'The queue is empty'

        else:

            max_priority = self.list[0]

            for item in self.list[1:]:

                if item.value.triage < max_priority.value.triage:
                    max_priority = item

            self.list.remove(max_priority)
            return max_priority

    def check_next_max_priority_patient(self):
        if self.is_empty():
            return 'The queue is empty'
        else:
            max_priority = self.list[0].data.triage

            for item in self.list[1:]:
                if item.data.triage < max_priority:
                    max_priority = item.data.triage

            return max_priority
    
    def priority_queue_size(self):
        return len(self.list)
    
    def delete(self):
        self.list = None
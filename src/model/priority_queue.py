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

    def insert(self, patient):
        self.list.append(patient)

    def remove_max_priority_patient(self, patient):

        if self.is_empty():
            return 'The queue is empty'

        else:

            max_priority = self.list[0].triage

            for item in self.list[1:]:

                if item.triage < max_priority:
                    max_priority = item.triage

            self.list.remove(max_priority)
            return max_priority

    def check_next_max_priority_patient(self):
        if self.is_empty():
            return 'The queue is empty'
        else:
            max_priority = self.list[0].triage

            for item in self.list[1:]:
                if item.triage < max_priority:
                    max_priority = item.triage

            return max_priority
    
    def priority_queue_size(self):
        return len(self.list)
    
    def delete(self):
        self.list = None
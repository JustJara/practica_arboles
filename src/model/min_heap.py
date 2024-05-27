'''
Modulo con la implementación de un MinHeap para el manejo de pacientes en un hospital

'''

import sys

sys.path.append('src')

#Importaciones necesarias para el funcionamiento correcto del programa
from model.patient import Patient
from model.queue import Queue

class MinHeap:
    '''
    Clase que contiene la implementación de un MinHeap para el manejo de pacientes en un hospital
    '''
    def __init__(self, data=None):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, patient: Patient):
        '''
        Este método inserta un nuevo paciente en el heap y mantiene la propiedad del heap mínimo.

        Parametros
        ----------
        patient : Patient
            Paciente a insertar en el heap
        '''
        if self.data is None:
            self.data = patient
        else:
            auxiliar_queue = Queue()
            auxiliar_queue.enqueue(self)

            while not auxiliar_queue.is_empty():

                current_node : MinHeap = auxiliar_queue.dequeue()
                
                #Valida si el nodo de la izquierda es nulo, si es así, se inserta el nuevo nodo y se llama a heapify_up para mantener la propiedad
                #Si no es nulo, se agrega a la cola auxiliar para seguir buscando un nodo nulo
                if current_node.leftchild is None:
                    current_node.leftchild = MinHeap(patient)
                    self.heapify_up(current_node.leftchild)
                    return
                else:
                    auxiliar_queue.enqueue(current_node.leftchild)

                #Valida si el nodo de la derecha es nulo, si es así, se inserta el nuevo nodo y se llama a heapify_up para mantener la propiedad
                #Si no es nulo, se agrega a la cola auxiliar para seguir buscando un nodo nulo
                if current_node.rightchild is None:
                    current_node.rightchild = MinHeap(patient)
                    self.heapify_up(current_node.rightchild)
                    return
                else:
                    auxiliar_queue.enqueue(current_node.rightchild)

    def heapify_up(self, node : 'MinHeap'):
        '''
        Este método mantiene la propiedad del heap mínimo subiendo el nodo en caso de ser necesario para mantener la propiedad.

        Parametros
        ----------
        node : MinHeap
            Nodo a subir en el heap
        '''
        while node != self:
            #Obtenemos el nodo padre
            parent = self.get_parent(node)
            
            #Comparamos si el triaje del nodo es menor al triaje del padre, si es así, se intercambian los nodos
            #Si no, se rompe el ciclo
            if parent and node.data.triage < parent.data.triage:
                parent.data, node.data = node.data, parent.data
                node = parent
            else:
                break
    
    def get_parent(self, node: 'MinHeap'):
        '''
        Este método encuentra el nodo padre de un nodo dado.

        Parametros
        ----------
        node : MinHeap
            Nodo hijo del cual se quiere encontrar el padre
        '''
        auxiliar_queue = Queue()
        auxiliar_queue.enqueue(self)

        
        while not auxiliar_queue.is_empty():
            current_node = auxiliar_queue.dequeue()
            #Valida si el nodo actual tiene como hijo izquierdo o derecho al nodo que se está buscando
            if current_node.leftchild == node or current_node.rightchild == node:
                return current_node
            #Si no es el nodo buscado, se agregan los hijos del nodo actual tanto a la izquierda como derecha a la cola auxiliar
            if current_node.leftchild is not None:
                auxiliar_queue.enqueue(current_node.leftchild)
            if current_node.rightchild is not None:
                auxiliar_queue.enqueue(current_node.rightchild)
        return None
    

    def next_patient_to_attend(self):
        '''
        Este método retorna el siguiente paciente a atender en el hospital sin eliminarlo del heap
        '''
        if self.data is None:
            return 'No hay pacientes en espera'
        return self.data

    def attend_next_patient(self):
        '''
        Este método atiende al siguiente paciente en el hospital, removiendolo del árbol y manteniendo la propiedad del heap mínimo
        '''

        if self.data is None:
            return 'No hay pacientes para atender'
        
        min_data = self.data
        #Se elimina el nodo raíz y se reemplaza por el último nodo del heap
        if not self.leftchild and not self.rightchild:
            self.data = None
            return min_data
        self.data = self.remove_last_node()
        self.heapify_down(self)
        return min_data

    def remove_last_node(self):
        '''
        Este método elimina el último nodo del heap y lo retorna
        '''

        auxiliar_queue = Queue()
        auxiliar_queue.enqueue(self)

        last_node = None
        parent = None

        while not auxiliar_queue.is_empty():
            current_node = auxiliar_queue.dequeue()
            
            #Verifica si el nodo actual tiene hijos, si es así, se agregan a la cola auxiliar
            if current_node.leftchild is not None:
                parent = current_node
                auxiliar_queue.enqueue(current_node.leftchild)
                
            #Verifica si el nodo actual tiene hijos, si es así, se agregan a la cola auxiliar
            if current_node.rightchild is not None:
                parent = current_node
                auxiliar_queue.enqueue(current_node.rightchild)
            #Se guarda el último nodo hasta el momento
            last_node = current_node
        #Verifica si el nodo padre tiene como hijo derecho al último nodo, si es así, se elimina la referencia
        if parent is not None and parent.rightchild == last_node:
            parent.rightchild = None
        #Verifica si el nodo padre tiene como hijo izquierdo al último nodo, si es así, se elimina la referencia
        elif parent is not None and parent.leftchild == last_node:
            parent.leftchild = None

        #Se retorna el último nodo ya habiendo eliminado la referencia
        return last_node.data
            

    def heapify_down(self, node: 'MinHeap'):
        '''
        Este método mantiene la propiedad del heap mínimo bajando el nodo en caso de ser necesario para mantener la propiedad.

        Parametros
        ----------
        node : MinHeap
            Nodo a bajar en el heap
        '''
        while node:
            smallest = node
            #Se compara el triaje del nodo actual con el triaje de sus hijos, si el triaje del hijo es menor, se intercambian los nodos
            #Si son iguales, se compara el id del paciente para verificar quién llegó antes
            if node.leftchild is not None and (
                node.leftchild.data.triage < smallest.data.triage or 
                (node.leftchild.data.triage == smallest.data.triage and node.leftchild.data.id < smallest.data.id)
            ):
                smallest = node.leftchild
            if node.rightchild and (
                node.rightchild.data.triage < smallest.data.triage or 
                (node.rightchild.data.triage == smallest.data.triage and node.rightchild.data.id < smallest.data.id)
            ):
                smallest = node.rightchild
            #Se comprueba que smallest si ha sido actualizado y es diferente al nodo actual, si es así, se intercambian los nodos
            if smallest != node:
                node.data, smallest.data = smallest.data, node.data
                node = smallest
            #Si no, se rompe el ciclo ya que el nodo está donde debe estar
            else:
                break

    def show_general_tree_waiting_room(self,prefix="", is_left=True):
        '''
        Este método muestra los pacientes en espera en el hospital en forma de árbol
        '''
        if self.data is not None:
            if self.leftchild:
                self.leftchild.show_general_tree_waiting_room(prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(self.data))
            if self.rightchild:
                self.rightchild.show_general_tree_waiting_room(prefix + ("    " if is_left else "│   "), True)


    def get_general_waiting_room(self) -> list[Patient]:
        '''
        Este método muestra los pacientes en espera en el hospital en forma de lista

        Returns
        -------

        waiting_room : list[Patient]
            Lista de pacientes en espera en el hospital   
        '''
        waiting_room = []
        auxiliar_queue = Queue()
        auxiliar_queue.enqueue(self)

        while not auxiliar_queue.is_empty():
            current_node : MinHeap = auxiliar_queue.dequeue()
            if current_node.data is not None:
                waiting_room.append(current_node.data)
                if current_node.leftchild is not None:
                    auxiliar_queue.enqueue(current_node.leftchild)
                if current_node.rightchild is not None:
                    auxiliar_queue.enqueue(current_node.rightchild)

        return waiting_room
            


    def get_patients_by_triage(self, triage: int):
        '''
        Este método muestra los pacientes en espera en el hospital por triaje
        
        Parametros
        ----------
        triage : int
            Triaje por el cual se desea filtrar los pacientes en espera

        Retorna
        -------
        waiting_room_by_triage: list[Patient]
            Lista de pacientes en espera en el hospital filtrados por triaje
        '''
        patients = self.get_general_waiting_room()
        waiting_room_by_triage = []
        for patient in patients:
            if patient.triage == triage:
                waiting_room_by_triage.append(patient)

        return waiting_room_by_triage

    
    def remove_patient(self, patient_ind:int):
        '''
        Eset método elimina un paciente con id específica en espera en el hospital manteniendo el heap mínimo

        Parametros
        ----------
        patient_ind : int
            Id del paciente a eliminar
        '''

        if self.data is None:
            return False
        auxiliar_queue = Queue()
        auxiliar_queue.enqueue(self)

        target = None
        while not auxiliar_queue.is_empty():
            current_node = auxiliar_queue.dequeue()
            #Si encuentra el nodo con el ID especificado, se guarda en target
            if current_node.data.id == patient_ind:
                target = current_node
                break
            #Si no es el nodo buscado, se agregan los hijos del nodo actual tanto a la izquierda como derecha a la cola auxiliar
            if current_node.leftchild is not None:
                auxiliar_queue.enqueue(current_node.leftchild)
            if current_node.rightchild is not None:
                auxiliar_queue.enqueue(current_node.rightchild)
        #Si se encontró el nodo, se reemplaza por el último nodo del heap y se llama a heapify_up y heapify_down para mantener la propiedad
        if target is not None:
            target.data = self.remove_last_node()
            if target != self:
                self.heapify_up(target)
                self.heapify_down(target)
            else:
                self.heapify_down(target)
            return True
        return False



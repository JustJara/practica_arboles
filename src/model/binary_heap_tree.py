'''
This module contains the implementation of a binary heap tree to store patients
'''
import sys
sys.path.append('src')

from model.patient import Patient
from model.priority_queue import PriorityQueue

class BinaryTreeNode:

    def __init__(self, data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def __str__(self, level=0):

        return str(self.data)

class BinaryHeap:
    '''
    This class represents a binary heap tree to store patients by triage emergency level
     ------------------------------------------------------------------------------
    | NIVEL DE URGENCIA  | TIPO DE URGENCIA  |    COLOR     |  TIEMPO DE ESPERA   |  
    -------------------------------------------------------------------------------
    |       1            |  RESUCITACION     |    ROJO      |  ATENCIÓN INMEDIATA |
    -------------------------------------------------------------------------------
    |       2            |  EMERGENCIA       |    NARANJA   |  10 - 15 MINUTOS    |
    -------------------------------------------------------------------------------
    |       3            |  URGENCIA         |   AMARILLO   |  60 MINUTOS         |
    -------------------------------------------------------------------------------
    |       4            |  URGENCIA MENOR   |   VERDE      |  2 HORAS            |
    -------------------------------------------------------------------------------
    |       5            |  SIN URGENCIA     |    AMARILLO  |  4 HORAS            |
    -------------------------------------------------------------------------------
    '''

    def __init__(self,root_node: BinaryTreeNode) -> None:
        
        self.root_node : BinaryTreeNode = root_node

    
    def __str__(self, level=0):
        ret = '  '*level + str(self.data) + '\n'

        if self.leftchild:
            ret += self.leftchild.__str__(level + 1)

        if self.rightchild:
            ret += self.rightchild.__str__(level + 1)

        return ret

    def patient_insertion(self, root_node: BinaryTreeNode):

        """
        Registrar (insertar) un paciente, debe ser posible agregar nuevos pacientes, el
        registro debe conservar el orden de llegada y la prioridad, el triaje 1 debe quedar
        en la raíz ó seguido de esta dependiendo del orden de llegada.
        
        This method performs the insertion of a patient by their priority level

        Parameters:
        -----------
            patient: Patient
                The patient to be inserted in the heap

        Returns
        -------
            Boolean
                True if the patient was inserted successfully, False otherwise

        """

        if not root_node:
            root_node = 
            return True
        else:
            custom_priority_queue = PriorityQueue()
            custom_priority_queue.enqueue(root_node)

            while not(custom_priority_queue.is_empty()):
                temporal_root_node = custom_priority_queue.dequeue()

                if temporal_root_node.leftchild is None:
                    temporal_root_node.leftchild = patient
                    return True

                custom_priority_queue.enqueue(temporal_root_node.leftchild)

                if temporal_root_node.rightchild is None:
                    temporal_root_node.rightchild = patient
                    return True

                custom_priority_queue.enqueue(temporal_root_node.rightchild)
                
        

    def check_next_patient(self):
        """

        Consultar paciente próximo a atención, sin eliminar de la cola de prioridad (solo
        consulta)

        This method returns the patient that should be attended next

        Returns
        -------
            Patient
                The patient that should be attended next

        """

        pass
    
    def patient_attended(self):
        """

        Opción atender siguiente, en esta opción se debe extraer el paciente que
        continua en atención acorde a la prioridad y orden de llegada

        This method removes the patient that should be attended next

        Returns
        -------
            Patient
                The patient that was attended

        """

        pass

    def show_patients(self, node,prefix="", is_left=True):
        """
        Consultar los pacientes que están en espera en general

        This method shows the patients in the heap

        """

        if not node:
            return
        
        if node.rightchild:
            self.show_patients(node.rightchild, prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.data))

        if node.leftchild:
            self.show_patients(node.leftchild, prefix + ("    " if is_left else "│   "), True)
        

    def show_patients_by_triage(self):
        """
        Consultar los pacientes que están en espera por triaje

        This method shows the patients in the heap by triage level

        """

        pass
    
    def delete_patient_from_heap(self, patient_id: int):
        """
        Opción eliminar paciente, el sistema debe dar la opción si un paciente se desea
        retirar de la sala de urgencias, este debe ser eliminado, conservando la
        prioridad de los restantes y el orden de llegada, la eliminación debe ser por
        nombre y/o por Id.

        This method deletes a patient from the heap

        Parameters:
        -----------
            patient_id: int
                The id of the patient to be deleted

        Returns
        -------
            Boolean
                True if the patient was deleted successfully, False otherwise

        """

        pass



bt = BinaryHeap(Patient('male','Juan',1,5))
bt.patient_insertion(Patient('male','Pedro',2,1))
bt.patient_insertion(Patient('female','Maria',3,2))
bt.patient_insertion(Patient('female','Maria',3,1))
bt.patient_insertion(Patient('female','Maria',3,3))
bt.show_patients(bt)

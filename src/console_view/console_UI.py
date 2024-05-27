'''
This module contains the console UI for the application.
'''
import sys
sys.path.append('src')

from model.min_heap import MinHeap
from model.patient import Patient
class ConsoleUI:

    def __init__(self) -> None:
        self.hospital = MinHeap()

    def show_menu(self):
        print('------------------------------------')
        print('1. Registrar paciente en la lista de espera')
        print('2. Consultar paciente próximo a atender')
        print('3. Atender paciente próximo')
        print('4. Mostar lista de espera general')
        print('5. Mostrar lista de espera por triaje')
        print('6. Mostrar lista de espera en vista de árbol')
        print('7. Retirar paciente de lista de espera')
        print('8. Salir')
        print('------------------------------------')


    def insert_automatic_patients(self):

        self.hospital.insert(Patient('M', 'Pedro',67,4))
        self.hospital.insert(Patient('F', 'Teresa', 45, 2))
        self.hospital.insert(Patient('M', 'Julio', 75, 1))
        self.hospital.insert(Patient('F', 'Sofía', 15, 4))
    
    def register_patient(self, gender : str, name : str, age : int, triage : int):
        patient = Patient(gender, name, age, triage)
        self.hospital.insert(patient)
        if patient:
            print(f'Paciente {patient} registrado con éxito')
        else:
            print('Error al registrar paciente')

    def show_next_patient(self):
        patient = self.hospital.next_patient_to_attend()
        if patient:
            print(f'El próximo paciente a atender es: {patient.name}')
        else:
            print('No hay pacientes en espera')

    def attend_patient(self):
        patient = self.hospital.next_patient_to_attend()
        if patient:
            print(f'Atendiendo a {patient}')
            self.hospital.attend_next_patient()
        else:
            print('No hay pacientes en espera')

    def show_waiting_room(self):
        print('Lista de espera general:')
        print(self.hospital.get_general_waiting_room())
    
    def show_waiting_room_by_triage(self, triage : int):
        print(f'Lista de espera para triaje {triage}:')
        print(self.hospital.get_patients_by_triage(triage))

    def show_waiting_room_tree(self):
        print('Lista de espera en vista de árbol:')
        self.hospital.show_general_tree_waiting_room()

    def remove_patient(self, patient_id : int):
        patient = self.hospital.remove_patient(patient_id)
        if patient:
            print(f'Paciente retirado con éxito')
        else:
            print('Error al retirar paciente')
    
    def run_app(self):
        self.insert_automatic_patients()
        while True:
            self.show_menu()
            option = int(input('Ingrese una opción: '))
            if option == 1:
                name = input('Ingrese nombre del paciente: ')
                gender = input('Ingrese género del paciente: ')
                age = int(input('Ingrese edad del paciente: '))
                triage = int(input('Ingrese triaje del paciente: '))
                self.register_patient(gender, name, age, triage)
            elif option == 2:
                self.show_next_patient()
            elif option == 3:
                self.attend_patient()
            elif option == 4:
                self.show_waiting_room()
            elif option == 5:
                triage = int(input('Ingrese triaje a consultar: '))
                self.show_waiting_room_by_triage(triage)
            elif option == 6:
                self.show_waiting_room_tree()
            elif option == 7:
                patient_id = int(input('Ingrese ID del paciente a retirar: '))
                self.remove_patient(patient_id)
            elif option == 8:
                print('Hasta pronto')
                break
            else:
                print('Opción no válida')
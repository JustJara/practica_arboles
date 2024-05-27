'''
Implementación de la clase paciente

'''

class Patient:
    '''
    Class that represents a patient in the hospital.
    '''

    id_counter = 1
    def __init__(self, gender, name, age, triage):
        self.id = Patient.id_counter
        Patient.id_counter += 1
        self.gender = gender
        self.nombre = name
        self.age = age
        self.triage = triage

    def __str__(self):
        return f'ID:{self.id} Nombre:{self.nombre} Triaje:({self.triage})'
    
    def __repr__(self) -> str:
        return self.__str__()




    
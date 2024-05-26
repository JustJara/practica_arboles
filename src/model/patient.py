'''
Implementación de la clase paciente

'''

class Patient:
    '''
    Class that represents a patient in the hospital.
    '''

    def __init__(self,gender: str, name: str, age: int, triage : int) -> None:
        
        self.name : str = name
        self.gender : str = gender
        self.age : int = age
        self.triage : int = triage

    def __str__(self) -> str:
        return self.name





    
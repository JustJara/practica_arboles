class Patient:
    id_counter = 1
    def __init__(self, gender, name, age, triage):
        self.id = Patient.id_counter
        Patient.id_counter += 1
        self.gender = gender
        self.nombre = name
        self.age = age
        self.triage = triage

    def __str__(self):
        return f'{self.id}: {self.nombre} ({self.triage})'

class MinHeap:
    def __init__(self, data=None):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, patient):
        if self.data is None:
            self.data = patient
        else:
            queue = [self]
            while queue:
                current = queue.pop(0)
                if not current.leftchild:
                    current.leftchild = MinHeap(patient)
                    self.heapify_up(current.leftchild)
                    return
                else:
                    queue.append(current.leftchild)
                if not current.rightchild:
                    current.rightchild = MinHeap(patient)
                    self.heapify_up(current.rightchild)
                    return
                else:
                    queue.append(current.rightchild)

    def heapify_up(self, node):
        while node != self:
            parent = self.get_parent(node)
            if parent and node.data.triage < parent.data.triage:
                parent.data, node.data = node.data, parent.data
                node = parent
            else:
                break

    def get_parent(self, node):
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current.leftchild == node or current.rightchild == node:
                return current
            if current.leftchild:
                queue.append(current.leftchild)
            if current.rightchild:
                queue.append(current.rightchild)
        return None

    def next_patient_to_attend(self):
        if self.data is None:
            return None
        return self.data

    def extract_min(self):
        if self.data is None:
            return None
        min_data = self.data
        if not self.leftchild and not self.rightchild:
            self.data = None
            return min_data
        self.data = self._remove_last_node()
        self._heapify_down(self)
        return min_data

    def _remove_last_node(self):
        
        queue = [self]
        last_node = None
        parent = None
        while queue:
            current = queue.pop(0)
            if current.leftchild:
                parent = current
                queue.append(current.leftchild)
            if current.rightchild:
                parent = current
                queue.append(current.rightchild)
            last_node = current
        if parent and parent.rightchild == last_node:
            parent.rightchild = None
        elif parent and parent.leftchild == last_node:
            parent.leftchild = None
        return last_node.data

    def _heapify_down(self, node):
        while node:
            smallest = node
            if node.leftchild and (
                node.leftchild.data.triage < smallest.data.triage or 
                (node.leftchild.data.triage == smallest.data.triage and node.leftchild.data.id < smallest.data.id)
            ):
                smallest = node.leftchild
            if node.rightchild and (
                node.rightchild.data.triage < smallest.data.triage or 
                (node.rightchild.data.triage == smallest.data.triage and node.rightchild.data.id < smallest.data.id)
            ):
                smallest = node.rightchild

            if smallest != node:
                node.data, smallest.data = smallest.data, node.data
                node = smallest
            else:
                break

    def display(self,prefix="", is_left=True):
        if self.data is not None:
            if self.leftchild:
                self.leftchild.display(prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(self.data))
            if self.rightchild:
                self.rightchild.display(prefix + ("    " if is_left else "│   "), True)

    def remove(self, numero_paciente):
        if self.data is None:
            return False
        queue = [self]
        target = None
        parent = None
        while queue:
            current = queue.pop(0)
            if current.data.numero_paciente == numero_paciente:
                target = current
                break
            if current.leftchild:
                parent = current
                queue.append(current.leftchild)
            if current.rightchild:
                parent = current
                queue.append(current.rightchild)
        if target:
            target.data = self._remove_last_node()
            if target != self:
                self.heapify_up(target)
                self._heapify_down(target)
            else:
                self._heapify_down(target)
            return True
        return False

    def get_all_patients(self):
        result = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current.data is not None:
                result.append(current.data)
                if current.leftchild:
                    queue.append(current.leftchild)
                if current.rightchild:
                    queue.append(current.rightchild)
        return result

    def get_patients_by_triaje(self, triaje):
        return [p for p in self.get_all_patients() if p.triaje == triaje]

# Ejemplo de uso
heap = MinHeap()

# Registro de pacientes
heap.insert(Patient("M", "Pedro", 67, 4))
heap.insert(Patient("F", "Teresa", 45, 2))
heap.insert(Patient("M", "Julio", 75, 1))
heap.insert(Patient("F", "Sofia", 15, 4))
heap.insert(Patient("M", "Juan", 30, 3))
heap.insert(Patient("F", "Maria", 60, 2))
heap.insert(Patient("M", "Carlos", 50, 1))
heap.insert(Patient("F", "Ana", 25, 1))
heap.insert(Patient("M", "Javier", 35, 2))
heap.insert(Patient("F", "Luisa", 55, 2))



# Atender siguiente paciente

# Consultar pacientes que están en espera
print("\nPacientes en espera:")
heap.display()
print('\n ------------------- \n')

print(heap.extract_min())
print('-------------------')
heap.display()
print('-------------------')
print(heap.extract_min())
print('-------------------')

heap.display()


class MinHeap:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        # Inserta un nuevo dato en el heap y mantiene la propiedad del heap mínimo.
        new_node = MinHeap(data)
        queue = [self]
        
        while queue:
            current = queue.pop(0)
            
            if not current.leftchild:
                current.leftchild = new_node
                self._heapify_up(current.leftchild)
                return
            else:
                queue.append(current.leftchild)
            
            if not current.rightchild:
                current.rightchild = new_node
                self._heapify_up(current.rightchild)
                return
            else:
                queue.append(current.rightchild)

    def _heapify_up(self, node):
        # Mantiene la propiedad del heap mínimo subiendo el nodo en caso de ser necesario.
        current = node
        while current != self:
            parent = self._get_parent(current)
            if parent and parent.data > current.data:
                parent.data, current.data = current.data, parent.data
                current = parent
            else:
                break

    def _get_parent(self, node):
        # Encuentra el nodo padre de un nodo dado.
        queue = [self]
        parent = None

        while queue:
            current = queue.pop(0)
            if current.leftchild == node or current.rightchild == node:
                return current
            if current.leftchild:
                queue.append(current.leftchild)
            if current.rightchild:
                queue.append(current.rightchild)

        return parent

    def display(self, level=0, prefix="Root: "):
        # Muestra el árbol binario de una manera legible.
        print(" " * (level * 4) + prefix + str(self.data))
        if self.leftchild:
            self.leftchild.display(level + 1, "L--- ")
        if self.rightchild:
            self.rightchild.display(level + 1, "R--- ")

# Caso de prueba
root = MinHeap(10)
root.insert(15)
root.insert(5)
root.insert(2)
root.insert(30)
root.insert(1)

root.display()


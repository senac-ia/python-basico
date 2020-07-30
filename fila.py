# https://docs.python.org/3.8/library/collections.html#collections.deque
class Fila:
    def __init__(self):
        self.fila = []
    
    def push(self, item):
        self.fila.append(item)
    
    def pop(self):
        if(self.esta_vazio()):
            return None
        else:
            return self.fila.pop()

    def esta_vazio(self):
        return len(self.fila) == 0
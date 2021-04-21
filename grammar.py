class produccion:
    def __init__(self,produc_nombre= None, rules = None):
        self.produc_nombre=produc_nombre
        self.rules = rules

class simbolo:
    def __init__(self, sim = None, terminal = None):
        self.sim = sim
        self.terminal = terminal

class iteracion:
    def __init__(self,id= None, pila = None, entrada = None, transicion= None, cambio=None):
        self.id = id
        self.pila = pila
        self.entrada = entrada
        self.transicion = transicion
        self.cambio = cambio


class gramatica:
    def __init__(self,nombre = None, producciones = None, sim_terminales = None, sim_Noterminales= None, state_inicial=None):
        self.nombre = nombre
        self.producciones = producciones
        self.sim_terminales = sim_terminales
        self.sim_Noterminales = sim_Noterminales
        self.state_inicial = state_inicial

    def imprimir_gramatica(self):

        for regla in self.producciones:
            print(regla.produc_nombre+"->",end="")
            #print(len(regla.rules))
            n=0
            for rule in regla.rules:
                n+=1                 
                if n>1:
                    print(" | ",end="")
                for r in rule:
                    print(r.sim,end="")
            print()

from leer_gramaticas import leer_gramaticas
from grammar import simbolo
#----------------------------------------------------
def seleccionar_gramatica():
    gramaticas = leer_gramaticas()

    for gra in gramaticas:
        print(gra.nombre)

    print("Buscar nombre")
    nombre = "Gramatica1"

    for g in gramaticas:
        if g.nombre == nombre:
            gramatica = g

    return gramatica

def imprimir_pila(pila,i,entrada):
    print("Entrada",end=" ")
    l = len(entrada)
    c = entrada[i:l]
    print(c)
    pila.reverse()
    for elemento in pila:
         print(elemento.sim,end="")
    pila.reverse()
    print()
#----------------------------------------------------------
def pda():
    gramatica = seleccionar_gramatica()
    entrada = "zazabzbz"
    gramatica.imprimir_gramatica()
    length = len(entrada)
    state = "i"
    pila = []
    i=0
    
    while (i<length):
        currentChart = entrada[i]
        if state=="i":
            valido = simbolo("#","NO")
            pila.append(valido)
            state = "p"

            imprimir_pila(pila,i,entrada)

        elif state =="p":
            inicial = simbolo(gramatica.state_inicial,"NO")
            pila.append(inicial)
            state = "q"
            imprimir_pila(pila,i,entrada)


        elif state == "q":
            for produccion in gramatica.producciones:
                cima = pila[-1]
                if cima.terminal=="NO" and cima.sim==produccion.produc_nombre:
                    if len(produccion.rules)==1:
                        pila.pop()
                        imprimir_pila(pila,i,entrada)
                        for elem in produccion.rules:
                            #print(elem[0].sim)
                            elem.reverse()
                            for r in elem:
                                pila.append(r)
                            imprimir_pila(pila,i,entrada)
                            elem.reverse()
                    else:
                        #regla = None
                        n=0
                        for rule in produccion.rules:
                            n+=1
                            
                            if rule[0].sim == entrada[i]:
                                #print("---------")
                                #print(currentChart)
                                pila.pop()
                                rule.reverse()
                                for el in rule:
                                    pila.append(el)
                                imprimir_pila(pila,i,entrada)
                                #print(n)
                                rule.reverse()

                elif cima.terminal=="SI" and cima.sim == entrada[i]:
                    i+=1
                    pila.pop()
                    imprimir_pila(pila,i,entrada)

                        







pda()
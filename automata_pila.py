from leer_gramaticas import leer_gramaticas
from grammar import simbolo
#----------------------------------------------------
def seleccionar_gramatica():
    gramaticas = leer_gramaticas()

    for gra in gramaticas:
        print(gra.nombre)

    print("Buscar nombre")
    nombre = "Grm1"

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
    #entrada = "zazabzbz"
    entrada = "abzba"
    gramatica.imprimir_gramatica()
    length = len(entrada)
    state = "i"
    pila = []
    error = False
    i=0
    
    while (i<=length):

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
                if pila[-1].terminal=="NO" and pila[-1].sim==produccion.produc_nombre:
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
                        cambiado = False

                        for rule in produccion.rules:

                            if rule[0].sim == entrada[i]:
                                cambiado = True
                                pila.pop()
                                rule.reverse()
                                for el in rule:
                                    pila.append(el)
                                imprimir_pila(pila,i,entrada)
                                rule.reverse()
                        if cambiado == False:
                                for rule in produccion.rules:
                                    if rule[0].terminal == "NO":
                                        cambiado == True
                                        pila.pop()
                                        rule.reverse()
                                        for el in rule:
                                            pila.append(el)
                                        print("####")
                                        imprimir_pila(pila,i,entrada)
                                        rule.reverse()


                elif pila[-1].terminal=="SI" and pila[-1].sim == entrada[i]:
                    i+=1
                    print(i)
                    pila.pop()
                    imprimir_pila(pila,i,entrada)
                elif pila[-1].terminal=="SI" and pila[-1].terminal != entrada[i]:
                    error = True
                    print("Error")
                    state = "f"
                    break
                elif len(pila)==1 and pila[0].sim=="#":
                    pila.pop()
                    state = "f"
                    break
        elif state =="f":
            print(i)
            if i==length and error==False:
                print(entrada+" es una palabra admitida")
            else:
                print("Error: "+entrada+" No es una palabra admitida")
            
            i=length+2

                        







pda()
from leer_gramaticas import leer_gramaticas
from grammar import simbolo
from grammar import iteracion
#----------------------------------------------------
def seleccionar_gramatica(gramaticas):
    #gramaticas = leer_gramaticas()
    print("Estas son las Gramáticas Cargadas en Memoria,Ingrese el nombre de la gramatica a seleccionar:")


    for gra in gramaticas:
        print("->"+gra.nombre)

    #print("Buscar nombre")
    #nombre = "Gramatica1"
    #nombre = "Grm1"
    nombre = input()

    for g in gramaticas:
        if g.nombre == nombre:
            gramatica = g

    return gramatica

def imprimir_pila(pila,i,entrada):
    pile = ""
    print("Entrada",end=" ")
    l = len(entrada)
    c = entrada[i:l]
    print(c)
    pila.reverse()
    for elemento in pila:
         print(elemento.sim,end="")
         pile+=elemento.sim
    pila.reverse()
    print()

    #return pile
#----------------------------------------------------------
def pda(gramaticas):
    gramatica = seleccionar_gramatica(gramaticas)

    print("Introduzca la palabra a evaluar")
    entrada = input()
    #entrada = "zazabzbz"
    #entrada = "abzba"
    #gramatica.imprimir_gramatica()
    length = len(entrada)
    state = "i"
    pila = []
    error = False
    i=0
    k=0
    iteraciones =  []
    
    while (i<=length):

        if state=="i":
            valido = simbolo("#","NO")
            pila.append(valido)
            state = "p"

            #pile = imprimir_pila(pila,i,entrada)
            imprimir_pila(pila,i,entrada)
            #it = iteracion('0'," ",entrada[0],"(i,$,$;p,#)","$ , $ ; #")
            #iteraciones.append(it)

        elif state =="p":
            print("###")          
            inicial = simbolo(gramatica.state_inicial,"NO")
            pila.append(inicial)
            state = "q"

            #pile = imprimir_pila(pila,i,entrada)
            imprimir_pila(pila,i,entrada)
            k+=1
            #it = iteracion(str(k),"#",entrada[i],"(p,$,$;q,"+gramatica.state_inicial+")","$ , $ ; "+gramatica.state_inicial)
            #iteraciones.append(it)


        elif state == "q":
            print("//////////")
            for produccion in gramatica.producciones:
                if pila[-1].terminal=="NO" and pila[-1].sim==produccion.produc_nombre:
                    if len(produccion.rules)==1:
                        pila.pop()
                        for elem in produccion.rules:
                            elem.reverse()
                            for r in elem:
                                pila.append(r)
                            imprimir_pila(pila,i,entrada)
                            elem.reverse()
                    else:
                        regla = None
                        cambiado = False
                        op = False

                        for rule in produccion.rules:

                            if rule[0].sim == entrada[i]:
                                cambiado = True
                                if len(rule)!=1 and i+1<=length:
                                    if rule[1].sim == entrada[i+1]:
                                        regla = rule
                                        op = True
                                    elif regla == None:
                                        regla = rule
                                elif regla == None or op == False:
                                    regla = rule
                    
                        
                        if cambiado == False:
                                opti = False
                                for rule in produccion.rules:
                                    if rule[0].terminal == "NO":
                                        for prod in gramatica.producciones:
                                            if rule[0].sim == prod.produc_nombre:
                                                for produc in prod.rules:
                                                    if produc[0].sim == entrada[i]:
                                                        regla = rule
                                                        opti = True

                                    if regla == None or opti == False:
                                        regla = rule
                                        
                            
                        if regla!=None:
                            regla.reverse()
                            pila.pop()
                            rel =""
                            for el in regla:
                                pila.append(el)
                                rel+=el.sim
                            #pile = imprimir_pila(pila,i,entrada)
                            imprimir_pila(pila,i,entrada)
                            regla.reverse()
                            k+=1
                            #it = iteracion(str(k),pile,entrada[i],"(q,$,"+pila[-1].sim+";q,"+rel+")","$ , "+produccion.produc_nombre+" ; "+rel+"\n")
                            #iteraciones.append(it)


                elif pila[-1].terminal=="SI" and pila[-1].sim == entrada[i]:
                    i+=1
                    #print(i)
                    pila.pop()
                    #pile = imprimir_pila(pila,i,entrada)
                    imprimir_pila(pila,i,entrada)
                    k+=1
                    #it = iteracion(str(k),pile,entrada[i],"(q,"+entrada[i]+","+entrada[i]+";q,$)",entrada[i]+" , "+entrada[i]+"; $\n")
                    #iteraciones.append(it)
                elif pila[-1].terminal=="SI" and pila[-1].sim != entrada[i]:
                    error = True
                    print("Error")
                    state = "f"
                    break
                elif len(pila)==1 and pila[0].sim=="#":
                    pila.pop()
                    k+=1
                    #it = iteracion(str(k),"#","$","(q,$,#;f,$)","-----")
                    #iteraciones.append(it)
                    state = "f"
                    break
        elif state =="f":
            print(i)
            if i==length and error==False:
                print(entrada+" es una palabra admitida")
                k+=1
                #it = iteracion(str(k),"$","$","f","-----")
                #iteraciones.append(it)
            else:
                print("Error: "+entrada+" No es una palabra admitida")
            
            i=length+2

        #return iteraciones
                        







#pda()
from leer_gramaticas import leer_gramaticas
from grammar import simbolo
from grammar import iteracion
#----------------------------------------------------

def obtener_pila(pila,i,entrada):
    pile = ""

    pila.reverse()
    for elemento in pila:

         pile+=elemento.sim
    pila.reverse()


    return pile
#----------------------------------------------------------
def pda(gramatica):


    print("Introduzca la palabra a evaluar")
    entrada = input()
    length = len(entrada)
    state = "i"
    pila = []
    error = ""
    i=0
    k=0
    iteraciones =  []
    
    while (i<=length):

        if state=="i":
            valido = simbolo("#","NO")
            pila.append(valido)
            state = "p"

            pile = obtener_pila(pila,i,entrada)

            it = iteracion('0'," ",entrada[0],"(i,$,$;p,#)","$ , $ ; #")
            iteraciones.append(it)


        elif state =="p":
         
            inicial = simbolo(gramatica.state_inicial,"NO")
            pila.append(inicial)
            state = "q"
            k+=1
            it = iteracion(str(k),"#",entrada[i],"(p,$,$;q,"+gramatica.state_inicial+")","$ , $ ; "+gramatica.state_inicial)
            iteraciones.append(it)


        elif state == "q":
            for produccion in gramatica.producciones:
                if pila[-1].terminal=="NO" and pila[-1].sim==produccion.produc_nombre:
              
                    rel = ""
                    inv = ""
                    if len(produccion.rules)==1:
                        pile = obtener_pila(pila,i,entrada)
                        pila.pop()
                        for elem in produccion.rules:
                            elem.reverse()
                            
                            for r in elem:
                                pila.append(r)
                                rel+=r.sim
                                inv = r.sim + inv
                            elem.reverse()

                            k+=1
                            it = iteracion(str(k),pile,entrada[i],"(q,$,"+produccion.produc_nombre+";q,"+inv+")","$ , "+produccion.produc_nombre+" ; "+inv)
                            iteraciones.append(it)
                            
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

                                                        if len(produc)!=1 and i+1<=length:

                                                            if produc[1].sim == entrada[i+1]:

                                                                regla = rule
                                                                opti = True
                                                            elif regla == None:
                                                                regla = rule
                                                        elif regla == None or opti == False:
                                                                regla = rule

                                    if regla == None or opti == False:
                                        regla = rule
                                        
                            
                        if regla!=None:
                            regla.reverse()                            
                            pile = obtener_pila(pila,i,entrada)
                            pila.pop()
                            rel =""
                            inv = ""
                            for el in regla:
                                pila.append(el)
                                rel+=el.sim
                                inv = el.sim + inv


                            regla.reverse()
                            k+=1
                            it = iteracion(str(k),pile,entrada[i],"(q,$,"+pila[-1].sim+";q,"+inv+")","$ , "+produccion.produc_nombre+" ; "+inv)
                            iteraciones.append(it)


                elif pila[-1].terminal=="SI" and pila[-1].sim == entrada[i]:                    

                    k+=1                    
                    pile = obtener_pila(pila,i,entrada)
                    it = iteracion(str(k),pile,entrada[i],"(q,"+entrada[i]+","+entrada[i]+";q,$)",entrada[i]+" , "+entrada[i]+"; $")
                    iteraciones.append(it)                    
                    pila.pop()
                    i+=1


                elif pila[-1].terminal=="SI" and pila[-1].sim != entrada[i]:
                    error = "ERROR = El Simbolo Terminal en la Cima de la pila No coincide con el Caracter a evaluar en la posición: "+str(i)+" de la cadena"

                    state = "f"
                    break
                elif len(pila)==1 and pila[0].sim=="#":
                    pila.pop()
                    k+=1

                    if len(entrada)>i:
                        entry = entrada[i]
                    else:
                        entry = "$"
                    it = iteracion(str(k),"#",entry,"(q,$,#;f,$)","-----")
                    iteraciones.append(it)
                    state = "f"
                    break


        elif state =="f":

            if i==length and error=="":
                print("La cadena: "+entrada+"  fue Aceptada")
                print()
                k+=1
                it = iteracion(str(k)," $ "," $ ","f","-----")
                iteraciones.append(it)
                it = iteracion("#","AP_"+gramatica.nombre,"","La Cadena = "+entrada+"  fue Aceptada",entrada)
                iteraciones.append(it)

            elif error !="" and i!=length:
                print("La cadena: "+entrada+"NO  fue Aceptada")
                print()
                it = iteracion("&","AP_"+gramatica.nombre,error,"La Cadena = "+entrada+" No fue Aceptada",entrada)
                iteraciones.append(it)                

            else:
                print("La cadena: "+entrada+"NO  fue Aceptada")
                print()
                it = iteracion("&","AP_"+gramatica.nombre,"ERROR = En la cima de la pila esta el simbolo de aceptación,  pero no se ha terminado de recorrer la cadena ","La Cadena = "+entrada+" No fue Aceptada", entrada)
                iteraciones.append(it)
            
            i=length+2

    return iteraciones
                        
def iterar(iteraciones):
    for tk in iteraciones:
        if tk.id!="&":
            print(tk.id,end=" | ")
            print(tk.pila, end=" | ")
            print(tk.entrada, end=" | ")
            print(tk.transicion, end=" | ")
            print()

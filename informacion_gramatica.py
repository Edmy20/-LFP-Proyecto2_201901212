import os 
def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")    

def seleccionar(m,y,gramaticas):
    print("Estas son "+y+"Cargadas en Memoria:")
    n = 0
    for gra in gramaticas:
        n+=1
        print(str(n)+". "+m+gra.nombre)
    
    print()
    print("Ingrese el numero correspondiente a su elección:")
    nombre = input()
    n=0

    for g in gramaticas:
        n+=1
        if str(n) == nombre:
            gramatica = g

    return gramatica


def mostrar_gramatica(gramaticas):
    gramatica = seleccionar("","las Gramaticas ",gramaticas)
    print()
    print("__________________________________________________________________________")
    gt = " , ".join(gramatica.sim_Noterminales)
    gn = " , ".join(gramatica.sim_terminales)
    print("Nombre de la Gramatica tipo 2: "+gramatica.nombre)
    print("No Terminales = { "+gn+" }")
    print("Terminales = { "+gt+" }")


    print("No terminal Inicial: ",gramatica.state_inicial)
    print("Producciones: ")
    gramatica.imprimir_gramatica()
    print("====================================")
    print("Para regresar al Menu Principal Presione: ENTER")
    en = input()
    borrarPantalla()

def llenar_transformaciones(gramatica):

    transformaciones = ""
    for produccion in gramatica.producciones:

        for rule in produccion.rules:
            transformaciones+="$ , "+produccion.produc_nombre+" ; "
            for r in rule:
                transformaciones+=r.sim
            transformaciones+="\n"

    return transformaciones

def llenar_ter(terminales):
    ter = ""
    for t in terminales:
        ter+=t+" , "+t+"; $\n"

    return ter

def label_grafo(gramatica):

    etiqueta = """a [shape = none label=<<table border="0" cellborder="1" cellspacing="0">
    <tr><td COLSPAN="2" BGCOLOR="skyblue">Nombre:"""
    etiqueta += "AP_"+gramatica.nombre+"</td></tr>"
    etq1=" , ".join(gramatica.sim_terminales)
    etiqueta += '<tr><td BGCOLOR="lightblue1">Terminales</td><td>'+etq1+'</td></tr>'
    etq2=" , ".join(gramatica.sim_Noterminales)
    etiqueta+= '<tr><td BGCOLOR="lightblue1" >No Terminales</td><td>'+etq2+'</td></tr>'
    etiqueta+= '<tr><td BGCOLOR="lightblue1" >Alfabeto de Pila</td><td>'+etq1+' , '+etq2+' , #</td></tr>'
    etiqueta+= '<tr><td BGCOLOR="lightblue1" >Estados</td><td> i , p , q , f  </td></tr>'
    etiqueta+= '<tr><td BGCOLOR="lightblue1" >Estado Inicial</td><td> i </td></tr>'
    etiqueta+= '<tr><td BGCOLOR="lightblue1" >Simbolo Inicial</td><td>'+gramatica.state_inicial+'</td></tr>'
    etiqueta+= """<tr><td BGCOLOR="lightblue1" >Estado de Aceptación</td><td> f </td></tr>
    </table>>]"""

    return etiqueta
    

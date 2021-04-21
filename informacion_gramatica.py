import os 
def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")    

def seleccionar_gramatica(gramaticas):
    borrarPantalla()
    print("Estas son las Gramáticas Cargadas en Memoria:")
    for gra in gramaticas:
        print("->"+gra.nombre)
    
    print()
    print("Ingrese el nombre de la gramatica a seleccionar:")
    nombre = input()

    for g in gramaticas:
        if g.nombre == nombre:
            gramatica = g

    return gramatica


def mostrar_gramatica(gramaticas):
    gramatica = seleccionar_gramatica(gramaticas)
    print()
    print("__________________________________________________________________________")
    print("Nombre de la Gramatica tipo 2: "+gramatica.nombre)
    print("No terminales: ",end="")
    print(gramatica.sim_Noterminales)
    print("Terminales: ",end="")
    print(gramatica.sim_terminales)
    print("No terminal Inicial: ",gramatica.state_inicial)
    print("Producciones: ")
    gramatica.imprimir_gramatica()

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
    etiqueta = "AP_"+gramatica.nombre+"\n"
    etiqueta += "Terminales = {"
    etq1=",".join(gramatica.sim_terminales)
    etiqueta+=etq1+"}\n"

    etiqueta+="No Terminales = {"
    etq2=",".join(gramatica.sim_Noterminales)
    etiqueta+=etq2+"}\n"

    etiqueta+="Alfabeto de Pila = {"+etq1+","+etq2+"#}\n"
    etiqueta+="Estados = {i,p,q,f}\nEstado Inical = {i}\nEstado de Aceptacion = {f}"

    return etiqueta
    

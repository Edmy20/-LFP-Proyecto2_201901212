from tkinter import Tk
from grammar import *
from tkinter.filedialog import askopenfilename

def cargar():
    Tk().withdraw()
    ruta = askopenfilename() 
    return ruta

def validar_gramatica(grammar):
    libre_contexto = "NO"
    
    for regla in grammar.producciones:
        
        for rule in regla.rules:
            size = len(rule)
            for r in range(size):

                if r!=1:
                    if rule[r].terminal == 'NO':
                        libre_contexto = 'SI'


    
    return libre_contexto



def definir_termino(terminales,no_terminales,der_produc):
    definido = []

    for term in der_produc:
        for ter in terminales:
            if ter == term:
                simb = simbolo(term,"SI")
        for termino in no_terminales:
            if termino == term:
                simb = simbolo(term,"NO")

        definido.append(simb)
    
    return definido

def agrupar_producciones(no_terminales, producciones):

    productions = []

    for nt in no_terminales:
        production = []
        for p in producciones:
            if p.produc_nombre == nt:
                production.append(p.rules)
        
        pros = produccion(nt,production)
        productions.append(pros)
    
    return productions
    


def leer_gramaticas():
    root = cargar()
    f = open (root,'r')
    n=0
    gramaticas = []

    for linea in f:
      if linea[0]!=" ":
        if n==0:
            name = linea.strip("\n")
            producciones = []
            n+=1
        elif n==1:
            terminos = linea.split(";")
            no_terminales= terminos[0].split(",")
            terminales = terminos[1].split(",")
            terminal_inicial = terminos[2].strip("\n")
            n+=1
        elif n==2 and linea[0]!="*":
            produc = linea.split("->")
            der_produc = produc[1].split()
            producs = definir_termino(terminales,no_terminales,der_produc)
            prod = produccion(produc[0],producs)
            producciones.append(prod)

        elif linea[0]=="*":
            n=0
            reglas = agrupar_producciones(no_terminales,producciones)
            grammar = gramatica(name,reglas,terminales,no_terminales,terminal_inicial)
            add_grammar = validar_gramatica(grammar)
            if add_grammar == 'SI':
                gramaticas.append(grammar)

           
    f.close()
    print()
    print("=================")
    print("!Archivo Cargado¡")
    print("=================")
    print()

    
    return gramaticas

import time
from leer_gramaticas import leer_gramaticas
from automata_pila import pda
from automata_pila import iterar
from informacion_gramatica import mostrar_gramatica
from informacion_gramatica import seleccionar
from pda_grafo import grafo_pda
from reporte import reportar
from recorrido import grafo_pda_recorrido

seguir = True
es = True

def esperar():
    for n in range(1,6):
        time.sleep(1)
        print(n)
        
while seguir:
    print("___________________________________ AUTOMATA DE PILA _____________________________________")
    print(">Edmy Marleny Mendoza Pol\n>201901212\n>Curso: Lenguajes Formales y de Programación\n>Seccion: A+")
    print("___________________________________________________________________________________________")
    if es:
        esperar()
        print("=============================================================================================")
        print("                                          !BIENVENIDO¡                          ")
        print("=============================================================================================")
    print("===============================Opciones del Menú Principal===================================")
    print("1.Cargar Archivo\n2.Mostrar Informción General de la Gramática\n3.Generar Autómata de Pila Equivalente")
    print("4.Reporte de Recorrido\n5.Reporte en Tabla\n6.Salir")

    op = input()

    if op=='1':
        gramaticas = leer_gramaticas()
        es = False
    elif op=='2':
        mostrar_gramatica(gramaticas)
        es = False
    elif op=='3':
        grafo_pda(gramaticas)
    elif op=='4':
        gramatica = seleccionar("AP_","los Automatas de Pila ",gramaticas)
        iteraciones = pda(gramatica)
        grafo_pda_recorrido(gramatica,iteraciones)
        es = False
        print()
    elif op=='5':
        gramatica = seleccionar("AP_","los Automatas de Pila ",gramaticas)
        ap = pda(gramatica)
        reportar("",ap)
        es = False
    elif op=='6':
        seguir=False


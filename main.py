import time
from leer_gramaticas import leer_gramaticas
from automata_pila import pda
from informacion_gramatica import mostrar_gramatica
#from informacion_gramatica import llenar_transformaciones
from informacion_gramatica import seleccionar_gramatica
from pda_grafo import grafo
from pda_grafo import grafo_pda
#from informacion_gramatica import label_grafo
#from informacion_gramatica import llenar_ter
seguir = True

def esperar():
    for n in range(1,6):
        time.sleep(1)
        print(n)
        
while seguir:
    print("___________________________________ AUTOMATA DE PILA  _____________________________________")
    print(">Edmy Marleny Mendoza Pol\n>201901212\n>Seccion: A+")
    print("___________________________________________________________________________________________")
    #esperar()
    print("---------!Bienvenido¡-------------")
    print("-------------------------Opciones del Menú Principal---------------------------------------")
    print("1.Cargar Archivo\n2.Mostrar Informción General de la Gramática\n3.Generar Autómata de Pila Equivalente")
    print("4.Reporte de Recorrido\nReporte en Tabla\n6.Salir")

    op = input()

    if op=='1':
        gramaticas = leer_gramaticas()
    elif op=='2':
        mostrar_gramatica(gramaticas)
    elif op=='3':
        grafo_pda(gramaticas)
    elif op=='4':
        pda(gramaticas)
        print()
    elif op=='5':
        print("5")
    elif op=='6':
        seguir=False


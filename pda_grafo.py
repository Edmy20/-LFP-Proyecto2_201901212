from graphviz import Digraph
from graphviz import Source
from informacion_gramatica import *
import pydot
import webbrowser

def generar_pda(nombre):
    contenido = '<divt>'+nombre+'<divt>'
    contenido+=  '<p><img src="Templates/'+nombre+'.png"></p>'
    t = open("Templates/template_pda.html",'r')
    f = open("Reporte_"+nombre+".html",'w',encoding="utf-8")
    template = t.read()
  
    cuerpo = template % (contenido)
    f.write(cuerpo)
    t.close()
    f.close()

    webbrowser.open_new_tab("Reporte_"+nombre+".html")

def grafo_pda(gramaticas):
    gramatica = seleccionar("","las Gramaticas ",gramaticas)

    dott = """digraph { 
        graph [rankdir=LR]
        i [label=i shape=circle style=filled fillcolor=skyblue]
        p [label=p shape=circle style=filled fillcolor=skyblue]
        q [label=q height=1 shape=circle width = 1 style=filled fillcolor=skyblue]
        f [label=f shape=doublecircle style=filled fillcolor=skyblue]"""

    etq = label_grafo(gramatica)
    dott+=etq

    etq1= llenar_transformaciones(gramatica)
    etq2 = llenar_ter(gramatica.sim_terminales)

    dott+='i -> p [label ="$ , $ ; #"]'
    dott+='p -> q [label="$ , $ ; '+gramatica.state_inicial+'"]'
    dott+='q:s -> q:s [label="'+etq2+'"]'
    dott+='q:n -> q:n [label="'+etq1+'"]'
    dott+= 'q -> f [label="$ , # , $"]}'

    nom = 'AP_'+gramatica.nombre



    src = Source(dott)
    src.render("Templates/"+nom, format = 'png')
    print()
    print("=========================================")
    print("       AUTOMATA GENERADO EXITOSAMENTE    ")
    print("=========================================")
    print()

    generar_pda(nom)





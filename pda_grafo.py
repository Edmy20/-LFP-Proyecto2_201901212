from graphviz import Digraph
from graphviz import Source
from informacion_gramatica import *
import pydot



def grafo(gramaticas):
    
    gramatica = seleccionar_gramatica(gramaticas)

    dot = Digraph('pda', filename='pda.gv')
    dot.attr(rankdir='LR', size='8,5')

    etq = label_grafo(gramatica)

    dot.attr(label=etq)
    dot.attr('node', shape='circle')
    dot.node('i')
    dot.node('p')
    dot.attr('node', shape='doublecircle')
    dot.node('f')
    dot.attr('node',shape='circle', height='1',width='1')
    dot.node('q')


    etq1= llenar_transformaciones(gramatica)
    etq2 = llenar_ter(gramatica.sim_terminales)



    dot.edge('i', 'p', label='$,$;#')
    dot.edge('p', 'q', label='$,$;'+gramatica.state_inicial)
    dot.edge('q', 'q', label=etq1+etq2)
    dot.edge('q', 'f', label='$,#,$')



    dot.view()
def crear_imagen_png(nombre):
    (graph,) = pydot.graph_from_dot_file("AP_"+nombre+".dot")
    #graph.write_png("AP_"+nombre+".pdf")
    graph.write("AP_"+nombre+".pdf")

def grafo_pda(gramaticas):
    gramatica = seleccionar_gramatica(gramaticas)

    dott = """digraph { 
        graph [rankdir=LR]
        i [label=i shape=circle]
        p [label=p shape=circle]
        q [label=q height=1 shape=circle width = 1]
        f [label=f shape=doublecircle]"""

    etq = label_grafo(gramatica)
    dott+="t [label = "+'"'+etq+'" shape=box]'

    etq1= llenar_transformaciones(gramatica)
    etq2 = llenar_ter(gramatica.sim_terminales)

    dott+='i -> p [label ="$ , $ ; #"]'
    dott+='p -> q [label="$ , $ ; '+gramatica.state_inicial+'"]'
    dott+='q:s -> q:s [label="'+etq2+'"]'
    dott+='q:n -> q:n [label="'+etq1+'"]'
    dott+= 'q -> f [label="$ , # , $"]}'

    file = open("AP_"+gramatica.nombre+".gv", "w")
    file.write(dott)
    file.close()

    #crear_imagen_png(gramatica.nombre)
    s = Source(dott, filename="AP_"+gramatica.nombre+".gv", format="pdf")
    s.view()



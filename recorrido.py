from graphviz import Digraph
from graphviz import Source
from graphviz import render
from informacion_gramatica import *
import pydot
import webbrowser

#-------------------------------------------------------------
def colorear_noterminales(gramatica,iteracion):

    noter = ""
    etq1 = []
    for produccion in gramatica.producciones:

        for rule in produccion.rules:
            transformaciones="$ , "+produccion.produc_nombre+" ; "
            for r in rule:
                transformaciones+=r.sim

            etq1.append(transformaciones)

    for a in etq1: 
        if a == iteracion.cambio:

            noter+='<tr><td><FONT COLOR="blue">'+a+'</FONT></td></tr>'
        else:
            noter+='<tr><td>'+a+'</td></tr>'

    return noter


#-------------------------------------------------------------------------
def colorear_terminos(terminales, iteracion):
    ter = ""
    etq2 = []
    for t in terminales:
        termi=t+" , "+t+"; $"
        etq2.append(termi)

    for a in etq2: 
        if a == iteracion.cambio:

            ter+='<tr><td><FONT COLOR="blue">'+a+'</FONT></td></tr>'
        else:
            ter+='<tr><td>'+a+'</td></tr>'

    return ter

#---------------------------------------------------------------------------            
def definir_estado(e,inicial,iteracion,m):
    estados = ""

    if e == "0":
        estados =  """digraph { 
        graph [rankdir=LR]
        i [label=<i> shape=circle style=filled fillcolor=skyblue]
        p [label=p shape=circle style=filled fillcolor=azure2]
        q [label=q height=1 shape=circle width = 1 style=filled fillcolor=azure2]
        f [label=f shape=doublecircle style=filled fillcolor=azure2]
        i -> p [label =<<FONT COLOR="blue">$ , $ ; #</FONT>>]
        q -> f [label =<$ , # ; $>]
        p -> q [label =<$ , $ ; """
        estados+=inicial+">]"

        estados+= """a [shape = none label=<<table border="0" cellborder="1" cellspacing="0">
<tr><td BGCOLOR="lightblue1">Iteracion</td><td BGCOLOR="lightblue1"><b>0</b></td></tr>
<tr><td BGCOLOR="lightblue1" >Pila</td><td>  </td></tr>
<tr><td BGCOLOR="lightblue1" >Entrada</td><td>  </td></tr>
</table>>]"""
    elif e== "1":
        estados =  """digraph { 
        graph [rankdir=LR]
        i [label=<i> shape=circle style=filled fillcolor=azure2]
        p [label=p shape=circle  style=filled fillcolor=skyblue]
        q [label=q height=1 shape=circle width = 1 style=filled fillcolor=azure2]
        f [label=f shape=doublecircle style=filled fillcolor=azure2]
        i -> p [label =<$ , $ ; #>]
        q -> f [label =<$ , # ; $>]"""
        estados +='p -> q [label =<<FONT COLOR="blue">$ , $ ; '+inicial+'</FONT>>]'

        estados+="""a [shape = none label=<<table border="0" cellborder="1" cellspacing="0">
        <tr><td BGCOLOR="lightblue1">Iteracion</td><td BGCOLOR="lightblue1"><b>"""
        estados+=str(iteracion.id)+"</b></td></tr>"
        estados+='<tr><td BGCOLOR="lightblue1">Pila</td><td> # </td></tr>'
        estados+='<tr><td BGCOLOR="lightblue1" >Entrada</td><td>'+iteracion.entrada+'</td></tr></table>>]'
    elif e == "f":
        estados =  """digraph { 
        graph [rankdir=LR]
        i [label=<i> shape=circle style=filled fillcolor=azure2]
        p [label=p shape=circle style=filled fillcolor=azure2]
        q [label=q height=1 shape=circle width = 1 style=filled fillcolor=azure2]
        f [label=f shape=doublecircle style=filled fillcolor=skyblue]
        i -> p [label =<$ , $ ; #>]
        p -> q [label =<$ , $ ; """
        estados+=inicial+">]"
        estados+='q->f [label =<$ , # ; $>]'

        estados+="""a [shape = none label=<<table border="0" cellborder="1" cellspacing="0">
        <tr><td BGCOLOR="lightblue1">Iteracion</td><td BGCOLOR="lightblue1"><b>"""
        estados+=str(iteracion.id)+"</b></td></tr>"
        estados+='<tr><td BGCOLOR="lightblue1">Pila</td><td>  </td></tr>'
        estados+='<tr><td BGCOLOR="lightblue1" >Entrada</td><td> </td></tr></table>>]'
        estados+="h [label=<¡La cadena ingresada es válida!> shape=note style=filled fillcolor=skyblue]"
    else:
        estados =  """digraph { 
        graph [rankdir=LR]
        i [label=<i> shape=circle style=filled fillcolor=azure2]
        p [label=p shape=circle style=filled fillcolor=azure2]
        q [label=q height=1 shape=circle width = 1 style=filled fillcolor=skyblue]
        f [label=f shape=doublecircle style=filled fillcolor=azure2]
        i -> p [label =<$ , $ ; #>]
        p -> q [label =<$ , $ ; """
        estados+=inicial+">]"

        if iteracion.pila == "#" and iteracion.transicion =="(q,$,#;f,$)" and iteracion.entrada == " $ ":
            estados+='q->f [label =<<FONT COLOR="blue">$ , # ; $</FONT>>]'
            estados+="""a [shape = none label=<<table border="0" cellborder="1" cellspacing="0">
            <tr><td BGCOLOR="lightblue1">Iteracion</td><td BGCOLOR="lightblue1"><b>"""
            estados+=str(iteracion.id)+"</b></td></tr>"
            estados+='<tr><td BGCOLOR="lightblue1">Pila</td><td> # </td></tr>'
            estados+='<tr><td BGCOLOR="lightblue1" >Entrada</td><td> </td></tr></table>>]'
            
        else:
            estados+="q -> f [label =<$ , # ; $>]"
            estados+="""a [shape = none label=<<table border="0" cellborder="1" cellspacing="0">
            <tr><td BGCOLOR="lightblue1">Iteracion</td><td BGCOLOR="lightblue1"><b>"""
            estados+=str(iteracion.id)+"</b></td></tr>"
            estados+='<tr><td BGCOLOR="lightblue1">Pila</td><td>'+iteracion.pila+'</td></tr>'
            estados+='<tr><td BGCOLOR="lightblue1" >Entrada</td><td>'+iteracion.entrada+'</td></tr></table>>]'
            if iteracion.id == str(m-2):
                estados+="h [label=<¡La cadena ingresada NO es válida!> shape=note style=filled fillcolor=skyblue]"

        
    
    return estados
#--------------------------------------------------------------------------
def escribir_recorrido(nombre,iteraciones):

    n = 0

    contenido = '<divt><center>Recorrido: AP_'+nombre+'</center></divt><br>'
    contenido += """<center><table class="todo">"""

    for iteracion in iteraciones:
        if iteracion.id != "#" and iteracion.id!="&":
            if n==0:
                contenido+='<tr>'
                nom = "Templates/imagen"+iteracion.id
                contenido+='<td><img src='+nom+'.png style="display:block;" width="100%" height="100%"></td>'
                n+=1
            elif n==1:
                nom = "Templates/imagen"+iteracion.id
                contenido+='<td><img src='+nom+'.png style="display:block;" width="100%" height="100%" ></td>'
                n+=1
            elif n==2:
                n=0
                nom = "Templates/imagen"+iteracion.id
                contenido+='<td><img src='+nom+'.png  style="display:block;" width="100%" height="100%"></td></tr>'
        else:
            contenido+='</table></center>'
            
    contenido += "<h1>"+iteraciones[-1].transicion+"</h1>"
    contenido += "<h3>"+iteraciones[-1].entrada+"</h3>"
    
    return contenido
#--------------------------------------------------------------------------
def reportar_recorrido(nombre, iteraciones):
    contenido = escribir_recorrido(nombre,iteraciones)
    t = open("Templates/template_recorrido.html",'r')
    f = open('Reporte_Recorrido_AP_'+nombre+'.html','w',encoding="utf-8")
    template = t.read()
  
    cuerpo = template % (contenido)
    f.write(cuerpo)
    t.close()
    f.close()

    webbrowser.open_new_tab('Reporte_Recorrido_AP_'+nombre+'.html')

#-----------------------------------------------------------------------
def grafo_pda_recorrido(gramatica,iteraciones):


    for iteracion in iteraciones:

        if iteracion.transicion == "f":
            dott = definir_estado("f",gramatica.state_inicial,iteracion,len(iteraciones))
        else:
            dott = definir_estado(iteracion.id,gramatica.state_inicial,iteracion,len(iteraciones))
        
        ter = colorear_terminos(gramatica.sim_terminales,iteracion)
        noter = colorear_noterminales(gramatica, iteracion)


        dott+="q:s -> q:s [label=<<table BORDER='0' CELLBORDER='0' CELLSPACING='0'>"+ter+"</table>>]"
        dott+="q:n -> q:n [label=<<table BORDER='0' CELLBORDER='0' CELLSPACING='0'>"+noter+"</table>>]}"


        if iteracion.id != "#" and iteracion.id!="&":
            nom = "Templates/imagen"+iteracion.id
            src = Source(dott)
            src.render(nom, format = 'png')
    print()

    print("=============================================")
    print(" REPORTE DE RECORRIDO GENERADO EXITOSAMENTE  ")
    print("=============================================")
    print()
    reportar_recorrido(gramatica.nombre,iteraciones)
            
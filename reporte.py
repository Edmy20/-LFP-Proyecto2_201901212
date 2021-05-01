import webbrowser


def escribir_reporte(nombre, iteraciones):
    encabezados = "<h1>Tabla: "+iteraciones[-1].pila+"</h1>"
    encabezados += "<h2>"+iteraciones[-1].transicion+"</h2>"
    
    encabezados += """<center>
    <table class="default">
                            <tr>
                                <th scope="row">ITERACIÓN</th>
                                <th> PILA<- </th>
                                <th> ENTRADA </th>
                                <th> TRANSICIONES </th>
                            </tr>"""  
    no_tk = """              <tr>
                                <th>%s</th>"""      
    tk_fila =             """ <td>%s</td>"""
    fin_fila=                   """ </tr>"""
    fin      =            """ </table></center>"""

    contenido = encabezados

    for tk in iteraciones:
        if tk.id!="&" and tk.id != "#":
            contenido+= no_tk % (str(tk.id))
            contenido+= tk_fila % (str(tk.pila))
            contenido+= tk_fila % (str(tk.entrada))
            contenido+= tk_fila % (str(tk.transicion))
            contenido+= fin_fila     
    contenido += fin
    contenido += "<h3>"+iteraciones[-1].entrada+"</h3>"
    
    return contenido


def reportar(nombre, iteraciones):
  contenido = escribir_reporte(nombre,iteraciones)
  t = open("Templates/template_reporte.html",'r')
  f = open('Reporte_Tabla_'+iteraciones[-1].pila+'.html','w',encoding="utf-8")
  template = t.read()
  
  cuerpo = template % (contenido)
  f.write(cuerpo)
  t.close()
  f.close()
  print()
  print("=========================================")
  print(" REPORTE EN TABLA GENERADO EXITOSAMENTE  ")
  print("=========================================")
  print()

  webbrowser.open_new_tab('Reporte_Tabla_'+iteraciones[-1].pila+'.html')
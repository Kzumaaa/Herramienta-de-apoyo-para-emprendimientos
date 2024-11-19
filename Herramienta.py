from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import os
import csv
import re

listaPersona = ["Persona Natural", "Persona Juridica"]
listaTrl = ["TRL 1-3", "TRL 1-5", "TRL 3-7", "TRL 4-6", "TRL 6-9"]
listaAntig = ["No requerido", "Menor a 12 meses", "Entre 12-24 meses", "Entre 24-36 meses", "Mayor a 36 meses"]
listaSector = ["Inteligencia Artificial", "Biotecnologia", "Fintech", "Tecnologias Limpias", "Software", "Todos"] 
listaNvVentas = ["Sin ventas", "0UF-2.400 UF", "2.400UF-25.000UF", "25.000-100.000UF"] 
listaVinculoUni = ["Sin vinculo universitario", "Si(Estudiante o egresado)", "Si(Colaboracion con universidades)"] 
listaCofinanciamiento = ["Sin cofinanciamiento", "Si(20% aporte propio)", "Si(30% aporte propio)", "Si(40% aporte propio)"] 
listaID = ["Bajo", "Moderado", "Moderado a alto", "Alto", "Muy alto"]
listaTraccionC = ["No requerido", "Con validacion de mercado", "Con traccion inicial(0UF-350UF)", "Con validacion inicial(350UF-1750UF)", "Con alta traccion comercial(Mas de 1750UF)"]

# Listas auxiliares para usuario

listaTrl_Usuario = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5", "Nivel 6", "Nivel 7", "Nivel 8", "Nivel 9"]
listaSector_Usuario = ["Inteligencia Artificial", "Biotecnologia", "Fintech", "Tecnologias Limpias", "Software"] 
# listaNvVentas_Usuario = ["0UF-2.400 UF", "2.400UF-25.000UF", "25.000-100.000UF"]
# listaVinculoUni_Usuario = ["Sin vinculo universitario", "Si(Estudiante o egresado)", "Si(Colaboracion con universidades)"]
listaID_Usuario = ["Bajo", "Moderado", "Alto", "Muy alto"]
# listaTraccionC_Usuario = ["Sin traccion comercial", "Con validacion de mercado", "Con traccion inicial(0UF-350UF)", "Con validacion inicial(350UF-1750UF)", "Con alta traccion comercial(Mas de 1750UF)"]

info = []
recomendacion = []

contador = 0

def aumentar_contador():
    global contador
    contador += 1
    
def disminuir_contador():
    global contador
    if contador != 0:
        contador -= 1
    
def guardar_data(nombre,tpersona,trl,antiguedad,sector,NVentas,VinculoUni,Cofinan,ID,TraccionC,Descripcion,subwindow):
    
    if nombre and tpersona and trl and antiguedad and sector and NVentas and VinculoUni and Cofinan and ID and TraccionC and Descripcion:
        datos = [nombre, tpersona, trl, antiguedad, sector, NVentas, VinculoUni, Cofinan, ID, TraccionC, Descripcion]
        lectura = []
         
        if os.path.isfile('datos.csv'):
            with open("datos.csv", "r") as text:
                for row in text:
                    parte = row.split(',')
                    if parte:
                        lectura.append(parte[0].strip())
            
        if nombre not in lectura:
            with open("datos.csv", "a", newline='') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(datos)
            
            messagebox.showinfo(message="Agregado con éxito", title="Aviso", parent=subwindow)
        else:
            messagebox.showwarning(title="Error", message="Este nombre ya esta utilizado", parent=subwindow)

    else:
        messagebox.showwarning(title="Error", message="Faltan datos", parent=subwindow)

def visualizar_data():
    global info
    global contador
    datos = []
    with open("datos.csv", "r") as text: # 2
        for row in text:
            datos.append(row)

    if contador < len(datos): # si el contador es 1 < 2
        info = datos[contador].split(',')
    else:
        contador = len(datos)-1

def agregar_fuente_financiamiento():
    boton_dos.config(state=DISABLED)

    subwindow = Toplevel(root)
    subwindow.geometry("1024x768")
    subwindow.title("Agregar nueva fuente de financiamiento")

    frame = Frame(subwindow)
    frame.pack(pady=40)

    user_info_frame = LabelFrame(frame, text="Nueva fuente de financiamiento")
    user_info_frame.pack(fill="both", expand="yes")

    # Seccion de labels

    nombre_emp_label = Label(user_info_frame, text="Nombre")
    persona_label = Label(user_info_frame, text="Tipo de persona")
    trl_label = Label(user_info_frame, text="Escala de madurez tecnologica (Trl)")
    antiguedad_label = Label(user_info_frame,text="Antiguedad de la empresa")
    sector_label = Label(user_info_frame,text="Sector")
    ventas_anuales_label = Label(user_info_frame, text="Nivel de ventas")
    vinculo_universidad_label = Label(user_info_frame, text="Vinculo con universidad")
    cofinanciamiento_label = Label(user_info_frame, text="Cofinanciamiento")
    componenteid_label = Label(user_info_frame, text="Componente de I+D (Investigacion y Desarrollo)")
    traccion_comercial_label = Label(user_info_frame, text="Traccion comercial")
    descripcion_label = Label(user_info_frame, text="Descripcion")

    # Seccion donde el moderador ingresa los datos

    nombre_emp_entry = Entry(user_info_frame,width=25)
    persona_combobox = Combobox(user_info_frame, values=listaPersona, state="readonly",width=25)
    trl_combobox = Combobox(user_info_frame, values=listaTrl, state="readonly",width=25)
    antiguedad_combobox = Combobox(user_info_frame, values=listaAntig, state="readonly",width=25)
    sector_combobox = Combobox(user_info_frame, values=listaSector, state="readonly",width=25)
    ventas_anuales_combobox = Combobox(user_info_frame, values=listaNvVentas, state="readonly",width=25)
    vinculo_universidad_combobox = Combobox(user_info_frame, values=listaVinculoUni, state="readonly",width=30)
    cofinanciamiento_combobox = Combobox(user_info_frame, values=listaCofinanciamiento, state="readonly",width=25)
    componenteid_combobox = Combobox(user_info_frame, values=listaID, state="readonly",width=25)
    traccion_comercial_combobox = Combobox(user_info_frame, values=listaTraccionC, state="readonly",width=40)
    descripcion_entry = Entry(user_info_frame, width=60)

    # Posicionamiento de labels, entry, combobox

    nombre_emp_label.grid(row=0, column=0)
    nombre_emp_entry.grid(row=1, column=0)
    persona_label.grid(row=2, column=0)
    persona_combobox.grid(row=3, column=0)
    trl_label.grid(row=4, column=0)
    trl_combobox.grid(row=5, column=0)
    antiguedad_label.grid(row=6, column=0)
    antiguedad_combobox.grid(row=7, column=0)
    sector_label.grid(row=8, column=0)
    sector_combobox.grid(row=9, column=0)
    ventas_anuales_label.grid(row=10, column=0)
    ventas_anuales_combobox.grid(row=11, column=0)
    vinculo_universidad_label.grid(row=12, column=0)
    vinculo_universidad_combobox.grid(row=13, column=0)
    cofinanciamiento_label.grid(row=14, column=0)
    cofinanciamiento_combobox.grid(row=15, column=0)
    componenteid_label.grid(row=16, column=0)
    componenteid_combobox.grid(row=17, column=0)
    traccion_comercial_label.grid(row=18, column=0)
    traccion_comercial_combobox.grid(row=19, column=0)
    descripcion_label.grid(row=20, column=0)
    descripcion_entry.grid(row=21, column=0)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=40, pady=4)

    # Botones

    boton_cierre = Button(user_info_frame, text="Volver",command=lambda: [subwindow.destroy(),boton_dos.config(state=NORMAL)])
    boton_cierre.grid(row=23, column=0, sticky="news")

    boton_guardado = Button(user_info_frame, text="Guardar", command=lambda: guardar_data(nombre_emp_entry.get(), persona_combobox.get(), trl_combobox.get(), antiguedad_combobox.get(), sector_combobox.get(), ventas_anuales_combobox.get(), vinculo_universidad_combobox.get(), cofinanciamiento_combobox.get(), componenteid_combobox.get(), traccion_comercial_combobox.get(), descripcion_entry.get(),subwindow))
    boton_guardado.grid(row=22, column=0, sticky="news")

def compatibilidad_fuente_financiamiento():
    boton_uno.config(state=DISABLED)

    subwindow = Toplevel(root)
    subwindow.geometry("1024x768")
    subwindow.title("Compatibilidad con fuente de financiamiento")

    frame = Frame(subwindow)
    frame.pack(pady=40)

    user_info_frame = LabelFrame(frame, text="Ingrese sus datos")
    user_info_frame.pack(fill="both", expand="yes")

    # Seccion de labels

    nombre_emp_label = Label(user_info_frame, text="Nombre")
    persona_label = Label(user_info_frame, text="Tipo de persona")
    trl_label = Label(user_info_frame, text="Escala de madurez tecnologica (Trl)")
    antiguedad_label = Label(user_info_frame,text="Antiguedad de la empresa")
    sector_label = Label(user_info_frame,text="Sector")
    ventas_anuales_label = Label(user_info_frame, text="Nivel de ventas")
    vinculo_universidad_label = Label(user_info_frame, text="Vinculo con universidad")
    cofinanciamiento_label = Label(user_info_frame, text="Cofinanciamiento")
    componenteid_label = Label(user_info_frame, text="Componente de I+D (Investigacion y Desarrollo)")
    traccion_comercial_label = Label(user_info_frame, text="Traccion comercial")

    # Seccion donde el moderador ingresa los datos

    nombre_emp_entry = Entry(user_info_frame,width=25)
    persona_combobox = Combobox(user_info_frame, values=listaPersona, state="readonly",width=25)
    trl_combobox = Combobox(user_info_frame, values=listaTrl_Usuario, state="readonly",width=25)
    antiguedad_combobox = Combobox(user_info_frame, values=listaAntig, state="readonly",width=25)
    sector_combobox = Combobox(user_info_frame, values=listaSector_Usuario, state="readonly",width=25)
    ventas_anuales_combobox = Combobox(user_info_frame, values=listaNvVentas, state="readonly",width=25)
    vinculo_universidad_combobox = Combobox(user_info_frame, values=listaVinculoUni, state="readonly",width=30)
    cofinanciamiento_combobox = Combobox(user_info_frame, values=listaCofinanciamiento, state="readonly",width=25)
    componenteid_combobox = Combobox(user_info_frame, values=listaID_Usuario, state="readonly",width=25)
    traccion_comercial_combobox = Combobox(user_info_frame, values=listaTraccionC, state="readonly",width=40)

    # Posicionamiento de labels, entry, combobox

    nombre_emp_label.grid(row=0, column=0)
    nombre_emp_entry.grid(row=1, column=0)
    persona_label.grid(row=2, column=0)
    persona_combobox.grid(row=3, column=0)
    trl_label.grid(row=4, column=0)
    trl_combobox.grid(row=5, column=0)
    antiguedad_label.grid(row=6, column=0)
    antiguedad_combobox.grid(row=7, column=0)
    sector_label.grid(row=8, column=0)
    sector_combobox.grid(row=9, column=0)
    ventas_anuales_label.grid(row=10, column=0)
    ventas_anuales_combobox.grid(row=11, column=0)
    vinculo_universidad_label.grid(row=12, column=0)
    vinculo_universidad_combobox.grid(row=13, column=0)
    cofinanciamiento_label.grid(row=14, column=0)
    cofinanciamiento_combobox.grid(row=15, column=0)
    componenteid_label.grid(row=16, column=0)
    componenteid_combobox.grid(row=17, column=0)
    traccion_comercial_label.grid(row=18, column=0)
    traccion_comercial_combobox.grid(row=19, column=0) 

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=40, pady=4)

    # Botones

    boton_cierre = Button(user_info_frame, text="Volver",command=lambda: [subwindow.destroy(),boton_uno.config(state=NORMAL)])
    boton_cierre.grid(row=23, column=0, sticky="news")

    boton_guardado = Button(user_info_frame, text="Consultar", command=lambda: comparar_data(nombre_emp_entry.get(), persona_combobox.get(), trl_combobox.get(), antiguedad_combobox.get(), sector_combobox.get(), ventas_anuales_combobox.get(), vinculo_universidad_combobox.get(), cofinanciamiento_combobox.get(), componenteid_combobox.get(), traccion_comercial_combobox.get(),subwindow))
    boton_guardado.grid(row=22, column=0, sticky="news")

def ordenar_lista():
    global recomendacion
    lista_ordenada = []
    datos = []
    with open("datos.csv", "r") as text:
        for row in text:
            parte = row.split(',')
            datos.append(parte)
    #print(datos)
    for x in range(len(recomendacion)):
        #print(recomendacion[x][0])
        for y in range(len(datos)):
            #print(datos[y])
            if recomendacion[x][0] == datos[y][0]:
                lista_ordenada.append(datos[y])
    return lista_ordenada

def comparar_data(nombre,tpersona,trl,antiguedad,sector,NVentas,VinculoUni,Cofinan,ID,TraccionC,subwindow): # en progreso
    if nombre and tpersona and trl and antiguedad and sector and NVentas and VinculoUni and Cofinan and ID and TraccionC:
        data = []
        global recomendacion
        global contador
        contador = 0
        
        recomendacion = []

        subwindow = Toplevel(root)
        subwindow.geometry("1400x768")
        subwindow.title("Fuentes de financiamiento")

        frame = Frame(subwindow)
        frame.pack(pady=40)

        user_info_frame = LabelFrame(frame, text="Fuentes de financiamiento disponibles")
        user_info_frame.pack(fill="both", expand="yes")
        
        with open("datos.csv", "r") as text:
            for row in text:
                data.append(row)

        for x in range(len(data)): # filas del archivo
            counter = 0
            datos = data[x].split(',')
            rec = []
            rec.append(datos[0])
            if tpersona == 'Persona Juridica':
                if datos[1] == "Persona Natural":
                    rec.append("Tipo persona no valida para este financiamiento")
                else:
                    counter += 1
                    rec.append("Tipo persona valida")
                maxmin = re.findall(r'\d+', datos[2])
                valor_trl = re.findall(r'\d+', trl)
                if int(valor_trl[0]) >= int(maxmin[0]) and int(valor_trl[0]) <= int(maxmin[1]):
                    counter += 1
                    rec.append("Su trl coincide con este financiamiento")
                elif int(valor_trl[0]) < int(maxmin[0]):
                    rec.append("Se recomienda subir la escala de madurez tecnologica")
                elif int(valor_trl[0]) > int(maxmin[1]):
                    rec.append("Su escala tecnologica supera la de esta fuente de financiamiento")
                
                if antiguedad != datos[3]:
                    if datos[3] == 'No requerido':
                        counter += 1
                        rec.append("Antiguedad cumplida")
                    elif listaAntig.index(antiguedad) < listaAntig.index(datos[3]):
                        rec.append("Se recomienda mas antiguedad")
                    elif listaAntig.index(antiguedad) > listaAntig.index(datos[3]):
                        rec.append("Superas la antiguedad requerida")
                else:
                    counter += 1
                    rec.append("Antiguedad cumplida")
                if sector != datos[4]:
                    if datos[4] == 'Todos':
                        counter += 1
                        rec.append("Sector valido")
                    else:
                        rec.append("El sector no coincide con esta fuente de financiamiento")
                else:
                    counter += 1
                    rec.append("Sector valido")
                if NVentas != datos[5]:
                    if listaNvVentas.index(NVentas) < listaNvVentas.index(datos[5]):
                        rec.append("Se recomienda aumentar el nivel de ventas")
                    elif listaNvVentas.index(NVentas) > listaNvVentas.index(datos[5]):
                        rec.append("El nivel de ventas supera el de la fuente de financiamiento")
                else:
                    counter += 1
                    rec.append("Nivel de ventas cumplido")
                if VinculoUni != datos[6]:
                    if datos[6] == "Sin vinculo universitario":
                        rec.append("Se recomienda abandonar el vinculo universitario")
                    elif VinculoUni == "Sin vinculo universitario":
                        rec.append("Se recomienda vincularse a universidad")
                    else:
                        counter += 1
                        rec.append("Vinculo universitario valido")
                else:
                    counter += 1
                    rec.append("Vinculo universitario valido")
                if Cofinan != datos[7]:
                    if datos[7] == "Sin cofinanciamiento":
                        counter += 1
                        rec.append("Cofinanciamiento cumplido")
                    elif listaCofinanciamiento.index(Cofinan) < listaCofinanciamiento.index(datos[7]):
                        rec.append("Se recomienda mayor cofinanciamiento")
                    elif listaCofinanciamiento.index(Cofinan) > listaCofinanciamiento.index(datos[7]):
                        rec.append("Cofinanciamiento superior al del financiamiento")
                else:
                    counter += 1
                    rec.append("Cofinanciamiento cumplido")
                if ID != datos[8]:
                    if len(datos[8].split()) > 2:
                        str = datos[8].replace(" a ",", ")
                        str = str.split(", ")
                        if ID.lower() == str[0].lower() or ID.lower() == str[1].lower():
                            counter += 1
                            rec.append("Componente de investigacion y desarrollo valido")
                        else:
                            lista_aux = [item.lower() for item in listaID_Usuario]
                            if lista_aux.index(ID.lower()) < lista_aux.index(str[0].lower()):
                                rec.append("Componente I+D inferior al de este financiamiento")
                            else:
                                rec.append("Componente I+D superior al de este financiamiento") 
                    else:
                        if listaID_Usuario.index(datos[8]) < listaID_Usuario.index(ID):
                            rec.append("Componente I+D superior al de este financiamiento")
                        else:
                            rec.append("Componente I+D inferior al de este financiamiento")
                else:
                    counter += 1
                    rec.append("Componente I+D valido para este financiamiento")
                if TraccionC != datos[9]:
                    if datos[9] == "No requerido":
                        counter += 1
                        rec.append("Traccion comercial no requerida")
                    elif TraccionC == "Con validacion de mercado" and datos[9] in listaTraccionC:
                        rec.append("No cumple con el requisito")
                    elif TraccionC in listaTraccionC and datos[9] == "Con validacion de mercado":
                        rec.append("No cumple con el requisito")
                    else:
                        rec.append("No cumple con el requisito")
                else:
                    counter += 1
                    rec.append("Traccion comercial cumplida")

            elif tpersona == 'Persona Natural': # Se agrega toda FF
                if datos[1] == "Persona Juridica":
                    rec.append("Se recomienda convertirse en persona juridica")
                else:
                    counter += 1
                    rec.append("Tipo de persona valida")
                
                maxmin = re.findall(r'\d+', datos[2])
                valor_trl = re.findall(r'\d+', trl)
                if int(valor_trl[0]) >= int(maxmin[0]) and int(valor_trl[0]) <= int(maxmin[1]):
                    counter += 1
                    rec.append("Su trl coincide con este financiamiento")
                elif int(valor_trl[0]) < int(maxmin[0]):
                    rec.append("Se recomienda subir la escala de madurez tecnologica")
                elif int(valor_trl[0]) > int(maxmin[1]):
                    rec.append("Su escala tecnologica supera la de esta fuente de financiamiento")
                
                if antiguedad != datos[3]:
                    if datos[3] == 'No requerido':
                        counter += 1
                        rec.append("Antiguedad cumplida")
                    elif listaAntig.index(antiguedad) < listaAntig.index(datos[3]):
                        rec.append("Se recomienda mas antiguedad")
                    elif listaAntig.index(antiguedad) > listaAntig.index(datos[3]):
                        rec.append("Superas la antiguedad requerida")
                else:
                    rec.append("Antiguedad cumplida")
                if sector != datos[4]:
                    if datos[4] == 'Todos':
                        counter += 1
                        rec.append("Sector valido")
                    else:
                        rec.append("El sector no coincide con esta fuente de financiamiento")
                else:
                    counter += 1
                    rec.append("Sector valido")
                if NVentas != datos[5]:
                    if listaNvVentas.index(NVentas) < listaNvVentas.index(datos[5]):
                        rec.append("Se recomienda aumentar el nivel de ventas")
                    elif listaNvVentas.index(NVentas) > listaNvVentas.index(datos[5]):
                        rec.append("El nivel de ventas supera el de la fuente de financiamiento")
                else:
                    counter += 1
                    rec.append("Nivel de ventas cumplido")
                if VinculoUni != datos[6]:
                    if datos[6] == "Sin vinculo universitario":
                        rec.append("Se recomienda abandonar el vinculo universitario")
                    elif VinculoUni == "Sin vinculo universitario":
                        rec.append("Se recomienda vincularse a universidad")
                    else:
                        counter += 1
                        rec.append("Vinculo universitario valido")
                else:
                    counter += 1
                    rec.append("Vinculo universitario valido")
                if Cofinan != datos[7]:
                    if datos[7] == "Sin cofinanciamiento":
                        counter += 1
                        rec.append("Cofinanciamiento cumplido")
                    elif listaCofinanciamiento.index(Cofinan) < listaCofinanciamiento.index(datos[7]):
                        rec.append("Se recomienda mayor cofinanciamiento")
                    elif listaCofinanciamiento.index(Cofinan) > listaCofinanciamiento.index(datos[7]):
                        rec.append("Cofinanciamiento superior al del financiamiento")
                else:
                    counter += 1
                    rec.append("Cofinanciamiento cumplido")
                if ID != datos[8]:
                    if len(datos[8].split()) > 2:
                        str = datos[8].replace(" a ",", ")
                        str = str.split(", ")
                        if ID.lower() == str[0].lower() or ID.lower() == str[1].lower():
                            counter += 1
                            rec.append("Componente de investigacion y desarrollo valido")
                        else:
                            lista_aux = [item.lower() for item in listaID_Usuario]
                            if lista_aux.index(ID.lower()) < lista_aux.index(str[0].lower()):
                                rec.append("Componente I+D inferior al de este financiamiento")
                            else:
                                rec.append("Componente I+D superior al de este financiamiento") 
                    else:
                        if listaID_Usuario.index(datos[8]) < listaID_Usuario.index(ID):
                            rec.append("Componente I+D superior al de este financiamiento")
                        else:
                            rec.append("Componente I+D inferior al de este financiamiento")
                else:
                    counter += 1
                    rec.append("Componente I+D valido para este financiamiento")
                if TraccionC != datos[9]:
                    if datos[9] == "No requerido":
                        counter += 1
                        rec.append("Traccion comercial no requerida")
                    elif TraccionC == "Con validacion de mercado" and datos[9] in listaTraccionC:
                        rec.append("No cumple con el requisito")
                    elif TraccionC in listaTraccionC and datos[9] == "Con validacion de mercado":
                        rec.append("No cumple con el requisito")
                    else:
                        rec.append("No cumple con el requisito")
                else:
                    counter += 1
                    rec.append("Traccion comercial cumplida")
            rec.append(counter)
            recomendacion.append(rec)

        recomendacion = sorted(recomendacion, key=lambda x: x[10], reverse=True)
        lista_ordenada = ordenar_lista()
        boton_anterior = Button(user_info_frame, text="Anterior", command=lambda: [disminuir_contador(), visualizar_data(), nombre_emp_label.config(text=lista_ordenada[contador][0]), persona_label.config(text=lista_ordenada[contador][1]), trl_label.config(text=lista_ordenada[contador][2]), antiguedad_label.config(text=lista_ordenada[contador][3]), sector_label.config(text=lista_ordenada[contador][4]), ventas_anuales_label.config(text=lista_ordenada[contador][5]), vinculo_universidad_label.config(text=lista_ordenada[contador][6]), cofinanciamiento_label.config(text=lista_ordenada[contador][7]), componenteid_label.config(text=lista_ordenada[contador][8]), traccion_comercial_label.config(text=lista_ordenada[contador][9]), recomendacion_persona_label.config(text=recomendacion[contador][1]),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_trl_label.config(text=recomendacion[contador][2]),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_antiguedad_label.config(text=recomendacion[contador][3]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_sector_label.config(text=recomendacion[contador][4]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_ventas_anuales_label.config(text=recomendacion[contador][5]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_vinculo_universidad_label.config(text=recomendacion[contador][6]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_cofinanciamiento_label.config(text=recomendacion[contador][7]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_componenteid_label.config(text=recomendacion[contador][8]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_traccion_comercial_label.config(text=recomendacion[contador][9])])
        boton_anterior.grid(row=0, column=0)

        boton_siguiente = Button(user_info_frame, text="Siguiente", command=lambda: [aumentar_contador(), visualizar_data(), nombre_emp_label.config(text=lista_ordenada[contador][0]), persona_label.config(text=lista_ordenada[contador][1]), trl_label.config(text=lista_ordenada[contador][2]), antiguedad_label.config(text=lista_ordenada[contador][3]), sector_label.config(text=lista_ordenada[contador][4]), ventas_anuales_label.config(text=lista_ordenada[contador][5]), vinculo_universidad_label.config(text=lista_ordenada[contador][6]), cofinanciamiento_label.config(text=lista_ordenada[contador][7]), componenteid_label.config(text=lista_ordenada[contador][8]), traccion_comercial_label.config(text=lista_ordenada[contador][9]), recomendacion_persona_label.config(text=recomendacion[contador][1]),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_trl_label.config(text=recomendacion[contador][2]),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_antiguedad_label.config(text=recomendacion[contador][3]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_sector_label.config(text=recomendacion[contador][4]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_ventas_anuales_label.config(text=recomendacion[contador][5]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_vinculo_universidad_label.config(text=recomendacion[contador][6]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_cofinanciamiento_label.config(text=recomendacion[contador][7]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_componenteid_label.config(text=recomendacion[contador][8]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_traccion_comercial_label.config(text=recomendacion[contador][9])])
        boton_siguiente.grid(row=0, column=1)

        fijo_nombre_emp_label = Label(user_info_frame, text="Nombre")
        fijo_persona_label = Label(user_info_frame, text="Tipo de persona")
        fijo_trl_label = Label(user_info_frame, text="Escala de madurez tecnologica (Trl)")
        fijo_antiguedad_label = Label(user_info_frame,text="Antiguedad de la empresa")
        fijo_sector_label = Label(user_info_frame,text="Sector")
        fijo_ventas_anuales_label = Label(user_info_frame, text="Nivel de ventas")
        fijo_vinculo_universidad_label = Label(user_info_frame, text="Vinculo con universidad")
        fijo_cofinanciamiento_label = Label(user_info_frame, text="Cofinanciamiento")
        fijo_componenteid_label = Label(user_info_frame, text="Componente de I+D (Investigacion y Desarrollo)")
        fijo_traccion_comercial_label = Label(user_info_frame, text="Traccion comercial")

        label_recomendacion = Label(user_info_frame, text="Recomendaciones")

        nombre_emp_usuario_label = Label(user_info_frame, text=nombre)
        persona_usuario_label = Label(user_info_frame, text=tpersona)
        trl_usuario_label = Label(user_info_frame, text=trl)
        antiguedad_usuario_label = Label(user_info_frame, text=antiguedad)
        sector_usuario_label = Label(user_info_frame, text=sector)
        ventas_anuales_usuario_label = Label(user_info_frame, text=NVentas)
        vinculo_universidad_usuario_label = Label(user_info_frame, text=VinculoUni)
        cofinanciamiento_usuario_label = Label(user_info_frame, text=Cofinan)
        componenteid_usuario_label = Label(user_info_frame, text=ID)
        traccion_comercial_usuario_label = Label(user_info_frame, text=TraccionC)

        nombre_emp_label = Label(user_info_frame, text=lista_ordenada[contador][0])
        persona_label = Label(user_info_frame, text=lista_ordenada[contador][1])
        trl_label = Label(user_info_frame, text=lista_ordenada[contador][2])
        antiguedad_label = Label(user_info_frame, text=lista_ordenada[contador][3])
        sector_label = Label(user_info_frame, text=lista_ordenada[contador][4])
        ventas_anuales_label = Label(user_info_frame, text=lista_ordenada[contador][5])
        vinculo_universidad_label = Label(user_info_frame, text=lista_ordenada[contador][6])
        cofinanciamiento_label = Label(user_info_frame, text=lista_ordenada[contador][7])
        componenteid_label = Label(user_info_frame, text=lista_ordenada[contador][8])
        traccion_comercial_label = Label(user_info_frame, text=lista_ordenada[contador][9])



        recomendacion_persona_label = Label(user_info_frame, text=recomendacion[contador][1])
        recomendacion_trl_label = Label(user_info_frame, text=recomendacion[contador][2])
        recomendacion_antiguedad_label = Label(user_info_frame, text=recomendacion[contador][3])
        recomendacion_sector_label = Label(user_info_frame, text=recomendacion[contador][4])
        recomendacion_ventas_anuales_label = Label(user_info_frame, text=recomendacion[contador][5])
        recomendacion_vinculo_universidad_label = Label(user_info_frame, text=recomendacion[contador][6])
        recomendacion_cofinanciamiento_label = Label(user_info_frame, text=recomendacion[contador][7])
        recomendacion_componenteid_label = Label(user_info_frame, text=recomendacion[contador][8])
        recomendacion_traccion_comercial_label = Label(user_info_frame, text=recomendacion[contador][9])

        fijo_nombre_emp_label.grid(row=1, column=0)
        fijo_persona_label.grid(row=2, column=0)
        fijo_trl_label.grid(row=3, column=0)
        fijo_antiguedad_label.grid(row=4, column=0)
        fijo_sector_label.grid(row=5, column=0)
        fijo_ventas_anuales_label.grid(row=6, column=0)
        fijo_vinculo_universidad_label.grid(row=7, column=0)
        fijo_cofinanciamiento_label.grid(row=8, column=0)
        fijo_componenteid_label.grid(row=9, column=0)
        fijo_traccion_comercial_label.grid(row=10, column=0)

        label_recomendacion.grid(row=1, column=3)

        nombre_emp_usuario_label.grid(row=1, column=1)
        persona_usuario_label.grid(row=2, column=1)
        trl_usuario_label.grid(row=3, column=1)
        antiguedad_usuario_label.grid(row=4, column=1)
        sector_usuario_label.grid(row=5, column=1)
        ventas_anuales_usuario_label.grid(row=6, column=1)
        vinculo_universidad_usuario_label.grid(row=7, column=1)
        cofinanciamiento_usuario_label.grid(row=8, column=1)
        componenteid_usuario_label.grid(row=9, column=1)
        traccion_comercial_usuario_label.grid(row=10, column=1)

        nombre_emp_label.grid(row=1, column=2)
        persona_label.grid(row=2, column=2)
        trl_label.grid(row=3, column=2)
        antiguedad_label.grid(row=4, column=2)
        sector_label.grid(row=5, column=2)
        ventas_anuales_label.grid(row=6, column=2)
        vinculo_universidad_label.grid(row=7, column=2)
        cofinanciamiento_label.grid(row=8, column=2)
        componenteid_label.grid(row=9, column=2)
        traccion_comercial_label.grid(row=10, column=2)

        recomendacion_persona_label.grid(row=2, column=3)
        recomendacion_trl_label.grid(row=3, column=3)
        recomendacion_antiguedad_label.grid(row=4, column=3)
        recomendacion_sector_label.grid(row=5, column=3)
        recomendacion_ventas_anuales_label.grid(row=6, column=3)
        recomendacion_vinculo_universidad_label.grid(row=7, column=3)
        recomendacion_cofinanciamiento_label.grid(row=8, column=3)
        recomendacion_componenteid_label.grid(row=9, column=3)
        recomendacion_traccion_comercial_label.grid(row=10, column=3)

        boton_cierre = Button(user_info_frame, text="Volver",command=lambda: [subwindow.destroy()])
        boton_cierre.grid(row=23, column=0, sticky="news")

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=40, pady=4)

    else:
        messagebox.showwarning(title="Error", message="Faltan datos", parent=subwindow)

def ver_fuente_financiamiento():
    boton_tres.config(state=DISABLED)
    global contador
    contador = 0
    visualizar_data()

    subwindow = Toplevel(root)
    subwindow.geometry("1024x768")
    subwindow.title("Fuentes de financiamiento")

    
    frame = Frame(subwindow)
    frame.pack(pady=40)

    user_info_frame = LabelFrame(frame, text="Fuentes de financiamiento disponibles")
    user_info_frame.pack(fill="both", expand="yes")

    boton_anterior = Button(user_info_frame, text="Anterior", command=lambda: [disminuir_contador(), visualizar_data(), nombre_emp_label2.config(text=info[0]), persona_label2.config(text=info[1]), trl_label2.config(text=info[2]), antiguedad_label2.config(text=info[3]), sector_label2.config(text=info[4]), ventas_anuales_label2.config(text=info[5]), vinculo_universidad_label2.config(text=info[6]), cofinanciamiento_label2.config(text=info[7]), componenteid_label2.config(text=info[8]), traccion_comercial_label2.config(text=info[9]), descripcion_label2.config(text=info[10])])
    boton_anterior.grid(row=0, column=0)

    boton_siguiente = Button(user_info_frame, text="Siguiente", command=lambda: [aumentar_contador(), visualizar_data(), nombre_emp_label2.config(text=info[0]), persona_label2.config(text=info[1]), trl_label2.config(text=info[2]), antiguedad_label2.config(text=info[3]), sector_label2.config(text=info[4]), ventas_anuales_label2.config(text=info[5]), vinculo_universidad_label2.config(text=info[6]), cofinanciamiento_label2.config(text=info[7]), componenteid_label2.config(text=info[8]), traccion_comercial_label2.config(text=info[9]), descripcion_label2.config(text=info[10])])
    boton_siguiente.grid(row=0, column=1)

    nombre_emp_label = Label(user_info_frame, text="Nombre")
    persona_label = Label(user_info_frame, text="Tipo de persona")
    trl_label = Label(user_info_frame, text="Escala de madurez tecnologica (Trl)")
    antiguedad_label = Label(user_info_frame,text="Antiguedad de la empresa")
    sector_label = Label(user_info_frame,text="Sector")
    ventas_anuales_label = Label(user_info_frame, text="Nivel de ventas")
    vinculo_universidad_label = Label(user_info_frame, text="Vinculo con universidad")
    cofinanciamiento_label = Label(user_info_frame, text="Cofinanciamiento")
    componenteid_label = Label(user_info_frame, text="Componente de I+D (Investigacion y Desarrollo)")
    traccion_comercial_label = Label(user_info_frame, text="Traccion comercial")
    descripcion_label = Label(user_info_frame, text="Descripcion")

    nombre_emp_label2 = Label(user_info_frame, text=info[0])
    persona_label2 = Label(user_info_frame, text=info[1])
    trl_label2 = Label(user_info_frame, text=info[2])
    antiguedad_label2 = Label(user_info_frame, text=info[3])
    sector_label2 = Label(user_info_frame, text=info[4])
    ventas_anuales_label2 = Label(user_info_frame, text=info[5])
    vinculo_universidad_label2 = Label(user_info_frame, text=info[6])
    cofinanciamiento_label2 = Label(user_info_frame, text=info[7])
    componenteid_label2 = Label(user_info_frame, text=info[8])
    traccion_comercial_label2 = Label(user_info_frame, text=info[9])
    descripcion_label2 = Label(user_info_frame, text=info[10])
    
    nombre_emp_label.grid(row=1, column=0)
    nombre_emp_label2.grid(row=1, column=1)
    persona_label.grid(row=2, column=0)
    persona_label2.grid(row=2, column=1)
    trl_label.grid(row=3, column=0)
    trl_label2.grid(row=3, column=1)
    antiguedad_label.grid(row=4, column=0)
    antiguedad_label2.grid(row=4, column=1)
    sector_label.grid(row=5, column=0)
    sector_label2.grid(row=5, column=1)
    ventas_anuales_label.grid(row=6, column=0)
    ventas_anuales_label2.grid(row=6, column=1)
    vinculo_universidad_label.grid(row=7, column=0)
    vinculo_universidad_label2.grid(row=7, column=1)
    cofinanciamiento_label.grid(row=8, column=0)
    cofinanciamiento_label2.grid(row=8, column=1)
    componenteid_label.grid(row=9, column=0)
    componenteid_label2.grid(row=9, column=1)
    traccion_comercial_label.grid(row=10, column=0)
    traccion_comercial_label2.grid(row=10, column=1)
    descripcion_label.grid(row=11, column=0)
    descripcion_label2.grid(row=11, column=1)

    boton_cierre = Button(user_info_frame, text="Volver",command=lambda: [subwindow.destroy(), boton_tres.config(state=NORMAL)])
    boton_cierre.grid(row=12, column=0, sticky="news")

    
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=40, pady=4)

    pass

def verificar_csv(boton):
    if os.path.isfile('datos.csv'):
        if boton == '1':
            compatibilidad_fuente_financiamiento()
        elif boton == '2':
            ver_fuente_financiamiento()
    else:
        messagebox.showerror(message="No existen datos")

root = Tk()
root.title("Mi Aplicación")
root.geometry("640x480")

boton_uno = Button(root, text="Ver compatibilidad con financiamientos", command=lambda: verificar_csv('1'))
boton_uno.pack(pady=20)

boton_dos = Button(root, text="Agregar fuente de financiamiento", command=agregar_fuente_financiamiento)
boton_dos.pack(pady=20)

boton_tres = Button(root, text="Ver fuentes de financiamientos disponibles", command=lambda: verificar_csv('2'))
boton_tres.pack(pady=20)

button_salir = Button(root, text="Salir", command=root.quit)
button_salir.pack(pady=20)

# Iniciar el bucle principal
root.mainloop()

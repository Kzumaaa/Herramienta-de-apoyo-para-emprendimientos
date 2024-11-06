from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import os
import csv

listaPersona = ["Persona Natural", "Persona Juridica"]
listaTrl = ["TRL 1-3", "TRL 4-6", "TRL 6-7"]
listaAntig = ["No requerido", "Menor a 12 meses", "Entre 12-24 meses", "Entre 24-36 meses", "Mayor a 36 meses"]
listaSector = ["Inteligencia Artificial", "Biotecnologia", "Fintech", "Tecnologias Limpias", "Software", "Todos"] 
listaNvVentas = ["Sin ventas", "0UF-2.400 UF", "2.400UF-25.000UF", "25.000-100.000UF"] 
listaVinculoUni = ["Sin vinculo universitario", "Si(Estudiante o egresado)", "Si(Colaboracion con universidades)"] 
listaCofinanciamiento = ["Sin cofinanciamiento", "Si(20% aporte propio)", "Si(30% aporte propio)", "Si(40% aporte propio)"] 
listaID = ["Requerido", "Opcional"]
listaTraccionC = ["No requerido", "Con validacion de mercado", "Con traccion inicial(0UF-350UF)", "Con validacion inicial(350UF-1750UF)", "Con alta traccion comercial(Mas de 1750UF)"]

# Listas auxiliares para usuario

# listaSector_Usuario = ["Inteligencia Artificial", "Biotecnologia", "Fintech", "Tecnologias Limpias", "Software"] 
# listaNvVentas_Usuario = ["0UF-2.400 UF", "2.400UF-25.000UF", "25.000-100.000UF"]
# listaVinculoUni_Usuario = ["Sin vinculo universitario", "Si(Estudiante o egresado)", "Si(Colaboracion con universidades)"]
listaID_Usuario = ["Con I+D", "Sin I+D"]
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

    # Seccion donde el moderador ingresa los datos

    nombre_emp_entry = Entry(user_info_frame,width=25)
    persona_combobox = Combobox(user_info_frame, values=listaPersona, state="readonly",width=25)
    trl_combobox = Combobox(user_info_frame, values=listaTrl, state="readonly",width=25)
    antiguedad_combobox = Combobox(user_info_frame, values=listaAntig, state="readonly",width=25)
    sector_combobox = Combobox(user_info_frame, values=listaSector, state="readonly",width=25)
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

def comparar_data(nombre,tpersona,trl,antiguedad,sector,NVentas,VinculoUni,Cofinan,ID,TraccionC,subwindow): # en progreso
    if nombre and tpersona and trl and antiguedad and sector and NVentas and VinculoUni and Cofinan and ID and TraccionC:
        data = []
        global recomendacion
        global contador
        contador = 0
        recomendacion = []

        subwindow = Toplevel(root)
        subwindow.geometry("1024x768")
        subwindow.title("Fuentes de financiamiento")

        frame = Frame(subwindow)
        frame.pack(pady=40)

        user_info_frame = LabelFrame(frame, text="Fuentes de financiamiento disponibles")
        user_info_frame.pack(fill="both", expand="yes")
        
        with open("datos.csv", "r") as text:
            for row in text:
                data.append(row)

        for x in range(len(data)): # filas del archivo
            datos = data[x].split(',')
            rec = []
            #i = 0
            if tpersona == 'Persona Juridica' and datos[1] == 'Persona Juridica': # Si el valor ingresado es Persona Juridica se descarta toda FF que requiera Persona Natural
                rec.append("Tipo persona valida")
                if trl != datos[2]: 
                    if listaTrl.index(trl) < listaTrl.index(datos[2]): # Si mi trl es menor que el de la fuente de financiamiento
                        rec.append("Se recomienda subir la escala de madurez tecnologica")
                        #print("Se recomienda subir la escala de madurez tecnologica")
                    elif listaTrl.index(trl) > listaTrl.index(datos[2]):
                        rec.append("Su escala tecnologica supera la de esta fuente de financiamiento")
                        #print("Su escala tecnologica supera la de esta fuente de financiamiento")
                else:
                    rec.append("Trl cumplido")
                    #print("Requisito cumplido")
                    #i += 1
                if antiguedad != datos[3]:
                    if datos[3] == 'No requerido':
                        rec.append("Antiguedad cumplida")
                        #print("Requisito cumplido")
                        #i += 1
                    elif listaAntig.index(antiguedad) < listaAntig.index(datos[3]): # 12 es menor q 24? Si
                        rec.append("Se recomienda mas antiguedad")
                        # print("Se recomienda mas antiguedad")
                    elif listaAntig.index(antiguedad) > listaAntig.index(datos[3]): # 12 es menor q 24? Si
                        rec.append("Superas la antiguedad requerida")
                        #print("Superas la antiguedad requerida")
                else:
                    rec.append("Antiguedad cumplida")
                    # print("Requisito cumplido")
                    #i += 1
                if sector != datos[4]:
                    if datos[4] == 'Todos':
                        rec.append("Sector valido")
                        #print("Requisito cumplido")
                    else:
                        rec.append("El sector no coincide con esta fuente de financiamiento")
                        #print("Tu emprendimiento no coincide con esta fuente de financiamiento")
                else:
                    rec.append("Sector valido")
                    #print("Requisito cumplido")
                    #i += 1
                if NVentas != datos[5]:
                    if listaNvVentas.index(NVentas) < listaNvVentas.index(datos[5]):
                        rec.append("Se recomienda aumentar el nivel de ventas")
                        #print("Se recomienda aumentar el nivel de ventas")
                    elif listaNvVentas.index(NVentas) > listaNvVentas.index(datos[5]):
                        rec.append("El nivel de ventas supera el de la fuente de financiamiento")
                        #print("El nivel de ventas supera el de la fuente de financiamiento")
                else:
                    #i += 1
                    rec.append("Nivel de ventas cumplido")
                    #print("Requisito cumplido")
                if VinculoUni != datos[6]:
                    if datos[6] == "Sin vinculo universitario":
                        rec.append("Se recomienda abandonar el vinculo universitario")
                        #print("Se recomienda abandonar el vinculo universitario")
                    elif VinculoUni == "Sin vinculo universitario":
                        rec.append("Se recomienda vincularse a universidad")
                        #print("Se recomienda vincularse a universidad")
                    else:
                        rec.append("Vinculo universitario valido")
                        #print("Vinculo universitario valido")
                else:
                    #i += 1
                    rec.append("Vinculo universitario valido")
                    #print("Requisito cumplido")
                if Cofinan != datos[7]:
                    if datos[7] == "Sin cofinanciamiento":
                        rec.append("Cofinanciamiento cumplido")
                        #print("Requisito cumplido")
                    elif listaCofinanciamiento.index(Cofinan) < listaCofinanciamiento.index(datos[7]): # 12 es menor q 24? Si
                        rec.append("Se recomienda mayor cofinanciamiento")
                        #print("Se recomienda mayor cofinanciamiento")
                    elif listaCofinanciamiento.index(Cofinan) > listaCofinanciamiento.index(datos[7]): # 12 es menor q 24? Si
                        rec.append("Cofinanciamiento superior al del financiamiento")
                        #print("Cofinanciamiento superior al del financiamiento")
                    #i += 1
                else:
                    rec.append("Cofinanciamiento cumplido")
                    #print("Requisito cumplido")
                if ID != datos[8]:
                    if datos[8] == "Opcional":
                        rec.append("ID validado")
                        #print("Requisito cumplido")
                    else:
                        rec.append("Se recomienda componente de investigacion y desarrollo")
                        #print("Se recomienda componente de investigacion y desarrollo")
                else:
                    rec.append("ID validado")
                    #print("Requisito cumplido")
                    #i += 1
                if TraccionC != datos[9]:
                    if datos[9] == "No requerido":
                        rec.append("Traccion comercial no requerida")
                        #print("Requisito cumplido")
                    elif TraccionC == "Con validacion de mercado" and datos[9] in listaTraccionC:
                        rec.append("No cumple con el requisito")
                        #print("No cumple con el requisito")
                    elif TraccionC in listaTraccionC and datos[9] == "Con validacion de mercado":
                        rec.append("No cumple con el requisito")
                        #print("No cumple con el requisito")
                    else:
                        rec.append("No cumple con el requisito")
                        #print("No cumple con el requisito")
                else:
                    rec.append("Traccion comercial cumplida")
                    #print("Requisito cumplido")
                    #i += 1

            elif tpersona == 'Persona Natural': # Se agrega toda FF
                if datos[1] == "Persona Juridica":
                    rec.append("Se recomienda convertirse en persona juridica")
                    #print("Se recomienda convertirse en persona juridica")
                else:
                    rec.append("Tipo de persona valida")
                if trl != datos[2]: 
                    if listaTrl.index(trl) < listaTrl.index(datos[2]): # Si mi trl es menor que el de la fuente de financiamiento
                        rec.append("Se recomienda subir la escala de madurez tecnologica")
                        #print("Se recomienda subir la escala de madurez tecnologica")
                    elif listaTrl.index(trl) > listaTrl.index(datos[2]):
                        rec.append("Su escala tecnologica supera la de esta fuente de financiamiento")
                        #print("Su escala tecnologica supera la de esta fuente de financiamiento")
                else:
                    rec.append("Trl cumplido")
                    #print("Requisito cumplido")
                    #i += 1
                if antiguedad != datos[3]:
                    if datos[3] == 'No requerido':
                        rec.append("Antiguedad cumplida")
                        #print("Requisito cumplido")
                        #i += 1
                    elif listaAntig.index(antiguedad) < listaAntig.index(datos[3]): # 12 es menor q 24? Si
                        rec.append("Se recomienda mas antiguedad")
                        # print("Se recomienda mas antiguedad")
                    elif listaAntig.index(antiguedad) > listaAntig.index(datos[3]): # 12 es menor q 24? Si
                        rec.append("Superas la antiguedad requerida")
                        #print("Superas la antiguedad requerida")
                else:
                    rec.append("Antiguedad cumplida")
                    # print("Requisito cumplido")
                    #i += 1
                if sector != datos[4]:
                    if datos[4] == 'Todos':
                        rec.append("Sector valido")
                        #print("Requisito cumplido")
                    else:
                        rec.append("El sector no coincide con esta fuente de financiamiento")
                        #print("Tu emprendimiento no coincide con esta fuente de financiamiento")
                else:
                    rec.append("Sector valido")
                    #print("Requisito cumplido")
                    #i += 1
                if NVentas != datos[5]:
                    if listaNvVentas.index(NVentas) < listaNvVentas.index(datos[5]):
                        rec.append("Se recomienda aumentar el nivel de ventas")
                        #print("Se recomienda aumentar el nivel de ventas")
                    elif listaNvVentas.index(NVentas) > listaNvVentas.index(datos[5]):
                        rec.append("El nivel de ventas supera el de la fuente de financiamiento")
                        #print("El nivel de ventas supera el de la fuente de financiamiento")
                else:
                    #i += 1
                    rec.append("Nivel de ventas cumplido")
                    #print("Requisito cumplido")
                if VinculoUni != datos[6]:
                    if datos[6] == "Sin vinculo universitario":
                        rec.append("Se recomienda abandonar el vinculo universitario")
                        #print("Se recomienda abandonar el vinculo universitario")
                    elif VinculoUni == "Sin vinculo universitario":
                        rec.append("Se recomienda vincularse a universidad")
                        #print("Se recomienda vincularse a universidad")
                else:
                    #i += 1
                    rec.append("Vinculo universitario valido")
                    #print("Requisito cumplido")
                if Cofinan != datos[7]:
                    if datos[7] == "Sin cofinanciamiento":
                        rec.append("Cofinanciamiento cumplido")
                        #print("Requisito cumplido")
                    elif listaCofinanciamiento.index(Cofinan) < listaCofinanciamiento.index(datos[7]): # 12 es menor q 24? Si
                        rec.append("Se recomienda mayor cofinanciamiento")
                        #print("Se recomienda mayor cofinanciamiento")
                    elif listaCofinanciamiento.index(Cofinan) > listaCofinanciamiento.index(datos[7]): # 12 es menor q 24? Si
                        rec.append("Cofinanciamiento superior al del financiamiento")
                        #print("Cofinanciamiento superior al del financiamiento")
                    #i += 1
                else:
                    rec.append("Cofinanciamiento cumplido")
                    #print("Requisito cumplido")
                if ID != datos[8]:
                    if datos[8] == "Opcional":
                        rec.append("ID validado")
                        #print("Requisito cumplido")
                    else:
                        rec.append("Se recomienda componente de investigacion y desarrollo")
                        #print("Se recomienda componente de investigacion y desarrollo")
                else:
                    rec.append("ID validado")
                    #print("Requisito cumplido")
                    #i += 1
                if TraccionC != datos[9]:
                    if datos[9] == "No requerido":
                        rec.append("Traccion comercial no requerida")
                        #print("Requisito cumplido")
                    elif TraccionC == "Con validacion de mercado" and datos[9] in listaTraccionC:
                        rec.append("No cumple con el requisito")
                        #print("No cumple con el requisito")
                    elif TraccionC in listaTraccionC and datos[9] == "Con validacion de mercado":
                        rec.append("No cumple con el requisito")
                        #print("No cumple con el requisito")
                    else:
                        rec.append("No cumple con el requisito")
                        #print("No cumple con el requisito")
                else:
                    rec.append("Traccion comercial cumplida")
                    #print("Requisito cumplido")
                    #i += 1
            recomendacion.append(rec)
        visualizar_data()
        boton_anterior = Button(user_info_frame, text="Anterior", command=lambda: [disminuir_contador(), visualizar_data(), nombre_emp_label.config(text=info[0]), persona_label.config(text=info[1]), trl_label.config(text=info[2]), antiguedad_label.config(text=info[3]), sector_label.config(text=info[4]), ventas_anuales_label.config(text=info[5]), vinculo_universidad_label.config(text=info[6]), cofinanciamiento_label.config(text=info[7]), componenteid_label.config(text=info[8]), traccion_comercial_label.config(text=info[9]), recomendacion_persona_label.config(text=recomendacion[contador][0]),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_trl_label.config(text=recomendacion[contador][1]),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_antiguedad_label.config(text=recomendacion[contador][2]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_sector_label.config(text=recomendacion[contador][3]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_ventas_anuales_label.config(text=recomendacion[contador][4]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_vinculo_universidad_label.config(text=recomendacion[contador][5]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_cofinanciamiento_label.config(text=recomendacion[contador][6]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_componenteid_label.config(text=recomendacion[contador][7]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_traccion_comercial_label.config(text=recomendacion[contador][8])])
        boton_anterior.grid(row=0, column=0)

        boton_siguiente = Button(user_info_frame, text="Siguiente", command=lambda: [aumentar_contador(), visualizar_data(), nombre_emp_label.config(text=info[0]), persona_label.config(text=info[1]), trl_label.config(text=info[2]), antiguedad_label.config(text=info[3]), sector_label.config(text=info[4]), ventas_anuales_label.config(text=info[5]), vinculo_universidad_label.config(text=info[6]), cofinanciamiento_label.config(text=info[7]), componenteid_label.config(text=info[8]), traccion_comercial_label.config(text=info[9]), recomendacion_persona_label.config(text=recomendacion[contador][0]),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_trl_label.config(text=recomendacion[contador][1]),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_antiguedad_label.config(text=recomendacion[contador][2]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_sector_label.config(text=recomendacion[contador][3]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_ventas_anuales_label.config(text=recomendacion[contador][4]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_vinculo_universidad_label.config(text=recomendacion[contador][5]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_cofinanciamiento_label.config(text=recomendacion[contador][6]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_componenteid_label.config(text=recomendacion[contador][7]), 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                recomendacion_traccion_comercial_label.config(text=recomendacion[contador][8])])
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

        nombre_emp_label = Label(user_info_frame, text=info[0])
        persona_label = Label(user_info_frame, text=info[1])
        trl_label = Label(user_info_frame, text=info[2])
        antiguedad_label = Label(user_info_frame, text=info[3])
        sector_label = Label(user_info_frame, text=info[4])
        ventas_anuales_label = Label(user_info_frame, text=info[5])
        vinculo_universidad_label = Label(user_info_frame, text=info[6])
        cofinanciamiento_label = Label(user_info_frame, text=info[7])
        componenteid_label = Label(user_info_frame, text=info[8])
        traccion_comercial_label = Label(user_info_frame, text=info[9])



        recomendacion_persona_label = Label(user_info_frame, text=recomendacion[contador][0])
        recomendacion_trl_label = Label(user_info_frame, text=recomendacion[contador][1])
        recomendacion_antiguedad_label = Label(user_info_frame, text=recomendacion[contador][2])
        recomendacion_sector_label = Label(user_info_frame, text=recomendacion[contador][3])
        recomendacion_ventas_anuales_label = Label(user_info_frame, text=recomendacion[contador][4])
        recomendacion_vinculo_universidad_label = Label(user_info_frame, text=recomendacion[contador][5])
        recomendacion_cofinanciamiento_label = Label(user_info_frame, text=recomendacion[contador][6])
        recomendacion_componenteid_label = Label(user_info_frame, text=recomendacion[contador][7])
        recomendacion_traccion_comercial_label = Label(user_info_frame, text=recomendacion[contador][8])

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

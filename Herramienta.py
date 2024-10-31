from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import csv

listaPersona = ["Persona Juridica", "Persona Natural"] # 
listaTrl = ["TRL 1-3", "TRL 4-6", "TRL 6-9"]
listaAntig = ["Menos de 12 meses", "Menos de 24 meses", "Menos de 36 meses", "Mas de 36 meses"]
listaSector = ["Inteligencia Artificial", "Biotecnologia", "Fintech", "Tecnologias Limpias", "Software", "Otros"]
listaNvVentas = ["No aplica", "0UF-2.400 UF", "2.400UF-25.000UF", "25.000-100.000UF"]
listaVinculoUni = ["No requerido", "Si(Estudiante o egresado)", "Si(Colaboracion con universidades)"] # 
listaCofinanciamiento = ["No requerido", "Si(20-30% aporte propio)", "Si(30% aporte propio)", "Si(40% aporte propio)"]
listaID = ["Moderado", "Moderado a alto", "Alto", "Muy alto"]
listaTraccionC = ["No se requiere traccion previa", "Requiere validacion de mercado", "Se requiere traccion inicial", "Se requiere validacion inicial", "Alta traccion comercial"]

info = []

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
        
        # error al crear el archivo por la busqueda de un valor inexistente
        
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
    with open("datos.csv", "r") as text:
        for row in text:
            datos.append(row)

    if contador < len(datos):
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
    trl_label = Label(user_info_frame, text="Trl")
    antiguedad_label = Label(user_info_frame,text="Antiguedad de la empresa")
    sector_label = Label(user_info_frame,text="Sector")
    ventas_anuales_label = Label(user_info_frame, text="Nivel de ventas")
    vinculo_universidad_label = Label(user_info_frame, text="Vinculo con universidad")
    cofinanciamiento_label = Label(user_info_frame, text="Cofinanciamiento")
    componenteid_label = Label(user_info_frame, text="Componente de I+D")
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
    traccion_comercial_combobox = Combobox(user_info_frame, values=listaTraccionC, state="readonly",width=30)
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

def ver_fuente_financiamiento():

    boton_tres.config(state=DISABLED)

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
    trl_label = Label(user_info_frame, text="Trl")
    antiguedad_label = Label(user_info_frame,text="Antiguedad de la empresa")
    sector_label = Label(user_info_frame,text="Sector")
    ventas_anuales_label = Label(user_info_frame, text="Nivel de ventas")
    vinculo_universidad_label = Label(user_info_frame, text="Vinculo con universidad")
    cofinanciamiento_label = Label(user_info_frame, text="Cofinanciamiento")
    componenteid_label = Label(user_info_frame, text="Componente de I+D")
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

def verificar_csv():
    if os.path.isfile('datos.csv'):
        ver_fuente_financiamiento()
    else:
        messagebox.showerror(message="No existen datos")

root = Tk()
root.title("Mi Aplicación")
root.geometry("640x480")

boton_uno = Button(root, text="Ver compatibilidad con financiamientos", command=lambda: messagebox.showinfo(message="Te me calmas crack, esta en proceso", title="En proceso"))
boton_uno.pack(pady=20)

boton_dos = Button(root, text="Agregar fuente de financiamiento", command=agregar_fuente_financiamiento)
boton_dos.pack(pady=20)

boton_tres = Button(root, text="Ver fuentes de financiamientos disponibles", command=verificar_csv) # manejo de errores cuando no existe el archivo
boton_tres.pack(pady=20)

button_salir = Button(root, text="Salir", command=root.quit)
button_salir.pack(pady=20)

# Iniciar el bucle principal
root.mainloop()

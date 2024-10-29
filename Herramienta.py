from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import csv

listaPersona = ["Persona Juridica", "Persona Natural"]
listaTrl = ["TRL 1-3", "TRL 4-6", "TRL 6-9"]
listaAntig = ["Sin restriccion", "Menos de 12 meses", "Menos de 24 meses", "Menos de 36 meses"]
listaSector = ["Cualquiera", "Inteligencia Artificial", "Biotecnologia", "Fintech", "Tecnologias Limpias", "Software"]
listaNvVentas = ["No aplica", "Menor a 100.000 UF", "Mas de 100.000 UF"]
listaVinculoUni = ["No requerido", "Si(Estudiante o egresado)", "Si(Colaboracion con universidades)"]
listaCofinanciamiento = ["No requerido", "Si(20-30% aporte propio)", "Si(30% aporte propio)", "Si(40% aporte propio)"]
listaID = ["Moderado", "Moderado a alto", "Alto", "Muy alto"]
listaTraccionC = ["No se requiere traccion previa", "Requiere validacion de mercado", "Se requiere traccion inicial", "Se requiere validacion inicial", "Alta traccion comercial"]


def guardar_data():
    
    if nombre_emp_entry.get() and persona_combobox.get() and trl_combobox.get() and antiguedad_combobox.get() and sector_combobox.get() and ventas_anuales_combobox.get() and vinculo_universidad_combobox.get() and cofinanciamiento_combobox.get() and componenteid_combobox.get() and traccion_comercial_combobox.get() and descripcion_entry.get():
        datos = [nombre_emp_entry.get(), persona_combobox.get(), trl_combobox.get(), antiguedad_combobox.get(), sector_combobox.get(), ventas_anuales_combobox.get(), vinculo_universidad_combobox.get(), cofinanciamiento_combobox.get(), componenteid_combobox.get(), traccion_comercial_combobox.get(), descripcion_entry.get()]

        with open("datos.csv", "a", newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(datos)
        
        messagebox.showinfo(message="Agregado con éxito", title="Aviso")

    else:
        messagebox.showwarning(title="Error", message="Faltan datos")


# def inicio():

#     lbl1 = Label(root, text="Elige una opcion")
#     lbl1.pack(pady=40)

#     button = Button(root, text="Ver compatibilidad con financiamientos", command=on_button_click)
#     button.pack(pady=40)

#     button2 = Button(root, text="Agregar fuente de financiamiento", command=agregar_fuente)
#     button2.pack(pady=40)

#     button3 = Button(root, text="Mostrar fuentes de financiamientos disponibles", command=on_button_click)
#     button3.pack(pady=40)

#     button4 = Button(root, text="Salir", command=root.quit)
#     button4.pack(pady=40)

root = Tk()
root.title("Mi Aplicación")
root.geometry("1024x768")

frame = Frame(root)
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
#financiamiento_label = Label(user_info_frame, text="Financiamiento previo")
vinculo_universidad_label = Label(user_info_frame, text="Vinculo con universidad")
cofinanciamiento_label = Label(user_info_frame, text="Cofinanciamiento")
componenteid_label = Label(user_info_frame, text="Componente de I+D")
traccion_comercial_label = Label(user_info_frame, text="Traccion comercial")
descripcion_label = Label(user_info_frame, text="Descripcion")

# Seccion donde el moderados ingresa los datos

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

boton_cierre = Button(user_info_frame, text="Salir",command=root.quit)
boton_cierre.grid(row=23, column=0, sticky="news")

boton_guardado = Button(user_info_frame, text="Guardar", command=guardar_data)
boton_guardado.grid(row=22, column=0, sticky="news")


# Iniciar el bucle principal
root.mainloop()

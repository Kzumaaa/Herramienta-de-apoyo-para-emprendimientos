from tkinter import *

class Ffinanciamiento:
    def __init__(self, nombre, tipoP, trl, antiguedad, sector, NvVentas, ReqVincUni, ReqCofinan, ReqID, ReqTrCo, Descripcion):
        self.N = nombre
        self.TP = tipoP
        self.TRL = trl
        self.ANT = antiguedad
        self.SC = sector
        self.NV = NvVentas
        self.RVU = ReqVincUni
        self.RC = ReqCofinan
        self.ID = ReqID
        self.TC = ReqTrCo
        self.D = Descripcion

    def mostrar_info(self):
        return (f"Fuente de financiamiento: {self.N}\n"
                f"Tipo de persona requerida: {self.TP}\n"
                f"TRL requerido: {self.TRL}\n"
                f"Antiguedad requerida: {self.ANT}\n"
                f"Sector requerido: {self.SC}\n"
                f"Nivel de ventas requeridas: {self.NV}\n"
                f"Vinculo con universidad requerido: {self.RVU}\n"
                f"Cofinanciamiento requerido: {self.RC}\n"
                f"I+D requerido: {self.ID}\n"
                f"Traccion comercial requerido: {self.TC}\n"
                f"Traccion comercial requerido: {self.D}\n")


def on_button_click():
    print("¡Hola, mundo!")

def mostrar_opcion(opcion):
    print(f"Seleccionaste: {opcion}")
# Crear la ventana principal

def inicio():

    lbl1 = Label(root, text="Elige una opcion")
    lbl1.pack(pady=40)

    button = Button(root, text="Ver compatibilidad con financiamientos", command=on_button_click)
    button.pack(pady=40)
    #button.place(x=70,y=500)

    button2 = Button(root, text="Agregar fuente de financiamiento", command=agregar_fuente)
    button2.pack(pady=40)
    #button2.place(x=280,y=500)

    button3 = Button(root, text="Mostrar fuentes de financiamientos disponibles", command=on_button_click)
    button3.pack(pady=40)
    #button3.place(x=490,y=500)
    
    button4 = Button(root, text="Salir", command=root.quit)
    button4.pack(pady=40)

def agregar_fuente():

    ventana_secundaria = Toplevel(root)
    ventana_secundaria.title("Ventana Secundaria")
    ventana_secundaria.geometry("800x600")

    listaPersona = ["Persona Juridica", "Persona Natural"]
    listaTrl = ["TRL 1-3", "TRL 4-6", "TRL 6-9"]
    listaAntig = ["Sin restriccion", "Menos de 12 meses", "Menos de 24 meses", "Menos de 36 meses"]
    listaSector = ["Cualquiera", "Inteligencia Artificial", "Biotecnologia", "Fintech", "Tecnologias Limpias", "Software"]
    listaNvVentas = ["No aplica", "Menor a 100.000 UF", "Mas de 100.000 UF"]
    listaVinculoUni = ["No requerido", "Si(Estudiante o egresado)", "Si(Colaboracion con universidades)"]
    listaCofinanciamiento = ["No requerido", "Si(20-30% aporte propio)", "Si(30% aporte propio)", "Si(40% aporte propio)"]
    listaID = ["Moderado", "Moderado a alto", "Alto", "Muy alto"]
    listaTraccionC = ["No se requiere traccion previa", "Requiere validacion de mercado", "Se requiere traccion inicial", "Se requiere validacion inicial", "Alta traccion comercial"]

    Persona = StringVar(ventana_secundaria)
    Trl = StringVar(ventana_secundaria)
    Antiguedad = StringVar(ventana_secundaria)
    Sector = StringVar(ventana_secundaria)
    NvVentas = StringVar(ventana_secundaria)
    VinculoUni = StringVar(ventana_secundaria)
    Cofinan = StringVar(ventana_secundaria)
    IplusD = StringVar(ventana_secundaria)
    TraC = StringVar(ventana_secundaria)
    # Ojito

    lbl1 = Label(ventana_secundaria, text="Nombre", bg="white")
    lbl1.place(x=10,y=10, width=200, height=30)

    txt1 = Entry(ventana_secundaria, bg="white")
    txt1.place(x=220,y=10, width=200, height=30)

    lbl2 = Label(ventana_secundaria, text="Tipo de Persona", bg="white")
    lbl2.place(x=10,y=50, width=200, height=30)

    menu2 = OptionMenu(ventana_secundaria,Persona ,*listaPersona)
    menu2.place(x=220,y=50, width=200, height=30)

    lbl3 = Label(ventana_secundaria, text="TRL", bg="white")
    lbl3.place(x=10,y=90, width=200, height=30)

    menu3 = OptionMenu(ventana_secundaria,Trl ,*listaTrl)
    menu3.place(x=220,y=90, width=200, height=30)

    lbl4 = Label(ventana_secundaria, text="Antiguedad", bg="white")
    lbl4.place(x=10,y=130, width=200, height=30)

    menu4 = OptionMenu(ventana_secundaria ,Antiguedad ,*listaAntig)
    menu4.place(x=220,y=130, width=200, height=30)

    lbl5 = Label(ventana_secundaria, text="Sector", bg="white")
    lbl5.place(x=10,y=170, width=200, height=30)

    menu5 = OptionMenu(ventana_secundaria ,Sector ,*listaSector)
    menu5.place(x=220,y=170, width=200, height=30)

    lbl6 = Label(ventana_secundaria, text="Nivel de ventas", bg="white")
    lbl6.place(x=10,y=210, width=200, height=30)

    menu6 = OptionMenu(ventana_secundaria ,NvVentas ,*listaNvVentas)
    menu6.place(x=220,y=210, width=200, height=30)

    lbl7 = Label(ventana_secundaria, text="Vinculo con universidad", bg="white")
    lbl7.place(x=10,y=250, width=200, height=30)

    menu7 = OptionMenu(ventana_secundaria ,VinculoUni ,*listaVinculoUni)
    menu7.place(x=220,y=250, width=200, height=30)

    lbl8 = Label(ventana_secundaria, text="Cofinanciamiento", bg="white")
    lbl8.place(x=10,y=290, width=200, height=30)

    menu8 = OptionMenu(ventana_secundaria ,Cofinan ,*listaCofinanciamiento)
    menu8.place(x=220,y=290, width=200, height=30)

    lbl9 = Label(ventana_secundaria, text="I+D", bg="white")
    lbl9.place(x=10,y=330, width=200, height=30)

    menu9 = OptionMenu(ventana_secundaria ,IplusD ,*listaID)
    menu9.place(x=220,y=330, width=200, height=30)

    lbl10 = Label(ventana_secundaria, text="Traccion comercial", bg="white")
    lbl10.place(x=10,y=370, width=200, height=30)

    menu10 = OptionMenu(ventana_secundaria ,TraC ,*listaTraccionC)
    menu10.place(x=220,y=370, width=230, height=30)

    lbl11 = Label(ventana_secundaria, text="Descripcion", bg="white")
    lbl11.place(x=10,y=410, width=200, height=30)

    txt2 = Entry(ventana_secundaria, bg="white")
    txt2.place(x=220,y=410, width=500, height=30)

    button4 = Button(ventana_secundaria, text="Guardar", command=ventana_secundaria.destroy)
    button4.place(x=10,y=540, width=60, height=30)

    button5 = Button(ventana_secundaria, text="Volver", command=ventana_secundaria.destroy)
    button5.place(x=720,y=540, width=60, height=30)


#menu.pack(side="left")

#corfo = Ffinanciamiento()

root = Tk()
root.title("Mi Aplicación")

root.geometry("800x600")

inicio()
# Crear un botón

#button.pack(side="bottom")




# Iniciar el bucle principal
root.mainloop()

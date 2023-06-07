#Registros de estudiantes 
# Estado academico Y estado de salud

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#FUNCIONES DE LA APP
# abrir toplevel codigos
def abrir_toplevel_codigos():
    global toplevel_CODIGOS
    toplevel_CODIGOS = Toplevel()
    toplevel_CODIGOS.title("CODIGOS")
    toplevel_CODIGOS.resizable(False, False)
    toplevel_CODIGOS.geometry("500x200")
    toplevel_CODIGOS.config(bg="white")

    # logo de la app
    lb_logo2 = Label(toplevel_CODIGOS, image=LOGO2, bg="white")
    lb_logo2.place(x=10,y=10)

    # etiqueta para valor en codigos
    lb_codigos = Label(toplevel_CODIGOS, text = "Codigo del estudiante  ")
    lb_codigos.config(bg="green4", fg="white", font=("Helvetica", 18))
    lb_codigos.place(x=250, y=20)

    # caja de texto para poner el codigo de estudiante
    entry_codigos = Entry(toplevel_CODIGOS, textvariable= CODIGOS)
    entry_codigos.config(bg="white", fg="Black", font=("Times New Roman", 20), width=9)
    entry_codigos.focus_set()
    entry_codigos.place(x=340,y=60)

   # boton para convertir
    bt_aceptar = Button(toplevel_CODIGOS,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=200, y=150, width=100, height=30)

# aceptar
def aceptar():
    global CODI
    CODI = int(CODIGOS.get())
    toplevel_CODIGOS.destroy()


def abrir_topleve_medicos():
    global toplevel_MEDICOS
    toplevel_MEDICOS = Toplevel()
    toplevel_MEDICOS.title("DATOS MEDICOS")
    toplevel_MEDICOS.resizable(False, False)
    toplevel_MEDICOS.geometry("500x200")
    toplevel_MEDICOS.config(bg="white")

    # logo de la app
    lb_LOGO3 = Label(toplevel_MEDICOS, image=LOGO3, bg="white")
    lb_LOGO3.place(x=10,y=10)

    # etiqueta para valor en altura
    lb_c = Label(toplevel_MEDICOS, text = "ALTURA EN METROS: ")
    lb_c.config(bg="white", fg="Black", font=("Helvetica", 18))
    lb_c.place(x=150, y=50)

    # caja de texto para ponerla altura 
    entry_c = Entry(toplevel_MEDICOS, textvariable= ALTURA)
    entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=400,y=50)

    # etiqueta para valor del peso
    lb_c = Label(toplevel_MEDICOS, text = "PESO EN KILOS: ")
    lb_c.config(bg="white", fg="Black", font=("Helvetica", 18))
    lb_c.place(x=200, y=90)

    # caja de texto para poner el peso
    entry_v = Entry(toplevel_MEDICOS, textvariable= PESO)
    entry_v.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_v.focus_set()
    entry_v.place(x=400,y=90)

   # boton para convertir
    bt_calcular = Button(toplevel_MEDICOS,text="CALCULAR", command=bre)
    bt_calcular.place(x=250, y=150, width=100, height=30)
    

def calcular():
    global Medico
    global MedicO
    Medico = float(ALTURA)
    MedicO = float(PESO)
    toplevel_MEDICOS.destroy()

def abrir_topleve_promedio():
    global toplevel_PROMEDIO
    toplevel_PROMEDIO = Toplevel()
    toplevel_PROMEDIO.title("DATOS MEDICOS")
    toplevel_PROMEDIO.resizable(False, False)
    toplevel_PROMEDIO.geometry("500x200")
    toplevel_PROMEDIO.config(bg="white")

    # logo de la app
    lb_LOGO4 = Label(toplevel_PROMEDIO, image=LOGO4, bg="white")
    lb_LOGO4.place(x=270,y=-5)

    # etiqueta para la nota1 
    lb_c = Label(toplevel_PROMEDIO, text = "CORTE 1: ")
    lb_c.config(bg="white", fg="Black", font=("Helvetica", 18))
    lb_c.place(x=75, y=10)

    # etiqueta para la nota2 
    lb_c = Label(toplevel_PROMEDIO, text = "CORTE 2: ")
    lb_c.config(bg="white", fg="Black", font=("Helvetica", 18))
    lb_c.place(x=75, y=40)

    # etiqueta para la nota3 
    lb_c = Label(toplevel_PROMEDIO, text = "CORTE 3: ")
    lb_c.config(bg="white", fg="Black", font=("Helvetica", 18))
    lb_c.place(x=75, y=70)

    # etiqueta para la nota4 
    lb_c = Label(toplevel_PROMEDIO, text = "CORTE 4: ")
    lb_c.config(bg="white", fg="Black", font=("Helvetica", 18))
    lb_c.place(x=75, y=100 )

    # caja de texto para poner NOTA 1
    entry = Entry(toplevel_PROMEDIO, textvariable= NOTA1)
    entry.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry.focus_set()
    entry.place(x=200,y=10)

    # caja de texto para poner NOTA 2
    entry_a = Entry(toplevel_PROMEDIO, textvariable= NOTA2)
    entry_a.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_a.focus_set()
    entry_a.place(x=200,y=40)

    # caja de texto para poner NOTA 3
    entry_b = Entry(toplevel_PROMEDIO, textvariable= NOTA3)
    entry_b.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_b.focus_set()
    entry_b.place(x=200,y=70)

    # caja de texto para poner NOTA 4
    entry_b = Entry(toplevel_PROMEDIO, textvariable= NOTA4)
    entry_b.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_b.focus_set()
    entry_b.place(x=200,y=100)

   # boton para dar promedio
    bt_aceptar = Button(toplevel_PROMEDIO,text="Aceptar", command=OKI)
    bt_aceptar.place(x=200, y=150, width=100, height=30)

    # aceptar
def OKI():
    global promedi
    promedi = float(NOTA1.get())
    promedi = float(NOTA2.get())
    promedi = float(NOTA3.get())
    promedi = float(NOTA4.get())
    toplevel_PROMEDIO.destroy()


def bre():
    global PESO
    global ALTURA
    PESO = float(PESO.get())
    ALTURA = float(ALTURA.get())

    a = PESO / ALTURA ** 2

    if a < 16:
        t_resultados.insert(INSERT, f"\n {int(CODIGOS.get())} = CRITERIO DE INGRESO EN HOSPITAL ")
    elif 16<= a <17:
        t_resultados.insert(INSERT, f"\n {int(CODIGOS.get())} = INFRAPESO ")
    elif 17<= a < 18:
        t_resultados.insert(INSERT, f"\n  {int(CODIGOS.get())}=BAJO PESO ")
    elif 18<= a <25:
        t_resultados.insert(INSERT, f"\n {int(CODIGOS.get())} = NORMAL  ")
    elif 25<= a <30:
        t_resultados.insert(INSERT, f"\n {int(CODIGOS.get())}=Sobrepeso (obesidad grado I) ")
    elif 30<= a < 35:
        t_resultados.insert(INSERT, f"\n  {int(CODIGOS.get())} = Sobrepeso crónico (obesidad grado II) ")
    elif 35<= a <40:
        t_resultados.insert(INSERT, f"\n  {int(CODIGOS.get())} =  Obesidad premórbida (obesidad grado III) ")
    else:
        a >40
        t_resultados.insert(INSERT, f"\n {int(CODIGOS.get())} Obesidad mórbida (obesidad de grado IV) ")


    toplevel_MEDICOS.destroy()
    
    

#ventana principal de la app

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# tamaño de la ventana
ventana_principal.geometry("1000x700")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="cyan")

#Variables globales

CODIGOS = StringVar()
ALTURA = StringVar()
PESO = StringVar()
NOTA1 = StringVar()
NOTA2 = StringVar()
NOTA3 = StringVar()
NOTA4 = StringVar()


#frame entrada datos
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="dark slate blue", width=900, height=180)
frame_entrada.place(x=50, y=30)

#Logo de la app
MEDICO = PhotoImage(file="img/MEDICOO.png")
lb_MEDICO = Label(frame_entrada, image=MEDICO, bg="white")
lb_MEDICO.place(x=0,y=-27)

PROFE = PhotoImage(file="img/Profe.png")
lb_PROFE = Label(frame_entrada, image=PROFE, bg="white")
lb_PROFE.place(x=650,y=-10)

LOGO3 = PhotoImage(file="img/MEDICOREX.png")
lb_LOGO3 = Label(frame_entrada, image=LOGO3, bg="white")

LOGO4 = PhotoImage(file="img/NOTAS.png")
lb_LOGO4 = Label(frame_entrada, image=LOGO4, bg="white")

#Titulo de la app
titulo = Label(frame_entrada, text="REGISTRO UIS")
titulo.config(bg = "white",fg="dark slate blue", font=("Arial Black", 20))
titulo.place(x=350,y=10)

# boton para abrir Toplevel para ingresar el codigo del estudiante
bt_CODIGOS = Button(frame_entrada, text="INGRESA TU CODIGO", command=abrir_toplevel_codigos)
bt_CODIGOS.place(x=400, y=60)
 # boton para abrir Toplevel para ingresar tus datos medicos
bt_MEDICO = Button(frame_entrada, text=" <----MEDICO", command=abrir_topleve_medicos)
bt_MEDICO.place(x=420, y=90)
 # boton para abrir Toplevel para ingresar tus notas parciales
bt_PROMEDIO = Button(frame_entrada, text="PROMEDIO-->", command=abrir_topleve_promedio)
bt_PROMEDIO.place(x=420, y=120)


LOGO2 = PhotoImage(file="img/logo_uis.png")


#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=900, height=400)
frame_resultados.place(x=50, y=250)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="white", font=("Courier", 24))
t_resultados.place(x=45,y=25,width=800,height=350)

ventana_principal.mainloop()
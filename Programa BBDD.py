from tkinter import *
from tkinter import messagebox
import mysql.connector

#-----------------------------------------------------------#

def conexion():
    miconexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="joajoa123",
        database="Usuarios"
        )
    micursor = miconexion.cursor()
    try:
        micursor.execute("CREATE DATABASE Usuarios")
        messagebox.showinfo("Base de Datos", "BBDD creada con éxito")
    except mysql.connector.errors.DatabaseError:
        messagebox.showwarning("Atención", "La BBDD ya existe")
    try:
        tabla_users = "CREATE TABLE datosusuarios (\
          id INT PRIMARY KEY AUTO_INCREMENT,\
          nombre_usuario VARCHAR(50) NOT NULL,\
          password VARCHAR(50) NOT NULL,\
          apellido VARCHAR(50) NOT NULL,\
          direccion VARCHAR(50) NOT NULL,\
          comentarios VARCHAR(150) NOT NULL\
        )"
        micursor.execute(tabla_users)
        messagebox.showinfo("Base de Datos", "Tabla creada con éxito")
    except mysql.connector.errors.ProgrammingError:
        messagebox.showwarning("Atención", "La tabla ya existe")
    micursor.close()
    miconexion.close()


def salir():
     valor=messagebox.askquestion("Salir","¿Deseas salir del programa?")
     if valor := True:
        root.destroy()

def direccion_basededatos():
        miconexion=mysql.connector.connect(
            host="localhost",
            user="root",
            password="joajoa123",
            database="Usuarios"
            )
        micursor=miconexion.cursor()
        micursor.execute ("show variables like 'datadir'")
        resultado=micursor.fetchone()
        print(resultado)
        micursor.close()
        miconexion.close()
        return resultado

def borrarcampos():
    miid.set("")
    minombre.set("")
    micontra.set("")
    miapellido.set("")
    midireccion.set("")
    textocomentario.delete(1.0, END)


def create():
    miconexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="joajoa123",
        database="Usuarios"
        )
    micursor=miconexion.cursor()
    insercion = "INSERT INTO datosusuarios (nombre_usuario, password, apellido, direccion, comentarios) VALUES (%s, %s, %s, %s, %s)"
    valores = (minombre.get(), micontra.get(), miapellido.get(), midireccion.get(), textocomentario.get(1.0, END))
    micursor.execute(insercion, valores)

    miconexion.commit()
    messagebox.showinfo("Base de datos", "Registro insertado con exito")
    micursor.close()
    miconexion.close()

def read():
    miconexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="joajoa123",
        database="Usuarios"
        )
    micursor=miconexion.cursor()    
    seleccion="select * from datosusuarios where id=" + miid.get()
    micursor.execute(seleccion)
    devolucion=micursor.fetchall()
    for usuario in devolucion:
        miid.set(usuario[0])
        minombre.set(usuario[1])
        micontra.set(usuario[2])
        miapellido.set(usuario[3])
        midireccion.set(usuario[4])
        textocomentario.insert(1.0, usuario[5])
    micursor.close()
    miconexion.close()

def update():
    miconexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="joajoa123",
        database="Usuarios"
        )
    micursor=miconexion.cursor()    
    actualizar="update datosusuarios set nombre_usuario= '" + minombre.get() + "', password= '" + micontra.get() + "', apellido= '" + miapellido.get() + "', direccion= '" + midireccion.get() + "', comentarios= '" + textocomentario.get(1.0, END) + "' where id=" + miid.get()
    micursor.execute(actualizar)
    miconexion.commit()
    messagebox.showinfo("Base de datos", "Registro actualizado con exito")
    micursor.close()
    miconexion.close()

def delete():
    miconexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="joajoa123",
        database="Usuarios"
        )
    micursor=miconexion.cursor()
    borrar="delete from datosusuarios where id = " + miid.get()
    micursor.execute(borrar)
    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con exito")
    miid.set("")
    minombre.set("")
    micontra.set("")
    miapellido.set("")
    midireccion.set("")
    textocomentario.delete(1.0, END)  
    micursor.close()
    miconexion.close()  

def droptable():
    miconexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="joajoa123",
        database="Usuarios"
        )
    micursor=miconexion.cursor()   
    tirar="drop table datosusuarios" 
    micursor.execute(tirar)
    messagebox.showinfo("Tabla borrada", "La tabla datosusarios ha sido eliminada")
    micursor.close()
    miconexion.close()

#-----------------------------------------------------------#

root=Tk()
root.title("Creador de BBDD")
root.geometry("500x350")

barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)

bbddmenu=Menu(barramenu, tearoff=0)
bbddmenu.add_command(label="Conectar", command=conexion)
bbddmenu.add_command(label="Direccion", command=direccion_basededatos)
bbddmenu.add_command(label="Salir", command=salir)

borrarmenu=Menu(barramenu, tearoff=0)
borrarmenu.add_command(label="Borrar campos", command=borrarcampos)

CRUDmenu=Menu(barramenu, tearoff=0)
CRUDmenu.add_command(label="Crear", command=create)
CRUDmenu.add_command(label="Leer", command=read)
CRUDmenu.add_command(label="Actualizar", command=update)
CRUDmenu.add_command(label="Borrar", command=delete)
CRUDmenu.add_command(label="Tirar", command=droptable)

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label="Licencia")
ayudamenu.add_command(label="Acerda de...")

barramenu.add_cascade(label="BBDD", menu=bbddmenu)
barramenu.add_cascade(label="Borrar", menu=borrarmenu)
barramenu.add_cascade(label="CRUD", menu=CRUDmenu)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)

#------------------------------------------------------#

frame1=Frame(root)
frame1.pack()

miid=StringVar()
minombre=StringVar()
micontra=StringVar()
miapellido=StringVar()
midireccion=StringVar()

cuadroID=Entry(frame1, textvariable=miid)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadronombre=Entry(frame1, textvariable=minombre)
cuadronombre.grid(row=1, column=1, padx=10, pady=10)

cuadrocontra=Entry(frame1, textvariable=micontra)
cuadrocontra.grid(row=2, column=1, padx=10, pady=10)
cuadrocontra.config(show="*")

cuadroapellido=Entry(frame1, textvariable=miapellido)
cuadroapellido.grid(row=3, column=1, padx=10, pady=10)

cuadrodireccion=Entry(frame1, textvariable=midireccion)
cuadrodireccion.grid(row=4, column=1, padx=10, pady=10)

textocomentario=Text(frame1, width=16, height=5)
textocomentario.grid(row=5, column=1, padx=10, pady=10)
scroll=Scrollbar(frame1, command=textocomentario.yview)
scroll.grid(row=5, column=2, sticky="nsew")
textocomentario.config(yscrollcommand=scroll.set)

#--------------------------------------------------------#

idlabel=Label(frame1, text="ID:")
idlabel.grid(row=0, column=0, padx=10, pady=10)

nombrelabel=Label(frame1, text="Nombre:")
nombrelabel.grid(row=1, column=0, padx=10, pady=10)

contralabel=Label(frame1, text="Contraseña:")
contralabel.grid(row=2, column=0, padx=10, pady=10)

apellidolabel=Label(frame1, text="Apellido:")
apellidolabel.grid(row=3, column=0, padx=10, pady=10)

direccionlabel=Label(frame1, text="Direccion:")
direccionlabel.grid(row=4, column=0, padx=10, pady=10)

comentarioslabel=Label(frame1, text="Comentarios:")
comentarioslabel.grid(row=5, column=0, padx=10, pady=10)

#-------------------------------------------------------------#

frame2=Frame(root)
frame2.pack()

botoncrear=Button(frame2, text="Create", command=create)
botoncrear.grid(row=1, column=0, padx=10, pady=10)

botonleer=Button(frame2, text="Read", command=read)
botonleer.grid(row=1, column=1, padx=10, pady=10)

botonactualizar=Button(frame2, text="Update", command=update)
botonactualizar.grid(row=1, column=2, padx=10, pady=10)

botonborrar=Button(frame2, text="Delete", command=delete)
botonborrar.grid(row=1, column=3, padx=10, pady=10)


root.mainloop()
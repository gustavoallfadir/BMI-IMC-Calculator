#-----Calculadora de imc------

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from io import open

root=Tk()
root.title("Calculadora de IMC")
root.geometry("+300+100")
root.resizable(0,0)


frame=Frame(root, width=500, height=600)
frame.pack()

#---Para poder encontrar la imagen desde el archivo ejecutable----

import os

def find_image(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

try:
    imagen=PhotoImage(file=find_image("redmatrix.png","."))
    fondo=Label(frame, image=imagen).place(x=0, y =0)
except:
    pass

#--------Variables--------------
pesoVar=StringVar()
alturaVar=StringVar()
IMCVar=StringVar()
DiagVar=StringVar()


#--------Funciones--------------

def calcular_IMC():
    peso=float(pesoVar.get())
    altura=float(alturaVar.get())
    imc=float("{0:.2f}".format(peso/(altura*altura)))
    
    IMCVar.set(imc)


    if imc < 1:
        DiagVar.set("error")
    
    elif imc < 16:
        DiagVar.set("Infrapeso severo")
    
    elif imc >15.99 and imc <17:
        DiagVar.set("Infrapeso moderado")
    
    elif imc >16.99 and imc <18.50:
        DiagVar.set("Bajo peso")

    elif imc >18.49 and imc <25:
        DiagVar.set("Peso ideal")
    
    elif imc > 24.99 and imc < 30:
        DiagVar.set("Sobrepeso")
    
    elif imc > 29.99 and imc < 35:
        DiagVar.set("Sobrepeso crónico (obesidad grado I)")
    
    elif imc > 34.99 and imc < 40:
        DiagVar.set("Obesidad premórbida (obesidad grado II)")
    
    elif imc > 39.99 and imc < 45:
        DiagVar.set("Obesidad mórbida (obesidad grado III)")

    elif imc > 44.99:
        DiagVar.set("obesidad hipermórbida (obesidad grado IV)")
    


def save():
    savepath=filedialog.asksaveasfilename(title="Guardar como archivo de texto", filetypes=[("Archivo de texto", ".txt")])

    archivo=open(savepath, "w")
    saveinfo=["Peso: "+pesoVar.get()+"kg","\n","Altura: "+alturaVar.get()+"m","\n","IMC: " + IMCVar.get(),"\n", "Diagnóstico: "+ DiagVar.get()]
    saver="".join(saveinfo)
    archivo.write(saver)
    archivo.close()

def salir():
    kill=messagebox.askyesno("Salir","¿Desea salir del programa?")
    if kill==TRUE:
        root.destroy()

def acerca_de():
    messagebox.showinfo("Calculadora de IMC","Programa escrito por Guzblack\nguz.black@gmail.com")
    
#--------Barra de menu----------
barramenu=Menu(root)

root.config(menu=barramenu)


menuArchivo=Menu(barramenu, tearoff=0)
menuArchivo.add_command(label="Guardar en archivo de texto",command=lambda:save())
menuArchivo.add_command(label="Salir", command=lambda:salir())


menuAyuda=Menu(barramenu,tearoff=0)
menuAyuda.add_command(label="Acerca de",command=lambda:acerca_de())

#-----------Textos de la barra menu----------

barramenu.add_cascade(label="Archivo",menu=menuArchivo)
barramenu.add_cascade(label="Ayuda",menu=menuAyuda)


#-----------Contenidos del frame------------

pesotxt=Label(frame, text="Peso (kg):", font=(20), fg="white", bg="black")
pesotxt.grid(row=0, column=0, padx=30, pady=30)

pesobox=Entry(frame,font=(20), width=15, textvariable=pesoVar)
pesobox.grid(row=0, column=1, padx=30, pady=30, sticky="w")

alturatxt=Label(frame, text="Altura (m):", font=(20), fg="white", bg="black")
alturatxt.grid(row=1, column=0, padx=30, pady=30)

alturabox=Entry(frame,font=(20), width=15, textvariable=alturaVar)
alturabox.grid(row=1, column=1, padx=30, pady=30,sticky="w")


IMCtxt=Label(frame, text="IMC calculado:", font=(20), fg="white", bg="black")
IMCtxt.grid(row=2, column=0, padx=30, pady=30)

IMCbox=Entry(frame,font=(20), width=15, textvariable=IMCVar)
IMCbox.grid(row=2, column=1, padx=30, pady=30, sticky="w" )
IMCbox.config(state="readonly")

diagtxt=Label(frame, text="Diagnóstico:", font=(20), fg="white", bg="black")
diagtxt.grid(row=3, column=0, padx=30, pady=30)


diagbox=Entry(frame,font=(20),width=33, textvariable=DiagVar)
diagbox.grid(row=3, column=1,sticky="w", columnspan=3, padx=30, pady=30)
diagbox.config(state="readonly")

#--------Botones------------------
botonCalcular=Button(frame, text="Calcular IMC", font=(20), fg="white", bg="black",command=calcular_IMC)
botonCalcular.grid(row=0,column=3, padx=30, pady=30, rowspan=3)
botonCalcular.config(height=4)



#MAINLOOP
root.mainloop()
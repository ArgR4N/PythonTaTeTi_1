from tkinter import*

#RAIZ

raiz = Tk()
raiz.title("Prueba 1")
raiz.resizable(0,1)
raiz.iconbitmap("icono.ico")
#raiz.geometry("500x250")
#raiz.config(bg = "white")

#FRAME

frame1=Frame(raiz)
frame1.pack()
#frame1.pack(side="left", anchor="n")
#frame1.pack(fill="x", expand= "true") 
#para que se expanda en el medio}
#y para que se expanda todo
#frame1.pack(fill="both", expand ="true")
frame1.config(relief="groove")
#frame1.config(bd=35)
#frame1.config(bg = "grey")
frame1.config(width ="150", height="150")
frame1.config(cursor="pirate")

#LABEL

label1=Label(frame1, text="nombre")
label1.grid(row = 0, column=0,sticky="e",padx = 50,pady=5)

label2=Label(frame1,text="apellido")
label2.grid(row=1,column=0,sticky="e",padx = 50,pady=5)

label3=Label(frame1,text="segundo nombre")
label3.grid(row=2,column=0,sticky="e",padx = 25,pady=5)

label4=Label(frame1,text="segundo apellido")
label4.grid(row=3,column=0,sticky="e",padx = 25,pady=5)

#entry
cuadro1=Entry(frame1)
cuadro1.grid(row=0, column = 1,pady=5)

cuadro2=Entry(frame1)
cuadro2.grid(row=1,column=1,pady=5)

cuadro3=Entry(frame1)
cuadro3.grid(row=2,column=1,pady=5)

cuadro4=Entry(frame1)
cuadro4.grid(row=3,column=1,pady=5)

#siempre al final
raiz.mainloop()
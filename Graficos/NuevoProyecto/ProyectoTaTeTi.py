from tkinter import *

#Raiz
raiz=Tk()
raiz.iconbitmap("icono.ico")

#Frame
frame1=Frame(raiz)
frame1.pack()


imagencirculo=PhotoImage(file="imagen1.gif")
imagenequis=PhotoImage(file="imagen2.gif")

win_o1=StringVar()
win_x1=StringVar()

win_o2=StringVar()
win_x2=StringVar()

win_o3=StringVar()
win_x3=StringVar()


win_o4=StringVar()
win_x4=StringVar()

win_o5=StringVar()
win_x5=StringVar()

win_o6=StringVar()
win_x6=StringVar()

win_o7=StringVar()
win_x7=StringVar()


win_o8=StringVar()
win_x8=StringVar()

win_o9=StringVar()
win_x9=StringVar()

#LINIEA 1---------------------------------------------------------

def o1():

		label1=Label(frame1, image=imagencirculo)
		label1.grid(row=3,column=0)
		win_o1.set("a")
		
def x1():

		label2=Label(frame1, image=imagenequis)
		label2.grid(row=3,column=0)
		win_x1.set("a")

def o2():

		label3=Label(frame1, image=imagencirculo)
		label3.grid(row=3,column=2)
		win_o2.set("a")
def x2():

		label4=Label(frame1, image=imagenequis)
		label4.grid(row=3,column=2)
		win_x2.set("a")

def o3():

		label5=Label(frame1, image=imagencirculo)
		label5.grid(row=3,column=4)
		win_o3.set("a")
def x3():

		label6=Label(frame1, image=imagenequis)
		label6.grid(row=3,column=4)
		win_x3.set("a")
#LINEA 2-----------------------------------------------------------

def o4():

		label5=Label(frame1, image=imagencirculo)
		label5.grid(row=4,column=0)
		win_o4.set("a")
def x4():

		label6=Label(frame1, image=imagenequis)
		label6.grid(row=4,column=0)
		win_x4.set("a")


def o5():

		label7=Label(frame1, image=imagencirculo)
		label7.grid(row=4,column=2)
		win_o5.set("a")
def x5():

		label8=Label(frame1, image=imagenequis)
		label8.grid(row=4,column=2)
		win_x5.set("a")


def o6():

		label8=Label(frame1, image=imagencirculo)
		label8.grid(row=4,column=4)
		win_o6.set("a")
def x6():

		label9=Label(frame1, image=imagenequis)
		label9.grid(row=4,column=4)
		win_x6.set("a")

#LINEA 3-----------------------------------------------------------

def o7():

		label10=Label(frame1, image=imagencirculo)
		label10.grid(row=5,column=0)
		win_x7.set("a")
def x7():

		label11=Label(frame1, image=imagenequis)
		label11.grid(row=5,column=0)
		win_o7.set("a")


def o8():

		label12=Label(frame1, image=imagencirculo)
		label12.grid(row=5,column=2)
		win_x8.set("a")
def x8():

		label13=Label(frame1, image=imagenequis)
		label13.grid(row=5,column=2)
		win_o8.set("a")


def o9():

		label14=Label(frame1, image=imagencirculo)
		label14.grid(row=5,column=4)
		win_x9.set("a")
def x9():

		label15=Label(frame1, image=imagenequis)
		label15.grid(row=5,column=4)
		win_o9.set("a")

#LINIEA 1---------------------------------------------------------

boton_o1=Button(frame1,text="o",width ="5", height="5", command=o1)
boton_o1.grid(row=0,column=0)

boton_x1=Button(frame1,text="x",width ="5", height="5", command=x1)
boton_x1.grid(row=0,column=1)



boton_o2=Button(frame1,text="o",width ="5", height="5", command=o2)
boton_o2.grid(row=0,column=2)

boton_x2=Button(frame1,text="x",width ="5", height="5", command=x2)
boton_x2.grid(row=0,column=3)



boton_o3=Button(frame1,text="o",width ="5", height="5", command=o3)
boton_o3.grid(row=0,column=4)

boton_x3=Button(frame1,text="x",width ="5", height="5", command=x3)
boton_x3.grid(row=0,column=5)

#LINEA 2-----------------------------------------------------------

boton_o4=Button(frame1,text="o",width ="5", height="5", command=o4)
boton_o4.grid(row=1,column=0)

boton_x4=Button(frame1,text="x",width ="5", height="5", command=x4)
boton_x4.grid(row=1,column=1)



boton_o5=Button(frame1,text="o",width ="5", height="5", command=o5)
boton_o5.grid(row=1,column=2)

boton_x5=Button(frame1,text="x",width ="5", height="5", command=x5)
boton_x5.grid(row=1,column=3)



boton_o6=Button(frame1,text="o",width ="5", height="5", command=o6)
boton_o6.grid(row=1,column=4)

boton_x6=Button(frame1,text="x",width ="5", height="5", command=x6)
boton_x6.grid(row=1,column=5)

#LINEA 3-----------------------------------------------------------

boton_o7=Button(frame1,text="o",width ="5", height="5", command=o7)
boton_o7.grid(row=2,column=0)

boton_x7=Button(frame1,text="x",width ="5", height="5", command=x7)
boton_x7.grid(row=2,column=1)



boton_o8=Button(frame1,text="o",width ="5", height="5", command=o8)
boton_o8.grid(row=2,column=2)

boton_x8=Button(frame1,text="x",width ="5", height="5", command=x8)
boton_x8.grid(row=2,column=3)



boton_o9=Button(frame1,text="o",width ="5", height="5", command=o9)
boton_o9.grid(row=2,column=4)

boton_x9=Button(frame1,text="x",width ="5", height="5", command=x9)
boton_x9.grid(row=2,column=5)

while win_o1!= ("a") and win_o2 != ("a") and win_o3 != ("a"):

	if	== ("a") and win_o2 == ("a") and win_o3 == ("a")

raiz.mainloop()
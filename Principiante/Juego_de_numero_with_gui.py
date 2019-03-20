import random

from tkinter import *

#interfaz grafica

raiz=Tk()

raiz.title("TheGame")

raiz.resizable(True,True)

raiz.geometry("650x350")

raiz.config(bg = "black")

#frame

fr1 = Frame()

fr1.pack()

fr1.config(bg = "grey")

fr1.config(width = "650", height = "350")

fr1.config(relief="groove")

fr1.config(bd = 15)

#label

lb1 = Label(fr1, text = "tengo un numero de 4 digitos y todos son diferentes adivinalo")

lb1.place(x = 143, y = 0)

#entry

tj1 = Entry(fr1)

tj1.place(x = 242.5,y = 21)

#inicio

print("         ")
nom = input ("Primero, dime tu nombre:")
print("   ")
print ("Okey " + nom + " empezemos...")
print ("El juego es facil, yo tengo un numero de 4 digitos diferentes entre si...")
print ("Si lo adivinas Ganas, si no Pierdes")

#generacion de numero

num1 = random.randint(0,9)

num2 = random.randint(0,9)
while num2 == num1:
    num2 = random.randint(0,9)

num3 = random.randint(0,9)
while num3 == num2 or num3 == num1:
    num3 = random.randint(0,9)

num4 = random.randint(0,9)
while num4 == num3 or num4 == num2 or num4 == num1:
    num4 = random.randint(0,9)

num = str(num1) + str(num2) + str(num3) + str(num4)

####print(num)

#comparacion numero de jugador con el numero

numj = input("Escriba su numero:")

####print(numj1 + " " +  numj2 + " " + numj3 + " " + numj4)

if numj == num:	
	print("Ecxelente trabajo " + nom + "!")
	print("De una!!!")

while numj != num:

	numj1 = (numj[0:1])

	numj2 = (numj[1:2])

	numj3 = (numj[2:3])

	numj4 = (numj[3:4])

	if str(numj1) == str(num1):
		print("  ")
		print ("primer digito correcto")
		print("  ")

	if str(numj2) == str(num2):
		print("  ")
		print ("segundo digito correcto")
		print("  ")

	if str(numj3) == str(num3):
		print("  ")
		print ("tercer digito correcto")
		print("  ")

	if str(numj4) == str(num4):
		print("  ")
		print ("cuarto digito correcto")
		print("  ")

	numj = input("numero incorrecto:")
	
	if numj == num:	
		print("  ")
		print("Bien " + nom + ", has ganado")








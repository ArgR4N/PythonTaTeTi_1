import random

print("  ")
nom = input ("Primero, dime tu nombre:")
print("  ")
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

#comparacion numero de jugador con el numero en su digito

numj = input("Escriba su numero:")

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

#comparacion numero de jugador con el numero en otro digito
	
	if str(numj1) == str(num2) or str(numj1) == str(num3) or str(numj1) == str(num4):
		print("  ")
		print("el primer digito va en otro lugar!")
		print("  ")

	if str(numj2) == str(num1)	or str(numj2) == str(num3) or str(numj2) == str(num4):
		print("  ")
		print("el segundo digito va en otro lugar!")
		print("  ")

	if str(numj3) == str(num1) or str(numj3) == str(num2) or str(numj3) == str(num4):
		print("  ")
		print("el tercer digito va en otro lugar!")
		print("  ")

	if str(numj4) == str(num1) or str(numj4) == str(num2) or str(numj4) == str(num3):
		print("  ")
		print("el cuarto digito va en otro lugar!")
		print("  ")
		
#final

	numj = input("numero incorrecto:")

	if numj == num:	
		print("  ")
		print("Bien " + nom + ", has ganado")

	
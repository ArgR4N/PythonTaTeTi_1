import random

#creacion de numeros que se repitan 0 - 9


















#COMIENZO

print("Comienzo")

#PREGUNTAS

primera_r = input("Quieres que genere un numero aleatorio? ")

if primera_r == ("si") or primera_r == ("Si") or primera_r == ("Correcto") or primera_r == ("correcto"):
	digitos_r = input("queres que los digitos se repitan? ")

#LOS DIGITOS SE REPITEN

if digitos_r == ("si") or digitos_r == ("Si") or digitos_r == ("Correcto") or digitos_r == ("correcto"):
	cantidad1_r = input("de cuantos digitos? ")

if cantidad1_r == ("1"):
	num11 = random.randint(0,9)
	numc11 = str(num11)
	print(numc11)

if cantidad1_r == ("2"):
	num21 = random.randint(0,9)
	numc21 = str(num11) + str(num21)
	print(numc21)

if cantidad1_r== ("3"):
	num31 = random.randint(0,9)
	numc31 = str(num11) + str(num21) + str(num31)
	print(numc31)

if cantidad1_r == ("4"):
	num41 = random.randint(0,9)
	numc41 = str(num11) + str(num21) + str(num31) + str(num41)
	print(numc41)

if cantidad1_r == ("5"):
	num51 = random.randint(0,9)
	numc51 = str(num11) + str(num21) + str(num31) + str(num41) + str(num51)
	print(numc51)

if cantidad1_r == ("6"):
	num61 = random.randint(0,9)
	numc61 = str(num11) + str(num21) + str(num31) + str(num41) + str(num51) + str(num61)
	print(numc61)

if cantidad1_r == ("7"):
	num71 = random.randint(0,9)
	numc71 = str(num11) + str(num21) + str(num31) + str(num41) + str(num51) + str(num61) + str(num71)
	print(numc71)

if cantidad1_r == ("8"):
	num81 = random.randint(0,9)
	numc81 = str(num11) + str(num21) + str(num31) + str(num41) + str(num51) + str(num61) + str(num71) + str(num81)
	print(numc81)

if cantidad1_r == ("9"):
	print(numc91)

if cantidad1_r == ("10"):
	print(numc01)

#LOS DIGITOS NO SE REPITEN

if digitos_r == ("no") or digitos_r == ("No") or digitos_r == ("negativo") or digitos_r == ("Negativo"):
	cantidad2_r = input("de cuantos digitos? ")

if cantidad2_r == ("1"):
	print(numc12) 

if cantidad2_r == ("2"):
	print(numc22) 

if cantidad2_r == ("3"):
	print(numc32) 

if cantidad2_r == ("4"):
	print(numc42) 

if cantidad2_r == ("5"):
	print(numc52) 

if cantidad2_r == ("6"):
	print(numc62) 

if cantidad2_r == ("7"):
	print(numc72) 

if cantidad2_r == ("8"):
	print(numc82) 

if cantidad2_r == ("9"):
	print(numc92) 

if cantidad2_r == ("0"):
	print(numc02) 

#NEGATIVAS

while primera_r != ("si") or primera_r != ("Si") or primera_r != ("Correcto") or primera_r != ("correcto"):
	negativa_r = input("dime de nuevo que no entendi por favor... ")


	num91 = random.randint(0,9)

num01 = random.randint(0,9)

#creacion de numeros que no se repitan 0 - 9

num12 = random.randint(0,9)

num22 = random.randint(0,9)
while num22 == num12:
    num22 = random.randint(0,9)

num32 = random.randint(0,9)
while num32 == num22 or num32 == num12:
    num32 = random.randint(0,9)

num42 = random.randint(0,9)
while num42 == num32 or num42 == num22 or num42 == num12:
    num42 = random.randint(0,9)

num52 = random.randint(0,9)
while num52 == num32 or num52 == num22 or num52 == num12 or num52 == num42:
    num52 = random.randint(0,9)

num62 = random.randint(0,9)
while num62 == num32 or num62 == num22 or num62 == num12 or num62 == num42 or num62 == num52:
    num72 = random.randint(0,9)

num72 = random.randint(0,9)
while num72 == num32 or num72 == num22 or num72 == num12 or num72 == num42 or num72 == num52 or num72 == num62:
    num72 = random.randint(0,9)

num82 = random.randint(0,9)
while num82 == num32 or num82 == num22 or num82 == num12 or num82 == num42 or num82 == num52 or num82 == num62 or num82 == num72:
    num82 = random.randint(0,9)

num92 = random.randint(0,9)
while num92 == num32 or num92 == num22 or num92 == num12 or num92 == num42 or num92 == num52 or num92 == num62 or num92 == num72 or num92 == num82:
    num92 = random.randint(0,9)

num02 = random.randint(0,9)
while num02 == num32 or num02 == num22 or num02 == num12 or num02 == num42 or num02 == num52 or num02 == num62 or num02 == num72 or num02 == num82 or num02 == num92:
    num02 = random.randint(0,9)

#creacion de numeros completos que se repiten 1d - 10d
















numc91 = str(num11) + str(num21) + str(num31) + str(num41) + str(num51) + str(num61) + str(num71) + str(num81) + str(num91)

numc01 = str(num11) + str(num21) + str(num31) + str(num41) + str(num51) + str(num61) + str(num71) + str(num81) + str(num91) + str(num01)

#creacion de numeros completos que no se repiten

numc12 = str(num12)

numc22 = str(num12) + str(num22)

numc32 = str(num12) + str(num22) + str(num32)

numc42 = str(num12) + str(num22) + str(num32) + str(num42)

numc52 = str(num12) + str(num22) + str(num32) + str(num42) + str(num52)

numc62 = str(num12) + str(num22) + str(num32) + str(num42) + str(num52) + str(num62)

numc72 = str(num12) + str(num22) + str(num32) + str(num42) + str(num52) + str(num62) + str(num72)

numc82 = str(num12) + str(num22) + str(num32) + str(num42) + str(num52) + str(num62) + str(num72) + str(num82)

numc92 = str(num12) + str(num22) + str(num32) + str(num42) + str(num52) + str(num62) + str(num72) + str(num82) + str(num92)

numc02 = str(num12) + str(num22) + str(num32) + str(num42) + str(num52) + str(num62) + str(num72) + str(num82) + str(num92) + str(num02)
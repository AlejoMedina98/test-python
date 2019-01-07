print("\t\tBienvenido al primer script de Python")
print("\n\n")

print("\tElige una de las siguiente opciones\n")

print("\t a) Sumar numeros")
print("\t b) Calcular edad")
print("\n")

respuesta = input("\tEscribe tu respuesta: ")

if respuesta == 'a' or respuesta == 'A':
	print("\n")
	num1 = float(input("\tIngresa el primer numero: "))
	num2 = float(input("\tIngresa el segundo numero: "))
	suma = num1 + num2
	print("\n\tLa suma de los dos valores es de ", suma)
	input()

elif respuesta == 'b' or respuesta == 'B':
	print("\n")
	actual = 2017
	nac = int(input("\tIngresa tu año de nacimiento: "))
	edad = actual - nac
	print("\n\tTu edad a este año es de ", edad)
	input()
else: 
	print("\n\tEscoge una opción correcta la próxima...")
	input()

print("\n\tEL PROGRAMA HA FINALIZADO CON ÉXITO")
input()

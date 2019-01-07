while True:
	print("""Bienvenido al menu iterativo
	Elige una opcion: 
	1) Saludo
	2) Sumar dos numeros
	3) Iterar
	4) Salir""")
	r = input()

	if r == '1':
		print("Hola, saludos desde la terminal de Rodrigo")
	elif r == '2':
		n1 = float(input("Ingresa el primer numero: "))
		n2 = float(input("Ingresa el segundo numero: ")) 
		print("La suma de los dos nuemeros es de ", n1+n2)
	elif r == '3':
		n = int(input("Cuantas veces quieres iterar: "))
		m = 0
		while m <= n:
			
			print("Iteracion numero ", m)
			m += 1
		else:
			print("Iteracion completa")
	elif r == '4':
		print("Saliendo de la temrinal...")
		break
	else: 
		print("Opcion no valida")
else:
	print("El while ha terminado")
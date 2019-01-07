while True: 
	print("""	Consola de Python
				Selecciona una ooción.

				CALCULAR AREA DE: 
				1) Cuadrado
				2) Triangulo
				3) Circulo
				4) Salir
	""")

	r = input("Escribe tu respuesta: ")

	if r == '1':
		print("Calcular el área de un cuadrado.")
		l1 = float(input("Ingresa el valor del primer lado: "))
		l2 = float(input("Ingresa el valor del segundo lado: "))
		area = l1*l2

		print("El área de tu cuadrado es de ", area)

	elif r == '2':
		print("Calcular el area de un triangulo.")
		base = float(input("Ingresa la base de tu triangulo: "))
		altura = float(input("Ingresa la altura de tu triangulo: "))

		area = (base*altura)/2

		print("El area de tu triangulo es de ", area)

	elif r == '3':
		print("Calcular el área de un circulo.")
		pi = 3.1416

		radio = float(input("Ingresa el radio de el circulo: "))

		area = pi*(radio**2)

		print("El area del circulo es de ", area)

	elif r == '4':
		print("Saliendo de la consola...")
		break
	else: 
		print("No te pases...esa opción no es válida")

#EL programa funcionó correctamentedffg

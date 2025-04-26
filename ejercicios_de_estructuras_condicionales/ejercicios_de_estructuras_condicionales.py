# def primer_ejercicio():
#     primero= int(input("Indicar el primer numero: "))
#     segundo= int(input("Indicar el segundo numero: "))
#     if primero > segundo:
#         print(f"la suma de {primero} + {segundo} es igual a {primero+segundo} y su resta es igual {primero-segundo}")
#     elif primero < segundo:
#         print(f"la divicion de {primero} / {segundo} es igual a {primero/segundo}")
# primer_ejercicio()

# def segundo_ejercicio():
#     nota_uno= int(input("Indica la primera nota: "))
#     nota_dos= int(input("Indica la segunda nota: "))
#     nota_tres= int(input("Indica la tercera nota: "))
#     resultado_notas= (nota_tres + nota_dos + nota_uno)/ 3
#     if resultado_notas >= 7:
#         print("PROMOCIONADO")
#     else:
#         print("No ha sido promocionado")
# segundo_ejercicio()

# def tercer_ejercicio():
#     numero= int(input("Indicar un numero entre el 1 y el 99: "))
#     if numero <= 9:
#         print(f"{numero} tiene un solo digito")
#     else:
#         print(f"{numero} tiene dos digitos")
# tercer_ejercicio()

# def cuarto_ejercicio():
#     numero_uno= int(input("Indica el primer numero: "))
#     numero_dos= int(input("Indica el segundo numero: "))
#     numero_tres= int(input("Indica el tercer numero: "))
#     maximo= (max(numero_dos, numero_tres, numero_uno))
#     print(f"el numero mas grande de la lista es el {maximo}")
# cuarto_ejercicio()

# def quinto_ejercicio():
#     numero_nulo= int(input("Indica un numero: "))
#     if numero_nulo < 0:
#       print(f"{numero_nulo} es un numero negativo")
#     elif numero_nulo == 0:
#          print(f"{numero_nulo} es nulo")
#     else:
#          print(f"{numero_nulo} es un numero positivo")

# quinto_ejercicio()


# def sexto_ejercicio():
#     numero_tres_cifras= int(input("Indica un numero entre 0 y 999: "))
#     if numero_tres_cifras in range(1,10):
#         print("tu numero tiene 1 sifra" )
#     elif numero_tres_cifras in range(10,100):
#         print("tu numero tiene 2 sifras" )
#     elif numero_tres_cifras in range(100,1000):
#         print("tu numero tiene 3 sifras" )
#     else:
#         print("error")
# sexto_ejercicio()

# def septimo_ejercicio():
#     preguntas_realizadas = int(input("Cuantas preguntas tenia el examen? "))
#     preguntas_correctas = int(input("Cuantas preguntas tuvo correctas? "))
#     resultado_de_la_prueba= preguntas_correctas / preguntas_realizadas *100
#     if resultado_de_la_prueba >= 90:
#         print(f"Obtuvo el nivel maximo")
#     elif resultado_de_la_prueba in range(75,90):
#         print(f"Obtuvo el nivel medio")
#     elif resultado_de_la_prueba in range(50,75):
#         print(f"Obtuvo el nivel regular")
#     elif resultado_de_la_prueba <50:
#         print(f"fuera de nivel")
# septimo_ejercicio()
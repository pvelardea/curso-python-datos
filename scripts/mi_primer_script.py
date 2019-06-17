import math
     
print("¡Hola Bienvenidos al curso de Python para el análisis de datos!")
print("¿Cuántos somos hoy en el curso?")

number = input()
number = int(number)
root = math.sqrt(number)

print("Oh!, espero que aprendan mucho")
print("Por cierto, la raiz de %i es %f" %(number, root))

# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y
# el número de céntimos del precio introducido.

precio = input("Introduzca el precio con dos decimales: ")
entero = precio[:precio.find(".")]
centimos = precio[precio.find(".") + 1:]

print("Numero de euros: " + entero)
print ("Numero de centimos: " + centimos)



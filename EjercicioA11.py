# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido
# de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
unidades = int(input("Numero de unidades: "))

print('{producto}: {unidades:3d} unidades por {precio:9.2f} = {total:11.2f} euros'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))

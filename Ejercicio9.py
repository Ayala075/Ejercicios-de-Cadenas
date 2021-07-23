# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa ante
# rior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("Introduzca su fecha de nacimiento de la siguiente manera(dd/mm/aaaa): ")
dia = fecha[:fecha.find("/")]
mes_anio = fecha[fecha.find('/') + 1:]
mes = mes_anio[:mes_anio.find("/")]
anio = mes_anio[mes_anio.find('/') + 1:]

print("Dia: " + dia)
print("Mes: " + mes)
print("Anio: " + anio)



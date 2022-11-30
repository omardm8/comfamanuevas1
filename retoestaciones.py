# entradas del problema
mes = input (" en que mes estas")

if mes == "marzo" or mes == "abril" or mes == "mayo":
    print ("estas en primavera")
elif mes == "junio" or mes == "julio" or mes == "agosto":
    print ("estas en verano")
elif mes == "septiembre" or mes == "octubre" or mes == "noviembre":
    print ("estas en otoño")
elif mes == "diciembre" or mes == "enero" or mes == "febrero":
    print ("estas en invierno")
else:
    print("vuelva a introducir el mes")

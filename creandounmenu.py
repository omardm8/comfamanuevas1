opcion =100
print("Empanadas el Machetico")
print("*************************\n")

print("1. Registrar empanada")
print("2. Ver empanada")
print("0. SALIR")

empanadas=[ ]


while opcion != 0:
    opcion= int (input("Digita una opcion: "))
    if opcion==1:
        
       empanada=input("digite el nombre de la empanada a registrar: ")
       empanadas.append(empanada)

    elif opcion==2:
        for empanada in empanadas:
            print(f"la empanada seleccionada es:{empanada}")
    elif opcion==0:
        break
    else:
        print("Apreciado Usuario, debe seleccionar una opcion validad...")

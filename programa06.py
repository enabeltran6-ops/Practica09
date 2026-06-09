n1 = int(input("Ingresa el primer valor: "))
n2 = int(input("Ingresa el seguno valor: "))

print("1. suma\n2. Resta\n3. Multiplicacion\n4. Division\n5 Cociente\n6. Residuo")
op = input("Selecciona un aoperacion: ")
while True:
    if op == "1":
        print("{}+{} = {}".format(n1, n2, n1+n2))
    elif op =="2":
        print("{}-{} = {}".format(n1, n2, n1-n2))
    elif op =="3":
        print("{}*{} = {}".format(n1, n2, n1*n2))
    elif op =="4":
        print("{}/{} = {}".format(n1, n2, n1/n2))
    elif op =="5":
        print("{}/{} = {}".format(n1, n2, n1//n2))
    elif op =="6":
        print("{}mod{} = {}".format(n1, n2, n1%n2))
    elif op == "7":
      break 
    else:
        print("La opcion no es valida")
print("1. suma\n2. Resta\n3. Multiplicacion\n4. Division\n5 Cociente\n6. Residuo")
print("7. salir")
op = input("Selecciona un aoperacion: ")
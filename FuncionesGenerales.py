from FuncionesPDF import*
listaNombre = []
listaEdades = []
def menu():
    opcion =1
    while(opcion!=0):
        print("1.Pedir datos")
        print("2.Imprimir datos")
        print("3. Generar PDF")
        print("4. Generar QR")
        print("0. Salir")
        opcion = int(input("Elige una opcion "))
        if(opcion ==1):
            pedirdatos()
        elif(opcion==2):
            imprimirdatos()
        elif(opcion==3):
            generarPDF(listaNombre,listaEdades)

def pedirdatos():
    listaNombre.append(input("Ingresa tu nombre "))
    listaEdades.append(input("Ingresa una edad "))
    print("Guardado")

def imprimirdatos():
    for i in range(len(listaNombre)):
        print(f"Nombre:{listaNombre[i]} Edad: {listaEdades[i]}")        
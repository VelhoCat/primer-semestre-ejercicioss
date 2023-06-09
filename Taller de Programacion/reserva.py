""" Este programa utiliza diccionarios en vez de listas
ya que es más flexible utilizar claves personalizadas.
Podría por ejemplo utilizar strings para las llaves. """


from time import sleep
import os

asientos = {}
CANT_ASIENTOS = 10*10

def Limpiar_Pantalla():
    # limpiar pantalla en Windows
    if os.name == 'nt':
        os.system('cls')
    # limpiar pantalla en mac y Linux
    else:
        os.system('clear')

def Formato_Valido(rut_p):
    if "-" in rut_p:
       i = 0
       while rut_p[i] != "-":
           if not rut_p[i].isdigit():
               return(False)
           i = i + 1
       return(True)
    else:
        return(False) 

def Rut_Valido(rut_p):
    MULTIPLICA = "234567234567"
    VERIFIFCADOR = " 123456789K0"
    suma = 0
    for i in range (rut_p.find("-")):
        suma = suma + int(MULTIPLICA[i]) * int(rut_p[rut_p.find("-")-1-i])
    resto = suma%11
    indice = 11-resto
    if VERIFIFCADOR[indice] == rut_p[rut_p.find("-")+1].upper():
        return(True)
    else:
        return(False)

#def Valida_Rut(rut):
    #print("rut: " ,rut)

def Reserva_Asientos():
    Limpiar_Pantalla()
    asiento = {}
    EDAD_MIN = 4
    EDAD_MAX = 100
    GALERIA_NINO = 2000
    GALERIA_ADULTO = 3000
    GALERIA_ADULTO_MAYOR = 2500
    PALCO_NINO = 3000
    PALCO_ADULTO = 5000
    PALCO_ADULTO_MAYOR = 4000
    precio = 0

    print("Precios:")
    print("Galería Niños: " ,str(GALERIA_NINO))
    print("Palco Niños: " ,str(PALCO_NINO))
    print("Galería Adultos: " ,str(GALERIA_ADULTO))
    print("Palco Adultos: " ,str(PALCO_ADULTO))
    print("Galería Adulto Mayor: " ,str(GALERIA_ADULTO_MAYOR))
    print("Palco Adulto Mayor: " ,str(PALCO_ADULTO_MAYOR))
    print("Asientos del 1 al 20: Palco, asientos del 21 al 100: Galería")
    print("")
    num_asiento = int(input("Elija su número de asiento: "))
    while num_asiento in asientos:
        print("Este asiento ya está ocupado!!")
        num_asiento = int(input("Elija su número de asiento: "))
    rut = input("Ingrese su rut sin puntos, con guion y digito verificador (ej:xxxxxxxx-x): ")
    while not Formato_Valido(rut):
        print("!!ERROR FORMATO NO VALIDO!!")
        rut = input("Ingrese su rut sin puntos, con guion y digito verificador (ej:xxxxxxxx-x): ")
    if Rut_Valido(rut):
        print("Este rut es valido")
    while not Rut_Valido(rut):
        print("Este rut es invalido")
        rut = input("Ingrese su rut sin puntos, con guion y digito verificador (ej:xxxxxxxx-x): ")
    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))
    while edad < EDAD_MIN or edad > EDAD_MAX:
        edad = int(input("Error, la edad debe ser mayor a {0} y menor a {1}. Ingrese su edad: ".format(EDAD_MIN,EDAD_MAX)))
    if edad > EDAD_MIN and edad < 18 and num_asiento > 20:
        precio = GALERIA_NINO
    elif edad > EDAD_MIN and edad < 18 and num_asiento <= 20:
        precio = PALCO_NINO
    if edad >= 18 and edad <= 60 and num_asiento > 20:
        precio = GALERIA_ADULTO
    elif edad >= 18 and edad <= 60 and num_asiento <= 20:
        precio = PALCO_ADULTO
    if edad > 60 and edad <= EDAD_MAX and num_asiento > 20:
        precio = GALERIA_ADULTO_MAYOR
    elif edad > 60 and edad <= EDAD_MAX and num_asiento <= 20:
        precio = PALCO_ADULTO_MAYOR
    asiento["Rut"] = rut
    asiento["Nombre"] = nombre
    asiento["Edad"] = edad
    asiento["Precio"] = precio
    asientos[num_asiento] = asiento
    print("Asiento reservado")
    print("Los datos del asiento comprado son:")
    print("Número de asiento:", num_asiento)
    print("Rut:", asiento["Rut"])
    print("Nombre:", asiento["Nombre"])
    print("Edad:", asiento["Edad"])
    print("Monto a pagar:", asiento["Precio"])

def Asientos_Disponibles():
    Limpiar_Pantalla()
    for i in range(CANT_ASIENTOS):        
        if i in asientos:
            print("X",end=' ')
        else:
            print(i+1,end=' ')

        if (i+1) % 10 == 0:
            print()
    sleep(2)
    
def Asientos_Ocupados():
    Limpiar_Pantalla()
    print("Asientos ocupados:")
    for i in asientos.keys():
        print(i)
    sleep(2)

def Total_Recaudado():
    Limpiar_Pantalla()
    sumatoria = sum(asiento["Precio"] for asiento in asientos.values())
    print("El total recaudado es: " ,sumatoria)
    sleep(2)

def Reembolsar_Asiento():
    Limpiar_Pantalla()
    rut_reembolso = input("Ingrese el rut de la persona cuyo asiento desea reembolsar: ")
    asiento_reembolso = None
    for num_asiento, asiento in asientos.items():
        if asiento["Rut"] == rut_reembolso:
            asiento_reembolso = asiento
            break
    if asiento_reembolso:
        print("Datos de la persona:")
        print("Rut:", asiento_reembolso["Rut"])
        print("Nombre:", asiento_reembolso["Nombre"])
        print("Edad:", asiento_reembolso["Edad"])
        print("Número de asiento comprado:", num_asiento)
        print("Monto a devolver:", asiento_reembolso["Precio"])
        del asientos[num_asiento]
        print("Asiento reembolsado con éxito.")
    else:
        print("No se encontró ningún asiento asociado al rut ingresado.")
    sleep(2)

def Menu():
    Limpiar_Pantalla()
    print("Bienvenido, para comprar un asiento, seleccione una de las siguientes opciones")
    print("1: Comprar asiento")
    print("2: Reembolsar asiento")
    print("3: Asientos Disponibles")
    print("4: Asientos Ocupados")
    print("5: Total Recaudado")
    print("S: Salir")

def Opciones(opcion):
    FINALIZAR = "s"
    FINAL = FINALIZAR.upper()
    OP = opcion.upper()
    if OP == FINAL:
        print("Programa finalizado con éxito.")
        exit()
        
    while opcion != FINALIZAR:
        if opcion == "1":
            Reserva_Asientos()
        elif opcion == "2":
            Reembolsar_Asiento()
        elif opcion == "3":
            Asientos_Disponibles()
        elif opcion == "4":
            Asientos_Ocupados()
        elif opcion == "5":
            Total_Recaudado()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        Menu()
        opcion = str(input("Opción a elegir: "))
        Opciones(opcion)

Menu()
opcion = str(input("Opción a elegir: "))
Opciones(opcion)

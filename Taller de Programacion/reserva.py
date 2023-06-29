""" Este programa utiliza diccionarios en vez de listas
ya que es más flexible utilizar claves personalizadas.
Podría por ejemplo utilizar strings para las llaves. """


asientos = {}

def Datos_Asientos():
    asiento = {}
    EDAD_MIN = 4
    EDAD_MAX = 100
    contador = 0
    ASIENTO_NIÑO = 2000
    ASIENTO_ADULTO = 3000
    ASIENTO_ADULTO_MAYOR = 2500
    datos = []
    num_asiento = int(input("Elija su número de asiento: "))
    while num_asiento in asientos:
        print("Este asiento ya está ocupado!!")
        num_asiento = int(input("Elija su número de asiento: "))
    rut = str(input("Ingrese su rut: "))
    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))
    while edad < EDAD_MIN or edad > EDAD_MAX:
        edad = int(input("Error, la edad debe ser mayor a {0} y menor a {1}. Ingrese su edad: ".format(EDAD_MIN,EDAD_MAX)))
    if edad > EDAD_MIN and edad <= 18:
        datos.append(ASIENTO_NIÑO)
    if edad > 18 and edad <= 60:
        datos.append(ASIENTO_ADULTO)
    if edad > 60 and edad <= EDAD_MAX:
        datos.append(ASIENTO_ADULTO_MAYOR)
    asiento["Rut"] = rut
    asiento["Nombre"] = nombre
    asiento["Edad"] = edad
    asiento["Precio"] = datos[contador]
    asientos[num_asiento] = asiento
    print("Asiento reservado")
    print("Los datos del asiento comprado son:")
    print("Número de asiento:", num_asiento)
    print("Rut:", asiento["Rut"])
    print("Nombre:", asiento["Nombre"])
    print("Edad:", asiento["Edad"])
    print("Monto a pagar:", asiento["Precio"])
    contador += 1

def Menu():
    print("Bienvenido, para comprar un asiento, seleccione una de las siguientes opciones")
    print("1: Comprar asiento")
    print("2: Reembolsar asiento")
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
            Datos_Asientos()
        elif opcion == "2":
            Reembolsar_Asiento()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        Menu()
        opcion = str(input("Opción a elegir: "))
        Opciones(opcion)

def Sumar_Precios():
    sumatoria = sum(asiento["Precio"] for asiento in asientos.values())
    return sumatoria

def Reembolsar_Asiento():
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

Menu()
opcion = str(input("Opción a elegir: "))
Opciones(opcion)
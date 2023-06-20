asientos = {}
asientos[1] = {'RUT' : '13878116-K', 'EDAD' : 43, 'PRECIO_ASIENTO' : 5000}
asientos[3] = {'RUT' : '21686094-2', 'EDAD' : 18, 'PRECIO_ASIENTO' : 6000}
asientos[5] = {'RUT' : '23511446-1', 'EDAD' : 12, 'PRECIO_ASIENTO' : 2000}

def asientos_ocupados():
    for clave, valor in asientos.items():
        print(clave)

def lista_valores():
    for clave, valor in asientos.items():
        print(valor)

def lista_edades():
    for clave, valor in asientos.items():
        print(valor['EDAD'])

# lista_llaves()
# lista_valores()
# lista_edades()


def suma_precios():
    total_precios = 0
    for clave, valor in asientos.items():
        total_precios += valor['PRECIO_ASIENTO']
    return total_precios

def reserva_asiento(asiento, rut, edad, precio):
    if asiento in asientos:
        print("Asiento %s ocupado" %asiento)
    else:
        asientos[asiento] = {'RUT' : rut, 'EDAD' : edad, 'PRECIO_ASIENTO' : precio}
        print("El asiento %s ha sido reservado" %asiento)

#print(suma_precios())

reserva_asiento(10,'247951873',28,5000)
reserva_asiento(5,'247951873',28,5000)
print(asientos)
asientos_ocupados()

#Crear una función que pregunte al usuario por los datos del asiento y que los reserve
#luego imprimir los asientos ocupados. Se debe salir con la opción (S)

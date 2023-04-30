#Constantes:
mensaje = '''Opciones de TV disponibles:
1.-> SAMSUNG 48 pulgadas $490.000
2.-> SAMSUNG 55 pulgadas $730.000
3.-> LG 49 pulgadas $500.000
4.-> LG 60 pulgadas $920.000
5.-> SONY 47 pulgadas $450.000'''

#Solicitamos modelo TV
print(mensaje)
MODELO = int(input("Ingrese el numero de modelo: "))
#Verificamos si el numero de modelo y cantidad son validos
if MODELO > 0 and MODELO < 6:
    CANTIDAD = int(input("Ingrese la cantidad de TVs a comprar: "))
    if CANTIDAD > 0 and CANTIDAD < 11:
        print("Cantidad de TV seleccionada: " + str(CANTIDAD))
        #Asignamos precio al TV seleccionado
        PRECIO = 0
        if MODELO == 1:
            PRECIO = 490000
        elif MODELO == 2:
            PRECIO = 730000
        elif MODELO == 3:
            PRECIO = 500000
        elif MODELO == 4:
            PRECIO = 920000
        elif MODELO == 5:
            PRECIO = 450000

        #Calculamos total sin descuento

        TOTAL = CANTIDAD * PRECIO

        #Calculamos descuento

        if TOTAL < 1500000:
            print("Su compra no tiene descuento")
        elif TOTAL >= 1500000 and TOTAL < 2500000:
            TOTAL = TOTAL * 0.95
            DESCUENTO = TOTAL * 0.05
            print("Su compra tiene un 5% de descuento equivalente a: $" + str(DESCUENTO))
        elif TOTAL >= 2500000 and TOTAL < 5000000:
            TOTAL = TOTAL * 0.85
            DESCUENTO = TOTAL * 0.15
            print("Su compra tiene un 15% de descuento equivalente a: $" + str(DESCUENTO))
        elif TOTAL >= 5000000:
            TOTAL = TOTAL * 0.75
            DESCUENTO = TOTAL * 0.25
            print("Su compra tiene un 25% de descuento equivalente a: $" + str(DESCUENTO))
        print("El total de su compra es: " + str(TOTAL))
    else:
        print("Cantidad no valida")
else:
    print("Modelo ingresado no valido")

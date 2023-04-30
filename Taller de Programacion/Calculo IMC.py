PESO_PERSONA = float(input("Ingrese el peso en kilos: "))
ESTATURA = float(input("Ingrese su estatura en metros: "))
IMC = PESO_PERSONA / ESTATURA**2
print("Su IMC es de: " + str(IMC))

if IMC < 18.5:
    print("Bajo peso")
elif IMC >= 18.5 and IMC < 24.9:
    print("Peso normal")
elif IMC >= 25 and IMC < 29.9:
    print("waton")
elif IMC >= 30 and IMC < 34.9:
    print("waton nivel 1")
elif IMC >= 35 and IMC < 39.9:
    print("waton nivel 2")
elif IMC >= 40:
    print("waton supersaiyajin")
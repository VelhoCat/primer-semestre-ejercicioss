def saluda(nombre, edad):
    mensaje = "hola {0}, ¿como estas?. Tu edad es {1} anios".format(nombre, edad) 
    return mensaje

input_usuario = str(input("ingrese un nombre: "))

print(saluda(input_usuario,15))
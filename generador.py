import random
import string
def generar_contrasena():
    longitud=int(input("Ingresa la longitud deseada: \n"))
    caracteres=string.ascii_letters+string.digits+string.punctuation
    contraseña=''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

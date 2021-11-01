import random
from werkzeug.security import generate_password_hash
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@[](){}%/\!¡#$&=¿?.,;:_*+-="
base = minus + mayus + numeros + simbolos
longitud = 32


for i in range(10):
    muestra = random.sample(base,longitud)
    password = "".join(muestra)
    passwordEncritado = generate_password_hash(password)
    print("Password aleatorio: ",password)
    print("password encritado: ",passwordEncritado)
    print("-----------------------------------------------------------")

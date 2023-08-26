import hashlib

def EncriptarPassword(data):
    #Esto es algo adicional, que se le combina con la contraseñá del usuario
    token_sha256 = "stellarhostingzone"
    #Aqui unimos la contraseñá y el token unico (El token debe ser unico por lo tanto no debe ser mostrado a nadie)
    encriptacion_reforzada = data + token_sha256
    #Comienza la encriptacion de la contraseñá
    sha256_hash = hashlib.sha256()
    
    #Ya encriptada, pone todo en mayusculas
    sha256_hash.update(encriptacion_reforzada.encode('utf-8'))
    return sha256_hash.hexdigest().upper()

# Solicitar dato al usuario
data = input("Ingrese un dato: ")

# Crea la encriptacion de la contraseñá
clave = EncriptarPassword(data)

# Mostrar el resultado en mayúsculas
print("Contraseña encriptada:", clave)

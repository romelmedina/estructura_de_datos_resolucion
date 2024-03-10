#ejercicio 9 sem_05

def palabras_con_longitud (conjunto, longitud):
    return  {palabra for palabra in conjunto if len (palabra) == longitud}

conjunto_palabras = {"casa", "perro" ,"gato", "sol", "luna", "oso"}

longitud_deseada = 4

resultado = palabras_con_longitud(conjunto_palabras, longitud_deseada)

print(resultado)
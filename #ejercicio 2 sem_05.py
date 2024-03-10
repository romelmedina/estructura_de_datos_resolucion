#ejercicio 2 sem_05

def palabras_con_letra_inicial (conjunto , letra) :
    palabras = set()
    for palabra in conjunto :
        if palabra.startswith(letra):
            palabra.add(palabra)
    return palabras

conjunto = {"manzana" , "banana" , "piña" , "melon"}
letra = "I"

resultado = palabras_con_letra_inicial(conjunto, letra)
print(resultado)
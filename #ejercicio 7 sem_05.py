#ejercicio 7 sem_05

def son_anagramas (palabra1 , palabra2) :
    return sorted(palabra1) == sorted(palabra2)

def anagramas_en_conjunto (conjunto):
    anagramas = set ()
    palabras = list(conjunto)
    for i in range(len (palabras)):
        for j in range (i + 1,  len(palabras)):
            if son_anagramas(palabras[i], palabras[j]):
                anagramas.add(palabras[i])
                anagramas.add(palabras[j])
    return anagramas

conjunto_palabras ={"roma" ,"amor", "perro", "rorpe", "casa", "saca"}

resultado = anagramas_en_conjunto(conjunto_palabras)

print(resultado)
"""Modifique el programa anterior con las siguientes funcionalidades:
- El juego tiene un bug. Si el usuario ingresa más de una letra, un número o
cualquier otro carácter inválido, el programa se comporta de manera inesperada. 
Modificalo para que en ese caso muestre el mensaje "Entrada no válida" y 
continúe el juego en la siguiente iteración.
- Modificá el juego para que al final de la partida se muestre el puntaje
del jugador. El puntaje se calcula de la siguiente forma: cada letra
incorrecta resta 1 punto, adivinar la palabra completa suma 6 puntos, y perder deja el puntaje en 0.
- Modificá el juego para que las palabras estén agrupadas por categoría.
Al inicio de cada partida, mostrar las categorías disponibles y permitir
que el usuario elija una. Ayuda: utilizá un diccionario donde las claves
sean los nombres de las categorías y los valores sean listas de palabras.
- Modificá el juego para que, al jugar varias rondas seguidas, no se
repita la misma palabra. Investigá la función random.sample() .
Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique
el cambio."""


import random
words = {
    "estructuras": ["cadena", "entero", "lista"],
    "partes": ["funcion", "bucle", "variable"],
    "global": ["python", "programa", "github"]  # Agregué "github" como mencionaste
}
print("Categorías disponibles:", list(words.keys()))
categoria = input("Elige una categoría: ")
while categoria not in words:
    print("Categoría inválida. Elige de:", list(words.keys()))
    categoria = input("Elige una categoría: ")
word = random.choice(words[categoria])
guessed = []
attempts = 6
puntaje = 0
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
        print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntaje += 6
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if len(letter) != 1 or not letter.isalpha():    #Verifica que ese carácter sea una letra 
        print("Entrada no válida")
        continue
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -=1
        print("Esa letra no está en la palabra.")
    print()
else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word}")
print(f"Puntaje final: {puntaje}")
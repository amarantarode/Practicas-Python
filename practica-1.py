"""1. Escribe un programa que solicite al usuario su año de nacimiento y muestre en qué
año cumplirá 18, 21 y 100 años.
2. Escribe un programa que solicite al usuario una cantidad de segundos y muestre
cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
hora, 1 minuto y 1 segundo.
3. Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar
del 1 al 10 utilizando un bucle for.
4. Crea un programa que dado un número N ingresado por el usuario, imprima los
números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue
donde haga falta.
5. Escribe un programa que simule una caja registradora: el usuario ingresa precios de
productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
acumulado. Nota: utilizá la sentencia break cuando haga falta.
6. Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
finalizar.
7. Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
espacios. Las palabras cortas deben ser excluidas del resultado final."""

# 1
"""
f_nac = int(input("Ingrese su año de nacimiento: "))
año_actual = 2026
año_18 = f_nac + 18
año_21 = f_nac + 21
año_100 = f_nac + 100
if año_18 < año_actual:
    print(f"Cumplió 18 años en el año {año_18}")    
else:
    print(f"Cumplirá 18 años en el año {año_18}")
if año_21 < año_actual:
    print(f"Cumplió 21 años en el año {año_21}")    
else:
    print(f"Cumplirá 21 años en el año {año_21}")
if año_100 < año_actual:
    print(f"Cumplió 100 años en el año {año_100}")    
else:
    print(f"Cumplirá 100 años en el año {año_100}")

# 2
seg = int(input("Ingrese una cantidad de segundos: "))
horas = seg // 3600
minutos = (seg % 3600) // 60
segundos = seg % 60
print(f"Los segundos introducidos equivalen a {horas} horas, {minutos} minutos, {segundos} segundos.")

# 3
entero = int(input("Ingrese un número entero: "))
for i in range(1,11):
    print(f"|{entero:>2} x {i:>2} | {entero * i:>3} |")
    
# 4
num = int(input("Ingrese un número: "))
for n in range (1, num+1):
    if n%5 == 0:
        continue        #continue permite saltarse la linea print y continuear el loop
    print(n)
    
#5
total = 0
while True:
    precio = float(input("Ingrese el precio del producto (0 para finalizar): "))
    if precio == 0:
        break           #break permite salir del loop cuando se ingresa 0
    total += precio
print(f"El total acumulado es: {total}")

#6
num = int(input("Ingrese un número: "))
multiplos_5 = []
no_multiplos_5 = []
for n in range(1, num+1):
    if n % 5 == 0:
        multiplos_5.append(n)
    else:
        no_multiplos_5.append(n)
print(f"Múltiplos de 5: {multiplos_5}")
print(f"Resto de los números: {no_multiplos_5}")"""

#7
palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()  #split hace que palabras sea una lista
nueva_oracion=''
for i in range (len(palabras)):     #len devuelve la cantidad de elementos en la lista
    if len(palabras[i]) >= 3:       #len devuelve la cantidad de caracteres en la palabra
        nueva_oracion = nueva_oracion + palabras[i] + ' '     
print(nueva_oracion)         

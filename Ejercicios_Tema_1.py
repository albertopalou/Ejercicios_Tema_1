#'''Ejercicios del tema 1. Curso 22/23'''

#1.1 Escribe una función cuya firma sea multiple(n, m), y que tome dos enteros y devuelva True is n es un múltiplo de m,
# es decir n = m*i, paa una algún entero i, o False en cualquier otro caso.
n=int(input("Numero entero: "))
m=int(input("Numero entero: "))
def multiplos(n,m):
    multiplos=n % m
    if multiplos==0:
        print(True)
    else:
        print(False)
    return multiplos

#1.2  Escribe una función cuya firma sea even(k), y que tome un valor entero y devuelva True is k es par o False en otro caso.
def even(k):
    k=int(input("escribe un numero entero: "))
    if k % 2==0:
        print(True)
    else:
        print(False)
    return even

#1.3 Escribe una función cuya firma sea minmax(data), y que tome una secuencia de uno o mas números, y que devuelva el máximo y mínimo de la secuencia
# No se puede usar las funciones min o max para implementar la solución.
lista = list(2,5,7,1,0,4,3)
lista.sort(reverse=True)
print(lista[0])
print(lista[6])

#1.4 Escribe una función  que come una numero entero positivo n y devuelva la suma de los cuadrados  de los cuadrados de todos los enteros positivos 
# menores a n. 
# Ejemplo: n = 5, solución 4**2 + 3**2 + 2**2 + 1**1
n = int(input("escribe un numero: "))
for i in range (n):
    suma =sum(i**2)
    print(suma)

#1.5 Escribe una función que tome un entero positivo y devuelva la suma de los cuadrados de los cuadrados de todos los números impares menores
# a n.
# Ejemplo: n = 7, solución 5**2 + 3**2 + 1**1
n = int(input("escribe un numero: "))
for i in range (n):
    if i//2!=0:
        sum(i)
    print

#1.6 Python permite utilizar números negativos como indices en un secuencia, tal como un string. Si el string tiene una longitud n, y la expresión
#  s[k] se usa para los indices −n ≤ k < 0, cual es el el indice equivalente  j ≥ 0 tal que s[j] have referencia a los mismos elementos?


#1.7 Cuales son los parámetros que se deben usar en el constructor de la función range para producir los valores, s 50, 60, 70, 80?


#1.8 Cuales son los parámetros que se deben usar en el constructor de la función range para producir los valores, 8, 6, 4, 2, 0, −2, −4, −6, −8?
for i in range(6,-5,2):
    print("s"+ str(i))

#1.9 Escribe una funcion que tome una secuencia de números y determine si todos los números en la secuencia son diferentes.
def num_dif(numeros):
    for numero in numeros:
        for i in numeros:
            if numero == i:
                print("hay dos numeros iguales")
            else:
                print("todos los numeros son diferentes")
numeros = [1,2,3,4]
num_dif(numeros)

#1.10 Escribe una función que tome dos listas a y b de longitud n de números enteros, y devuelva el producto escalar de a y b.
# Es decir, devuelva una vector c de longitud n tal que  c[i] = a[i] · b[i], para i = 0,...,n− 1.
def producto_escalar (lista1, lista2):
    result = []
    for i in range(len(lista1)):
        result.append[i] = lista1[i]*lista2[i]
    return result
lista1 = [1,2,3,4]
lista2 = [1,2,3,6]

producto_escalar = [x*y for x,y in zip(lista1, lista2)]
print(producto_escalar)

# 1.11 Escribe una función que cuente el numero de vocales en una un cadena de caracteres dada.
cadena="Que buen dia hace hoy"
contador_vocales=0
for i in cadena:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        contador_vocales+=1
        print(contador_vocales)

# 1.12 Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:
"Hola Mundo"      #string
[1, 10, 100]      #list
-25               #int
1.167             #float
["Hola", "Mundo"] #list

# 1.13 Realiza un programa que siga las siguientes instrucciones:
#    • Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
#    • Crea un conjunto llamado administradores con los administradores Juan y Marta.
#    • Borra al administrador Juan del conjunto de administradores.
#    • Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
#    • Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
usuarios = ["Marta","David","Elvira","Juan","Marcos"]
administradores = ["Marta","Juan"]
nuevos_administradores=[administradores.append("Marta")]
nuevos_administradores.append("Marcos")
for i in usuarios:
    print(f"{i} es un usuario")
    for j in nuevos_administradores:
        print(f"{j} es un adminitrador")

 
# 1.14 Crea un script llamado tabla.py que realice las siguientes tareas:
#    • Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
#    • El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
#    • En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
#    • El script contendrá un bucle for que itere el número de veces del primer argumento.
#    • Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
#    • Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.
#    • Ejecuta el código y observa el resultado.
#    • Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.
filas = input("Introduce el numero de filas: ")
columnas = input("Introduce el numero de columnas: ")
def tabla(filas, columnas):
    for i in filas:
        print(" * ")
        for j in columnas:
            print(" * ", end="")
tabla(filas, columnas)

# 1.15 Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
#resultado = 10/0
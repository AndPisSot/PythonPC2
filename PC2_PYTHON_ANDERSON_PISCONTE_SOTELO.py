# Estructuras Iterativas:

# Problema 1:
# Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
# en el rango de 1500 y 2700 (ambos incluidos)

# Definimos el inicio,final
from string import digits


iniciar = 1500
terminar = 2700
# Creamos una variable lista para guardar los numeros pedidos
resultado = []

# Usamos buble : for
for num in range(iniciar, terminar + 1):
    # Verificamos si el número es divisible por 7 y múltiplo de 5
    if num % 7 == 0 and num % 5 == 0:
        resultado.append(num)
# Imprimimos 
print('Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:{}'.format(resultado))

# Problema 2:
# Escriba un programa en Python para construir el siguiente patrón.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# Número máximo de estrellas en la fila central
maximo_estrellas = 5

# Parte ascendente 
for i in range(1, maximo_estrellas + 1,1):
    print('* ' * i)

# Parte descendente 
for i in range(maximo_estrellas - 1, 0, -1):
    print('* ' * i)

# Problema 3:
# Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
# ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
# números.
# Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
# números pares e impares.

# Inicializamos los contadores de pares e impares
pares = 0
impares = 0
numeros = []
# Bucle while 
while True:
    # Solicitamos numeros al usuario
    numero = input("Ingrese un número (o 'salir' para terminar): ")

    # Verificamos si el usuario desea salir
    if numero.lower() == 'salir':
        break

    try:
        # Convertimos el input 
        numero = int(numero)

       # Agregamos a la lista
        numeros.append(numero)


        # Evaluamos si el número es par o impar
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        # En caso de que el input no sea un número válido, informamos al usuario
        print("Por favor, ingrese un número válido.")

# Imprimimos 
print('Números introducidos:{}'.format(numeros))
print('Cantidad de números pares:{}'.format(pares))
print('Cantidad de números impares:{}'.format(impares))

# Problema 4:
# Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
# pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
# materias.
# Puede usar el siguiente esquema a manera de ejemplo
# {
# Alumno: Juan,
# Notas: [10, 12, 15]
# }
# Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
# completo de los alumnos.
# Nota:
# El uso de listas con diccionarios le será de utilidad.

# Inicializamos una lista 
alumnos = []

# Bucle para el ingreso de datos de los alumnos
while True:
    # Solicitamos el nombre del alumno
    nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")

    # Verificamos si el usuario desea salir
    if nombre.lower() == 'salir':
        break

    # Solicitamos las calificaciones del alumno
    try:
        notas = []
        for i in range(1, 4):
            nota = float(input('Ingrese la calificación {} para {}:'.format(i,nombre)))
            notas.append(nota)
    except ValueError:
        print("Por favor, ingrese una calificación válida.")
        continue

    # Agregamos los datos del alumno a la lista
    alumno = {
        'Alumno': nombre,
        'Notas': notas
    }
    alumnos.append(alumno)

# Mostramos el listado completo
print("\nListado de alumnos y sus calificaciones:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# Funciones:
# Problema 5:
# Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
# Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
# Ejemplo:
# Número ingresado: 15789000 y Dígito: 0
# Cantidad de veces 0 en el número: 4
# Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
# count.

def contar_digito(numero, digito):
    # Convertimos el número y el dígito a cadenas de caracteres
    numero_str = str(numero)
    digito_str = str(digito)
    
    # Utilizamos el método count para contar las ocurrencias del dígito en el número
    cantidad = numero_str.count(digito_str)
    
    return cantidad

# Función principal para interactuar con el usuario
def main():
    try:
        # Solicitar el ingreso del número y del dígito al usuario
        numero = int(input("Ingrese un número entero: "))
        digito = input("Ingrese un dígito: ")

        # Verificamos que el dígito ingresado sea un único carácter y un dígito válido
        if len(digito) == 1 and digito.isdigit():
            digito = int(digito)
            resultado = contar_digito(numero, digito)
            print('Cantidad de veces {} en el número {}: {}'.format(digito,numero,resultado))
        else:
            print("Por favor, ingrese un único dígito válido.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Llamada a la función principal
main()

# Problema 6:
# Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
# Nota: La secuencia de Fibonacci es la serie de números:
# 0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
# Cada número siguiente se obtiene sumando los dos números anteriores

def fibonacci_series(limit):
    # Inicializamos la serie de Fibonacci con los primeros dos números
    a, b = 0, 1
    series = [a]

    # Generamos la serie de Fibonacci hasta el límite dado
    while b <= limit:
        series.append(b)
        a, b = b, a + b

    return series

# Establecemos el límite de la serie de Fibonacci
limite = 50

# Obtenemos la serie de Fibonacci
serie_fibonacci = fibonacci_series(limite)

# Imprimimos la serie de Fibonacci
print('Serie de Fibonacci entre 0 y {}:'.format(limite))
print(serie_fibonacci)

# Problema 7:
# Escriba una función de Python que tome un número como parámetro y verifique que el número sea
# primo o no.

def es_primo(numero):
    # Un número menor o igual a 1 no es primo
    if numero <= 1:
        return False
    
    # Verificar divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

# uso
numero = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(numero):
    print('El número {} es primo.'.format(numero))
else:
    print('El número {} no es primo.'.format(numero))

# Problema 8:
# Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
# función acepta el número como argumento   

def factorial(numero):
    # El factorial de 0 es 1
    if numero == 0:
        return 1
    
    # Inicializamos el resultado como 1
    resultado = 1
    
    # Calculamos el factorial multiplicando cada número desde 1 hasta el número dado
    for i in range(1, numero + 1):
        resultado *= i
    
    return resultado

# Ejemplo de uso
numero = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
if numero >= 0:
    resultado = factorial(numero)
    print('El factorial de {} es: {}'.format(numero,resultado))
else:
    print("Por favor, ingrese un número entero no negativo.")

# Métodos de Cadenas:
# Problema 9:
# Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
# por ejemplo, omitiendo las vocales.
# Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
# texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
# minúsculas.   

def omitir_vocales(cadena):
    # Definimos una lista con las vocales en mayúsculas y minúsculas
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    # Creamos una nueva cadena con las vocales omitidas
    nueva_cadena = ''.join(caracter for caracter in cadena if caracter not in vocales)
    
    return nueva_cadena

# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingrese una cadena de texto: ")

# Aplicar la función para omitir las vocales
texto_sin_vocales = omitir_vocales(texto)

# Imprimir el resultado
print("Texto con las vocales omitidas:")
print(texto_sin_vocales)

# Problema 10:
# En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
# fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
# lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
# en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
# ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
# 1636!
# Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
# 8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
# la lista abajo:
# [
# "Enero",
# "Febrero",
# "Marzo",
# "Abril",
# "Mayo",
# "Junio",
# "Julio",
# "Agosto",
# "Septiembre",
# "Octubre",
# "Noviembre",
# "Diciembre"
# ]
# Luego, genere esa misma fecha en formato AAAA-MM-DD.
# Ejemplos:
# - Input: 9/8/1636 | Output: 1636-09-08
# - Input: Septiembre 8, 1636 | Output: 1636-09-08
# - Input: 1/1/1970 | Output: 1970-01-01
# Nota:
# - Los métodos de listas y string le resultarán de gran utilidad.
# - Nota que si empleamos print(f"{n:02}") , esta completará con 0 valos a la izquierda de un
# número

def obtener_formato_fecha(fecha):
    if '/' in fecha:
        partes = fecha.split('/')
        dia = partes[1]
        if len(dia) == 1:
            dia = '0' + dia
        mes = partes[0]
        if len(mes) == 1:
            mes = '0' + mes
        año = partes[2]
    else:
        meses = {
            "Enero": "01",
            "Febrero": "02",
            "Marzo": "03",
            "Abril": "04",
            "Mayo": "05",
            "Junio": "06",
            "Julio": "07",
            "Agosto": "08",
            "Septiembre": "09",
            "Octubre": "10",
            "Noviembre": "11",
            "Diciembre": "12"
        }
        partes = fecha.split()
        dia = partes[1][:-1]
        if len(dia) == 1:
            dia = '0' + dia
        mes = meses[partes[0]]
        año = partes[2]

    return [año, mes, dia]

def formatear_fecha(fecha):
    partes = obtener_formato_fecha(fecha)
    return f"{partes[0]}-{partes[1]}-{partes[2]}"

# Solicitar al usuario que ingrese una fecha
fecha_usuario = input("Ingrese una fecha en formato mes-día-año (MM/DD/AAAA) o (mes día, año): ")

# Formatear la fecha
fecha_formateada = formatear_fecha(fecha_usuario)

# Imprimir la fecha en el nuevo formato
print("Fecha formateada AAAA-MM-DD :{}".format(fecha_formateada))
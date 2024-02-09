
def explicación():
    tupla=(2,4,6)
    fecha=(9,"febrero",2024)

    print(tupla)
    print(fecha)

    palabras = int(input("cuantas palabras desea agregar "))
    if palabras < 1:
        print("Invalid")
    else:
        lista = []
        for i in range (palabras):
            palabras = input(f" Ingrese la palabra{i+1} ") #f es para concatenar jnto a el valor inicial
            lista +=[palabras]
        print(f"la lista final es: {lista} ")


def ingresar():
    enteros=[]
    
    for x in range(5):
        num = int(input("Ingresar el número "))
        enteros.append(num)
    impresora(enteros)
    sumar(enteros)
def impresora(enteros):
    print("Los datos de la lista son")
    for x in enteros:
        print(x)
def sumar(enteros):
    acum=0
    for x in enteros:
        acum +=x
    print("La sumatoria es: ",acum)

ingresar()

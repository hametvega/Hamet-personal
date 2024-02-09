texto= "Buenos días definiendo un parametro en una función"
#función sin parametros
def Mensaje ():
    n1= int(input("Ingrese el primer numero "))
    n2= int(input("Ingrese el segundo numero "))
    Calculo(n1,n2)
    positivo(n1,n2)
#con parametros
def Calculo(num1,num2):
    if num1 > num2:
        print("El primer número es el mayor")
    elif num1 == num2:
        print("ambos son número iguales")
    else:
        print("el segundo numero es el mayor")



def positivo(p1,p2):
    if p1>0 and p2>0:
        print("El número es positivo ")
    if p1<0 and p2>0:
        print("El primero numero es negativo ")
    if p1>0 and p2<0:
        print("El segundo numero es negativo ")
    else:
        print("Ambos números son negativos ")

Mensaje()
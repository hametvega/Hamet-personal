
#Función sin parametros y sin retorno
def inicio():
    print("Menu principal")
    print("Seleccione la opción correcta")
    print("1. Operar sumar")
    print("2. Operar resta")
    print("3. Operar Multiplitación")
    print("4. Operar división")
    print("5. Salir")
def main():
    while True:
        inicio()
        opcion = int(input("Seleccione la opción"))
        if opcion==1:
            print("Molidad de Suma Activada")
            num1= int(input("Ingrese el primer numero "))
            num2= int(input("Ingrese el segundo numero "))
            suma= num1+num2
            print("El resultado de la suma es_:")
        elif opcion==2:
            print("Modalidad Resta Activada")
            num1= int(input("Ingrese el primer numero "))
            num2= int(input("Ingrese el segundo numero "))
            suma= num1-num2
            print("El resultado de la resta es_:")
        elif opcion==3:
            print("Modalidad Multiplicación Activada")
            num1= int(input("Ingrese el primer numero "))
            num2= int(input("Ingrese el segundo numero "))
            suma= num1*num2
            print("El resultado de la Multiplicación es_:")
        elif opcion==4:
            print("Modalidad División Activada")
            num1= int(input("Ingrese el primer numero "))
            num2= int(input("Ingrese el segundo numero "))
            division= num1/num2
            print("El resultado de la división es_:")
        elif opcion==5:
            print("Saliste vivo de esta")
        else:
            print("Mala selección de numeros")
            break
    
inicio()
main()
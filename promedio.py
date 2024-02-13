promedio = 0
num = 0
acum=0
print ("escribe 10 numeros para promediar")
while acum < 10:
    
    num=int(input("Digita el numero"))
    promedio=promedio+num
    acum=acum+1

promedio=promedio/10
print("Su promedio es:",promedio)

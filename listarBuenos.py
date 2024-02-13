#definir listas
nombres=[] #los corchetes indican que es una lista
notas=[]
Excelente=0
Bueno=0
Deficiente=0
AlumnosE=[]
#Datos de la lista
for x in range(4):
    Nom=input("Porfavor ingrese el nombre del alumno ")
    nombres.append(Nom)
    No = int(input("Ingrese las notas del alumno "))
    notas.append(No) #el .append indica que guardaremos un dato en una lista
    
#función que hará la lista
for y in range(len(nombres)): #El "len" Es para mostrar la cantidad de datos en la lsita
    print(nombres[y])
    print(notas[y])
    if notas[y] >= 8:
        print("el estado de las notas del alumno es excelente ")
        print("----------------------------------------------")
        #mostrar alumnos Excelentes
        #AlumnosE.append(nombres[y]) 
        Excelente+=1
    elif notas[y] >=4:
        print("el estado de las notas del alumno es bueno ")
        print("----------------------------------------------")
        Bueno+=1
    else:
        print("el estado de las notas del alumno es Excelente ")
        print("----------------------------------------------")
        Deficiente +=1
print("listado de alumnos", nombres)
eliminar=[]

for z in (len(notas)):
    if notas[z]>=4 and notas[z]<=7:
        notas.pop(z) #.pop es para borrar datos de una lista
        nombres.pop(z)        
        eliminar.append(z)
        
        
for b in sorted(eliminar,reverse=True): #sorted es para ordenar una lista
        notas.pop(b)
        nombres.pop(b)
        
        

print("Los nombres de los mejores alumnos son: ", AlumnosE)
print("----------------------------------------------")
print("Nombres con notas entre 4 y 7", nombres(z))






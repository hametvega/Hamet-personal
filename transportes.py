"""
De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.

Para guardar esta informacion
Nombre: Lista para guardar los nombres de los conductores.
kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.

Al finalizar se muestra la lista con los nombres de conduct
"""
Conductores=[]
Kt=[]
todos_k= 0

No_conducotres=int(input("Cantidad de conductores "))
for Tc in range (No_conducotres):
    Nconductor=input("Escriba el nombre del conductor_:")
    Conductores.append(Nconductor)
    todos_k=0
    
    for y in range(2):    
        Kim=int(input("cuantos kilometros recorrio al día {y}"))
        todos_k = todos_k + Kim
        
    Kt.append(todos_k)


print("nombre de los conductores",Conductores)
print("Kilometros de cada conductor",Kt)





#llenar tablas




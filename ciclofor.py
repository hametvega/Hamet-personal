# # frase = input("ingresa una frase_:")
# # letra = input("ingresa la letra que vas a buscar_:")
# # Cletra = 0

# # for i in frase:
# #     if  i == letra:
# #         Cletra +=1
# # print ("La letra",letra, "aprace en la frase:",Cletra)

"""jr2"""
# for x in range (1,20,5):
#     print(x)
"""jr 3"""
# gastos=0
# más=0
# menos=0
# empleados=int(input("Ingrese el # de empleados"))

# for ini in range(empleados):
#     sueldo =float(input("Ingrese el valor del  empleados"))
#     gastos +=1
#     if sueldo >=13 and sueldo <=30:
#         más +=1
#     elif sueldo >30:
#         menos +=1
# print("empleados que ganan más_:",más)
# print("empleados que estan en el promedio_:",menos)
"""jr4"""
"""Se cuenta con la siguiente información:
Las edades de 6 estudiantes del turno mañana.
Las edades de 7 estudiantes del turno tarde.
Las edades de 12 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de 
los tres turnos tiene un promedio de edades mayor."""

# Mañana=6
# pm=0
# ptm=0
# promm=0
# Tarde=7
# pt=0
# ptt=0
# promt=0
# Noche=12
# ptn=0
# pa=0
# promn=0

# for Mañana in range (1,7):
#     pm=int(input("ingresa las edades de lo estudiantes de la mañana_:"))
#     ptm=ptm+pm
#     promm=ptm/6
# print("-----------------------------------------------------")
# for Tarde in range (1,8):
#     pt=int(input("ingresa las edades de lo estudiantesde la tarde_:"))
#     ptt=ptt+pt
#     promt=ptt/7
# print("-----------------------------------------------------")
# for Noche in range (1,13):
#     pn=int(input("ingresa las edades de lo estudiantes de la noche_:"))
#     ptn=ptn+pn
#     pormn=ptn/12

# if ptm > ptt:
#     print("El curso con el mayor promedio es el de la maña con",ptm)
#     print("-----------------------------------------------------")
# elif ptm<ptt:
#     print("el curso con mayor promedio es_:",ptn)
#     print("-----------------------------------------------------")
# else:
#     print("el curso con mayor promedio es_:",ptn)
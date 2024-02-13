Personas={
    "Nombre":"Hamet Manuel",
    "Apellido":"Vega Gómez",
    "Estatura": 1.65,
    "Edad":17,
    "Email":"hamet2303@gmail.com",
    "Ciudad_Nacimiento":"Bogotá",
    "Genero":["Femenino","Masculino","otro"]
}
print(Personas)
#para acceder a un dato en concreto
print("El nombre de la persona es:", {Personas["Nombre"]}) 
#agregar un elemento al diccionarío
Personas["telefono"]=3214325614
print (Personas)
#Modificar valor de los elementos
Personas["telefono"]=3223824956
print(Personas)
#modificar el nombre de os elementos
Personas["celular"]=Personas.pop("telefono")
print(Personas)
#eliminar elementos
del Personas["celular"]
print (Personas)
#iterar los items de las clves
for clave,valor in Personas.items():
    print(clave + ":" + valor)
print(Personas)


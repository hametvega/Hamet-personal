def registrar():
    #definimos el diccionario
    agenda={}
    respuesta = "s"
    
    while respuesta=="s":
        fecha =input("ingrese la feca con formato dd/mm/aa : ")
        lista=[]
        while respuesta =="s":
            hora = input("Ingrese la hora de la actividad: h/m")
            actividad = input("¿Que nombre le daras a tu actividad?")
            #el valor de .apend toma un solo dato y se agregan parentesis tantos datos se deseen agregar
            lista.append((hora,actividad))
            respuesta = input("¿deseas ingresar otra actividad en la misma fecha? S/N")
        #guardamos en la fecha de la agenda lo que esta en lista
        agenda[fecha]=lista
        respuesta = input("Desea ingresar otra fecha s/n :")
    #para dar como respuesta <el item>
    return agenda

def mostrar(agenda):
    print("listado de la agenda")
    #el for es para indicar por donde inicia 
    for fecha in agenda:
        for hora, actividad in agenda[fecha]:
            print(hora,actividad)
agenda=registrar()
mostrar(agenda)

        
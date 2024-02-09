ancho = int(input("Ingresa el ancho del rectangulo "))
alto= int(input("Ingresar la altura del rectangulo "))
caracte = input("Ingresar el relleno del rectangulo")

def dibujar(an,alto,letra):
    for i in range (an):
        for j in range (alto):
            print(letra,end="")
        print()
dibujar (ancho,alto,caracte)







import random
Secreto =random.randint(1,2)
Numero = int(input("¿Cual será el npumero Secreto? 🤫"))

while Numero != Secreto:
    if Numero < Secreto:
        print("el numero es mayor ⬆️")
    else:
        print("El numero es menor ⬇️")
    Numero = int(input("🫤 Intentalo otra vez"))
print("🎉Felicidades! El numero secreto es:",Secreto)
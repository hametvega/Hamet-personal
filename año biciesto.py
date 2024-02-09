
# añoactual = int(input("ingresa el año actual "))
# año = int(input("Ingresa el año a evaluar "))
def añovis(añc,añ):
    
    if añ < añc:#añadidura
        if (añ %4 == 0) and (añc %100 !=0 ):
            print("El año fue visiesto ")
    elif añ > añc:
        if (añ %4 == 0) and (añc %100 !=0 ):
            print("El año sera visiesto")
    else:
        print("el año no es visiesto")   
añovis (añoactual,año)
#calcular años visiestos con rango

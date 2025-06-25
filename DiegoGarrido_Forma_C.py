stock_fortificados=500
stock_iluminados=500
lista_fortificados=[]
lista_iluminados=[]

def validacion_string(mensaje:str):
    while True:
        string=input(mensaje)
        string_limpio=string.strip()
        if len(string_limpio)==0:
            print("Error: Debe ingresar un string valido")
            continue
        else:
            break
    return(string_limpio)

def validacion_entero(mensaje:str):
    while True:
        try:
            entero=int(input(mensaje))
            break
        except ValueError:
            print("Error: Debe ingresar un numero entero")
            continue
    return(entero)


def compra_fortificados(mensaje:str):
    print(mensaje)
    while True:
        repeticion=False
        nombre_comprador=validacion_string("Ingrese su nombre: ")
        if nombre_comprador in lista_fortificados:
            print("Error: El nombre de comprador esta repetido. No pueden haber dos entradas al mismo nombre")
            repeticion=True
        if repeticion==False: 
            break

    while True:
        tipo_entrada=validacion_string("Ingrese tipo de entrada (G/V): ")
        if tipo_entrada.lower()!="g" and tipo_entrada.lower()!="v":
            print("Error: Debe ingresar G (Galeria) o V (VIP) para confirmar su tipo de entrada")
            continue
        else:
            break
    
    while True:
        codigo=validacion_string("Ingrese codigo de confirmacion: ")
        if len(codigo)!=6 or any(i.isupper() for i in codigo)==False or " " in codigo:
            print("Error: Codigo no valido. Intente otra vez. (Su codigo debe tener 6 caracteres, ningun espacio, y al menos una mayuscula)")
            continue
        else:
            print("Codigo Validado")
            break

    lista_fortificados.append(nombre_comprador)
    global stock_fortificados
    stock_fortificados-=1
    return(print('¡Entrada registrada con exito para "los Fortificados"!'))

def compra_iluminados(mensaje:str):
    print(mensaje) 
    while True:
        repeticion=False
        nombre_comprador=validacion_string("Ingrese su nombre: ")
        if nombre_comprador in lista_iluminados:
            print("Error: El nombre de comprador esta repetido. No pueden haber dos entradas al mismo nombre")
            repeticion=True
        if repeticion==False: 
            break

    while True:
        tipo_entrada=validacion_string("Ingrese tipo de entrada (CV/PAL): ")
        if tipo_entrada.lower()!="cv" and tipo_entrada.lower()!="pal":
            print("Error: Debe ingresar 'CV' (Cancha VIP) o 'PAL' (Palco) para confirmar su tipo de entrada")
            continue
        else:
            break
    
    while True:
        codigo=validacion_string("Ingrese codigo de confirmacion: ")
        if len(codigo)!=5 or " " in codigo:
            print("Error: Codigo no valido. Intente otra vez. (Su codigo debe tener 5 digitos y no tener espacios)")
            continue
        else:
            mayusculas=0
            for i in codigo:
                if i.isupper():
                    mayusculas+=1
            if mayusculas<3:
                print("Error: Codigo no valido. Intente otra vez. (Su codigo debe tener almenos 3 mayusculas)")
                continue
            else:
                print("Codigo Validado")
                break

    lista_iluminados.append(nombre_comprador)
    global stock_iluminados
    stock_iluminados-=1
    return(print('¡Entrada registrada con exito para "los Iluminados"!'))

def imprimir_entradas(mensaje:str):
    print(mensaje)
    print('Entradas disponibles para "los Fortificados": ',stock_fortificados)
    print('Entradas disponibles para "los Iluminados": ',stock_iluminados)

def salir(mensaje:str):
    print(mensaje)

while True:
    print("TOTEM AUTOSERVICIO CONCERTOS ROCK AND CHILE")
    print('1.- Comprar entrada a "los Fortificados" ')
    print('2.- Comprar entrada a "los Iluminados" ')
    print("3.- Stock de entradas para ambos conciertos")
    print("4.- Salir")

    opcion=validacion_entero("Ingrese opcion: ")

    if opcion==1:
        compra_fortificados('Ha seleccionado Comprar entrada a "los Fortificados"')
    elif opcion==2:
        compra_iluminados('Ha seleccionado Comprar entrada a "los Iluminados"')
    elif opcion==3:
        imprimir_entradas("Lista de entradas:")
    elif opcion==4:
        salir("Programa terminado...")
        break
    else:
        print("Debe ingresar una opcion valida!!")
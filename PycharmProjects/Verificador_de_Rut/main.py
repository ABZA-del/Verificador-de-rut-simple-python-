import time

while True:
    rut = input("Digita tu rut:")
    longitud = len(rut)
    digito_verificador = (rut[longitud-1])
    copia_rut = rut
# Todo:En la forma en que esta hecho, si hay una K el codigo daba error y esta fue la forma de resolverlo
    if "K" in rut.upper():
        copia_rut = rut[:-1]
        copia_rut = copia_rut + "0"
    copia_rut = int(copia_rut)
    copia_rut = int(copia_rut/10)
    multiplicador = 2
    suma = 0
    digito_verificador_obtenido = ""
# Todo: Aqui se realiza la formula
    while copia_rut != 0:
        ultimo_numero = copia_rut%10
        suma = suma + ultimo_numero*multiplicador
        multiplicador += 1
        copia_rut = int(copia_rut/10)
        if multiplicador == 8:
            multiplicador = 2
# Todo: Ahora hay que dividir la suma total por 11 y convertir a entero, multiplicar por 11 y eso restarle la suma
# Todo: y al final a 11 restarle el resultado de la operacion anterior

        digito_verificador_obtenido = 11-(suma-(int(suma/11)*11))
# Todo: Si el digito es 10 pasa a ser K y si es 11 pasa a ser 0
    if digito_verificador_obtenido == 10:
        digito_verificador_obtenido = "K"
    elif digito_verificador_obtenido == 11:
        digito_verificador_obtenido = "0"
    digito_verificador_obtenido = str(digito_verificador_obtenido)
# Todo: Se comprueba si el digito dado es igual al digito obtenido por la formula y segun el resultado se valida
    if digito_verificador_obtenido == digito_verificador.upper():
        print("Rut valido")
    else:
        print("Rut invalido")
# Todo: Se reincia el programa dependiendo de la respuesta del usuario, si da una no valida se cerrara de igual manera
    Reiniciar = input("Quieres ingresar otro rut? S/N: ")
    if Reiniciar.lower() == "s":
        print("Reiniciando.....")
        time.sleep(2)
    elif Reiniciar.lower() == "n":
        print("Terminando programa.....")
        time.sleep(2)
        exit("cls")
    else:
        print("Respuesta invalida\n"
              "cerrando de todas maneras.....")
        time.sleep(2)
        exit("cls")


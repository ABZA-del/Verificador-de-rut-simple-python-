"""RUT_CHECKER"""
import time
import os


def get_rut(rut):

    digito_verificador = (rut[-1])
    copia_rut = rut
# Todo:En la forma en que esta hecho, si hay una K el codigo daba error y esta fue la forma de resolverlo
    if "K" in rut.upper():
        copia_rut = rut[:-1]
        copia_rut = copia_rut + "0"
    return int(copia_rut), digito_verificador


def operations(copia_rut):
    # el operador // devuelve valor entero
    copia_rut = copia_rut//10
    multiplicador = 2
    suma = 0
    digito_verificador_obtenido = ""
# Aqui se realiza la formula
    while copia_rut != 0:
        ultimo_numero = copia_rut % 10
        suma = suma + ultimo_numero*multiplicador
        multiplicador += 1
        copia_rut = copia_rut//10
        if multiplicador == 8:
            multiplicador = 2
# Ahora hay que dividir la suma total por 11 y convertir a entero, multiplicar por 11 y eso restarle la suma
# y al final a 11 restarle el resultado de la operacion anterior    
        digito_verificador_obtenido = 11-(suma-((suma//11)*11))
# Si el digito es 10 pasa a ser K y si es 11 pasa a ser 0
    if digito_verificador_obtenido == 10:
        digito_verificador_obtenido = "K"
    elif digito_verificador_obtenido == 11:
        digito_verificador_obtenido = "0"
    return str(digito_verificador_obtenido)
# Se comprueba si el digito dado es igual al digito obtenido por la formula y segun el resultado se valida


def compare_the_digits(digito_verificador_obtenido, digito_verificador):
    if digito_verificador_obtenido == digito_verificador.upper():
        print("Rut valido")
    else:
        print("Rut invalido")


def Restart():
    try:
        user_answer = input("��Desea reiniciar el programa? (S/N):")
        if user_answer.upper() == "S":
            main()
        elif user_answer.upper() == "N":
            print("Cerrando programa")
            exit()
        else:
            print("Ni idea que significa esa respuesta")
            time.sleep(2)
            Restart()
    except (Exception):
        print("Error" + Exception)
        time.sleep(2)
        Restart()


def main():
    rut = input("Ingresa tu rut: ")
    compare_the_digits(operations(get_rut(rut)[0]), get_rut(rut)[1])
    Restart()


if __name__ == "__main__":
    main()



# este es el archivo pýthon en el cual mis compañeros y yo 
# trabajaremos para crear una calculadora de manera colaborativa

def sumar(numero1,numero2):
    return numero1+numero2
def restar(numero1,numero2):
    return numero1-numero2

def multiplicacion(num1,num2):
    resultadoM = num1 * num2;
    return resultadoM;
def division(num1, num2):
    try:
        resultadoD = num1 / num2;
    except ZeroDivisionError:
        resultadoD="no se puede dividir por cero"
    return resultadoD;

while True:
    print("que operacion desea realizar?")
    print("1 sumar")
    print("2 restar")
    print("3 multiplicar")
    print("4 dividir")
    print("5 salir")
    op=int(input("ingrese una opcion"))
    if op==1:
        num1=int(input("ingrese un numero"))
        num2=int(input("ingrese otro numero"))
        print(sumar(num1,num2))
    if op==2:
        num1=int(input("ingrese un numero"))
        num2=int(input("ingrese otro numero"))
        print(restar(num1,num2)) 
    if op==3:
        num1=int(input("ingrese un numero"))
        num2=int(input("ingrese otro numero"))
        print(multiplicacion(num1,num2))
    if op==4:
        num1=int(input("ingrese un numero"))
        num2=int(input("ingrese otro numero"))
        print(division(num1,num2))
    if op==5:
        break           



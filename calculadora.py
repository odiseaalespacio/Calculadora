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
    resultadoD = num1 / num2;
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
        
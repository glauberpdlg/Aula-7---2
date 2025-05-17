def soma(a,b):
    s = a + b
    print("{} + {} = {}".format(a,b,s))

def subtrai(a,b):
    st = a - b
    print("{} - {} = {}".format(a,b,st))

def mult(a,b):
    m = a * b
    print("{} * {} = {}".format(a,b,m))

def div(a,b):
    if b!=0:
        d = a / b
        print("{} / {} = {}".format(a,b,d))
    else:
        print("valores inválidos")
while True:
    def calculadora(a,b):
        operacoes = int(input("\n1- soma \n2- subtração \n3- multiplicação \n4- divisão \nEscolha sua operação desejada: "))
        if operacoes == 1:
            soma(a,b)
        elif operacoes == 2:
            subtrai(a,b)
        elif operacoes == 3:
            mult (a,b)
        elif operacoes == 4:
            div (a,b)
    
    f = int(input("Digite o primeiro número: "))
    
    g = int(input("Digite o segundo número: "))

    print(100*"-")

    calculadora(f,g)
 

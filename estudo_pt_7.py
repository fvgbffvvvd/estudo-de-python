#cap 5 repetições 
n = int(input("Tabuada de:"))
i = int(input("digite um numero inicial :"))
f = int(input("digite um numero final :"))
x = 1

while x <= f :
    print("{} + {} = {}".format(n, x, n + x))
    x=x+1
programa que calcula a mutiplicação e imprime como soma 
n = int(input("digite um numero :"))
fim = int(input("digite um valor:"))

x = 1
while x <= fim:
     print("+",n)
     x = x + 1 

teste para divisão 
n = int(input("digite um numero :"))# dividendo 
fim = int(input("digite outro numero:"))# divisor 
d = n / fim
x = 1
while x <= fim:
     print(d)
     x = x + 1 

pontos = 0
questão = 1
while questão <= 3:
    resposta = input("Resposta da questão %d: " % questão)
    if questão == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questão == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questão == 3 and (resposta == "d" or resposta == "D") :
        pontos = pontos + 1
    questão +=1
    print("O aluno fez %d ponto(s)" % pontos)


taxa = int(input("digite o deposito inicial :"))
x = taxa
juros = int(input("valor de juros :")) 
y = juros 
calculo = x * y
z = calculo //100
print(z)


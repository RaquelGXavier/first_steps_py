#o usuário irá escolher os números que serão somados
#note que, nesse caso, os números serão concatenados
#Concatenar:termo usado em computação que designa a operação de unir o conteúdo de duas strings 
a=input("Digite o primeiro numero:")
b=input("Agora, digite o segundo número:")
soma=a+b
print("A soma de", a, "+", b, "eh igual a", soma)

#agora, vamos fazer com que os números sejam realmente somados
#para isso, teremos que mudar o tipo da variavel, de str para int

a=input("Escolha mais um numero:")
b=input("Escolha outro número:")
a=int(a)
b=int(b)
soma=a+b
print("A soma de:",a,"+",b,"sera então",soma)
print("Entendeu qual é a diferença entre os comandos?")

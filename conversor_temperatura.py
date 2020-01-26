#Conversão de temperatura
temperatura_Fahrenheit = 78
F=temperatura_Fahrenheit
temperatura_Celsius = ((F-32)*5)/9
print("A temperatura em Celsius será:",temperatura_Celsius)

#O problema desse programa é que sempre que quiser uma nova
#temperatura, terei que alterar o valor da mesma.
#Para melhorar o programa, usaremos a funcionalidade "input"

F=input("Digite uma temperatura em Fahrenheit:")
#a função input sempre devolve uma string, então devemos converter
F=float(F)
temperatura_Celsius = ((F-32)*5)/9
print("A temperatura em Celsius será:",temperatura_Celsius,"°C")

#para continuarmos testando a função input, esse programa irá quebrar
#o número de segundos em horas, minutos e segundos
segundos=input("Entre com o número de segundos a ser convertido:")
#como sabemos, input semre retorna uma string. Então, vamos converter para um inteiro
segundos=int(segundos)
total_segs=segundos
horas = total_segs//3600
#no python 3, lembre-se que o operador // devolve um número inteiro
segs_restantes = total_segs%3600 #% operador devolve o resto da divisão
minutos = segs_restantes//60
segs_restantes_final = segs_restantes%60
segundos_final = segs_restantes_final

print(horas,"horas,",minutos,"minutos,","e",segundos_final,"segundos")

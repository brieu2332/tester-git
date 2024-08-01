from datetime import date #para saber a data atual

#voce esta na branch develop


#variaveis
anoAtual = date.today().year #coloca o ano atual dentro da vari ano
nome = ""
anoDeNascimento = 0
calculoIdade = 0

#entrada
nome = input('diga seu nome:')
anoDeNascimento = int(input('coloque sua data de nascimento:'))

#mostra e calcula idade
calculoIdade = anoAtual - anoDeNascimento
print(calculoIdade)



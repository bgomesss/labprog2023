'''
Exercícios sobre os comandos de condição em python
'''

from datetime import date, datetime

TODAY = datetime.now()

def exemploSe():
    n1 = float(input('Nota1: '))
    n2 = float(input('Nota2: '))
    media = (n1 + n2) / 2
    if media >= 6:                  #SE
        print('APROVADO!!!')
    else:                           #SENAO
        pf = float(input('Nota da PF: '))
        media = (media + pf) / 2
        if media >= 5:
            print('APROVADO NA PF!!!')
        else:
            print('REPROVADO!!!')

def exemploSe2():
    opcao = int(input('Opção: '))
    if opcao == 0:
        print('Escolheu 0')
    elif opcao == 1:
        print('Escolheu 1')
    elif opcao == 2:
        print('Escolheu 2')
    elif opcao == 3:
        print('Escolheu 3')    
    else:
        print('Opção Inválida!')
        
#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q01():
    valor1=int(input('Digite o primeiro valor: '))
    valor2=int(input('Digite o primeiro valor: '))
    resultado=valor1 + valor2
    if  resultado>10:
        print('A soma dos valores é maior que 10: ',resultado)

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q02():
    valor1=int(input('Digite o primeiro valor: '))
    valor2=int(input('Digite o primeiro valor: '))
    resultado=valor1 + valor2
    if resultado>20:
        print('A soma dos valores é maior que 20: ',resultado)
        print('A soma dos valores é: ',resultado+8)
    elif resultado<=20:
        print('A soma dos valores é menor ou igual 20: ',resultado)
        print('A soma dos valores é: ',resultado-5)
    
#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q03():
    numero=int(input('Digite um número inteiro: '))
    if not (numero%3):
         print('o número digitado é multiplo de 3')
    else:
        print('o número digitado não é multiplo de 3')
             
        

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q04():
    numero=int(input('Digite um número: '))
    if numero % 5 == 0:
        print(f'{numero} é divisivel por 5')
    else:
        print(f'{numero} não é divisivel por 5')

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q05():
    numero=int(input('Digite um número: '))
    if numero % 3 == 0 and numero % 7 ==0:
        print(f'{numero} é divisivel por 3 e 7')
    else:
        print(f'{numero} não é divisivel por 3 e 7')

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q06():
    salario_bruto=int(input('Digite o salario bruto: '))
    prestação=int(input('Digite o valor da prestação: '))
    if prestação > (salario_bruto*30)/100:
        print(f'{prestação} o imprestimo não pode ser concedido')
    else:
        print(f'{prestação} o emprestimo pode ser concedido')   

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q07():
    pass
    numero=int(input('Digite um número: '))
    if 20 <= numero <= 50:
        print(f'O número {numero} está compreendido entre 20 e 50.')
    else:
        print(f'O número {numero} não está compreendido entre 20 e 50.')
#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q08():
    pass
    numero=int(input('Digite um número: '))
    if numero>20:
         print(f'O número {numero} é maior que 20')
    elif numero == 20:
        print(f'O número {numero} é igual a 20')
    else:
         print(f'O número {numero} é menor que 20')
#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q09():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    import datetime
    ano_atual = datetime.datetime.now().year
    if ano_nascimento <= ano_atual and ano_nascimento > 0:
        idade = ano_atual - ano_nascimento
        print(f"Sua idade é: {idade} anos")
    else:
        print("Ano de nascimento inválido. Certifique-se de inserir um ano válido.")

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = int(input("Digite o terceiro número inteiro: "))
    numeros = [num1, num2, num3]
    numeros_ordenados = sorted(numeros)
    print("Os números em ordem crescente são:", numeros_ordenados[0], numeros_ordenados[1], numeros_ordenados[2])


#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():    
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))
    maior_numero = numero1
    if numero2 > maior_numero:
        maior_numero = numero2
    if numero3 > maior_numero:
        maior_numero = numero3
    print("O maior número é:", maior_numero)


#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos
def q12():
    idade = int(input("Digite a idade da pessoa: "))
    if idade >= 18:
        print("A pessoa é maior de idade.")
    if idade > 65:
        print("A pessoa tem mais de 65 anos.")
    if idade < 18:
        print("A pessoa é menor de idade.")
#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
def q13():
    nome_aluno = input("Digite o nome do aluno: ")
    nota_prova1 = float(input("Digite a nota da prova 1: "))
    nota_prova2 = float(input("Digite a nota da prova 2: "))
    media = (nota_prova1 + nota_prova2) / 2

    if media >= 7:
        situacao = "Aprovado"
    elif media < 3:
        situacao = "Reprovado"
    else:
        situacao = "em Prova Final"
    print("Nome do aluno:", nome_aluno)
    print("Nota da prova 1:", nota_prova1)
    print("Nota da prova 2:", nota_prova2)
    print("Média das notas:", media)
    print("Situação:", situacao)

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def q14():
    salario = float(input("Digite o salário da pessoa: "))
    if salario <= 600:
        desconto_inss = 0
    elif salario <= 1200:
        desconto_inss = salario * 0.20
    elif salario <= 2000:
        desconto_inss = salario * 0.25
    else:
        desconto_inss = salario * 0.30
    print("Desconto do INSS: R$", desconto_inss)

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def q15():
    valor_compra = float(input("Digite o valor de compra do produto: "))
    if valor_compra < 20.00:
        lucro_percentual = 0.45
    else:
        lucro_percentual = 0.30
    valor_venda = valor_compra + (valor_compra * lucro_percentual)
    print("Valor de venda: R$", valor_venda)


#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def q16():
    idade = int(input("Digite a idade do nadador: "))
    if idade >= 5 and idade <= 7:
        categoria = "Infantil A"
    elif idade >= 8 and idade <= 10:
        categoria = "Infantil B"
    elif idade >= 11 and idade <= 13:
        categoria = "Juvenil A"
    elif idade >= 14 and idade <= 17:
        categoria = "Juvenil B"
    else:
        categoria = "Sênior"
    print("Categoria do nadador:", categoria)


#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00
def q17():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    if idade <= 10:
        valor = 30.00
    elif idade <= 29:
        valor = 60.00
    elif idade <= 45:
        valor = 120.00
    elif idade <= 59:
        valor = 150.00
    elif idade <= 65:
        valor = 250.00
    else:
        valor = 400.00
    print("Nome da pessoa:", nome)
    print("Valor a pagar: R$", valor)

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
def q18():
    numero = int(input("Digite um número inteiro entre 1 e 12: "))
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    if numero >= 1 and numero <= 12:
        mes = meses[numero]
        print("Mês correspondente:", mes)
    else:
        print("Não existe mês com este número.")

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".
def q19():
    pontos = []
    for i in range(3):
        jogador = float(input(f"Digite os pontos obtidos pelo jogador {i+1}: "))
        pontos.append(jogador)
    pontos.sort(reverse=True)
    soma_pontos = sum(pontos)
    if soma_pontos > 100:
        media_pontos = soma_pontos / 3
        print("Pontos em ordem decrescente:", pontos)
        print("Média aritmética dos pontos:", media_pontos)
    else:
        print("Equipe desclassificada")

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
def q20():
    saldo_medio = float(input("Digite o saldo médio do cliente: "))
    credito = 0.0
    if saldo_medio <= 500:
        credito = 0.0
    elif saldo_medio <= 1000:
        credito = saldo_medio * 0.30
    elif saldo_medio <= 3000:
        credito = saldo_medio * 0.40 
    else:
        credito = saldo_medio * 0.50 
    print("Saldo Médio:", saldo_medio)
    print("Valor de Crédito: R$", credito)

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
def q21():

    nome_livro = input("Nome do livro: ")

    tipo_usuario = input("Tipo de usuário (professor ou aluno): ")

    if tipo_usuario.lower() == "professor":
        total_dias = 10
    elif tipo_usuario.lower() == "aluno":
        total_dias = 3
    else:
        print("Tipo de usuário inválido.")
        total_dias = 0

    if total_dias > 0:
        print("\nRecibo:")
        print("Nome do livro:", nome_livro)
        print("Tipo de usuário:", tipo_usuario)
        print("Total de dias para devolução:", total_dias)


#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
def q22():
       
    percurso_km = float(input("Digite o percurso em quilômetros: "))

    tipo_carro = input("Digite o tipo do carro (A, B ou C): ")

    if tipo_carro == 'A':
        consumo_por_litro = 12
    elif tipo_carro == 'B':
        consumo_por_litro = 9
    elif tipo_carro == 'C':
        consumo_por_litro = 8
    else:
        print("Tipo de carro inválido.")
        consumo_por_litro = 0

    if consumo_por_litro > 0:
        consumo_estimado = percurso_km / consumo_por_litro
        print(f"O consumo estimado de combustível é de {consumo_estimado:.2f} litros.")


#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano 180cal Abacaxi 75cal   Chá 20cal
#Peixe 230cal   Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal  Mousse diet 170cal  Suco de melão 100cal
#Carne 350cal   Mousse chocolate 200cal Refrigerante diet 65cal

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

opcao = int(input('Digite o número da questão: '))
match opcao:
    case 1: q01()
    case 2: q02()
    case 3: q03()
    case 4: q04()
    case 5: q05()
    case 6: q06()
    case 7: q07()
    case 8: q08()
    case 9: q09()
    case 10: q10()
    case 11: q11()
    case 12: q12()
    case 13: q13()
    case 14: q14()
    case 15: q15()
print('Opção Inválida!')
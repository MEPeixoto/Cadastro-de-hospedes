#seu código aqui
qtd_pessoa = int(input('Qual a quantidade de hóspedes?'))
#deixamos o quarto sem valor pois vamos dar o valor quando utilizarmos o .append
quarto = []

for i in range(qtd_pessoa):
    nome = input('Insira o seu nome: ')
    nome = nome.capitalize()
    #nome.capitalize foi utilizado para por a primeira letra em maiúsculo.

    cpf = input('Insira o cpf de {} somente os números: '.format(nome))
    if len(cpf) == 11 and cpf.isnumeric():
#utilizamos o len(cpf) 11 e o cpf.isnumeric para verificar se o cpf digitado contem somente números e se são 11 números

        hospede = (nome, 'cpf: {}.'.format(cpf))
        quarto.append(hospede)
#utilizamos o append para dar a quantidade de pessoas para a reserva do quarto.

    else: 
        print('Cpf do(a) {} inválido. O cpf digitado não contém os 11 números.'.format(nome))
        continue
#aqui verificamos qual nome está com o cpf inválido retornando com o nome para correção.

print(quarto)
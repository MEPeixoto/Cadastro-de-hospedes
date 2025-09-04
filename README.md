# Cadastro-de-hospedes

## Sobre o Projeto
Este é um projeto simples em Python desenvolvido durante meus estudos de programação.  
O objetivo é praticar conceitos básicos como:
- Estruturas de repetição (`for`);
- Estruturas condicionais (`if/else`);
- Manipulação de strings e listas;
- Entrada de dados pelo usuário.

Este repositório faz parte da minha jornada de aprendizado e servirá para acompanhar minha evolução na programação.

# Sistema de Cadastro de Hóspedes

Este programa em **Python** foi desenvolvido para cadastrar hóspedes em
um quarto de hotel, validando o **CPF** informado e armazenando os dados
em uma lista.

------------------------------------------------------------------------

## Funcionalidades

-   Solicita a quantidade de hóspedes que serão cadastrados.\
-   Para cada hóspede:
    -   Solicita o **nome** e ajusta a primeira letra para maiúscula.
    -   Solicita o **CPF** (somente números).
    -   Valida se o CPF contém **exatamente 11 dígitos numéricos**.
-   Caso o CPF seja válido, o hóspede é adicionado à lista `quarto`.\
-   Caso seja inválido, o sistema emite uma mensagem de erro e solicita
    o próximo cadastro.\
-   Ao final, exibe todos os hóspedes cadastrados com sucesso.

------------------------------------------------------------------------

## Estrutura do Código

``` python
qtd_pessoa = int(input('Qual a quantidade de hóspedes?'))

quarto = []

for i in range(qtd_pessoa):
    nome = input('Insira o seu nome: ')
    nome = nome.capitalize()
   
    cpf = input('Insira o cpf de {} somente os números: '.format(nome))
    if len(cpf) == 11 and cpf.isnumeric():
        hospede = (nome, 'cpf: {}.'.format(cpf))
        quarto.append(hospede)
    else: 
        print('Cpf do(a) {} inválido. O cpf digitado não contém os 11 números.'.format(nome))
        continue

print(quarto)
```

------------------------------------------------------------------------

## Exemplo de Uso

### Entrada:

    Qual a quantidade de hóspedes? 2
    Insira o seu nome: ana
    Insira o cpf de Ana somente os números: 12345678901
    Insira o seu nome: joão
    Insira o cpf de João somente os números: 1234

### Saída:

    Cpf do(a) João inválido. O cpf digitado não contém os 11 números.
    [('Ana', 'cpf: 12345678901.')]

------------------------------------------------------------------------

## Tecnologias Utilizadas

-   Python 3.x
-   Estruturas de repetição (`for`)
-   Estruturas condicionais (`if/else`)
-   Manipulação de strings e listas


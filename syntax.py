# ==============================================================================
# Bloco 1: O "Feijão com Arroz" (Variáveis, Operadores e Condicionais)
# Para aquecer os braços e calibrar a sintaxe básica.
# ==============================================================================

# 1. Declare três variáveis (nome, idade, altura) com seus tipos corretos 
# e imprima formatado usando f-strings.
nome = 'Sonserino'
idade = 33
altura = 1.78

f'{nome} tem {idade} anos, {altura} de altura e está cansado.'
# 2. Peça dois números ao usuário e exiba a soma, subtração, multiplicação, 
# divisão real, divisão inteira e o resto da divisão.


# 3. Receba um número inteiro e diga se ele é par ou ímpar (sem usar funções).


# 4. Receba três notas, calcule a média aritmética e exiba se o aluno foi 
# Aprovado (>= 7), Recuperação (5 a 6.9) ou Reprovado (< 5).


# 5. Receba um ano e determine se ele é bissexto (regrinha matemática do 
# divisor de 4, 100 e 400).


# 6. Peça um valor em metros e exiba-o convertido em centímetros e milímetros.


# 7. Escreva um programa que receba a velocidade de um carro. Se ultrapassar 
# 80 km/h, exiba que ele foi multado e o valor da multa (R$ 7,00 por cada km 
# acima do limite).


# 8. Receba o salário de um funcionário e calcule o reajuste: salários até 
# R$ 1.500,00 ganham 15%; acima disso, ganham 10%.


# 9. Crie uma calculadora simples que recebe dois números e uma string 
# operadora (+, -, *, /) e realiza a operação correspondente.


# 10. Peça três números e exiba qual é o maior e qual é o menor deles.


# ==============================================================================
# Bloco 2: A Repetição (Loops while e for)
# Aqui você começa a controlar o fluxo do tempo dentro da máquina.
# ==============================================================================

# 11. Imprima todos os números pares de 1 a 100 usando um laço for.


# 12. Faça um programa que leia 5 números (usando loop) e mostre a soma 
# e a média deles.


# 13. Calcule o fatorial de um número inteiro fornecido pelo usuário 
# usando um laço while.


# 14. Gere a tabela de tabuada de um número de 1 a 10 usando for.


# 15. Peça um número inteiro ao usuário e diga se ele é um número primo ou não.


# 16. Escreva o jogo do "Acerte o Número": o programa define um número fixo 
# (ex: 42) e o usuário tenta adivinhar usando while. O programa diz se o 
# palpite foi maior ou menor até ele acertar.


# 17. Imprima os primeiros N termos da Sequência de Fibonacci, onde N é 
# informado pelo usuário.


# 18. Receba uma string do usuário e conte quantas vogais existem nela 
# usando um laço.


# 19. Crie um loop que peça números ao usuário indefinidamente. O loop só 
# para se o usuário digitar 0. No final, mostre a soma de todos os números 
# digitados.


# 20. Desenhe um triângulo de asteriscos no terminal com N linhas baseado 
# no input do usuário (Ex se N=3):
# *
# **
# ***


# ==============================================================================
# Bloco 3: As Estruturas de Dados (Listas, Tuplas e Sets)
# Manipulação de coleções de dados na unha.
# ==============================================================================

# 21. Crie uma lista com 10 números inteiros. Remova os duplicados sem usar 
# a função set() (faça varrendo a lista).


# 22. Receba 5 nomes de usuários, guarde em uma lista e exiba-os em ordem 
# alfabética inversa.


# 23. Escreva um programa que junte duas listas de tamanhos diferentes em uma 
# terceira lista, alternando os elementos (Ex: [1, 2] e ['a', 'b', 'c'] 
# vira [1, 'a', 2, 'b', 'c']).


# 24. Crie uma lista com 20 números aleatórios. Separe-os em duas listas: 
# uma de pares e outra de ímpares, e imprima as três.


# 25. Dada uma lista de números, encontre o segundo maior valor sem ordenar 
# a lista (sem usar .sort()).


# 26. Crie duas tuplas contendo coordenadas (X, Y) e calcule a distância 
# euclidiana entre esses dois pontos.


# 27. Peça duas frases ao usuário e, utilizando set, exiba quais palavras 
# aparecem em ambas as frases (interseção) e quais são exclusivas de cada uma.


# 28. Escreva um programa que verifique se uma palavra digitada é um 
# palíndromo (ex: "arara") manipulando os índices da lista/string.


# 29. Crie uma lista de strings e utilize List Comprehension para gerar uma 
# nova lista contendo apenas as strings que possuem mais de 5 caracteres 
# e começam com a letra "A".


# 30. Simule o funcionamento de uma Pilha (Stack) usando uma lista: crie um 
# menu com opções de Push (inserir), Pop (remover o último) e Exibir pilha.


# ==============================================================================
# Bloco 4: Dicionários e Funções (Modularização e Mapeamento)
# Organizando o código e associando chaves a valores.
# ==============================================================================

# 31. Crie uma função que recebe um número e retorna True se for primo 
# e False caso contrário.


# 32. Escreva uma função chamada reverso() que recebe uma string e retorna 
# ela invertida, caractere por caractere, usando um laço.


# 33. Crie um dicionário que represente um produto (nome, preço, estoque). 
# Peça ao usuário uma quantidade comprada, atualize o estoque e exiba 
# o valor total da compra.


# 34. Faça uma função que receba uma quantidade indeterminada de números 
# (usando *args) e retorne a soma de todos os valores elevados ao quadrado.


# 35. Escreva um programa que leia o nome e a média de 3 alunos, guardando 
# tudo em um dicionário (chave: nome, valor: média). No final, mostre quem 
# teve a maior média.


# 36. Construa uma função que conte a frequência de cada caractere em uma 
# string e retorne essa contagem em um dicionário.


# 37. Crie uma função que receba dois argumentos nomeados (usando **kwargs): 
# desconto e imposto. A função deve aplicar essas taxas a um preço base 
# e retornar o valor final.


# 38. Crie uma agenda telefônica simples usando um dicionário aninhado 
# (um dicionário dentro de outro). O programa deve permitir Adicionar, 
# Buscar e Deletar um contato.


# 39. Escreva uma função lambda que filtre os números múltiplos de 3 de 
# uma lista usando a função nativa filter().


# 40. Crie uma função recursiva para calcular a potência de um número 
# (base ^ expoente) sem usar o operador **.


# ==============================================================================
# Bloco 5: Avançando o Fundamento (Arquivos, Exceções e POO Básica)
# A transição para a Engenharia de Software robusta.
# ==============================================================================

# 41. Crie um programa que tente abrir um arquivo de texto inexistente e 
# trate o erro usando try / except FileNotFoundError, exibindo uma 
# mensagem amigável.


# 42. Escreva uma função que receba dois valores e tente dividir o primeiro 
# pelo segundo. Trate as exceções de ZeroDivisionError e TypeError 
# (caso enviem uma string).


# 43. Crie um script que crie (ou abra) um arquivo chamado notas.txt. 
# O programa deve pedir ao usuário para digitar várias notas e salvá-las 
# linha por linha no arquivo.


# 44. Faça um programa que leia o arquivo notas.txt gerado no exercício 
# anterior, calcule a média das notas salvas e exiba na tela.


# 45. Crie uma classe chamada Pessoa com os atributos nome e idade, e um 
# método apresentar() que imprima os dados da pessoa.


# 46. Crie uma classe ContaBancaria com atributos titular, saldo (privado) 
# e os métodos depositar() e sacar(). Garanta que o saldo não fique negativo.


# 47. Implemente o conceito de Herança: crie uma classe mãe Veiculo 
# (com modelo e ano) e uma classe filha Moto (com o atributo específico 
# cilindradas). Instancie a filha e chame os métodos herdados.


# 48. Crie uma classe Retangulo com atributos largura e altura. Use o 
# decorador @property para criar um método que calcula a área, permitindo 
# acessá-lo como se fosse um atributo estático (objeto.area).


# 49. Escreva um programa que leia um arquivo CSV simples (separado por vírgulas) 
# contendo colunas de "Nome,Idade" linha por linha usando manipulação de strings 
# puras (método .split()), sem importar o módulo csv.


# 50. O Desafio Final: Crie uma classe No (Node) que possui um valor e um 
# ponteiro para o próximo nó (self.proximo = None). Usando essa classe, monte 
# manualmente uma Estrutura de Lista Encadeada (Linked List) simples com 
# 3 elementos conectados e crie um método para percorrer os nós imprimindo 
# os valores na tela.

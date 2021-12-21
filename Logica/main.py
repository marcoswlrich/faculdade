
while True:
    # declaração da variável nome tipo string - digitada pelo usuário
    name = str(input('Nome da criança: '))
    # declaração da variável idade do tipo número inteiro - digitada pelo ususário
    age = int(input('Idade: '))
    # Estrutura de condição if para verificar as idades do usuário e imprimir escolaridade na tela
    if age >= 1 and age <= 5:
        print('O aluno(a) {} tem {} anos e está na Educação Infantil.'.format(name, age))
    elif age >= 6 and age <= 10:
        print('O aluno(a) {} tem {} anos e está no Ensino Fundamental I.'.format(name, age))
    elif age >= 11 and age <= 14:
        print('O aluno(a) {} tem {} anos e está no Ensino Fundamental II.'.format(name, age))
    elif age >= 15:
        print('O aluno(a) {} tem {} anos e está no Ensino Médio.'.format(name, age))
    # Declarei uma variável do tipo inteiro para usar no if juntamente com o break para encerrar o programa
    response = int(input('Deseja continuar? 0-Não 1-Sim: '))
    if response == 0:  # encerrar o programa
        break

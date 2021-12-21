# importando o método para gerar números aleatórios
from random import randint


# --------------------------- Funções -------------------------------

# -------------------- função para o cabeçalho ----------------------

def funcCabecalho():
    print('***********Menu***********')
    print('1 - Nova inscrição')
    print('2 - Visualizar inscrição')
    print('0 - Encerrar')


# ----------------------------- função para as opções -------------------

# Para verificar as opções do usuário e exibir erros
# parametro text para verificação do tipo string
# parametro min para verificação - limitando com número mínimo - do tipo num inteiro
# parametro max para verifircação - limitando com número máximo - tipo num inteiro
# While para loop até digitar a opção correta
def funcOpcao(text: str, min: int, max: int):
    while True:
        try:
            op = int(input(text))
        except ValueError:
            print('Erro: digite uma opção válida!')
            continue
        else:
            if min <= op <= max:
                return op
            print('Erro: digite uma opção válida!')
            continue


# ------------------------------- função para nome -----------------------

# Para verificar se o nome digitado é correto
# parametro do tipo string
# While para loop até digitar a opção correta
# variável nome vazia para retornar ao final da função e do while o nome correto
def funcNome(text: str):
    nome = ''
    while not nome:
        # slipt() - Para dividir cada palavra da string em uma lista, sendo cada palavra um item da lista
        # isalpha() - Método para verificar se cada item da lista nome se consiste em
        # caracteres alfabéticos e retornando com a condição if a variável nome vazia caso seja opção inválida
        # laço de repetição for para verificar cada item da lista com split()
        nome = input(text)  # entrada do usuário
        for i in nome.split(' '):
            if not i.isalpha():
                print('Erro: digite um nome válido!')
                nome = ''
                break
    return nome

# ------------------------------- função para email ----------------------------------

# Verifica se o email digitado pelo usuário é correto
# parametro texto para verificar se é um email válido e entrada
# função verifica o uso de @ e pontos
def funcEmail(text: str):
    while True:
        email = input(text) #entrada do usuário
        # find() - método para encontrar os caracteres especificados
        if email.find('@') != -1 and email.find('.') != -1 and email.find(' ') == -1:

            return email

        print('Erro: digite um email válido!')


# -------------------------- função para telefone ------------------------------------

# Para verificar se o telefone digitado é valido
# parametro text para verificação entrada
# aceitando somente números inteiros
# laço while até digitar um telefone válido
def funcTelefone(text: str):

    while True:
        try:
            telefone = int(input(text)) # entrada usuário

        except ValueError:
            print('Erro: digite um telefone válido!')
            continue
        else:
            return telefone


# -------------------------- função para o curso -----------------------------------

# Verificar se o curso digitado é valido
# aceitando apenas caracteres alfabéticos
# parametro text para verificação e entrada
# laço até digitar um curso válido
def funcCurso(text: str):

    curso = ''

    while not curso:
        curso = input(text)  # entrada usuário
        # slipt() - Para dividir cada palavra da string em uma lista, sendo cada palavra
        # um item da lista.
        # isalpha() - Método para verificar se cada item da lista nome se consiste em
        # caracteres alfabéticos e retornando com a condição if a variável nome
        # vazia caso seja opção inválida.
        # laço de repetição for para verificar cada item da lista com split()
        for i in curso.split(' '):
            if not i.isalnum():
                print('Erro: digite um curso válido!')
                curso = ''
                break

    return curso.upper()


# ------------------------------------função para gerar o voucher ------------------------

# Para gerar voucher de inscrição que armazena em dicionário = {}
# parametro cadastro em tipo lista de cadastro de pessoas
# a função retorna um voucher único para cada cadastro
# Se a lista de cadastro estiver vazia  é gerado um voucher
# Enquanto o 'voucher' for falso o laço while se repete, -> not false == True
def voucher(cadastros: list):
    inscricao = {}

    # método randômico randint() para gerar voucher entre 100 a 400.
    # condição que armazena no dicionário 'inscrição' na chave 'voucher' de cada inscrição
    # retornando o mesmo ja com voucher
    if not cadastros:
        voucher = randint(100, 400)
        inscricao['voucher'] = voucher
        return inscricao

    voucher = 0

    while not voucher:
        # Gera um número de voucher aleatório
        # laço de repetição for para verificar e evitar voucher iguais recebendo 0 e retornando ao laço
        # até ter número de voucher diferente
        voucher = randint(100, 400)
        for i in cadastros:
            if i['voucher'] == voucher:
                voucher = 0
                break

    inscricao['voucher'] = voucher
    return inscricao

# ---------------------------- Rodando o programa ----------------------------

# Variável para armazenar os dados cadastrados do tipo lista ou array
cadastros = []

# laço while para o cadastro

while True:
    #cabeçalho
    funcCabecalho()

    # Verificar opção digitada pelo usuário
    opcao = funcOpcao('Opção escolhida: ', 0, 2)

    # Para nova inscrição
    if opcao == 1:
        # Gerando o voucher
        inscricao = voucher(cadastros)
        # Cadastro do nome e add nome no dicionário {} - inscrição
        nome = funcNome('Digite o seu nome: ')
        inscricao['nome'] = nome
        # Cadastro de email e add o email no dicionário inscrição {}
        email = funcEmail('Digite o seu email: ')
        inscricao['email'] = email
        # Cadastro de telefone e add o telefone no dicionário inscrição {}
        telefone = funcTelefone('Digite o telefone: ')
        inscricao['telefone'] = telefone
        # Cadastro do curso e add o curso no dicionário inscrição {}
        curso = funcCurso('Digite o curso: ')
        inscricao['curso'] = curso

        # Add a nova inscrição à lista de cadastros
        cadastros.append(inscricao)

    # Opção para visualizar a inscrição
    elif opcao == 2:
        if cadastros == []:
            print('Nenhuma inscrição cadastrada')
        print('------------------Lista de inscrições------------------')
        # laço for para passar em cada item do cadastro
        for cadastro in cadastros:
            # laço para passar na chave e valores do dicionário e exibir na tela
            for i, j in cadastro.items():

                print('{}\t:\t{}'.format(i, j))
            print('------------------')

    # Opção para fechar o programa
    elif opcao == 0:
        print('Programa encerrado!')
        break

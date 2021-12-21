# Variável de entrada digitada pelo usuário
nome = str(input('Digite um nome: '))
# O método upper() é para alterar todos os caracteres da string em maiúsculas.
nomeUpper = nome.upper()
print(nomeUpper)
# Utilizei o laço for juntamente com a função range() para passar sobre cada letra para poder
# verificar com o if se é igual aos caracteres procurados e substituir.
# A função len() é para retornar o tamanho da string e ajudar o range() com o for em sua verificação,
# pois i = 0 e o for segue seu laço até o que len() retornar do tamanho da string.
# Para receber as alterações do laço da lista dentro do if utilizo fatiamento e concatenação e
# a variavel nomeUpper vai recebendo a strings e suas alterações no laço
for i in range(len(nomeUpper)):

    if nomeUpper[i] == 'A':
        nomeUpper = nomeUpper[:i] + '@' + nomeUpper[i+1:]
    elif nomeUpper[i] == 'E':
        nomeUpper = nomeUpper[:i] + '&' + nomeUpper[i+1:]
    elif nomeUpper[i] == 'I':
        nomeUpper = nomeUpper[:i] + '!' + nomeUpper[i+1:]
    elif nomeUpper[i] == 'O':
        nomeUpper = nomeUpper[:i] + '#' + nomeUpper[i+1:]
    elif nomeUpper[i] == 'U':
        nomeUpper = nomeUpper[:i] + '*' + nomeUpper[i+1:]

# Imprime na tela o resultado
print(nomeUpper)

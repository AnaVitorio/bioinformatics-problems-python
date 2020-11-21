arquivo = open('rosalind_ini5.txt', 'r')
lista = arquivo.readlines()
tamanho = len(lista)

x = 0
while x <= tamanho:
    if x % 2 == 0 and x != 0:
        print(lista[x-1], end='') 
    x = x + 1

arquivo.close()


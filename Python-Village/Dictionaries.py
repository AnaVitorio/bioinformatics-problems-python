# -*- coding: utf-8 -*-

def word_count():
    arquivo = open('rosalind_ini6.txt', 'r')
    separar_frase = arquivo.readlines()
    separar_frase = str(separar_frase).split(" ")

    #Pegando somente os valores únicos desse arquivo    
    unique_values = set(separar_frase)     
    
    #Passando os valores únicos para dentro de uma lista
    lista_unique_values = []
    for word in unique_values:
        lista_unique_values.append(word)   
    
    # Passando as palavras da lista para um dicionário e a quantidade de vezes que essas palavras aparecem no aquivo original 
    dicionario = {}
    for word in lista_unique_values:
        dicionario[word] = separar_frase.count(word)  
    
    # Exibindo cada palavra e o número de vezes que ela aparece
    for key, value in dicionario.items():
       print(key +" "+ str(value))

word_count()
  
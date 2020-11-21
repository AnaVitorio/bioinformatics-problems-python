n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
i = n1
soma = 0
while i <= n2:
    if i % 2 != 0:
        soma = soma + i
    i = i + 1

print(soma)
    

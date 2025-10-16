a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))

maior = max(a, b, c)
menor = min(a, b, c)
meio = a + b + c - maior - menor

print ("Maior: %i" %(maior))
print ("Menor: %i" %(menor))
print ("Meio: %i" %(meio))
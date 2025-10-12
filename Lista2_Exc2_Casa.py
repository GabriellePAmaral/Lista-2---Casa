num = int(input("Digite um número inteiro entre o e 100:"))

num_chave = 47

if num < num_chave:
    d = num_chave - num
    print ("A diferença é de: %i" %(d))
else:
    d = num - num_chave
    print ("A diferença é de: %i" %(d))
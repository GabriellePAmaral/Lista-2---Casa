nota = float(input("Digite a nota:"))

parte_inteira = int(nota)
parte_decimal = nota - parte_inteira

if parte_decimal > 0.5:
    nota_arredondada = parte_inteira + 1
else:
    nota_arredondada = parte_inteira

print("Nota arredondada: %i" %(nota_arredondada))
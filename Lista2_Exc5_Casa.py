salario = float(input("Digite seu salário bruto:"))
horas_trabalhadas = float(input("Digite o total de horas trabalhadas:"))

desconto_renda = 0
desconto_encargos = 0
adicional = 0

if salario < 800.00:
    desconto_renda = 0
    desconto_encargos = 0
elif 800.00 <= salario <= 1600.00:
    desconto_renda = salario * 0.08
    desconto_encargos = salario * 0.05
else:
    desconto_renda = salario * 0.15
    desconto_encargos = salario * 0.07
salario_pos_descontos = salario - desconto_renda - desconto_encargos

if horas_trabalhadas > 160:
    valor_hora = salario / 160
    hora_extra = horas_trabalhadas - 160
    adicional = valor_hora * hora_extra * 0.5

salario_liquido = salario_pos_descontos + adicional
print("Salário líquido: R$ %.2f" %(salario_liquido))
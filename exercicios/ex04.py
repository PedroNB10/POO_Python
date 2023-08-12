renda = float(input("Digite o salario:"))


if renda > 4664.68:
    aliquota = renda *0.275   
elif renda  > 3751.06:
    aliquota = renda *0.225
elif renda > 2826.65:
    aliquota = renda *0.15
elif renda > 1903.99:
    aliquota = renda *0.075
else:
    aliquota = 0

print("a aliquota da renda {} é de {}".format(renda,aliquota))

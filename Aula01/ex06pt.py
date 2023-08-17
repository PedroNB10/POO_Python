
# rever
palavra = input("Digite string:")

palin = True

for i in range(0,int(len(palavra)/2)):
    if palavra[i] != palavra[len(palavra)-i-1]:
        palin = False
        break
    if palin:
        print(palavra+' é um palíndromo')
    else:
        print(palavra+' não é um palíndromo')


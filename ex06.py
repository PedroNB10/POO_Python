
palavra = input("Digite string:")

palavraInv = palavra[::1]

if palavra == palavraInv:
    print(palavra + 'é um palindromo')

else:
    print(palavra+ ' não é um palindromo')

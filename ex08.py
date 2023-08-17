

def celsius_para_farenheit(numero):
    numero = numero * 1.8 + 32
    return numero

numero = float(input("Temp em Celsius:"))

numero_convertido = celsius_para_farenheit(numero)

print(f"Temp em Farenheit: {numero_convertido}")


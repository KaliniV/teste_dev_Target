numero1 = 0
numero2 = 1
numero3 = 0
i = int(input("Digite um numero: "))
while i > numero3:
    numero3 = numero1 + numero2
    numero1 = numero2
    numero2 = numero3
if i == 0:
    print("O zero se encontra na sequência")
elif i == numero3:
    print("O numero se encontra na sequência")
else:
    print("o numero não se encontra na sequência")

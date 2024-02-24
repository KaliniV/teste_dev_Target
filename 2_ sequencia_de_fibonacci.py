numero1 = 0
numero2 = 1
numero3 = 0
i = int(input("Digite um número: "))
while i > numero3:
    numero3 = numero1 + numero2
    numero1 = numero2
    numero2 = numero3
if i == 0:
    print("O zero está na sequência.")
elif i == numero3:
    print("O número está na sequência.")
else:
    print("O número não está na sequência.")

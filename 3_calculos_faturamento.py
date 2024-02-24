import json

with open("dados.json", encoding="utf-8") as meu_json:
    dados = json.load(meu_json)

maior = 0
menor = 0
diamaior = 0
diamenor = 0
soma = 0
qtd = 0
media = 0
soma2 = 0
for i in dados:
    if i["valor"] > maior:
        maior = i["valor"]
        diamaior = i["dia"]

    if i["valor"] < menor or i["valor"] != 0:
        menor = i["valor"]
        diamenor = i["dia"]
    if i["valor"] != 0.0:
        soma += i["valor"]
        qtd += 1
        media = soma / qtd
        if i["valor"] > media:
            soma2 += 1
print(f"Maior valor de faturamento: R${maior}, dia:{diamaior}.")
print(f"Menor valor de faturamento: R${menor}, dia:{diamenor}.")
print(f"Número de dias que o faturamento foi maior que a média: {soma2} dias.")

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
ValorTotal = sp + rj + mg + es + outros

porcentagem = (sp / ValorTotal) * 100
print(f"SP - {porcentagem:.0f}%")

porcentagem = (rj / ValorTotal) * 100
print(f"RJ - {porcentagem:.0f}%")

porcentagem = (mg / ValorTotal) * 100
print(f"MG - {porcentagem:.0f}%")

porcentagem = (es / ValorTotal) * 100
print(f"ES - {porcentagem:.0f}%")

porcentagem = (outros / ValorTotal) * 100
print(f"Outros - {porcentagem:.0f}%")

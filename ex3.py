nomes=["joao","ricardo","gabriel","ezaquiel","Alberto"]

mais_longo = nomes[0]
mais_curto = nomes[0]

for nome in nomes:
    if len(nome) > len(mais_longo):
        mais_longo = nome

    if len(nome) < len(mais_curto):
        mais_curto = nome
X=len(mais_curto)
Y=len(mais_longo)

print(X,mais_curto)
print(Y,mais_longo)


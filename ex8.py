
def calcular_imc(peso, altura_m):
    return peso / (altura_m ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Excesso de peso"
    else:
        return "Obesidade"


peso = 62  
altura_cm = 175  
altura_m = altura_cm / 100  


imc = calcular_imc(peso, altura_m)
classificacao = classificar_imc(imc)


print("=== Cálculo de IMC ===")
print(f"Peso: {peso} kg")
print(f"Altura: {altura_cm} cm ({altura_m:.2f} m)")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
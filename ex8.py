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

def obter_peso():
    while True:
        entrada = input("Digite o seu peso (em kg): ")
        try:
            peso = float(entrada)
            if peso <= 0:
                print("Erro: o peso deve ser maior que zero.\n")
            elif peso > 300:
                print("Aviso: insira o peso em kg, não em gramas ou outro formato.\n")
            else:
                return peso
        except ValueError:
            print("Erro: introduza um número válido para o peso.\n")

def obter_altura_cm():
    while True:
        entrada = input("Digite a sua altura (em cm): ")
        try:
            altura = float(entrada)
            if altura <= 0:
                print("Erro: a altura deve ser maior que zero.\n")
            elif altura < 100:
                print("Aviso: insira a altura em centímetros, não em metros.\n")
            else:
                return altura
        except ValueError:
            print("Erro: introduza um número válido para a altura.\n")

print("=== Cálculo de IMC ===\n")

peso = obter_peso()
altura_cm = obter_altura_cm()
altura_m = altura_cm / 100

imc = calcular_imc(peso, altura_m)
classificacao = classificar_imc(imc)

print("\n=== Resultado ===")
print(f"Peso: {peso:.1f} kg")
print(f"Altura: {altura_cm:.1f} cm ({altura_m:.2f} m)")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")

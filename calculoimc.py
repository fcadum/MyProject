# Solicita ao usuário que digite o peso e altura
peso = float(input("Digite o seu peso (em kg) "))
altura = float(input("Digite a sua altura (em metro): "))

# Calcula o IMC (Índice de Massa Corporal)
imc = peso / (altura * altura)

# Exibe o IMC calculado
print(f"Seu IMC é: {imc:.2f}")

# Verifica a faixa de peso com base no IMC calculado
if imc > 25:
    print("Acima do peso ideal.")
elif imc < 18:
    print("Abaixo do peso ideal.")
else:
    print("O seu peso está OK!")
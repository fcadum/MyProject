# Classificar time, 1º é campeão, entre 1º e 6º é Libertadores , entre 7º  e 12º é Sul Americana e rebaixado entre os 4 últimos

time = (input("Digite o seu time: "))
posição = int(input("Digite a classificação do seu time no Campeonato Brasileiro: "))

if 1 <= posição <= 20:
    print(f"O {time}  ")

    if posição == 1:
        print(" é Campeão!")
    elif 1 < posição <= 6:
        print(" está classificado para a Libertadores.")
    elif 7 <= posição <= 12:
        print("está classificado para Sul-Americana.")
    elif 13 <= posição <= 16:
        print("Não classificado para Libertadores e Sul-Americana!")
    elif posição > 16:
        print("foi rebaixado!")
else:
    print("Digite a classificação entre 1 e 20!")
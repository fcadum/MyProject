#Demonstração de operadores lógicos em condicionais...
print("O que você vai fazer amanhã de manhã")
print("dormir / estudar / planejar")
manha = input()
print("O que você vai fazer amanhã a tarde?")
print("jogar / treinar / trabalhar")
tarde = input()

if not manha or not tarde:
    print("Você precisa dizer o que vai fazer!")
else:
    if manha == "dormir" or tarde == "jogar":
        print("Você se está desperdiçando o seu dia!")
    elif manha == "estudar" or tarde == "treinar":
        print("Que bom! Você irá se aperfeiçoar!")
    elif manha == "planejar" or tarde == "trabalhar":
        print("Para trabalhar melhor, devo me planejar")
    else:
        print("Não combinamos essa ações...")

print("Tenha um bom dia!")

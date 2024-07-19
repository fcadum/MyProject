

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2) / 2

if media < 4:
    print("Aluno reprovado.")
elif media >= 6:
    print("Aluno aprovado direto.")
else:    
    print("Aluno em recuperação.")

    nota3 = float(input("Digite a nota da recuperação: "))
    if nota3 >= 5:
        print("Aprovado na recuperação!")
    if nota3 < 5:
        print("Reprovado na recuperação!")

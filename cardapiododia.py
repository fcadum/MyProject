      #Demonstração das tarefas dos dias da semana...
print("Digite o dia para saber o cardápio do dia: ")
print("2. Segunda-feira")
print("3. Terça-feira")
print("4. Quarta-feira")
print("5. Quinta-feira")
print("6. Sexta-feira")
semana = int(input())

match semana:
    case 2:
        print("frango à milanesa")
    case 3:
        print("carne assada")
    case 4:
        print("Linguiça Acebolada")
    case 5:
        print("bife a parmegiana")
    case 6:
        print("feijoada")
    case _:
        print("Não entregamos aos fins de semana!!")
print("Agradecemos a preferência!!")
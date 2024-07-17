      #Demonstração das tarefas dos dias da semana...
print("Digite número correspondente ao dia da semama que gostaria de verificar: ")
print("2. Segunda-feira")
print("3. Terça-feira")
print("4. Quarta-feira")
print("5. Quinta-feira")
print("6. Sexta-feira")
print("7. Sábado")
print("8. Domingo")
dia = int(input())


match dia:
    case 2:
        print("Arrumar a sala.")
    case 3:
        print("Limpar a cozinha.")
    case 4:
        print("Organizar os armários.")
    case 5:
        print("Lavar o banheiro.")
    case 6:
        print("Arrumar os quartos.")
    case 7:
        print("Cortar a grama.")
    case 8:
        print("Limpar a piscina.")
    case _:
        print("Você precisa inserir um dia da semana válido!!")
    
print("Bom serviço!!!")
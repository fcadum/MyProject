# Digitar 3 números e falar se estao em ordem crescento ou decrescente, se não falar que estão misturados...

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

resultado = (x , y , z)

if x < y < z:
        print("Ordem crescente.")
elif x > y > z:
        print("Ordem decrescente.")
else:
        print("Eles estão misturados!")

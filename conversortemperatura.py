# Seria possível utilizar as estruturas condicionais if/elif/else ou match/case,
# Para pernonalizar este programa, de forma que ele ofereç as três conversões?
# Por exemplo, ele poderia perguntar ao usuário qual a unidae ed medida e qual valor de temperatura ele quer converter e a partir daí, realizar os cálculos necessários...

print("Digite a temperatura que gostaria de converter... ")
escolha = int(input("1. Celsius / 2. Kelvin / 3. Fahernheint"))
temperatura = int(input("Digite o valor da temperatura: "))


match escolha:
    case 1:
        kelvin = temperatura + 273
        fahrenheit = (9 / 5 * temperatura) - 32
        print(f"Aconversão de Celsius para Kelvin será {kelvin}.")
        print(f"A conversão de Celsius para fahrenheit será {fahrenheit}")
    case 2:
        celsius = temperatura - 273
        fahrenheit = * (temperatura - 273) + 32
        print(f"A conversão de Kelvin para Celsius será {celsius}.")
        print(f"A conversão de Kelvin para Fahrenheit será {fahrenheit}.")
    case 3:
        celsius =  5/9 * (temperatura - 32)
        kelvin = (temperatura - 32) / 1.8 + 273
        print(f"A temperatura de Fahrenheit para Celsius será {celsius}.")
        print(f"A temperatura de Fahrenheit para Kelvin será {kelvin}")



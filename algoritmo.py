alcool = float(input("digite o valor do alcool: "))
gasolina = float(input("digite o valor da gasolina: "))
formula = alcool/gasolina



print("-" *30)
print("Cálculadora Alcool X Gasolina")
print("-" *30)
print ( "A Razão entre alcool x gasolina é: ", formula)
if formula < 0.70:
    print ("é melhor utilizar alcool!")
else:
    print("é melhor utilizar Gasolina!")
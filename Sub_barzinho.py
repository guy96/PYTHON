


cerveja = {
    '1 - Antarctica': 6.00,
    '2 - Skol': 6.5,
    '3 - Brahma': 8.20,
    '4 - Sol': 8.25,
    '5 - Nortenha': 16.80,
    '6 - Proibida': 4.8,
    '7 - Devassa': 5.9,
    '8 - Heineken': 9.0
}

print("Escolha a cerveja pelo número")

print(cerveja)



escolha = int(input('Qual o número da cerveja voce deseja?'))
q= float(input("Qual quantidade de cervejas voce deseja? Digite em numeros"))

if escolha == 1:
    valorTotal=6*q
    nome = "Antártica"
    print(nome,'custa',valorTotal,'reais, por',q,'cerveja(s)')

elif escolha == 2:
    valorTotal=6.5*q
    nome = 'Skol'
    print(nome,'custa',valorTotal,'reais, por',q,'cerveja(s)')

elif escolha==3:
    valorTotal=8.2*q
    nome = 'Brahma'
    print(nome,'custa',valorTotal,'reais, por',q,'cerveja(s)')

elif escolha==4:
    valorTotal=8.25*q
    nome = 'Sol'
    print(nome,'custa',valorTotal,'reais, por',q,'cerveja(s)')

elif escolha==5:
    valorTotal=16.25*q
    nome = 'Nortenha'
    print(nome,'custa',valorTotal,'reais, por',q,'cerveja(s)')

elif escolha==6:
    valorTotal=4.8*q
    nome = 'Proibida'
    print(nome,'custa',valorTotal,'reais, por',q,'cerveja(s)')

elif escolha==7:
    valorTotal=5.9*q
    nome = 'Devassa'
    print(nome,'custa',valorTotal,'reais, por',q,'cerveja(s)')

elif escolha==8:
    valorTotal=9*q
    nome = 'Heineken'
    print(nome,'custa',valorTotal,'reais, por',q,'cerveja(s)')
else:
    print("Opção inválida. Por favor selecione um dos números")


















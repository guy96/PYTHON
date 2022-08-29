from ast import Add
import os
import sys

def menu():
 print("***Python Calculator***\n")
 print("Seja em vindo(a) à calculadora ! Escolha uma das opções abaixo:\n")
 print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
menu()
opção_desejada = int (input ("Digite a opção desejada: "))

n1 = float(input("Digite o 1° valor: "))
n2 = float(input("Digite o 2° valor: "))

def add(n1,n2):
 add = n1+n2
 print(n1," + ",n2," = ",add)

def subtracao(n1,n2):
 subtracao = n1-n2
 print(n1," - ",n2, " = ",subtracao)

def multiplicacao(n1,n2):
 multiplicacao = n1*n2
 print(n1," * ",n2, " = ",multiplicacao)

def divisao(n1,n2):
 divisao = n1/n2
 print(n1," / ",n2," = ",divisao)

if opção_desejada == 1:
    add(n1,n2)
elif opção_desejada == 2:
    subtracao(n1,n2)
elif opção_desejada == 3:
    multiplicacao(n1,n2)
elif opção_desejada == 4:
    divisao(n1,n2)
else:
    print("Opção inválida!!!")

encerramento = int(input ("Digite 1 para reiniciar ou qualquer tecla para encerrar: "))
    
if encerramento == 1:
 python= sys.executable
 os.execl(python, python,* sys.argv)
else:
    print("Obrigado e até logo!")
    exit()
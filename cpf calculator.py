#!/bin/python


#Algoritmo para calcular CPF

CPF = raw_input("Digite seu CPF: ")
cont = 0

for index in range(CPF.len):
	cont = ord(CPF[index]) + cont

if cont == 33 || cont == 44 || cont == 55:
	print("CPF verdadeiro!")
else:
	print("CPF falso!")
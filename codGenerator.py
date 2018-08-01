#!/bin/python

class Passwords:

	def geratorPassword(scope):
		passwordNow = ""
		index = 0
		for index in range(scope):
			passwordNow = passwordNow + "0"
			index = index + 1
		passwords = []
		passwords.append(passwordNow)
		index = 0
		while index < passwordNow.len:
			tempPassword = runningInThePesWord(passwordNow)
			jindex = 0
			while tempPassword.len < tempPassword.len * scope:
				tempPassword[tempPassword.len] = chr(ord(tempPassoword[tempPassoword.len - jindex]) + 1)
				passwordNow = tempPassword
				Passwords.append(passwordNow)
				jindex = jindex + 1
				#Fazer com que figue gerando senhas aleatorias!
		return passwords

	def runningInThePesWord(Word)[]:
		wordLen = Word.len
		wordMixed = []
		index = 0
		while wordLen < index:
			wordMixed.append(Word[index])
			index = index + 1
		return wordMixed
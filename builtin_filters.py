import math

def Modulo2(num):
	return num % 2

def Modulo3(num):
	return num % 3

def Digits(num):
	return int(math.log10(num)) + 1

def IsPrime(num):
	if num == 1:
		return 0
	elif num == 2:
		return 1
	primeVar = 1
	digits = int(math.log10(num)) + 1
	if digits > 12:
		for divider in range(2, int(num/10000000000)):
			if num % divider == 0:
				primeVar = 0
		for i in range(2,10000000001):
			for divider in range(int((i-1)*num/10000000000), int(i*num/10000000000)):
				if num % divider == 0:
					primeVar = 0
		return primeVar

	elif digits > 9:
		for divider in range(2, int(num/10000000)):
			if num % divider == 0:
				primeVar = 0
		for i in range(2,10000001):
			for divider in range(int((i-1)*num/10000000), int(i*num/10000000)):
				if num % divider == 0:
					primeVar = 0
		return primeVar

	elif digits > 6:
		for divider in range(2, int(num/10000)):
			if num % divider == 0:
				primeVar = 0
		for i in range(2,10001):
			for divider in range(int((i-1)*num/10000), int(i*num/10000)):
				if num % divider == 0:
					primeVar = 0
		return primeVar

	elif digits > 3:
		for divider in range(2, int(num/10)):
			if num % divider == 0:
				primeVar = 0
		for i in range(2,11):
			for divider in range(int((i-1)*num/10), int(i*num/10)):
				if num % divider == 0:
					primeVar = 0
		return primeVar

	else:
		for divider in range(2,num):
			if num % divider == 0:
				primeVar = 0
		return primeVar

def Mod2Vis(num):
	if Modulo2(num) == 0:
		return " "
	else:
		return "X"

def Mod3Vis(num):
	if Modulo3(num) == 0:
		return " "
	elif Modulo3(num) == 1:
		return "X"
	else:
		return "O"

def PrimeVis(num):
	if IsPrime(num) == 0:
		return "_"
	else:
		return "X"



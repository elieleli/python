def fatorial(n):
	fat = 1
	i = 1
	while i <= n:
		fat*= i
		i += 1
	return fat

def reverso (lst):
	revers = []
	for x in lst:
		revers = [x] + revers
	return revers
def mesma (lst):
	mesma =[]
	for x in lst:
		mesma.append(x)
	return mesma

def par(x):
	if x%2==0:
		return True
	else:
		return False

def media(lst):
	total = 0
	divi = len(lst)
	for i in lst:
		total += i
	resultado = total/divi
	return resultado

def iguais(x,lst):
	cont = 0
	for i in lst:
		if i == x:
			cont += 1
	return cont
def identico (lst):
	lista = []
	for i in lst:
		if iguais(i,lst) > 1:
			lista.append(i)
	return lista
def duplicata(lst):
	newlst = []
	for i in lst:
		if i not in newlst:
			newlst.append(i)
	return newlst
def qsort(lst):
	leng=len(lst)
	if leng <= 1:
		return lst
	else:
		pivo = lst [0]
	menores = []
	iguais = []
	maiores = []
	for i in lst:
		if i > pivo:
			maiores.append(i)
		elif i == pivo:
			iguais.append(i)
		else:
			menores.append(i)
	return qsort(menores) + iguais + qsort(maiores)
print(qsort([1,2,3,1,5,6,3,2]))

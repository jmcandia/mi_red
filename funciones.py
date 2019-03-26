def remover_enesimo(s, n):
	#r = ""
	#for i in range(len(s)):
	#	if n != i:
	#		r = r + s[i]
	#return r
	return s[0:n] + s[n+1:len(s)]

def mostrar_estados_amigos(lista_amigos):
	for amigo in lista_amigos:
		archivo = open(amigo+".user", "r")
		for i in range(7):
			linea = archivo.readline().rstrip()
		print(amigo+":", linea)
		archivo.close()

mostrar_estados_amigos(['John Connor'])
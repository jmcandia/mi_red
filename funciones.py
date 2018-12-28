def remover_enesimo(s, n):
	#r = ""
	#for i in range(len(s)):
	#	if n != i:
	#		r = r + s[i]
	#return r
	return s[0:n] + s[n+1:len(s)]

print(remover_enesimo("Hasta Luego", 10))
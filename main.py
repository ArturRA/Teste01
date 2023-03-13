
# Verifica se o triangulo e valido
def is_triangle(a,b,c):
	if a+b>=c and b+c>=a and c+a>=b:
		return True
	else:
		return False

# Verifica qual o tipo de triangulo
def type_of_triangle(a,b,c):
	if a==b and b==c:
		print('Triangulo e equilatero.\n')
	elif a==b or b==c or a==c:
		print('Triangulo e isosceles.\n')
	else:
		print('Triangulo e escaleno\n')

if __name__ == "__main__":
	
	executar = True
	while(executar):
		# Lendo as entradas exemplo: 15;17.5;9
		entradas = input('Digite os valores de a, b e c separados por ";" e usando "." para separar a parte decimal.\n' +
						 'Exemplo: 15;17.5;9\n')
		lista_de_entradas = entradas.split(";")
		a = float(lista_de_entradas[0])
		b = float(lista_de_entradas[1])
		c = float(lista_de_entradas[2])

		if is_triangle(a,b,c):
			type_of_triangle(a,b,c)
		else:
			print('Triangulo e invalido.\n')

		while True:
			continuar = input('Deseja checar mais um triangulo? Responda sim ou nao.\n')
			if continuar == 'sim':
				executar = True
				break
			elif continuar == 'nao':
				executar = False
				print('Terminando o programa...')
				break
			else:
				print('Comando invalido.')
				continue

	
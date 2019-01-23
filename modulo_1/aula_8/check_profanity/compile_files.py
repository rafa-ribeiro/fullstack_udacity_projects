# 
# Experimento utilizando a Built-in function compile().
# 
def compile_files():
	py_file = open("./check_profanity.py")

	code_py_file = py_file.read()
	name_py_file = py_file.name

	print("Compilando... " + name_py_file)
	
	try:
		code_obj = compile(code_py_file, 'py_file', 'exec')
		exec(code_obj)
		print(name_py_file + " compilado com Sucesso!")
	except IndentationError:
		print("Erro na indentacao do script.")
	except SyntaxError:
		print("Erro ao compilar o arquivo: " + py_file.name)

	py_file.close()

compile_files()
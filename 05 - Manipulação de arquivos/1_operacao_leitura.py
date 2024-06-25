arquivo = open(
    r'C:\Users\nicol\Development\Back-End\Python\python-ai-backend-developer\05 - Manipulação de arquivos\lorem.txt',
    "r")

print(arquivo.read())  # -> Devolve o arquivo completo

# -> Devolve uma linha por vez
print(arquivo.readline())
# for linha in arquivo.readline():
# print(linha)

print(arquivo.readlines())  # -> Devolve uma lista de strings com todas as linhas do arquivo (Iterando o conteúdo)
# for linha in arquivo.readlines():
# print(linha)

# Dica
# while len(linha := arquivo.readline()):
#     print(linha)

arquivo.close()

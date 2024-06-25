arquivo = open(r"C:\Users\nicol\Development\Back-End\Python\python-ai-backend-developer\05 - Manipulação de "
               r"arquivos\teste.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n","Escrevendo","\n","um","\n","novo","\n","texto"])
arquivo.close()
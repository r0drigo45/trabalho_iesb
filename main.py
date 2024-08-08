def main():
    arquivo = open('teste.txt','r')
    texto = arquivo.read()
    split = texto.split()
    print(len(texto))


main()
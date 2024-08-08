def ler_nome_arq():
    print('insira o caminho do arquivo')
    # lendo caminho para o arquivo do stdin
    caminho = input('>> ')
    return str(caminho)

def main():
    caminho = ler_nome_arq()
    arquivo = open(caminho,'r')
    texto = arquivo.read()
    # split sem argumentos usa whitespace como separador
    # e quebra todas as ocorrências em uma lista de strings
    split = texto.split()
    print(len(split))


main()
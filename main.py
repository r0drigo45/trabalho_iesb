def ler_nome_arq():
    print('insira o caminho do arquivo')
    # lendo caminho para o arquivo do stdin
    caminho = input('>> ')
    return str(caminho)

def main():
    caminho = ler_nome_arq()
    try:
        arquivo = open(caminho,'r')
    except:
        print(f"Caminho inválido '{caminho}'")
        return
    
    try:
        # le o conteudo do arquivo como str
        texto = arquivo.read()
    except:
        print(f'Falha ao ler o arquivo {arquivo.name}')
        return
    # split sem argumentos usa whitespace como separador
    # e quebra todas as ocorrências em uma lista de strings
    split = texto.split()
    print(len(split))


main()
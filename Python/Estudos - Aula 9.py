

def escrever_arquivo(texto):
    arquivo = open('estudos.txt', mode='w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, mode='a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, mode='r')
    texto = arquivo.read()
    print(texto)

def media_alunos(nome_arquivo):
    arquivo = open(nome_arquivo, mode='r')
    aluno_nota = arquivo.read()
    # Aqui estamos separando nossa string em uma lista
    # Nesse caso, estamos pegando o documento e colocando cada linha em uma
    # posição de uma lista
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)

    #Vamos criar uma lista para armazenar os valores da média das notas
    lista_media = []
    lista_notas = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #Aqui estamos separando o nome das notas e usando o
        # método .pop para remove o elemento na posição especificada

        media = lambda notas: sum([int(i) for i in notas]) / 4
        # aqui estamos usando a função lambda para somar os elementos de nossa lista
        lista_media.append({aluno:media(lista_notas)})

    print(lista_media)

    return lista_notas



if __name__ == '__main__':
    #escrever_arquivo('Rafael, 10, 9, 8 ,7\n')
    #atualizar_arquivo('estudos.txt','Bruno, 6, 5, 10 ,7\n')
    #ler_arquivo('estudos.txt')
    #media_alunos('estudos.txt')
    lista_media = media_alunos('estudos.txt')



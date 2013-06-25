# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


refeicaoReg = namedtuple("refeicaoReg", "id, descricao")
listarefeicao = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listarefeicao)):
        if listarefeicao[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_refeicao():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual é o nome da ementa? ")
    
    registo = refeicaoReg(cod, nome)
    listarefeicao.append(registo)


def pesquisar_refeicao():
    cod = input("Qual é a ementa que deseja pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhuma ementa referente a esse código"
        return

    print "Código: ", listarefeicao[pos].id
    print "Nome: ", listarefeicao[pos].nome
    


def listar_refeicao():
    for i in range (len(listarefeicao)):
        print "Código: ", listarefeicao[i].id
        print "Nome: ", listarefeicao[i].nome
        
  

def eliminar_aluno():
    cod = input ("Código da ementa a eliminar--> ")
    pos = encontrar_posicao(cod)

    if pos == -1: 
        print "Não existe nenhuma ementa com esse codigo"
        return

    # TODO: Confirmar eliminação
    listarefeicao.pop(pos)


    
def alterar_aluno():
    cod = input ("Código do aluno a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    listaAlunos[pos] = listaAlunos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.alunos()

        if op == '1':
            inserir_aluno()
        elif op =='2':
            listar_alunos()
        elif op == '3':
            pesquisar_aluno()
        elif op == '4':
            alterar_aluno()
        elif op == '5':
            eliminar_aluno()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"











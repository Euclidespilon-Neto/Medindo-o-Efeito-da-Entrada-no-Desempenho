class No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


def inserir(raiz, chave):
    if raiz is None:
        return No(chave)

    atual = raiz

    while True:
        if chave < atual.chave:
            if atual.esq is None:
                atual.esq = No(chave)
                break
            atual = atual.esq

        elif chave > atual.chave:
            if atual.dir is None:
                atual.dir = No(chave)
                break
            atual = atual.dir

        else:
            break

    return raiz


def buscar(raiz, chave):
    """
    Retorna True se a chave existir.
    """
    no = raiz

    while no:
        if chave == no.chave:
            return True

        if chave < no.chave:
            no = no.esq
        else:
            no = no.dir

    return False


def altura(raiz):
    if raiz is None:
        return 0

    fila = [(raiz, 1)]
    maior_altura = 0

    while fila:
        no, nivel = fila.pop()

        if nivel > maior_altura:
            maior_altura = nivel

        if no.esq is not None:
            fila.append((no.esq, nivel + 1))

        if no.dir is not None:
            fila.append((no.dir, nivel + 1))

    return maior_altura


def em_ordem(raiz, saida=None):
    """
    Retorna as chaves em ordem crescente.
    """
    saida = [] if saida is None else saida

    if raiz:
        em_ordem(raiz.esq, saida)
        saida.append(raiz.chave)
        em_ordem(raiz.dir, saida)

    return saida
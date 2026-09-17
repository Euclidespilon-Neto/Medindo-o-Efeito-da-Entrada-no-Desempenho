class No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


def inserir(raiz, chave):
    """
    Insere uma chave na BST.
    Não permite duplicatas.
    """
    if raiz is None:
        return No(chave)

    if chave < raiz.chave:
        raiz.esq = inserir(raiz.esq, chave)

    elif chave > raiz.chave:
        raiz.dir = inserir(raiz.dir, chave)

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
    """
    Calcula a altura da árvore.
    """
    if raiz is None:
        return 0

    return 1 + max(
        altura(raiz.esq),
        altura(raiz.dir)
    )


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
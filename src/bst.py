class No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


def inserir(raiz, chave):
    if raiz is None:
        return No(chave)

    if chave < raiz.chave:
        raiz.esq = inserir(raiz.esq, chave)

    elif chave > raiz.chave:
        raiz.dir = inserir(raiz.dir, chave)

    return raiz


def buscar(raiz, chave):
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

    return 1 + max(
        altura(raiz.esq),
        altura(raiz.dir)
    )
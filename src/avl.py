class No:
    __slots__ = ('chave', 'esq', 'dir', 'altura')

    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None
        self.altura = 1


def altura(no):
 
    return no.altura if no else 0


def atualizar_altura(no):
 
    no.altura = 1 + max(
        altura(no.esq),
        altura(no.dir)
    )


def fator(no):
 
    if no is None:
        return 0

    return altura(no.esq) - altura(no.dir)


def rotacao_direita(y):

    x = y.esq
    B = x.dir

    x.dir = y
    y.esq = B

    atualizar_altura(y)
    atualizar_altura(x)

    return x


def rotacao_esquerda(x):
    
    y = x.dir
    B = y.esq

    y.esq = x
    x.dir = B

    atualizar_altura(x)
    atualizar_altura(y)

    return y


def equilibrar(no):

    atualizar_altura(no)

    f = fator(no)

    if f > 1 and fator(no.esq) >= 0:
        return rotacao_direita(no)

    if f < -1 and fator(no.dir) <= 0:
        return rotacao_esquerda(no)

    if f > 1 and fator(no.esq) < 0:
        no.esq = rotacao_esquerda(no.esq)
        return rotacao_direita(no)

    if f < -1 and fator(no.dir) > 0:
        no.dir = rotacao_direita(no.dir)
        return rotacao_esquerda(no)

    return no


def inserir(raiz, chave):

    if raiz is None:
        return No(chave)

    if chave < raiz.chave:
        raiz.esq = inserir(raiz.esq, chave)

    elif chave > raiz.chave:
        raiz.dir = inserir(raiz.dir, chave)

    else:
        return raiz

    return equilibrar(raiz)


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


def em_ordem(raiz, saida=None):
    saida = [] if saida is None else saida

    if raiz:
        em_ordem(raiz.esq, saida)
        saida.append(raiz.chave)
        em_ordem(raiz.dir, saida)

    return saida
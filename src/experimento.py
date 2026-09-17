import random
from pathlib import Path
import time
import csv

import bst
import avl


TAMANHOS = [100, 300, 600, 900]


def construir_bst(valores):
    raiz = None

    inicio = time.perf_counter()

    for valor in valores:
        raiz = bst.inserir(raiz, valor)

    fim = time.perf_counter()

    return raiz, fim - inicio


def construir_avl(valores):
    raiz = None

    inicio = time.perf_counter()

    for valor in valores:
        raiz = avl.inserir(raiz, valor)

    fim = time.perf_counter()

    return raiz, fim - inicio


def medir_buscas(modulo, raiz, valores):
    inicio = time.perf_counter()

    for valor in valores:
        modulo.buscar(raiz, valor)

    fim = time.perf_counter()

    return fim - inicio


resultados = []


for n in TAMANHOS:

    # -----------------------------
    # ENTRADA ORDENADA
    # -----------------------------

    valores = list(range(n))

    raiz_bst, tempo_bst = construir_bst(valores)
    raiz_avl, tempo_avl = construir_avl(valores)

    resultados.append([
        "BST",
        "ordenada",
        n,
        bst.altura(raiz_bst),
        tempo_bst,
        medir_buscas(bst, raiz_bst, valores)
    ])

    resultados.append([
        "AVL",
        "ordenada",
        n,
        avl.altura(raiz_avl),
        tempo_avl,
        medir_buscas(avl, raiz_avl, valores)
    ])


    
    # -------------------------- ENTRADA ALEATÓRIA --------------------------
    

    valores = list(range(n))
    random.shuffle(valores)

    raiz_bst, tempo_bst = construir_bst(valores)
    raiz_avl, tempo_avl = construir_avl(valores)

    resultados.append([
        "BST",
        "aleatoria",
        n,
        bst.altura(raiz_bst),
        tempo_bst,
        medir_buscas(bst, raiz_bst, valores)
    ])

    resultados.append([
        "AVL",
        "aleatoria",
        n,
        avl.altura(raiz_avl),
        tempo_avl,
        medir_buscas(avl, raiz_avl, valores)
    ])

PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_DADOS = PASTA_PROJETO / "dados"

PASTA_DADOS.mkdir(exist_ok=True)

ARQUIVO_RESULTADOS = PASTA_DADOS / "resultados.csv"

with open(
    ARQUIVO_RESULTADOS,
    "w",
    newline="",
    encoding="utf-8"
) as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow([
        "estrutura",
        "entrada",
        "n",
        "altura",
        "tempo_construcao",
        "tempo_buscas"
    ])

    escritor.writerows(resultados)
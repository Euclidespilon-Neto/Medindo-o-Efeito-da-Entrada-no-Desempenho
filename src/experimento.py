import random
from pathlib import Path
import time
import csv

import bst
import avl


TAMANHOS = [2000, 4000, 8000, 16000, 32000]


PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_DADOS.mkdir(exist_ok=True)

ARQUIVO_RESULTADOS = PASTA_DADOS / "resultados.csv"


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


# Cria o arquivo e escreve o cabeçalho
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


# Executa os testes
for n in TAMANHOS:

    print(f"\n======================")
    print(f"Testando n = {n}")
    print(f"======================")

    # -------------------------
    # ENTRADA ORDENADA
    # -------------------------

    valores = list(range(n))

    print("BST ordenada...")
    raiz_bst, tempo_bst = construir_bst(valores)

    print("AVL ordenada...")
    raiz_avl, tempo_avl = construir_avl(valores)

    resultado_bst = [
        "BST",
        "ordenada",
        n,
        bst.altura(raiz_bst),
        tempo_bst,
        medir_buscas(bst, raiz_bst, valores)
    ]

    resultado_avl = [
        "AVL",
        "ordenada",
        n,
        avl.altura(raiz_avl),
        tempo_avl,
        medir_buscas(avl, raiz_avl, valores)
    ]


    # grava imediatamente
    with open(
        ARQUIVO_RESULTADOS,
        "a",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(resultado_bst)
        escritor.writerow(resultado_avl)


    print("Resultados ordenados salvos.")


    # -------------------------
    # ENTRADA ALEATÓRIA
    # -------------------------

    valores = list(range(n))
    random.shuffle(valores)

    print("BST aleatória...")
    raiz_bst, tempo_bst = construir_bst(valores)

    print("AVL aleatória...")
    raiz_avl, tempo_avl = construir_avl(valores)

    resultado_bst = [
        "BST",
        "aleatoria",
        n,
        bst.altura(raiz_bst),
        tempo_bst,
        medir_buscas(bst, raiz_bst, valores)
    ]

    resultado_avl = [
        "AVL",
        "aleatoria",
        n,
        avl.altura(raiz_avl),
        tempo_avl,
        medir_buscas(avl, raiz_avl, valores)
    ]


    with open(
        ARQUIVO_RESULTADOS,
        "a",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(resultado_bst)
        escritor.writerow(resultado_avl)


    print("Resultados aleatórios salvos.")


print("\nExperimento concluído.")
print(f"Arquivo salvo em:")
print(ARQUIVO_RESULTADOS)
import csv
from pathlib import Path

import matplotlib.pyplot as plt


PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_RESULTADOS = PASTA_PROJETO / "dados" / "resultados.csv"
PASTA_GRAFICOS = PASTA_PROJETO / "graficos"
PASTA_GRAFICOS.mkdir(exist_ok=True)


def ler_resultados():
    dados = []
    with open(ARQUIVO_RESULTADOS, encoding="utf-8", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            dados.append({
                "estrutura": linha["estrutura"],
                "entrada": linha["entrada"],
                "n": int(linha["n"]),
                "tempo": float(linha["tempo_mediano"]),
            })
    return dados


def main():
    dados = ler_resultados()

    plt.figure(figsize=(10, 6))

    for estrutura, entrada in (
        ("BST", "ordenada"),
        ("BST", "aleatoria"),
        ("AVL", "ordenada"),
        ("AVL", "aleatoria"),
    ):
        serie = [
            item for item in dados
            if item["estrutura"] == estrutura and item["entrada"] == entrada
        ]
        serie.sort(key=lambda item: item["n"])

        plt.plot(
            [item["n"] for item in serie],
            [item["tempo"] for item in serie],
            marker="o",
            label=f"{estrutura} - {entrada}",
        )

    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel("Tempo mediano de construção (s)")
    plt.title("BST x AVL — entrada ordenada e aleatória")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", alpha=0.35)
    plt.legend()
    plt.tight_layout()
    plt.savefig(PASTA_GRAFICOS / "comparacao_bst_avl.png", dpi=180)
    plt.close()

    print(f"Gráfico salvo em: {PASTA_GRAFICOS / 'comparacao_bst_avl.png'}")


if __name__ == "__main__":
    main()

# Medindo-o-Efeito-da-Entrada-no-Desempenho
Alunos: Euclides &amp; Gabriela


# Comparação entre BST simples e AVL

## Integrantes

- Gabriela de Araújo Reis
- Euclides Carlos Pilon Neto

## O que investigamos

Este trabalho compara o comportamento de uma árvore binária de busca
simples (BST) com uma árvore AVL.

O objetivo é verificar como a ordem de inserção dos dados influencia
a altura da árvore e o tempo necessário para realizar operações.

Foram utilizadas entradas:

- em ordem crescente;
- em ordem aleatória.

Foram testados diferentes tamanhos de entrada.

## Hipótese

Esperamos que a BST apresente bom desempenho quando os dados forem
inseridos em ordem aleatória, mas apresente pior desempenho quando os
dados forem inseridos em ordem crescente.

Esperamos que a AVL mantenha comportamento mais estável, pois realiza
rotações para manter a árvore balanceada.

## Experimento

Para cada tamanho de entrada:

1. criamos uma BST simples;
2. criamos uma AVL;
3. inserimos as mesmas chaves nas duas estruturas;
4. medimos o tempo de construção;
5. medimos a altura final;
6. realizamos buscas;
7. registramos os resultados.

## Resultados

Os resultados completos estão disponíveis em:

dados/resultados.csv

Os gráficos gerados estão na pasta:

graficos/

## Conclusão

[Preencher depois das medições.]

## Como executar

Execute:

python src/experimento.py

Os resultados serão exibidos no terminal e gravados na pasta dados/.

# DIÁRIO DO EXPERIMENTO

## Objetivo

Comparar uma BST simples e uma AVL e medir como a ordem de entrada altera o tempo necessário para construir cada estrutura.

A análise final utiliza entrada ordenada e aleatória, cinco tamanhos que dobram a cada passo, três execuções válidas por ponto, mediana, descarte de uma execução inicial de aquecimento e semente fixa.

## O que esperávamos antes de medir

Antes dos testes, esperávamos que a BST simples tivesse bom comportamento com entradas aleatórias, mas sofresse com entradas ordenadas. A hipótese era que chaves em ordem crescente fariam a árvore crescer apenas para a direita e aumentar sua altura junto com `n`.

Para a AVL, esperávamos alturas pequenas tanto com entrada ordenada quanto aleatória, porque a estrutura executa rotações para manter o balanceamento.

Também esperávamos que a AVL pudesse ser mais lenta que uma BST que já estivesse em boa forma, pois precisa atualizar alturas, verificar o fator de balanceamento e eventualmente realizar rotações.

## Etapas, erros e intercorrências

### 1. Primeiros testes com entradas pequenas

As primeiras medições utilizavam tamanhos pequenos e vários tempos ficavam próximos de zero. Isso dificultava separar o crescimento real do ruído de medição.

**Ajuste:** passamos a trabalhar com tamanhos que dobram entre si e com valores maiores, para analisar principalmente `T(2n) / T(n)` em vez de olhar apenas para segundos absolutos.

### 2. Problema ao criar o CSV

Em uma das primeiras versões ocorreu uma falha na chamada `with open(...)` usada para escrever `resultados.csv`. O caminho dependia da pasta em que o terminal estava aberto.

**Correção:** o caminho passou a ser calculado a partir do próprio `experimento.py` usando `Path(__file__).resolve().parent.parent`. A pasta `dados/` também passou a ser criada automaticamente.

### 3. `RecursionError` na BST

A primeira implementação da inserção da BST era recursiva. Ao testar milhares de elementos ordenados, ocorreu:

```text
RecursionError: maximum recursion depth exceeded
```

A entrada ordenada havia transformado a BST em um caminho muito profundo. O problema não indicava que a regra da BST estava incorreta; a implementação recursiva esbarrou no limite de recursão do Python justamente porque a estrutura degenerou.

**Correção:** a inserção da BST foi reescrita de forma iterativa, mantendo a mesma regra de ordenação. A função usada para obter a altura da BST também foi tornada iterativa para evitar o mesmo limite durante a medição.

### 4. Tentativa com tamanhos excessivamente grandes

Foi testada a sequência:

```python
[4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000]
```

Depois de eliminar o `RecursionError`, a BST ordenada passou a executar, mas os tamanhos maiores tornaram a execução excessivamente longa. Uma execução foi interrompida e gerou:

```text
KeyboardInterrupt
```

**Conclusão dessa tentativa:** trocar recursão por iteração elimina o limite da pilha, mas não elimina o custo algorítmico de uma BST degenerada.

### 5. CSV aparentemente vazio durante a execução

Em uma versão anterior, o arquivo só era preenchido ao final de todos os testes. Como alguns pontos demoravam bastante, parecia que nada estava sendo gravado.

**Correção:** os resultados passaram a ser salvos progressivamente. Assim, cada ponto concluído já fica registrado em disco.

### 6. Primeira rodada completa ainda não seguia todo o protocolo

Uma rodada intermediária utilizou apenas quatro tamanhos:

```python
[4000, 8000, 16000, 32000]
```

Além disso, cada ponto era medido apenas uma vez e `random.shuffle()` era usado sem semente fixa.

Ao revisar o enunciado completo, percebemos que a atividade exigia explicitamente:

- cinco tamanhos dobrando;
- três execuções por ponto;
- mediana;
- descarte da primeira execução;
- semente fixa.

Essa rodada intermediária foi mantida apenas como parte do processo de desenvolvimento e **não é a rodada usada na análise final**.

### 7. Protocolo final corrigido

A versão definitiva passou a usar:

```python
TAMANHOS = [1000, 2000, 4000, 8000, 16000]
EXECUCOES_VALIDAS = 3
SEMENTE = 42
```

Para cada combinação de tamanho, estrutura e cenário:

1. uma execução é feita como aquecimento e descartada da análise;
2. são realizadas três execuções válidas;
3. a mediana dessas três execuções é calculada;
4. a mediana é salva em `dados/resultados.csv`;
5. todas as medições individuais são registradas em `dados/medicoes.csv` para conferência;
6. a razão `T(2n) / T(n)` é calculada usando as medianas.

A entrada aleatória é produzida com uma semente fixa (`42`), tornando a sequência reproduzível. Para um mesmo `n`, BST e AVL recebem exatamente a mesma ordem de chaves.

## O que encontramos na rodada final

### BST ordenada

As alturas foram:

```text
1000, 2000, 4000, 8000, 16000
```

ou seja, exatamente iguais a `n`.

As razões do tempo mediano foram:

```text
3,656×
4,055×
3,917×
4,086×
```

O valor ficou consistentemente próximo de `4×`, compatível com crescimento quadrático para a construção completa.

### BST aleatória

As alturas foram:

```text
21, 24, 26, 36, 33
```

As razões foram:

```text
2,325×
2,045×
2,456×
2,215×
```

A mudança em relação à BST ordenada foi grande: a altura deixou de acompanhar `n` e o crescimento ficou pouco acima de `2×` quando `n` dobrou, compatível com o caso médio `n log n` para a construção.

### AVL ordenada

As alturas ficaram em:

```text
10, 11, 12, 13, 14
```

As razões foram:

```text
2,101×
2,203×
2,263×
2,079×
```

A ordem crescente praticamente não afetou a altura porque o balanceamento corrigiu a estrutura durante as inserções.

### AVL aleatória

As alturas foram:

```text
12, 13, 14, 16, 17
```

As razões foram:

```text
2,227×
2,222×
2,250×
2,072×
```

O padrão foi semelhante ao cenário ordenado, novamente compatível com `n log n` para a construção completa.

## Observações finais

O processo mostrou por que o protocolo de medição é importante. Uma única execução pode sofrer ruído; por isso a rodada final usa três medições válidas e mediana. Uma entrada aleatória sem semente fixa dificulta reproduzir a experiência; por isso a versão final usa semente `42`.

Os erros encontrados também ajudaram a entender a própria estrutura estudada. O `RecursionError` e a lentidão que levou ao `KeyboardInterrupt` não foram problemas aleatórios: ambos apareceram porque a BST ordenada se tornou extremamente profunda.

O gráfico final e a tabela do README utilizam somente os dados da rodada que atende integralmente ao protocolo final da atividade.

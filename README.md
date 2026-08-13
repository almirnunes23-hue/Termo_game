# 🤖 Bot para o Termo

Bot desenvolvido em **Python** para automatizar partidas do
[Termo](https://term.ooo), utilizando **Selenium** para interagir com o
navegador e uma base de palavras para encontrar possíveis soluções.

## 📌 Como funciona

A cada tentativa, o programa:

1.  Escolhe uma palavra da lista de palavras disponíveis.
2.  Envia a palavra para o Termo através do Selenium.
3.  Lê o estado de cada letra no tabuleiro.
4.  Armazena as informações em uma base de conhecimento.
5.  Filtra a lista de palavras de acordo com as informações descobertas.
6.  Escolhe uma nova palavra entre as candidatas restantes.
7.  Repete o processo.

## 🧠 Base de conhecimento

O bot mantém informações sobre cada letra do alfabeto em um dicionário
chamado `uberdict`.

Cada letra possui:

``` python
{
    "certas": set(),
    "erradas": set(),
    "repeticoes": 0
}
```

-   **`certas`**: posições nas quais a letra foi confirmada.
-   **`erradas`**: posições nas quais a letra não pode aparecer.
-   **`repeticoes`**: quantidade mínima conhecida de ocorrências da
    letra.

O uso de `set()` permite armazenar posições sem duplicá-las.

## 🔎 Filtragem

Depois de cada tentativa, o programa filtra a lista de palavras,
eliminando candidatas que contradizem as informações descobertas.

São consideradas informações como:

-   posição correta de uma letra;
-   posições nas quais uma letra não pode aparecer;
-   quantidade mínima de ocorrências de uma letra;
-   letras que não aparecem na palavra.

Exemplo:

``` python
palavras = [
    p for p in palavras
    if p[pos] == letra
]
```

Para verificar a quantidade de ocorrências:

``` python
palavras = [
    p for p in palavras
    if p.count(letra) >= repeticoes
]
```

## 🛠️ Tecnologias utilizadas

-   Python
-   Selenium
-   Chrome / ChromeDriver
-   `random`
-   `unicodedata`
-   `string`

## 📂 Estrutura sugerida

``` text
termo-bot/
│
├── termo_bot.py
├── palavras com 5 letras.txt
├── README.md
├── .gitignore
└── requirements.txt
```

## ⚙️ Instalação

Clone o repositório:

``` bash
git clone URL_DO_SEU_REPOSITORIO
cd termo-bot
```

Instale as dependências:

``` bash
pip install selenium
```

Execute o programa:

``` bash
python termo_bot.py
```

## ⚠️ Observações

O projeto depende da estrutura HTML interna do site do Termo e utiliza
**Shadow DOM** para acessar o tabuleiro.

Por isso, alterações na estrutura do site podem exigir alterações no
código.

A qualidade da filtragem também depende da lista de palavras utilizada
como base.

## 🚧 Estado do projeto

Projeto em desenvolvimento.

Uma das partes centrais do projeto é a lógica de filtragem e a
construção da base de conhecimento, especialmente para situações
envolvendo **letras repetidas com resultados diferentes**.

## 📚 Objetivo

Este projeto também serve como estudo de:

-   automação de navegador;
-   Selenium e Shadow DOM;
-   estruturas de dados em Python;
-   dicionários e conjuntos (`dict` e `set`);
-   filtragem de listas;
-   construção de uma base de conhecimento;
-   tratamento lógico de informações incompletas;
-   resolução de problemas por restrições.

------------------------------------------------------------------------

**Autor:** Almir Nunes\
**Linguagem:** Python

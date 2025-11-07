# Fashion Stock

Fashion Stock é um sistema para gerenciamento de estoque de moda, desenvolvido em Python com Streamlit para interface web, utilizando SQLite3 como banco de dados. A modelagem de dados foi elaborada com auxílio do draw.io e o protótipo da interface foi desenhado no Figma.

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Modelagem de Dados](#modelagem-de-dados)
- [Protótipos](#protótipos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Utilizar](#como-utilizar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuições](#contribuições)
- [Licença](#licença)

---

## Visão Geral

Fashion Stock ajuda pequenas lojas ou marcas independentes de moda a organizarem seus estoques, cadastro de produtos, movimentações e relatórios, tudo via uma interface web amigável.

## Funcionalidades

- Cadastro e edição de produtos (roupas, acessórios, etc.)
- Controle de entradas e saídas do estoque
- Visualização e geração de relatórios
- Busca e filtragem avançada
- Interface intuitiva baseada em protótipos do Figma

## Modelagem de Dados

A estrutura do banco de dados foi projetada no [draw.io](https://app.diagrams.net/), facilitando o entendimento das entidades e das relações:

![Modelagem de Dados - Draw.io](docs/modelagem-dados.png)

- **Produto:** código, nome, descrição, categoria, tamanho, cor, quantidade, preço
- **Movimentação:** entrada ou saída, quantidade, data, usuário responsável
- **Usuário:** controle de acesso e registro de ações

> O arquivo da modelagem pode ser encontrado em `docs/modelagem-dados.drawio`.

## Protótipos

O layout e navegação do Fashion Stock foram desenhados no Figma garantindo uma experiência de usuário consistente:

- ![Tela Inicial](docs/tela-inicial.png)
- ![Cadastro de Produto](docs/cadastro-produto.png)
- ![Movimentação de Estoque](docs/movimentacao-estoque.png)

Os arquivos dos protótipos estão disponíveis em `docs/`.

## Tecnologias Utilizadas

- **Python**: Lógica do backend e integração com o banco de dados.
- **Streamlit**: Framework para produção da interface web interativa.
- **SQLite3**: Banco de dados leve e eficiente.
- **Draw.io**: Modelagem visual de dados.
- **Figma**: Protótipo de telas e fluxos do usuário.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/arthurresendes/fashion_stock.git
   cd fashion_stock
   ```

2. (Recomendado) Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Como Utilizar

Execute a aplicação web com Streamlit:

```bash
streamlit run app.py
```

Acesse pelo navegador o endereço sugerido (http://localhost:8501).

O banco SQLite3 será utilizado automaticamente, e os dados ficarão registrados na pasta local.


## Contribuições

Sinta-se livre para abrir issues e pull requests com melhorias, reportar bugs, ou sugerir novas funcionalidades!

1. Fork o projeto
2. Crie sua branch (`git checkout -b minha-melhor-branch`)
3. Commit suas alterações
4. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT.

---

**Autor:** [Arthur Resendes](https://github.com/arthurresendes)

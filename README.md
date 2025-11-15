# Fashion Stock

## Visão Geral

O Fashion Stock é um sistema web para controle e gerenciamento de estoque de roupas, focado no varejo de moda. Foi desenvolvido em Python, utilizando o framework Streamlit para a interface, e SQLite para o banco de dados.

---

## Estrutura do Projeto

- **Programa/**  
  Scripts Python para criação de bancos, inserção de dados, login e interface principal (`main_st.py`).
- **Modelagem/**  
  Modelos de dados em diagramas e exemplos de entidades (Produto, Usuário).
- **Documentação/**  
  Arquivos explicativos, RF , RNFs , modelagen.

---

## Funcionalidades

1. **Autenticação de Usuário**
   - Cadastro e login com senha criptografada (token aleatório).
   - Armazenamento seguro no SQLite.

2. **Cadastro de Produtos**
   - Formulário para inserir dados detalhados.
   - Tipos, marcas, tamanhos, cores, gênero, preço, quantidade, promoção e descrição.

3. **Atualização de Produtos**
   - Interface para atualizar preço ou outras informações.

4. **Consulta de Produtos**
   - Busca por nome, tipo ou outros atributos.
   - Resultados apresentados na tela.

5. **Navegação Amigável**
   - Menu lateral com opções para cada funcionalidade.

---

## Fluxo do Usuário

1. Usuário acessa o sistema.
2. Realiza login.
3. Escolhe a ação desejada via menu lateral.
4. Preenche ou consulta formulários.
5. Encerra sessão de forma segura.

---

## Banco de Dados

- **Usuário:** id_user, nome, senha
- **Produto:** id_prod, tipo, marca, tamanho, cor, gênero, preço_unitario, quantidade, promocao, descricao

Scripts para criação de tabelas e inserção de dados estão em `Programa/`.

---

## Instruções de Uso

1. Instalar dependências com `pip install streamlit`.
2. Executar scripts para criar bancos e usuários.
3. Rodar o sistema principal com `streamlit run Programa/main_st.py`.

---

## Protótipo Visual — Figma

- **Tela de Login:**  
  Campos para nome e senha, botão de entrar, feedback visual de erro ou sucesso.

- **Menu Lateral:**  
  Ícones para Cadastro, Atualizar, Consultar e Sair. Aparência moderna e responsiva.

- **Cadastro de Produto:**  
  Formulários com campos suspensos e validações. Layout limpo, botões de confirmação.

- **Consulta de Produtos:**  
  Barra de busca, caixa de resultado em lista ou tabela.

- **Atualização de Produto:**  
  Seleção do produto, campo para novo preço ou atributo, botão de atualização.

---

## Contribuições

Este projeto foi desenvolvido pensando em grandes problemas em gestão de estoque.  
Interessados em integrar, ampliar ou adquirir podem entrar em contato para customização ou negociação.

---

**Equipe Fashion Stock**  
[Seu contato ou LinkedIn]

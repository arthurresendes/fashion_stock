import streamlit as st
from selecionando_users_login import lista_usuarios
from querys import cadastrar_prod

def login():
    st.title("Tela de Login Fashion-Stock")

    nome = st.text_input("Digite seu nome:")
    senha = st.text_input("Digite sua senha:", type="password")
    submit = st.button("Entrar")

    if submit:
        informacoes = (nome, senha)
        lista_users_permitidos = lista_usuarios()

        if informacoes in lista_users_permitidos:
            st.session_state["logado"] = True
            st.session_state["pagina"] = "Menu"
            st.rerun()
        else:
            st.warning("Login não permitido")

def menu_principal():

    st.sidebar.title("📋 Menu de Navegação")
    pagina = st.sidebar.radio(
        "Escolha uma opção:",
        ["Menu","📦 Cadastro", "✏️ Atualizar", "🔍 Selecionar"]
    )
    st.session_state["pagina"] = pagina

    if pagina == "Menu":
        st.header("Menu Fashion-Stock")
        st.subheader("Informações sobre o site")
        st.write("  O fashion stock foi criado com um proposito, muitos sistemas de estoque no varejo de roupas não tem um controle necessário e eficiente das roupas que são armazenadas nas suas lojas, sendo assim podendo gerar menos lucros e mais dor de cabeça, visto isso o fashion stock traz uma solução onde por meio de um sistema web com formulários todas as informações de roupas irão vir de um banco de dados.")

    elif pagina == "📦 Cadastro":
        st.header("Cadastro de Produtos")
        st.write("Aqui você pode cadastrar novas roupas no estoque.")
        tipo = st.selectbox("Tipo", ["Camisa", "Calça", "Vestido", "Jaqueta"])
        marca = st.text_input("Marca:")
        cor = st.text_input("Cor:")
        tamanho = st.selectbox("Tamanho", ["P", "M", "G", "GG"])
        genero = st.selectbox("Gênero", ["M","F","AMBOS"])
        preco = st.number_input("Preço (R$):", min_value=0.0, step=0.1)
        quantidade = st.number_input("Quantidade:")
        descricao = st.text_area("Descrição:")
        if st.button("Cadastrar"):
            try:
                cadastrar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao)
                st.success("Produto cadastrado com sucesso")
            except:
                st.warning("Erro ao cadastrar, preencha todos os campos corretamente")

    elif pagina == "✏️ Atualizar":
        st.header("Atualizar Produto")
        st.write("Aqui você pode atualizar informações de produtos já cadastrados.")
        id_prod = st.text_input("ID do produto:")
        novo_preco = st.number_input("Novo preço (R$):", min_value=0.0, step=0.1)
        if st.button("Atualizar"):
            st.info(f"Preço do produto {id_prod} atualizado para R$ {novo_preco}!")

    elif pagina == "🔍 Selecionar":
        st.header("Consultar Produtos")
        st.write("Aqui você pode visualizar informações de produtos cadastrados.")
        busca = st.text_input("Buscar por nome ou tipo:")
        if st.button("Pesquisar"):
            st.success(f"Resultados da busca por '{busca}' apareceriam aqui.")

        
    if st.button("Sair"):
        st.session_state["logado"] = False
        st.rerun()

if "logado" not in st.session_state:
    st.session_state["logado"] = False

if st.session_state["logado"]:
    menu_principal()
else:
    login()
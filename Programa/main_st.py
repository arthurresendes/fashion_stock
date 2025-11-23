import streamlit as st
from selecionando_users_login import lista_usuarios
from querys import cadastrar_prod, selecao_marca,selecao_cor,atualizar_prod,selecao

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

    st.sidebar.title("Menu de Navegação")
    pagina = st.sidebar.radio(
        "Escolha uma opção:",
        ["Menu","Cadastro", "Atualizar", "Selecionar"]
    )
    st.session_state["pagina"] = pagina

    if pagina == "Menu":
        st.header("Menu Fashion-Stock")
        st.subheader("Informações sobre o site")
        st.write("  O fashion stock foi criado com um proposito, muitos sistemas de estoque no varejo de roupas não tem um controle necessário e eficiente das roupas que são armazenadas nas suas lojas, sendo assim podendo gerar menos lucros e mais dor de cabeça, visto isso o fashion stock traz uma solução onde por meio de um sistema web com formulários todas as informações de roupas irão vir de um banco de dados.")
        if st.button("Sair"):
            st.session_state["logado"] = False
            st.rerun()

    elif pagina == "Cadastro":
        st.header("Cadastro de Produtos")
        st.write("Aqui você pode cadastrar novas roupas no estoque.")
        tipo = st.selectbox("Tipo", ["Camisa", "Calça", "Vestido", "Jaqueta"])
        marca = st.text_input("Marca:")
        cor = st.text_input("Cor:")
        tamanho = st.selectbox("Tamanho", ["P", "M", "G", "GG"])
        genero = st.selectbox("Gênero", ["M","F","Unissex"])
        preco_input = st.text_input("Preço (R$):")
        quantidade_input = st.text_input("Quantidade:")
        descricao = st.text_area("Descrição:")
        
        if st.button("Cadastrar"):
            try:
                preco_input = preco_input.replace(",", ".")
                preco = float(preco_input)
                quantidade = int(quantidade_input)
                cadastrar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao)
                st.success("Produto cadastrado com sucesso")
            except:
                st.warning("Erro ao cadastrar, preencha todos os campos corretamente")

    elif pagina == "Atualizar":
        selectbox_marca = selecao_marca()
        selectbox_cor = selecao_cor()
        
        st.header("Atualizar Produto")
        tipo = st.selectbox("Tipo", ["Camisa", "Calça", "Vestido", "Jaqueta"])
        marca = st.selectbox("Marca", selectbox_marca)
        cor = st.selectbox("Cor",selectbox_cor)
        tamanho = st.selectbox("Tamanho", ["P", "M", "G", "GG"])
        genero = st.selectbox("Gênero", ["M","F","AMBOS"])
        preco_input = st.text_input("Preço (R$):")
        quantidade_input = st.text_input("Quantidade:")
        descricao = st.text_area("Descrição:")
        
        if st.button("Atualizar"):
            try:
                preco_input = preco_input.replace(",", ".")
                preco = float(preco_input)
                quantidade = int(quantidade_input)
                atualizar_prod(tipo,marca,cor,tamanho,genero,preco,quantidade,descricao)
                st.success("Produto atualizado com sucesso")
            except:
                st.warning("Erro ao atualizar, preencha todos os campos corretamente")

    elif pagina == "Selecionar":
        st.header("Consultar Produtos")
        selectbox_marca = selecao_marca()
        selectbox_cor = selecao_cor()
        
        
        st.write("Aqui você pode visualizar informações de produtos cadastrados.")
        tipo = st.selectbox("Tipo", ["Camisa", "Calça", "Vestido", "Jaqueta"])
        marca = st.selectbox("Marca", selectbox_marca)
        cor = st.selectbox("Cor",selectbox_cor)
        tamanho = st.selectbox("Tamanho", ["P", "M", "G", "GG"])
        genero = st.selectbox("Gênero", ["M","F","AMBOS"])
        
        if st.button("Selecionar"):
            try:
                df = selecao(tipo,marca,cor,tamanho,genero)
                st.download_button(
                    label="Download",
                    data=df.to_excel(index=False),
                    file_name="resultado_selecao.xlsx"
                    )
                st.success("Selecão feita com sucesso")
                
            except:
                st.warning("Erro ao selecionar, preencha todos os campos corretamente")


if "logado" not in st.session_state:
    st.session_state["logado"] = False

if st.session_state["logado"]:
    menu_principal()
else:
    login()
import streamlit as st
from io import BytesIO
from create_tables import inicializar_bancos
from querys import cadastrar_prod, selecao_marca,selecao_cor,atualizar_prod,selecao,validar_login
from dashs import grafico_tipos_qtd, grafico_menor_preco

inicializar_bancos()

def login():
    st.title("Tela de Login Fashion-Stock")

    nome = st.text_input("Digite seu nome:")
    senha = st.text_input("Digite sua senha:", type="password")
    submit = st.button("Entrar")

    if submit:
        validar_user = validar_login(nome,senha)

        if validar_user:
            st.session_state["logado"] = True
            st.session_state["pagina"] = "Menu"
            st.rerun()
        else:
            st.warning("Login não permitido")

def menu_fashion():
        st.header("Menu Fashion-Stock")
        st.subheader("Informações sobre o site")
        st.write("  O fashion stock foi criado com um proposito, muitos sistemas de estoque no varejo de roupas não tem um controle necessário e eficiente das roupas que são armazenadas nas suas lojas, sendo assim podendo gerar menos lucros e mais dor de cabeça, visto isso o fashion stock traz uma solução onde por meio de um sistema web com formulários todas as informações de roupas irão vir de um banco de dados.")
        st.subheader("Consulte dashboards do seu estoque !!")
        
        maior_quantidade_tipo = st.button("Maior quantidade por tipo em estoque")
        figura = grafico_tipos_qtd()
        if maior_quantidade_tipo:
            st.pyplot(figura)
        
        menor_preco = st.button("Produto com menor preço")
        figura2 = grafico_menor_preco()
        if menor_preco:
            st.pyplot(figura2)

def cadastrar():
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

def atualizar():
        selectbox_marca = selecao_marca()
        selectbox_cor = selecao_cor()
        
        st.header("Atualizar Produto")
        st.write("Aqui você pode atualizar roupas já existentes no estoque.")
        tipo = st.selectbox("Tipo", ["Camisa", "Calça", "Vestido", "Jaqueta"])
        marca = st.selectbox("Marca", selectbox_marca)
        cor = st.selectbox("Cor",selectbox_cor)
        tamanho = st.selectbox("Tamanho", ["P", "M", "G", "GG"])
        genero = st.selectbox("Gênero", ["M","F","Unissex"])
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

def selecionar():
        st.header("Consultar Produtos")
        selectbox_marca = selecao_marca()
        selectbox_cor = selecao_cor()
        
        
        st.write("Aqui você pode visualizar informações de produtos cadastrados.")
        tipo = st.selectbox("Tipo", ["Camisa", "Calça", "Vestido", "Jaqueta"])
        marca = st.selectbox("Marca", selectbox_marca)
        cor = st.selectbox("Cor",selectbox_cor)
        tamanho = st.selectbox("Tamanho", ["P", "M", "G", "GG"])
        genero = st.selectbox("Gênero", ["M","F","Unissex"])
        
        if st.button("Selecionar"):
            try:
                df = selecao(tipo,marca,cor,tamanho,genero)
                
                output = BytesIO()
                df.to_excel(output, index=False, sheet_name="Resultados")
                output.seek(0)
                
                st.download_button(
                    label="Download seleção em Arquivo EXCEL(xlsx)",
                    data=output,
                    file_name="resultado_selecao.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                
                st.success("Selecão feita com sucesso")
                
            except:
                st.warning("Erro ao selecionar, preencha todos os campos corretamente")

def menu_principal():
    st.sidebar.title("Menu de Navegação")
    pagina = st.sidebar.radio(
        "Escolha uma opção:",
        ["Menu","Cadastro", "Atualizar", "Selecionar", "Sair"]
    )
    st.session_state["pagina"] = pagina
    
    if pagina == "Menu":
        menu_fashion()
    elif pagina == "Cadastro":
        cadastrar()
    elif pagina == "Atualizar":
        atualizar()
    elif pagina == "Selecionar":
        selecionar()
    elif pagina == "Sair":
        st.session_state["logado"] = False
        st.rerun()
    else:
        return "Erro"


if "logado" not in st.session_state:
    st.session_state["logado"] = False

if st.session_state["logado"]:
    menu_principal()
else:
    login()
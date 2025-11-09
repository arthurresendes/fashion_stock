import streamlit as st
from Programa.selecionando_users_login import lista_usuarios

def login_screen():
    st.title("Tela de Login Fashion-Stock")

    nome = st.text_input("Digite seu nome:")
    senha = st.text_input("Digite sua senha:", type="password")
    submit = st.button("Entrar")

    if submit:
        informacoes = (nome, senha)
        lista_users_permitidos = lista_usuarios()

        if informacoes in lista_users_permitidos:
            st.session_state["logado"] = True
            st.rerun()
        else:
            st.warning("Login não permitido")

def menu_screen():
    st.title("Menu Fashion-Stock")
    st.success("Login realizado com sucesso!")
    st.write("Bem-vindo ao sistema, selecione uma opção:")

    if st.button("Sair"):
        st.session_state["logado"] = False
        st.rerun()

if "logado" not in st.session_state:
    st.session_state["logado"] = False

if st.session_state["logado"]:
    menu_screen()
else:
    login_screen()

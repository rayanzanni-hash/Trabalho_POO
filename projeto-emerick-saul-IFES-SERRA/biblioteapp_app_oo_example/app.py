import streamlit as st
import pandas as pd
from src.services import UsuarioService, ResultadoService

# Instâncias dos serviços
usuarios = UsuarioService()
resultados = ResultadoService()

# Menu lateral
menu = st.sidebar.selectbox(
    "Menu", 
    ["Cadastrar Aluno", "Cadastrar Professor", "Enviar CSV (Aluno)", "Ver Resultados (Professor)"]
)

# --- Cadastro de Aluno ---
if menu == "Cadastrar Aluno":
    st.header("Cadastrar Aluno")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    matricula = st.text_input("Matrícula")
    if st.button("Salvar"):
        usuarios.registrar_aluno(nome, email, matricula)
        st.success("Aluno cadastrado!")

# --- Cadastro de Professor ---
elif menu == "Cadastrar Professor":
    st.header("Cadastrar Professor")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    matricula = st.text_input("Matrícula do Professor")
    if st.button("Salvar"):
        usuarios.registrar_professor(nome, email, matricula)
        st.success("Professor cadastrado!")

# --- Upload de CSV pelo Aluno ---
elif menu == "Enviar CSV (Aluno)":
    st.header("Enviar CSV de Resultados")
    
    aluno_id = st.number_input("ID do Aluno", min_value=1, step=1)
    arquivo = st.file_uploader("Escolha o arquivo CSV", type=["csv"])
    
    if arquivo is not None:
        try:
            try:
                 df = pd.read_csv(arquivo, encoding="utf-8")
            except UnicodeDecodeError:
                 arquivo.seek(0)
                 df = pd.read_csv(arquivo, encoding="ISO-8859-1")

            lista_resultados = df.to_dict(orient="records")
    
            if st.button("Enviar Resultados"):
                resultados.registrar_csv(aluno_id, lista_resultados)
                st.success("Resultados enviados com sucesso!")

        except Exception as e:
            st.error(f"Erro ao processar o CSV: {e}")

# --- Consulta de resultados para Professor ---
elif menu == "Ver Resultados (Professor)":
    st.header("Resultados dos Alunos")
    
    dados = resultados.repo.get_by_professor()
    
    for r in dados:
        resultado_id, aluno_id, nome_dp, tempo, valor, processado, comentario = r
        
        aluno = usuarios.repo.get(aluno_id)
        nome_aluno = aluno.nome if aluno else "Aluno não encontrado"
        
        st.write(f"*Aluno:* {nome_aluno} (ID: {aluno_id})")
        st.write(f"Data Point: {nome_dp}")
        st.write(f"Tempo: {tempo}")
        st.write(f"Valor: {valor}")
        st.write(f"Processado: {processado}")
        st.write(f"Comentário: {comentario}")
        st.markdown("---")

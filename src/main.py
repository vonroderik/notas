import csv
import os
import streamlit as st

# Dicionário para armazenar os alunos
alunos = {}

# Caminho do arquivo CSV
caminho_arquivo = os.path.join(os.path.dirname(__file__), "..", "data", "notas.csv")

# Carregando os dados do CSV
with open(caminho_arquivo, encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        ra = int(row["RA"])
        alunos[ra] = {
            "Registro Acadêmico": ra,
            "Vivência 1": row["vivencia1"],
            "Vivência 2": row["vivencia2"],
            "Vivência 3": row["vivencia3"],
            "Prova Prática": row["prova_pratica"],
            "Total": row["total"]  # Soma das notas
        }

# Interface com Streamlit
st.title("Consulta de Notas dos Alunos")
st.write("Digite seu Registro Acadêmico para verificar suas notas:")

# Entrada do usuário para o RA
identificacao = st.text_input("Registro Acadêmico (RA)", "").strip()

# Verifica se o RA foi digitado
if identificacao:
    try:
        identificacao = int(identificacao)
        aluno_encontrado = alunos.get(identificacao)

        if aluno_encontrado:
            aluno_encontrado["Registro Acadêmico"] = str(aluno_encontrado["Registro Acadêmico"])
            st.success("Dados do aluno encontrados!")
            st.table(aluno_encontrado)  # Exibe em formato de tabela
        else:
            st.error("RA não encontrado.")
    except ValueError:
        st.error("Por favor digite apenas números.")
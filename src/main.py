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
        ra = int(row["ra"])
        alunos[ra] = {
            "Registro Acadêmico": ra,
            "Vivência 1": float(row["vivencia1"]),
            "Vivência 2": float(row["vivencia2"]) if row["vivencia2"].strip() else 0.0,  # Evita erro por valores vazios
            "Vivência 3": float(row["vivencia3"]),
            "Prova Prática": float(row["prova_pratica"]),
            "Total": float(row["total"])  # Soma das notas
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
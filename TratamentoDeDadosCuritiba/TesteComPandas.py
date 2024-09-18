import pandas as pd
import os

try:
    caminho_arquivo = "c:\\eventos\\eventos.csv"

    df = pd.read_csv(caminho_arquivo, sep=';', header=None)
    if df.empty:
        raise ValueError("O arquivo CSV está vazio ou mal formatado.")

    frequencia_valores = df[16].value_counts()

    valor_mais_frequente = frequencia_valores.idxmax()
    frequencia = frequencia_valores.max()

    print(f"Valor mais frequente na coluna 16: {valor_mais_frequente}, Frequência: {frequencia}")
except FileNotFoundError:
    print(f"Arquivo não encontrado: {caminho_arquivo}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

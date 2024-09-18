import pandas as pd
import os
from collections import defaultdict

try:
    caminho_arquivo = "c:\\eventos\\eventos.csv"

    with open(caminho_arquivo, "r") as arqEventos:
        eventos = []
        
        for linha in arqEventos:
            atributos = linha.strip().split(";")
            eventos.append(atributos)
        
        if not eventos:
            raise ValueError("O arquivo CSV está vazio ou mal formatado.")

        frequencia_valores = defaultdict(int)

        for atributos in eventos:
            if len(atributos) > 16:
                valor_coluna_16 = atributos[16]
                frequencia_valores[valor_coluna_16] += 1

        valor_mais_frequente = max(frequencia_valores, key=frequencia_valores.get)
        frequencia = frequencia_valores[valor_mais_frequente]

        print(f"Valor mais frequente na coluna 16: {valor_mais_frequente}, Frequência: {frequencia}")
except FileNotFoundError:
    print(f"Arquivo não encontrado: {caminho_arquivo}")
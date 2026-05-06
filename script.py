import pandas as pd 
import matplotlib.pyplot as plt 
import os
import sys

def verificar_arquivo(caminho: str):

    # Verifica a existência do arquivo que vai ser lido pelo script
    if not os.path.exists(caminho):
        print(f"\n Arquivo não encontrado: {caminho}\n")

        print("Diretório atual:")
        print(os.getcwd())

        print("\n Arquivos disponíveis na pasta:")
        for f in os.listdir():
            print("-", f)

        sys.exit(1)

def carregar_dados(caminho_arquivo: str) -> pd.DataFrame:

    df = pd.read_excel(caminho_arquivo)

    # Converte coluna de data para datetime 
    df["data"] = pd.to_datetime(df["data"])
    print(df["data"].head())

    return df


def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:

    # Esse trecho trata os valores ausentes nas colunas que possuem dados incompletos
    df["nivel_rio_m"] = df["nivel_rio_m"].interpolate()
    df["ndvi"] = df["ndvi"].interpolate()
    print("Rodou")

    return df


def main():
    caminho = "dados.xlsx"

    verificar_arquivo(caminho)

    df = carregar_dados(caminho)
    df = tratar_dados(df)


if __name__ == "__main__":
    main()
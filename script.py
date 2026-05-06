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

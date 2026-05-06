# teste-pratico-INPP
## Descrição
Este script em python foi elaborado com o objetivo de realizar a análise dos dados de um arquivo csv que contém:

- Data;
- Temperatura;
- Nível do rio;
- Ndvi.

## Tecnologias utilizadas 

- Python  
- Pandas  
- Matplotlib  
- OpenPyXL

## Como rodar o projeto 

### 1 - Clone o repositório 
```bash
git clone https://github.com/MatheusParizotto/teste-pratico-INPP
```

### 2 - Instalar as depêndencias
```bash
pip install pandas matplotlib openpyxl
```

### 3 - Rode o script
```bash
python script.py
```

## Justificativa para as tecnologias utilizadas 
A linguagem python foi escolhida devido à sua versatilidade e facilidade de uso dentro do campo de análise de dados. As bibliotecas 
(Pandas, matplotlib e openpyxl) foram selecionadas respectivamente por realizar a leitura de dados de forma simples, geração de 
gráficos intuitivos e pela leitura de arquivos excel. Por último, a técnica de interpolação linear foi adotada para preencher valores 
ausentes de uma forma que mantivesse o padrão dos dados apresentados, pois estima os valores de forma "reta", pegando como referência
o valor anterior e o próximo.

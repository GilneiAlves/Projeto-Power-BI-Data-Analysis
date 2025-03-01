import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Plota um histograma + densidade para visualizar a distribuição de uma variável.
def visualizar_distribuicao(df, col_name, bins=30):
    """
    Plota um histograma e um gráfico de densidade para visualizar a distribuição de uma variável numérica.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna numérica.
    - bins: Número de bins para o histograma (padrão: 30).

    Retorna:
    - Um gráfico da distribuição da variável.
    """
    plt.figure(figsize=(10, 5))
    sns.histplot(df[col_name], bins=bins, kde=True)
    plt.title(f'Distribuição de {col_name}')
    plt.xlabel(col_name)
    plt.ylabel('Frequência')
    plt.grid()
    plt.show()

# Conta quantos valores únicos existem em cada coluna.
def contar_valores_unicos(df):
    """
    Conta o número de valores únicos para cada coluna.

    Retorna:
    - DataFrame com o número de valores únicos por coluna.
    """
    return df.nunique().to_frame(name="Valores Únicos")

# Retorna e plota a matriz de correlação das variáveis numéricas.
def matriz_correlacao(df, metodo="pearson"):
    """
    Gera e plota uma matriz de correlação entre as variáveis numéricas.

    Parâmetros:
    - df: DataFrame do pandas.
    - metodo: Método de correlação ('pearson', 'spearman', 'kendall').

    Retorna:
    - DataFrame com a matriz de correlação.
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(method=metodo), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f'Matriz de Correlação ({metodo})')
    plt.show()
    return df.corr(method=metodo)

# Retorna colunas que possuem apenas um valor único.
def encontrar_colunas_constantes(df):
    """
    Identifica colunas constantes (que possuem apenas um valor único).

    Retorna:
    - Lista com os nomes das colunas constantes.
    """
    return [col for col in df.columns if df[col].nunique() == 1]

# Calcula o coeficiente de skewness para ver se os dados estão enviesados.
def detectar_skewness(df):
    """
    Calcula o coeficiente de skewness (assimetria) das colunas numéricas.

    Retorna:
    - DataFrame com os valores de skewness.
    """
    skew_values = df.select_dtypes(include=[np.number]).skew()
    return pd.DataFrame({"Skewness": skew_values}).sort_values(by="Skewness", ascending=False)

# Conta a quantidade de outliers por coluna numérica.
def outliers_por_coluna(df, metodo="iqr", fator=1.5):
    """
    Conta a quantidade de outliers em cada coluna numérica.

    Parâmetros:
    - df: DataFrame do pandas.
    - metodo: 'desvio_padrao' ou 'iqr'.
    - fator: Multiplicador para a detecção de outliers.

    Retorna:
    - DataFrame com a contagem de outliers por coluna.
    """
    outliers = {}
    for col in df.select_dtypes(include=[np.number]).columns:
        if metodo == "desvio_padrao":
            limite = fator * df[col].std()
            media = df[col].mean()
            count = df[(df[col] < media - limite) | (df[col] > media + limite)].shape[0]
        elif metodo == "iqr":
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            limite_inferior = Q1 - fator * IQR
            limite_superior = Q3 + fator * IQR
            count = df[(df[col] < limite_inferior) | (df[col] > limite_superior)].shape[0]
        outliers[col] = count
    return pd.DataFrame.from_dict(outliers, orient="index", columns=["Outliers"])

# Gera um boxplot para visualizar possíveis outliers.
def boxplot_coluna(df, col_name):
    """
    Plota um boxplot para visualizar a distribuição de uma variável numérica.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna numérica.

    Retorna:
    - Um gráfico boxplot.
    """
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col_name])
    plt.title(f'Boxplot de {col_name}')
    plt.grid()
    plt.show()

# Conta os valores mais frequentes de uma variável categórica.
def contar_categorias(df, col_name, top_n=10):
    """
    Conta os valores únicos de uma coluna categórica e retorna os 'top_n' mais frequentes.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna categórica.
    - top_n: Número de categorias mais frequentes a serem exibidas.

    Retorna:
    - DataFrame com as categorias mais frequentes.
    """
    return df[col_name].value_counts().head(top_n).to_frame(name="Frequência")

# Exibe quantas categorias únicas cada variável categórica tem.
def analisar_categorias(df):
    """
    Analisa colunas categóricas do DataFrame.

    Retorna:
    - DataFrame com o número de categorias únicas por coluna categórica.
    """
    colunas_categoricas = df.select_dtypes(include=["object", "category"]).columns
    return df[colunas_categoricas].nunique().to_frame(name="Categorias Únicas")

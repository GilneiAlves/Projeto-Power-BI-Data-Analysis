import numpy as np
import pandas as pd

# Substitui outliers por NaN usando desvio padrão ou IQR.
def excluir_outliers(df, col_name, metodo="desvio_padrao", fator=2.7):
    """
    Remove outliers de uma coluna de um DataFrame.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna para verificar outliers.
    - metodo: 'desvio_padrao' (default) ou 'iqr' para Interquartile Range.
    - fator: Multiplicador do desvio padrão ou IQR (quanto maior, menos valores serão removidos).

    Retorna:
    - DataFrame com outliers substituídos por NaN.
    """
    if metodo == "desvio_padrao":
        intervalo = fator * df[col_name].std()
        media = df[col_name].mean()
        df.loc[(df[col_name] < media - intervalo) | (df[col_name] > media + intervalo), col_name] = np.nan
    
    elif metodo == "iqr":
        Q1 = df[col_name].quantile(0.25)
        Q3 = df[col_name].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - fator * IQR
        limite_superior = Q3 + fator * IQR
        df.loc[(df[col_name] < limite_inferior) | (df[col_name] > limite_superior), col_name] = np.nan
    
    return df

# Retorna um DataFrame com os valores considerados outliers.
def identificar_outliers(df, col_name, metodo="desvio_padrao", fator=2.7):
    """
    Identifica outliers em uma coluna de um DataFrame sem removê-los.

    Retorna um DataFrame com as linhas que possuem outliers.
    """
    if metodo == "desvio_padrao":
        intervalo = fator * df[col_name].std()
        media = df[col_name].mean()
        return df[(df[col_name] < media - intervalo) | (df[col_name] > media + intervalo)]
    
    elif metodo == "iqr":
        Q1 = df[col_name].quantile(0.25)
        Q3 = df[col_name].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - fator * IQR
        limite_superior = Q3 + fator * IQR
        return df[(df[col_name] < limite_inferior) | (df[col_name] > limite_superior)]

# Exibe os tipos de dados presentes no DataFrame.
def verificar_tipos_dados(df):
    """
    Retorna um resumo dos tipos de dados presentes no DataFrame.
    """
    return df.dtypes.to_frame(name="Tipo de Dado")

# Preenche valores NaN usando média, mediana, moda ou zero.
def preencher_nulos(df, metodo="media"):
    """
    Preenche valores nulos em um DataFrame.

    Parâmetros:
    - df: DataFrame do pandas.
    - metodo: 'media', 'mediana', 'moda' ou 'zero'.

    Retorna o DataFrame com valores nulos preenchidos.
    """
    df = df.copy()
    
    for col in df.select_dtypes(include=[np.number]).columns:
        if metodo == "media":
            df[col] = df[col].fillna(df[col].mean())
        elif metodo == "mediana":
            df[col] = df[col].fillna(df[col].median())
        elif metodo == "moda":
            df[col] = df[col].fillna(df[col].mode()[0])
        elif metodo == "zero":
            df[col] = df[col].fillna(0)
    
    return df

# Normaliza uma coluna usando Min-Max ou Z-score.
def normalizar_coluna(df, col_name, metodo="min_max"):
    """
    Normaliza uma coluna de um DataFrame.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna a ser normalizada.
    - metodo: 'min_max' (default) ou 'z_score'.

    Retorna o DataFrame com a coluna normalizada.
    """
    if metodo == "min_max":
        df[col_name] = (df[col_name] - df[col_name].min()) / (df[col_name].max() - df[col_name].min())
    
    elif metodo == "z_score":
        df[col_name] = (df[col_name] - df[col_name].mean()) / df[col_name].std()
    
    return df

# Remove linhas duplicadas do DataFrame.
def remover_duplicatas(df, colunas=None, manter="primeiro"):
    """
    Remove duplicatas de um DataFrame.

    Parâmetros:
    - df: DataFrame do pandas.
    - colunas: Lista de colunas para verificar duplicatas (se None, verifica todas as colunas).
    - manter: 'primeiro' (default) mantém a primeira ocorrência, 'último' mantém a última, False remove todas as duplicatas.

    Retorna:
    - DataFrame sem duplicatas.
    """
    return df.drop_duplicates(subset=colunas, keep=manter)

# Exibe a quantidade e percentual de valores NaN em cada coluna.
def contar_valores_nulos(df):
    """
    Retorna um resumo com a quantidade e percentual de valores nulos em cada coluna.
    """
    total_nulos = df.isnull().sum()
    percentual_nulos = (df.isnull().sum() / len(df)) * 100
    return pd.DataFrame({"Total Nulos": total_nulos, "Percentual (%)": percentual_nulos})

# Substitui valores específicos em uma coluna.
def substituir_valores(df, col_name, valores_antigos, novo_valor):
    """
    Substitui valores específicos em uma coluna.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna onde os valores serão substituídos.
    - valores_antigos: Lista ou único valor a ser substituído.
    - novo_valor: Valor pelo qual substituir.

    Retorna:
    - DataFrame com os valores substituídos.
    """
    df[col_name] = df[col_name].replace(valores_antigos, novo_valor)
    return df

# Converte uma coluna para um novo tipo de dado, incluindo datetime.
def converter_tipo_dado(df, col_name, tipo):
    """
    Converte o tipo de dado de uma coluna.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna a ser convertida.
    - tipo: Tipo de dado desejado (ex: 'int', 'float', 'category', 'datetime').

    Retorna:
    - DataFrame com a coluna convertida.
    """
    if tipo == "datetime":
        df[col_name] = pd.to_datetime(df[col_name], errors="coerce")
    else:
        df[col_name] = df[col_name].astype(tipo, errors="ignore")
    return df

# Retorna estatísticas como média, mediana, desvio padrão, mínimo e máximo de cada coluna numérica.
def gerar_resumo_estatistico(df):
    """
    Retorna um resumo estatístico do DataFrame, incluindo média, mediana, desvio padrão, mínimo e máximo.

    Retorna:
    - DataFrame com resumo estatístico.
    """
    resumo = df.describe().T
    resumo["mediana"] = df.median()
    return resumo[["count", "mean", "mediana", "std", "min", "max"]]
import pandas as pd
import numpy as np

# Tratar valores nulos (NaN) em um DataFrame. A função permitirá a escolha do método de tratamento...
def trata_valores_nulos(df: pd.DataFrame, metodo: str = 'remover', valor: float = None) -> pd.DataFrame:
    """
    Função para tratar valores nulos (NaN) em um DataFrame.

    Parâmetros:
    - df: pd.DataFrame - O DataFrame a ser tratado.
    - metodo: str - Método de tratamento ('remover', 'preencher_medio', 'preencher_mediana', 'preencher_moda', 'preencher_valor').
    - valor: float - Valor a ser utilizado para preencher (caso o método seja 'preencher_valor').

    Retorna:
    - pd.DataFrame - O DataFrame após o tratamento dos valores nulos.
    """
    
    if metodo == 'remover':
        # Remove as linhas que contêm valores nulos
        return df.dropna()

    elif metodo == 'preencher_medio':
        # Preenche os valores nulos com a média da coluna
        return df.fillna(df.mean())

    elif metodo == 'preencher_mediana':
        # Preenche os valores nulos com a mediana da coluna
        return df.fillna(df.median())

    elif metodo == 'preencher_moda':
        # Preenche os valores nulos com a moda da coluna
        return df.apply(lambda col: col.fillna(col.mode()[0]))

    elif metodo == 'preencher_valor':
        if valor is None:
            raise ValueError("É necessário fornecer um valor para preencher os valores nulos.")
        # Preenche os valores nulos com um valor específico
        return df.fillna(valor)

    else:
        raise ValueError("Método inválido. Escolha entre 'remover', 'preencher_medio', 'preencher_mediana', 'preencher_moda' ou 'preencher_valor'.")

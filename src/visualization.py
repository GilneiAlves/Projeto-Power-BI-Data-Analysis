import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Mostra a distribuição de uma variável numérica.
def plot_histograma(df, col_name, bins=30):
    """
    Plota um histograma para visualizar a distribuição de uma variável numérica.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna numérica.
    - bins: Número de bins (padrão: 30).
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col_name], bins=bins, kde=True)
    plt.title(f'Histograma de {col_name}')
    plt.xlabel(col_name)
    plt.ylabel('Frequência')
    plt.grid()
    plt.show()

# Plota um boxplot para detectar outliers e dispersão.
def plot_boxplot(df, col_name):
    """
    Plota um boxplot para visualizar outliers e dispersão de uma variável numérica.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna numérica.
    """
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col_name])
    plt.title(f'Boxplot de {col_name}')
    plt.grid()
    plt.show()

# Mostra um gráfico de barras das categorias mais frequentes.
def plot_barras(df, col_name, top_n=10):
    """
    Plota um gráfico de barras para visualizar a frequência de valores em uma coluna categórica.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna categórica.
    - top_n: Número de categorias mais frequentes a serem exibidas.
    """
    plt.figure(figsize=(10, 5))
    df[col_name].value_counts().head(top_n).plot(kind='bar', color='skyblue')
    plt.title(f'Top {top_n} Categorias em {col_name}')
    plt.xlabel(col_name)
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

# Plota um heatmap com a correlação entre variáveis numéricas.
def plot_matriz_correlacao(df, metodo="pearson"):
    """
    Plota um heatmap da matriz de correlação.

    Parâmetros:
    - df: DataFrame do pandas.
    - metodo: Método de correlação ('pearson', 'spearman', 'kendall').
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(method=metodo), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f'Matriz de Correlação ({metodo})')
    plt.show()

# Exibe a relação entre duas variáveis numéricas.
def plot_dispersao(df, x_col, y_col, hue=None):
    """
    Plota um gráfico de dispersão para visualizar a relação entre duas variáveis numéricas.

    Parâmetros:
    - df: DataFrame do pandas.
    - x_col: Nome da variável no eixo X.
    - y_col: Nome da variável no eixo Y.
    - hue: Coluna para diferenciar pontos por cor (opcional).
    """
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, alpha=0.7)
    plt.title(f'Dispersão entre {x_col} e {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid()
    plt.show()

# Plota uma linha temporal para análise de tendências.
def plot_linha(df, x_col, y_col, group_col=None):
    """
    Plota um gráfico de linha para séries temporais ou tendências.

    Parâmetros:
    - df: DataFrame do pandas.
    - x_col: Nome da variável no eixo X (geralmente tempo).
    - y_col: Nome da variável no eixo Y.
    - group_col: Nome da coluna para agrupar e traçar múltiplas linhas (opcional).
    """
    plt.figure(figsize=(10, 5))
    if group_col:
        sns.lineplot(data=df, x=x_col, y=y_col, hue=group_col)
    else:
        sns.lineplot(data=df, x=x_col, y=y_col)
    plt.title(f'Tendência de {y_col} ao longo de {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid()
    plt.show()

# Exibe um gráfico de pizza para análise de proporções.
def plot_pie_chart(df, col_name, top_n=5):
    """
    Plota um gráfico de pizza para visualizar proporções de categorias.

    Parâmetros:
    - df: DataFrame do pandas.
    - col_name: Nome da coluna categórica.
    - top_n: Número de categorias mais frequentes a serem exibidas.
    """
    top_values = df[col_name].value_counts().head(top_n)
    plt.figure(figsize=(7, 7))
    plt.pie(top_values, labels=top_values.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
    plt.title(f'Distribuição de {col_name}')
    plt.show()

# Gera um pairplot para visualizar correlações e padrões entre múltiplas variáveis.
def plot_pairplot(df, cols=None, hue=None):
    """
    Plota um pairplot para visualizar relações entre múltiplas variáveis numéricas.

    Parâmetros:
    - df: DataFrame do pandas.
    - cols: Lista de colunas a serem analisadas (se None, usa todas numéricas).
    - hue: Coluna categórica para diferenciar cores (opcional).
    """
    sns.pairplot(df[cols] if cols else df, hue=hue, diag_kind="kde")
    plt.show()

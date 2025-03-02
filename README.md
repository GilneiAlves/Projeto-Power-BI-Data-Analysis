# Análise Exploratória e Visualização de Dados de E-commerce Brasileiro

## Descrição

Este projeto visa realizar uma análise exploratória de dados (EDA) e o tratamento de dados do conjunto de dados de e-commerce brasileiro da Olist, disponível no Kaggle. O objetivo é extrair insights valiosos sobre o comportamento dos clientes, o desempenho de vendas e outras métricas relevantes. Os dados serão tratados com Python e visualizados com Power BI.

## Conjunto de Dados

- **Fonte:** Kaggle (Olist Brazilian E-Commerce Public Dataset)  
- **Link:** [Kaggle - Olist Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Descrição do Conjunto de Dados

### Conjunto de dados públicos de comércio eletrônico brasileiro da Olist

Este conjunto de dados contém informações sobre 100 mil pedidos realizados entre 2016 e 2018 em diversos marketplaces no Brasil. Ele permite analisar os pedidos sob várias perspectivas, como:

- **Status do pedido**
- **Preço**
- **Pagamento**
- **Desempenho do frete**
- **Localização do cliente**
- **Atributos do produto**
- **Avaliações escritas pelos clientes**

Além disso, há um conjunto de dados de geolocalização que relaciona os códigos postais brasileiros às suas coordenadas de latitude e longitude.

Esses são dados comerciais reais, que foram anonimizados. As referências às empresas e parceiros no texto da análise foram substituídas pelos nomes das grandes casas da franquia *Game of Thrones*.

### Contexto

Este conjunto de dados foi generosamente fornecido pela **Olist**, a maior loja de departamentos em marketplaces brasileiros. A Olist conecta pequenas empresas de todo o Brasil a canais de vendas de forma simples, com um único contrato. Esses comerciantes podem vender seus produtos através da Olist Store e enviá-los diretamente aos clientes utilizando os parceiros logísticos da Olist.

Para mais informações, acesse o [site da Olist](https://www.olist.com).

Após a compra de um produto na Olist Store, o vendedor é notificado para atender ao pedido. Quando o cliente recebe o produto ou a data estimada de entrega chega, ele recebe uma pesquisa de satisfação por e-mail, onde pode avaliar a experiência de compra e escrever comentários.

## Ferramentas e Tecnologias

### Python

- **Análise Exploratória de Dados (EDA)**
- **Tratamento e Limpeza de Dados**
- **Transformação de Dados**

### Bibliotecas Python

- `pandas`: Manipulação e análise de dados tabulares.
- `numpy`: Computação numérica e operações com arrays.
- `matplotlib`: Criação de gráficos e visualizações estáticas.
- `seaborn`: Visualização de dados estatísticos.
- `os`: Manipulação de arquivos e diretórios.
- Todas as bibliotecas com as versões utilizadas estão listadas no `requirements.txt`.

### Power BI

- Criação de dashboards interativos.
- Visualização de métricas e KPIs.
- Publicação e compartilhamento de relatórios (.pbip).

### Git

- Controle de versão do código.
- Colaboração e compartilhamento do projeto.

## Etapas do Projeto

### 1. Coleta de Dados

- Download do conjunto de dados do Kaggle.
- Organização dos arquivos em diretórios apropriados.

### 2. Análise Exploratória de Dados (EDA)

- Carregamento dos dados em DataFrames do Pandas.
- Análise descritiva das variáveis (estatísticas, distribuições, etc.).
- Identificação de valores ausentes e outliers.
- Visualização de dados com Matplotlib e Seaborn.
- Identificação de padrões e insights iniciais.

### 3. Tratamento e Limpeza de Dados

- Tratamento de valores ausentes (imputação, remoção, etc.).
- Remoção de outliers e dados inconsistentes.
- Transformação de variáveis (criação de novas colunas, padronização, etc.).
- Preparação dos dados para análise e visualização.

### 4. Modelagem de Dados (Opcional)

- Criação de modelos de machine learning para previsão ou classificação (se aplicável).
- Avaliação do desempenho dos modelos.

### 5. Visualização de Dados com Power BI

- Importação dos dados tratados para o Power BI.
- Criação de medidas e colunas calculadas.
- Desenvolvimento de dashboards interativos com gráficos e tabelas.
- Publicação do relatório no Power BI Service (.pbip).

### 6. Publicação no GitHub

- Criação de um repositório no GitHub.
- Upload dos arquivos do projeto (código Python, arquivos de dados tratados, relatório do Power BI, etc.).
- Atualização do `README.md` com informações sobre o projeto.
- Criação de uma `Estrutura.md` para nortear o desenvolvimento do projeto.

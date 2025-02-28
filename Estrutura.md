# Projeto-Power-BI-Data-Analysis/

│
├── data/                            # Pasta para armazenar dados brutos
│   ├── raw/                         # Arquivos originais do Kaggle (sem alterações, formato .csv)
│   │   ├── olist_customers_dataset.csv            # Informações sobre os clientes e sua localização
│   │   ├── olist_geolocation_dataset.csv          # Informações de códigos postais e suas coordenadas lat/lng
│   │   ├── olist_orders_dataset.csv               # Informações sobre os pedidos realizados
│   │   ├── olist_order_items_dataset.csv          # Informações sobre os itens comprados em cada pedido
│   │   ├── olist_order_payments_dataset.csv       # Informações sobre as opções de pagamento
│   │   ├── olist_order_reviews_dataset.csv        # Avaliações dos clientes sobre os produtos comprados
│   │   ├── olist_products_dataset.csv             # Informações sobre os produtos vendidos
│   │   ├── olist_sellers_dataset.csv              # Informações sobre os vendedores
│   │   └── product_category_name_translation.csv  # Tradução da categoria do produto para o inglês
│   │
│   └── processed/                                 # Dados processados e preparados para análise
│       ├── stg_data.db                            # Dados brutos gravados no banco de dados
│       └── dw_data.db                             # Dados limpos e transformados no banco de dados
│
├── notebooks/                       # Notebooks Jupyter para a análise exploratória de dados (EDA)
│   ├── 00_introduction.ipynb         # Introdução ao projeto e organização dos notebooks
│   ├── 01_data_loading.ipynb        # Carregamento dos dados
│   ├── 02_data_cleaning.ipynb       # Limpeza e pré-processamento dos dados
│   ├── 03_data_analysis.ipynb       # Análise exploratória dos dados
│   ├── 04_visualization.ipynb       # Visualização e criação de gráficos
│   └── analysis_summary.md          # Resumo das descobertas e insights
│
├── reportPowerBI/                   # Relatórios e outputs gerados no Power BI
│   └── Vendas.pbip                  # Relatório e gráficos do Power BI
│
├── src/                             # Scripts auxiliares e funções reutilizáveis
│   ├── data_preprocessing.py        # Funções para limpeza e transformação dos dados
│   ├── data_analysis.py             # Funções para análise de dados e cálculo de métricas
│   └── visualization.py             # Funções para visualização de dados
│
├── requirements.txt                 # Dependências do projeto
├── .gitignore                       # Arquivos e pastas a serem ignorados pelo Git
└── README.md                        # Documentação do projeto (instruções, objetivos, etc.)

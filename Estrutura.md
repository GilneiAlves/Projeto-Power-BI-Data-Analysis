# Projeto-Power-BI-Data-Analysis/

``` 
├── data/                            # Pasta para armazenar dados brutos
│   ├── raw/                         # Arquivos originais do Kaggle (sem alterações formato .csv)
│   │   ├── olist_customers_dataset.csv            # Informações sobre o cliente e sua localização
│   │   ├── olist_geolocation_dataset.csv          # Informações de códigos postais brasileiros e suas coordenadas lat/lng
│   │   ├── olist_orders_dataset.csv               # Informações sobre os itens comprados em cada pedido
│   │   ├── olist_order_items_dataset.csv          # Informações sobre os itens comprados em cada pedido
│   │   ├── olist_order_payments_dataset.csv       # Informações sobre as opções de pagamento dos pedidos
│   │   ├── olist_order_reviews_dataset.csv        # Informações sobre as avaliações feitas pelos clientes
│   │   ├── olist_products_dataset.csv             # Informações sobre os produtos vendidos pela Olist
│   │   ├── olist_sellers_dataset.csv              # Informações sobre os vendedores que atenderam pedidos feitos na Olist
│   │   └── product_category_name_translation.csv  # Traduz o product_category_name para inglês.
│   │
│   └── processed/                                 # Pasta para armazenar dados pré-processados e processados
│       ├── stg_data.db                            # Dados brutos gravados no banco
│       └── dw_data.db                             # Dados limpos e transformados gravados no banco
│
├── notebooks/                       # Jupyter Notebooks para EDA
│   ├── 01_data_loading.ipynb        # Carregamento dos dados
│   ├── 02_data_cleaning.ipynb       # Limpeza e pré-processamento
│   ├── 03_data_analysis.ipynb       # Análise exploratória dos dados
│   ├── 04_visualization.ipynb       # Visualização e gráficos
│   └── analysis_summary.md          # Resumo de insights e descobertas
│
├── reportPowerBI/                   # Relatórios e outputs gerados
│   └── Vendas.pbip                  # Gráficos e imagens
│
├── src/                             # Scripts auxiliares e funções reutilizáveis
│   ├── data_preprocessing.py        # Funções para limpeza e transformação de dados
│   ├── data_analysis.py             # Funções para análise e métricas
│   └── visualization.py             # Funções para visualização de dados
│
├── requirements.txt                 # Dependências do projeto
├── .gitignore                       # Arquivos e pastas a serem ignorados pelo Git
└── README.md                        # Documentação do projeto
```

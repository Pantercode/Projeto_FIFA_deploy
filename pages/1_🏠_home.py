import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

# Carregar o dataset na sessão para evitar recarregamento
if "data" not in st.session_state:
    try:
        # Lendo o arquivo CSV
        df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
        
        # Filtrando os dados
        current_year = datetime.today().year
        df_data = df_data[df_data["Contract Valid Until"] >= current_year]
        df_data = df_data[df_data["Value(£)"] > 0]
        df_data = df_data.sort_values(by="Overall", ascending=False)
        
        # Armazenando os dados na sessão
        st.session_state["data"] = df_data
    except FileNotFoundError:
        st.error("Arquivo 'CLEAN_FIFA23_official_data.csv' não encontrado. Verifique o caminho e tente novamente.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao carregar o dataset: {e}")

# Título principal
st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️")

# Sidebar com o link para o desenvolvedor
st.sidebar.markdown(
    "Desenvolvido por [Marcell Felipe](https://www.linkedin.com/in/marcell-felipe-de-paula-oliveira-219525199/)"
)

# Botão para acessar o Kaggle
if st.button("Acesse os dados no Kaggle"):
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

# Descrição do conjunto de dados
st.markdown(
    """
    Este é um conjunto de dados oficial do FIFA23, abrangendo informações detalhadas
    de **jogadores de futebol profissionais de 2017 a 2023**. 
    
    ### O que este conjunto de dados oferece?
    - Dados demográficos dos jogadores.
    - Características físicas e estatísticas de jogo.
    - Detalhes do contrato e afiliações de clubes.
    
    Com **mais de 17.000 registros**, é uma ferramenta valiosa para:
    - Analistas de futebol e entusiastas.
    - Pesquisadores interessados em estudar métricas de desempenho, avaliação de mercado e desenvolvimento de jogadores.
    
    Explore atributos de jogadores, análise de clubes, posicionamento de jogadores e tendências no futebol ao longo do tempo.
    """
)

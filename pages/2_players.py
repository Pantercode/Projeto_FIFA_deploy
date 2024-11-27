import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

# Garantir que os dados estão na sessão
if "data" not in st.session_state:
    st.error("Os dados não foram carregados. Certifique-se de inicializar os dados corretamente.")
else:
    df_data = st.session_state["data"]

    # Sidebar para seleção de clube
    clubes = df_data["Club"].dropna().value_counts().index
    club = st.sidebar.selectbox("Clube", clubes)

    # Filtrar jogadores do clube selecionado
    df_players = df_data[df_data["Club"] == club]
    players = df_players["Name"].dropna().value_counts().index
    player = st.sidebar.selectbox("Jogador", players)

    # Obter estatísticas do jogador selecionado
    player_stats = df_data[df_data["Name"] == player].iloc[0]

    # Exibir informações do jogador
    st.image(player_stats["Photo"], width=150)
    st.title(player_stats["Name"])

    st.markdown(f"**Clube:** {player_stats['Club']}")
    st.markdown(f"**Posição:** {player_stats['Position']}")

    # Colunas para exibir informações do jogador
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown(f"**Idade:** {player_stats['Age']}")
    col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100:.2f} m")
    col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f} kg")

    st.divider()

    st.subheader(f"Overall: {player_stats['Overall']}")
    st.progress(int(player_stats["Overall"]))

    # Exibir métricas adicionais do jogador
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
    col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
    col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")


#streamlit run "c:/Users/marcell.oliveira/Desktop/streamlit/Projeto Streamlit FIFA/Projeto_FIFA_deploy/pages/2_players.py"
##streamlit run "c:/Users/marcell.oliveira/Desktop/streamlit/Projeto Streamlit FIFA/Projeto_FIFA_deploy/pages/3_teams.py"
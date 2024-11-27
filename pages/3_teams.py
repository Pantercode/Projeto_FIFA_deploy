import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

# Garantir que os dados estejam carregados
if "data" not in st.session_state:
    st.error("Os dados não foram carregados. Certifique-se de inicializar os dados corretamente.")
else:
    df_data = st.session_state["data"]

    # Sidebar para seleção de clube
    clubes = df_data["Club"].dropna().value_counts().index
    club = st.sidebar.selectbox("Selecione o Clube", clubes)

    # Filtrar dados do clube selecionado
    df_filtered = df_data[df_data["Club"] == club].set_index("Name")

    # Exibir logo do clube e título do clube
    st.markdown(f"## {club}")
    if "Club Logo" in df_filtered.columns and pd.notna(df_filtered.iloc[0]["Club Logo"]):
        st.image(df_filtered.iloc[0]["Club Logo"], width=150)

    # Definir colunas a exibir na tabela
    columns = [
        "Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined',
        'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)'
    ]

    # Garantir que apenas as colunas que existem no DataFrame sejam usadas
    columns = [col for col in columns if col in df_filtered.columns]

    # Exibir a tabela com os dados formatados
    def format_currency(value):
        """Formata valores monetários."""
        if pd.notna(value):
            return f"£{value:,.0f}"
        return "N/A"

    df_filtered_display = df_filtered[columns].copy()

    # Formatar colunas monetárias
    for col in ['Value(£)', 'Wage(£)', 'Release Clause(£)']:
        if col in df_filtered_display.columns:
            df_filtered_display[col] = df_filtered_display[col].apply(format_currency)

    # Exibir a tabela com os dados do clube
    st.dataframe(
        df_filtered_display.style.format({
            "Overall": "{:.0f}",
            "Height(cm.)": "{:.2f} cm",
            "Weight(lbs.)": "{:.2f} lbs"
        })
    )

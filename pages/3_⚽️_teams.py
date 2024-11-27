import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

# Garantir que os dados estejam carregados
if "data" not in st.session_state:
    st.error("Os dados não foram carregados. Certifique-se de inicializar os dados corretamente.")
else:
    df_data = st.session_state["data"]

    # Sidebar para seleção de clube
    clubes = df_data["Club"].value_counts().index
    club = st.sidebar.selectbox("Clube", clubes)

    # Filtrar dados do clube selecionado
    df_filtered = df_data[df_data["Club"] == club].set_index("Name")

    # Exibir logo do clube e título
    if "Club Logo" in df_filtered.columns:
        st.image(df_filtered.iloc[0]["Club Logo"])
    st.markdown(f"## {club}")

    # Colunas a exibir
    columns = [
        "Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
        'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)'
    ]

    # Garantir que as colunas existam
    columns = [col for col in columns if col in df_filtered.columns]

    # Exibir tabela com dados
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

    # Exibir a tabela com imagens
    st.dataframe(
        df_filtered_display.style.format({
            "Overall": "{:.0f}",
            "Height(cm.)": "{:.2f} cm",
            "Weight(lbs.)": "{:.2f} lbs"
        })
    )

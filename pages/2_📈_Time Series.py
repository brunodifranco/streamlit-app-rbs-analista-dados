import streamlit as st
import plotly.express as px
from utils import data_setup

def make_filters_time_series(df):
    """
    Construção dos filtros.
    
    """
    st.sidebar.header("Filtros")
    creative_filter = st.sidebar.multiselect('Selecione o tipo de criativo', 
                                        default=["Custom", "Custom template"],
                                        options=list(df['CreativeType'].unique()), 
                                        max_selections=3)

    date_min = df['Date'].min().to_pydatetime()
    date_max = df['Date'].max().to_pydatetime()

    date_range = st.sidebar.slider("Selecionar Intervalo de Datas", 
                                min_value=date_min, 
                                max_value=date_max, 
                                value=(date_min, date_max))

    return creative_filter, date_range


def make_plots_time_series(filtered_data):
    """
    Construção dos plots.
    
    """
    fig1 = px.line(filtered_data, 
                x='Date', 
                y='ClickThroughConversions', 
                color='CreativeType', 
                hover_name="WeekDay",
                title="Conversões Diretas")

    fig1.update_layout(height=700)
    fig1.update_xaxes(title_text='Data')
    fig1.update_yaxes(title_text="Conversões Diretas")

    fig2 = px.line(filtered_data, 
                x='Date', 
                y='ViewThroughConversions', 
                color='CreativeType', 
                hover_name="WeekDay",
                title="Conversões Indiretas")

    fig2.update_layout(height=700)
    fig2.update_xaxes(title_text='Data')
    fig2.update_yaxes(title_text="Conversões Indiretas")

    fig3 = px.line(filtered_data, 
                x='Date', 
                y='TotalConversions', 
                color='CreativeType', 
                hover_name="WeekDay",
                title=f"Conversões Totais")

    fig3.update_layout(height=700)
    fig3.update_xaxes(title_text='Data')
    fig3.update_yaxes(title_text="Conversões Totais")

    # Renderize os gráficos no Streamlit
    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.plotly_chart(fig3, use_container_width=True)

    return None

if __name__ == "__main__":    
    st.header("Séries Temporais de Conversões por Tipo de Criativo")    
    st.markdown('- ##### Nessa página você encontra as séries temporais de conversões diretas, indiretas e totais, com a possibilidade de filtrar por tipo de criativo, além selecionar o período desejado para a análise. ')
    st.markdown('- Os filtros estão na lateral da página, sendo possível escolher no máximo 3 tipos de criativos por vez para a visualização conjunta. Passando o mouse por cima de cada gráfico são retornadas mais informações, como o número exato de conversões e a data exata, incluindo o dia da semana.')

    # Initial setup
    df = data_setup("data/Base de dados - Case Analista Jr - RBS Performance.csv")
    
    df = (df[[
            "Date", 
            "WeekDay"
            "CreativeType", 
            "ClickThroughConversions",
            "ViewThroughConversions",
            "TotalConversions"]]
            .groupby(["Date", "CreativeType"])
            .sum()
            .reset_index())
    
    # Filters
    creative_filter, date_range = make_filters_time_series(df)
    filtered_data = df[(df['CreativeType'].isin(creative_filter)) & (df['Date'] >= date_range[0]) & (df['Date'] <= date_range[1])]

    # Plots
    make_plots_time_series(filtered_data)
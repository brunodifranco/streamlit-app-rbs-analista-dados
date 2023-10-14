import streamlit as st
import plotly.express as px
from utils import data_setup

def make_filters_heat_map():
    """
    Construção dos filtros.
    
    """
    metric_options = [
                    "ConversionRate",
                    "ClickThroughRate"
                    ]
    st.sidebar.header("Filtros")
    selected_metric = st.sidebar.selectbox("Selecione a taxa desejada", metric_options)

    return selected_metric


def make_plots_heat_map(df, selected_metric):
    """
    Construção dos plots.
    
    """
    fig = px.imshow(df.pivot_table(index='WeekDay', columns='CreativeType', values=selected_metric, aggfunc='median'),
                    x=df["CreativeType"].unique(),
                    y=df["WeekDay"].unique(),
                    color_continuous_scale='YlOrRd',
                    title=f'Mapa de Calor de {selected_metric} por Dia da Semana e Tipo de Criativo')
    fig.update_layout(height=700)
    fig.update_xaxes(title_text='Tipo de Criativo')
    fig.update_yaxes(title_text='Dia da Semana')

    st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == "__main__":    
    st.header("Mapa de Calor da Taxa Escolhida por Dia da Semana e Tipo de Criativo")    
    st.markdown('- ##### Aqui está o mapa de calor de duas taxas a serem escolhidas: ConversionRate e ClickThroughRate.')
    st.markdown('- Esses mapas de calor relacionam a mediana dessas taxas com outras duas variáveis: o dia da semana do anúncio e o tipo de criativo.')

    # Initial setup
    df = data_setup("data/Base de dados - Case Analista Jr - RBS Performance.csv")
    df["Month"] = df["Date"].dt.month

    # Filters
    selected_metric = make_filters_heat_map()

    # Plots
    make_plots_heat_map(df, selected_metric)
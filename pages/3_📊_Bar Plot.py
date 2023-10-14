import streamlit as st
import plotly.express as px
from utils import data_setup

def make_filters_box_plots(df):
    """
    Construção dos filtros.
    
    """
    st.sidebar.header("Filtros")

    metric_options = [
                "ClickThroughConversions",
                "ViewThroughConversions", 
                "TotalConversions", 
                "TotalImpressions",
                "TotalClicks"
                 ]

    selected_metric = st.sidebar.selectbox("Selecione a métrica desejada", metric_options)
    selected_months = st.sidebar.multiselect("Selecione os meses", 
                                             list(df["Month"].unique()), 
                                             default=[6, 7, 8])

    return selected_metric, selected_months

def make_bar_plots(filtered_data):
    """
    Construção dos plots.
    
    """
    fig = px.bar(filtered_data, x='CreativeType', y=selected_metric, title=f'Total por Tipo de Criativo: {selected_metric}')
    fig.update_layout(height=700)
    fig.update_xaxes(title_text='Tipo de Criativo')
    fig.update_yaxes(title_text=selected_metric)
    st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == "__main__":    
    st.header("Gráfico de Barras para Métricas Desejadas")    
    st.markdown('- ##### Aqui está o gráfico de barras com o somatório de uma dentre cinco escolhas de métricas para o período em questão.')
    st.markdown(' - Os filtros estão na lateral da página, sendo possível escolher entre as seguintes métricas: Conversões Diretas, Conversões Indiretas, Total de Conversões, Total de Impressões e Total de Cliques. É possível escolher somente uma métrica por vez, porém os meses podem ser escolhidos conjuntamente.')
   
    # Initial setup
    df = data_setup("data/Base de dados - Case Analista Jr - RBS Performance.csv")
    df["Month"] = df["Date"].dt.month
    df["WeekDay"] = df["Date"].dt.day_name(locale="pt_BR.utf8")

    df = (df[[
            "Month",
            "CreativeType", 
            "ClickThroughConversions",
            "ViewThroughConversions",
            "TotalConversions",
            "TotalImpressions",
            "TotalClicks"]]
            .groupby(["Month", "CreativeType"])
            .sum()
            .reset_index())

    # Filters
    selected_metric, selected_months = make_filters_box_plots(df)
    filtered_data = df[df["Month"].isin(selected_months)].groupby("CreativeType").sum().reset_index().drop(columns="Month")

    # Plots
    make_bar_plots(filtered_data)
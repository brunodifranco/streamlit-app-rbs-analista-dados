import streamlit as st
from utils import logo_display

# Initial Configs
st.set_page_config(
                page_title='Ads Performance Analysis',
                layout='wide')

# Título centralizado
st.markdown('<h1 align="center">Ads Performance Analysis </h1>', unsafe_allow_html=True)

if __name__ == "__main__":    
   logo_display("pic/logo.png")

   st.markdown('- #### Olá, aqui você irá encontrar visualizações referentes a análises de anúncios de um cliente fictício.')
   st.markdown('#')

   st.markdown('- ##### Na página Time Series você encontra as séries temporais de conversões diretas, indiretas e totais, com a possibilidade de filtrar por tipo de criativo, além selecionar o período desejado para a análise.')
   st.markdown('#')

   st.markdown('- ##### Na página Bar Plot está o gráfico de barras com o somatório de uma dentre cinco escolhas de métricas para o período em questão.')
   st.markdown('#')
    
   st.markdown('- ##### Na página Heat Map estão presentes mapas de calor de duas taxas (que podem ser escolhidas manualmente): ConversionRate e ClickThroughRate. Esses mapas de calor relacionam a mediana dessas taxas com outras duas variáveis: o dia da semana do anúncio e o tipo de criativo.')
   st.markdown('#')
    
   st.markdown('- ###### Feito por: Bruno Di Franco Albuquerque, como parte do teste técnico para a vaga de Analista de Dados Jr na RBS.')
    
   st.markdown('#')
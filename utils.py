from pandas.core.frame import DataFrame

def logo_display(logo: str) -> None:
    import streamlit as st

    """
    Used for logo display
    """

    (
    col1, 
    col2,
    col3, 
    col4, 
    col5, 
    col6, 
    col7, 
    col8, 
    col9, 
    col10, 
    col11, 
    col12, 
    col13,
    col14,
    col15,
    col16,
    col17
    ) = st.columns(17)

    with col1:
        st.text(" ")

    with col2:
        st.text(" ")

    with col3:
        st.text(" ")

    with col4:
        st.text(" ")

    with col5:
        st.text(" ")

    with col6:
        st.text(" ")

    with col7:
        st.text(" ")

    with col8:
        st.text(" ")
    
    with col9:
        st.image(logo)
    
    with col10:
        st.text(" ")

    with col11:
        st.text(" ")

    with col12:
        st.text(" ")
    
    with col13:
        st.text(" ")

    with col14:
        st.text(" ")

    with col15:
        st.text(" ")

    with col16:
        st.text(" ")

    with col17:
        st.text(" ")

    return None

def data_setup(data_path: str) -> DataFrame:
    """   
        Renomeia as colunas, e cria duas novas variáveis: TotalConversions e ConversionRate.

        Parameters
        ----------
        data_path : str
            Caminho do arquivo original.

        Returns
        -------
        df : pandas.core.frame.DataFrame
            DataFrame do pandas.
    
    """ 
    import pandas as pd

    df = pd.read_csv(data_path, sep=";")
        
    # Ajustes iniciais
    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
    df["totalLineItemLevelCtr"] = df["totalLineItemLevelCtr"].str.replace(",", ".").astype(float)

    df = df.rename(
            columns={
            "advertiserName" : "AdvertiserName",
            "date" : "Date",
            "creativeType" : "CreativeType",
            "deviceCategoryName" : "DeviceName",        
            "totalLineItemLevelImpressions" : "TotalImpressions", 
            "totalLineItemLevelClicks" : "TotalClicks",
            "totalLineItemLevelCtr" : "ClickThroughRate",
            "clickThroughConversions" : "ClickThroughConversions",
            "viewThroughConversions" : "ViewThroughConversions"
            })

    # Novas métricas
    df["TotalConversions"] = df["ClickThroughConversions"] + df["ViewThroughConversions"]
    df["ConversionRate"] = df["TotalConversions"]/df["TotalImpressions"]

    return df

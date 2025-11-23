import streamlit as st
import pandas as pd

# essa função define alguns parâmetros da página
# por exemplo, se o layout vai ocupar a página inteira, se vai ser só centralizado, se vai ser mais à direita ou à esquerda
# etc
# também podemos colocar título, ícone, enfim
st.set_page_config(page_title="Meu Site Streamlit")

# antes de mais nada, a fim de fazer os dashboards mais tarde, vamos dividir a página entre o texto e o dashboards
# para isso, vamos dividir ela em containers diferentes

with st.container():
    # a forma mais simples de colocar texto na página é com o .write()
    # a exemplo:
    # st.write("Meu primeiro site com Streamlit. Olá mundo. Hehehehehe.")

    # para ficar melhor formatado, vamos inserir um header, um título:
    st.title("Dashboard de Contratos")
    # podemos inserir, também, um cabeçalho:
    #st.header("Meu primeiro site com Streamlit. Olá mundo. Hehehehehe.")
    # e um subcabeçalho:
    #st.subheader("Olá.")

    # um textinho normal
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo de maio")

    # para colocar links dentro do write, podemos fazer:
    st.write("Quer me ver fazendo sexo gay gostoso? [Clique aqui](https://www.reddit.com/r/expedition33/comments/1osus1a/what_happened_when_expedition_60_went_under_the)")


# agora vamos criar um *DASHBOARD*, a parte BOA
with st.container():
    # aqui pra ficar separado visualmente
    st.write("-------")
    
    # baixamos um arquivo com os resultados dos contratos em .csv
    # vamos abrí-lo com pandas
    dados = pd.read_csv('./py/análise de dados/arquivostreamlit/resultados.csv', index=False)
    
    # vamos usar, agora, o area_chart
    # é um jeito mais fácil que o altair_chart, porém menos customizável. Mas ele vai servir para o caso
    # vamos usá-lo para fazer um gráfico
    st.area_chart(dados, x="Data", y="Contratos")
    
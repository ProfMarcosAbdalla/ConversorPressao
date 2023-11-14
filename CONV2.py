import pandas as pd
import streamlit as st
import numpy as np

df = pd.read_csv('CONV.csv', header = 0)

def conv(ent,sai):
    ent_index = df.columns.get_loc(ent)
    sai_index = df.columns.get_loc(sai)
    cv = df.iloc[ent_index,sai_index]
    return cv

##a = conv('psi','bar',10)
##print(a)
st.title('Conversor de Unidades de Pressão')

cn = (df.columns.values)
col1,col2 = st.columns(2,gap="small")
ent = col1.selectbox('Unidade de Entrada',options=cn)
sai = col2.selectbox('Unidade de Saída',options=cn)
col1.write(ent)
col2.write(sai)

col1,col2,col3 = st.columns(3,gap="small")
val = col1.number_input('Valor a ser convertido em '+ent)
resp = conv(ent,sai) # str
r = float(resp)
col2.write('x '+str(resp))
nc = col3.number_input('Casas decimais', value = 3)
st.subheader('Valor convertido: '+ str(np.round(r*val,nc))+' '+sai)

    

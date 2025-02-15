import streamlit as st
import pandas as pd
import os
import sklearn.ensemble as en
import joblib

st.title('Used Car Price Prediction')


current_dir = os.getcwd()

model_path = os.path.join(current_dir, "models/linear_reg.joblib")
labelencoder_path = os.path.join(current_dir, "models/labelencoder.joblib")



datas=pd.read_csv('ss.csv')

datas=datas.loc[:,['Year','Present_Price', 'Kms_Driven',
'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
lis=list()
for i in datas.columns:
    if(datas[i].dtype=='category' or datas[i].dtype=='object'):
        a = st.selectbox(i.title(), options=datas[i].unique())
    else:
        if(len(datas[i].unique())<=6):
            a = st.selectbox(i.title(), options=datas[i].unique())
        else:
            datas[i]=datas[i].astype(float)
            a = st.number_input(i.title(),min_value=datas[i].min(),max_value=datas[i].max(),value=datas[i].median(),step=0.5)
    lis.append(a)


@st.cache_data
def load_model(f):
    return joblib.load(f)



def preprocess(input):
    input['Fuel_Type']=fuel_type.transform(input['Fuel_Type'])
    input['Seller_Type']=seller_type.transform(input['Seller_Type'])
    input['Transmission']=transmission.transform(input['Transmission'])
    return input


if st.button('Predict Price'):
    ss=datas.columns
    dic={}
    for i in range(len(ss)):
        dic[ss[i]]=[lis[i]]
    dff=pd.DataFrame(dic)
    rf_reg = load_model(model_path)
    fuel_type,seller_type,transmission = load_model(labelencoder_path)
    dff=preprocess(dff)
    prediction = rf_reg.predict(dff)

    st.write(f"Prediction of the Entered Car Price  is {prediction[0][0] : .2f} Lakhs")
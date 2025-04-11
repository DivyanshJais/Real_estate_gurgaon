import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Plotting Demo")

with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline_xg.pkl','rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your Inputs')

property_type = st.selectbox('Property type',['flat','house'])
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
bedroom = int(st.selectbox('Number of Bedroom', sorted(df['bedRoom'].unique().tolist())))
bathroom = int(st.selectbox('Number of Bathroom', sorted(df['bathroom'].unique().tolist())))
balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
facing = st.selectbox('Facing of house', sorted(df['facing'].unique().tolist()))
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
built_up_area = float(st.number_input('Built up area'))
servant_room = int(st.selectbox('Servant Room', ["1", "0"]))
#servant_room_value = 1 if servant_room == "Yes" else 0

store_room = int(st.selectbox('Store Room', ["1", "0"]))
#store_room_value = 1 if store_room == "Yes" else 0

furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    data = [[property_type, sector, bedroom, bathroom, balcony, facing, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony', 'facing','agePossession', 'built_up_area', 'servant room', 'store room','furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price-0.12
    high = base_price +0.12
    st.text("The Price of the flat is between {:.2f} Cr and {:.2f} Cr".format(low,high))
    #st.text("The Price of the flat is {:.2f} Cr".format(base_price))
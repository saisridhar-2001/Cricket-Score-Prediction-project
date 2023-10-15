import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

pipe=pickle.load(open('pipeT20.pkl','rb'))


teams=['India','Australia','England','New Zealand','Pakistan','South Africa','West Indies','Sri Lanka','Bangladesh','Afghanistan','Zimbabwe','Ireland','Scotland','Netherlands','Kenya','Namibia']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title("Cricket Score Predicter")
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs=st.number_input('overs Done')
with col5:
    wickets=st.number_input('wickets falled')
    
if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    Wickets_Left = 10-wickets
    crr = current_score/overs
    
    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 'current_score': [current_score],'balls_left': [balls_left], 'Wickets_Left': [wickets], 'crr': [crr]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))

import joblib
import streamlit as st
import category_encoders
import pandas as pd
import sklearn

Model= joblib.load("Model_Flight_Ticket_Final.pkl")
Inputs= joblib.load("Inputs_Flight_Ticket_Final.pkl")

def prediction(Airline, Source, Destination, Duration, Additional_Info,
       Total_Stops, Dep_Day, Dep_Month, Dep_Hour,
       Dep_Minute, Arrival_Day, Arrival_Month, Arrival_Hour,
       Arrival_Minute):
    test_df=pd.DataFrame(columns=Inputs)
    test_df.loc[0,'Airline']= Airline
    test_df.loc[0,'Source']= Source
    test_df.loc[0,'Destination']= Destination
    test_df.loc[0,'Duration']= Duration
    test_df.loc[0,'Additional_Info']= Additional_Info
    test_df.loc[0,'Total_Stops']= Total_Stops
    test_df.loc[0,'Dep_Day']= Dep_Day
    test_df.loc[0,'Dep_Month']= Dep_Month
    test_df.loc[0,'Dep_Hour']= Dep_Hour
    test_df.loc[0,'Dep_Minute']= Dep_Minute
    test_df.loc[0,'Arrival_Day']= Arrival_Day
    test_df.loc[0,'Arrival_Month']= Arrival_Month
    test_df.loc[0,'Arrival_Hour']= Arrival_Hour
    test_df.loc[0,'Arrival_Minute']= Arrival_Minute
    result= Model.predict(test_df)
    return result[0]

def main():    
    ## Setting up the page title
    st.set_page_config(page_title= 'Flight Tickets Price Prediction')
    
     # Add a title in the middle of the page using Markdown and CSS
    st.markdown("<h1 style='text-align: center;text-decoration: underline;color:GoldenRod'>Flight Tickets Price Prediction</h1>", unsafe_allow_html=True)
    
    Airline=st.selectbox('Insert Airline Company',  ['Air India', 'Jet Airways', 'IndiGo', 'SpiceJet', 'Multiple carriers', 'GoAir',
 'Vistara', 'Air Asia', 'Vistara Premium economy',
 'Multiple carriers Premium economy', 'Trujet'])
    
    Source=st.selectbox('Insert Departure City',['Kolkata', 'Delhi', 'Banglore', 'Chennai', 'Mumbai'])
    
    Destination=st.selectbox('Insert Arrival City',['Banglore', 'Cochin', 'New Delhi', 'Kolkata', 'Delhi', 'Hyderabad'])
    
    Duration=st.number_input('Insert duration of flight in minutes',min_value=30, max_value=2500, value=500,step=50)
    
    Additional_Info=st.selectbox('Insert Additional_Info',['No Info', 'In-flight meal not included', 'No check-in baggage included',
 '1 Long layover', 'Change airports', 'Red-eye flight'])

    Total_Stops=st.slider('Choose number of stops', min_value=0, max_value=4, value=2,step=1)
    
    Dep_Day=st.slider('Choose Depature Day', min_value=1, max_value=31, value=15,step=1)

    Dep_Month=st.slider('Choose Depature Month', min_value=1, max_value=12, value=6,step=1)

    Dep_Hour=st.slider('Choose Depature Hour', min_value=1, max_value=23, value=15,step=1)

    Dep_Minute=st.slider('Choose Depature Minute', min_value=1, max_value=59, value=30,step=1)

    Arrival_Day=st.slider('Choose Arrival Day', min_value=1, max_value=31, value=15,step=1)
    
    Arrival_Month=st.slider('Choose Arrival Month ', min_value=1, max_value=12, value=6,step=1)

    Arrival_Hour=st.slider('Choose Arrival Hour',min_value=1, max_value=23, value=15,step=1)

    Arrival_Minute=st.slider('Choose Arrival Minute', min_value=1, max_value=59, value=30,step=1)
    
    if st.button('predict'):
        results= prediction(Airline, Source, Destination, Duration, Additional_Info,Total_Stops, Dep_Day, Dep_Month, Dep_Hour, Dep_Minute, Arrival_Day, Arrival_Month, Arrival_Hour,Arrival_Minute)
        st.text(f"The Ticket Price is {int(results)} ")
main()

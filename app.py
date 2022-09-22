import requests
import json
from datetime import datetime
import pandas as pd
import streamlit as st
from datetime import timedelta
from PIL import Image

######## MAIN FUNCTIONS ################

def request(option_origine,option_destination,option_date):
    """
    Return a dataframe with the train available based on the parameters : option_origine,option_destination,option_date through the API

    param :
        option_origine : Origine city
        option_destination : Arrival city
        option_date : Date 
    
    return : 
        df_all_train : Dataframe with the corresponding trains
    """
    # Separate the option_date into 3 values (day, month, year)
    day = option_date.day
    month = option_date.month
    year = option_date.year

    # personnalized url with the good parameter 
    url = 'https://ressources.data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&facet=date&facet=origine&facet=destination&facet=od_happy_card&refine.origine={}&refine.date={}%2F{}%2F{}&refine.destination={}'.format(option_origine,year,month,day,option_destination)
    
    response_API_tgv = requests.get(url) # get the request response of the API

    data = response_API_tgv.text # Convert into text
    
    parse_json = json.loads(data) #Convert into json format

    data_array = [] #numpy array to store the features

    for i in range(len(parse_json['records'])): # for each element return by the API
        record = parse_json['records'][i]['fields'] # take the features of the record number i
        date = record['date'] # date of the train
        arrival_time = record['heure_arrivee'] # arrival time of train
        departure_time = record['heure_depart'] # departure time of train
        origine = record['origine'] # Departure city
        destination = record['destination'] # Arrival city

        data_point = [origine, destination, date, departure_time, arrival_time]
        data_array.append(data_point) # Append data point in the numpy array

    df_all_train = pd.DataFrame(data_array, columns = ['Origine', 'Destination', 'Date', 'Departure_time', 'Arrival_time']) #construct the dataframe
    
    return df_all_train


def param(df_city_origine,df_city_destination):
    """
    Return the parameters values of the departure city, arrival city and the date based on user input
    
    param : 
        df_city_origine : all unique city origine
        df_city_destination : all unique city destination
    
    return : 
        option_origine : origine city based on user input
        option_destination : destination city based on user input
        option_date : departure date based on user input
        bouton_launch_search : True or False if the search button is pressed
    """
    
    # Departure city 
    values_origine = df_city_origine.values.flatten()
    option_origine = st.sidebar.selectbox(
        "Departure city",
        values_origine,
        index = list(values_origine).index('PARIS (intramuros)')
        )

    # Arrival city 
    values_destination = df_city_destination.values.flatten()
    option_destination = st.sidebar.selectbox(
        "Destination city",
        values_destination,
        index = list(values_destination).index('LA ROCHELLE VILLE')
        )

    # Date
    today = datetime.now()
    option_date = st.sidebar.date_input(
        "Departure date",
        today,
        min_value = today,
        max_value = today + timedelta(days=29)
        )

    # True if the search button is pressed or False otherwise
    bouton_launch_search = st.sidebar.button("Search")

    return option_origine,option_destination,option_date,bouton_launch_search



########### MAIN PROGRAM ###############

if __name__ == "__main__":
    st.set_page_config(
     page_title="Train web app",
     page_icon="🚅",
     layout="centered",
     initial_sidebar_state="expanded",
    )

    # Import the two csv files of the departure and arrival cities
    PATH_DEPARTURE_CITY = '/Users/pierre-louis.danieau/Documents/perso_divers/medium/article/departure_city.csv'
    PATH_DESTINATION_CITY = '/Users/pierre-louis.danieau/Documents/perso_divers/medium/article/destination_city.csv'
    df_ville_origine = pd.read_csv(PATH_DEPARTURE_CITY)
    df_ville_destination = pd.read_csv(PATH_DESTINATION_CITY)
    del df_ville_origine['Unnamed: 0']
    del df_ville_destination['Unnamed: 0']

    # User inputs for the origine, destination and date
    option_origine,option_destination,option_date,bouton_launch_search = param(df_ville_origine,df_ville_destination)

    # Add a title
    st.markdown("<h1 style='text-align: center; color: RoyalBlue;'>Train web app in real time</h1>", unsafe_allow_html=True)

    image = Image.open('train.jpg')
    col1_first, col2_first = st.columns([1, 1])
    with col1_first:
        st.write(' ')
        st.image(image, caption='Photo by @Macrovector', width = 200)
    with col2_first:
        st.write(' ')
        with st.expander("🚆 Information about the Web App", expanded = True):
            st.write("""
                    Define your criteria in the left bar to search for trains eligible for the TGV Max subscription.
                    Data scrapped with the SNCF API in real time.
                    """)

    st.write(' ')
    # If the user made a request (if he had clicked on the search button)
    if bouton_launch_search == True:
        df = request(option_origine,option_destination,option_date) # request the data

        if df.shape[0] == 0: # if no trains are available 
            st.write(' ')
            st.markdown("<h4 style='text-align: center; color: RoyalBlue;'>No trains available with TGV max membership for this moment </h4>", unsafe_allow_html=True)

        else : # if trains are available
            st.markdown("<h4 style='color: Black;'>Train list available with TGV Max membership :  </h4>", unsafe_allow_html=True)
            st.dataframe(df) # show the dataframe


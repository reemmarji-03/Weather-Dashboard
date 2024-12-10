import streamlit as st
import plotly.express as px 
from backend import get_data
import lookups

st.title(lookups.app_title)

place = st.text_input(lookups.text_input_statement)


days = st.slider(lookups.slider_title, min_value=lookups.min_forcasted_days, 
                 max_value=lookups.max_forcasted_days, 
                 help= lookups.slider_help_statement)

option = st.selectbox(lookups.select_box_statement,
                      (lookups.option_one, lookups.option_two))   

st.subheader(f"{option} for the next {days} days in {place}")

# get data
try:
    if place:

        filtered_data = get_data(place, days)

        if option==lookups.option_one:
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': "Dates", 'y':"Temperature (c)"})
            st.plotly_chart(figure)

        if option==lookups.option_two:
            columns = st.columns(8)
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]

            for index, condition in enumerate(sky_conditions):
                condition = condition.lower()
                with columns[index % 8]: 
                    st.image(f"images/{condition}.png", width=115)
except KeyError:
    st.text(lookups.invalid_place_error)       


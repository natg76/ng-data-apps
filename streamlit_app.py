import streamlit as slt
import pandas as pd

slt.title("Adhi's Cafe - New Healthy Diner")

slt.header("Breakfast menu")

slt.text("🥣  Idly, Vadai & Sambar")
slt.text("🥗 Bread Omlette")
slt.text("🐔 🥑🍞 Sausage, Bacon, Eggs, Hashbrown and Toast")

slt.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = slt.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
slt.dataframe(fruits_to_show)

slt.header("Fruityvice Fruit Advice!")

fruit_choice = slt.text_input('What fruit would you like information about?','Kiwi')
slt.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
slt.text(fruityvice_response.json())

# Normalize the JSON data into a data frame 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
slt.dataframe(fruityvice_normalized)


import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
slt.text("Hello from Snowflake:")
slt.text(my_data_row)

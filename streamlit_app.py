import streamlit as slt
import pandas as pd

slt.title("My parents new healthy diner")

slt.header("Breakfast menu")

slt.text("🥣  Idly, Vadai & Sambar")
slt.text("🥗 Bread Omlette")
slt.text("🐔 🥑🍞 Sausage, Bacon, Eggs, Hashbrown and Toast")

slt.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = slt.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avacado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
slt.dataframe(fruits_to_show)


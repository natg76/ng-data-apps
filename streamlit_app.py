import streamlit as slt
import pandas as pd

slt.title("My parents new healthy diner")

slt.header("Breakfast menu")

slt.text("🥣  Idly, Vadai & Sambar")
slt.text("🥗 Bread Omlette")
slt.text("🐔 🥑🍞 Sausage, Bacon, Eggs, Hashbrown and Toast")

slt.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

slt.dataframe(my_fruit_list)

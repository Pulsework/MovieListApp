import os
import streamlit as st

from deta import Deta

DETA_KEY = "b0lebgxq9jl_bWGx2X1SDMa7gvcKu88A2z7yr59nihyc"

# Load the environment variables
# DETA_KEY = st.secrets["DETA_KEY"]

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("movieListBase")

def insert_movie(title, year, comment, addedBy):
    """Returns the list of movies"""
    return db.put({"key": title, "year": year, "comment": comment, "addedBy": addedBy})

def fetch_all_movies():
    """Returns a dict of all movies"""
    res = db.fetch()
    return res.items

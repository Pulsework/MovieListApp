import os

from deta import Deta

# Load the environment variables
DETA_KEY = st.secrets["DETA_KEY"]

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("movieListBase")

def insert_movie(title, year, comment):
    """Returns the list of movies"""
    return db.put({"key": title, "year": year, "comment": comment})

def fetch_all_movies():
    """Returns a dict of all movies"""
    res = db.fetch()
    return res.items

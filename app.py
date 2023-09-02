import streamlit as st
from streamlit_option_menu import option_menu

import database as db # Local import

# ---------- SETTINGS -----------
movies = []
page_title = "Top Tier Movies"
layout = "centered"
# -------------------------------

st.set_page_config(page_title=page_title, layout=layout)
st.title(page_title)

st.subheader("A place to for you to add your favorite movies into a list.")
st.caption("What's up Jacob. You know what to do :film_projector:")

# --- Hide Streamlit Style ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

# --- Begin Body -----
title_format = '<p style="font-size: 20px; font-weight: bold; margin-bottom: 0; padding: 0;">Title</p>'
year_format = '<p style="font-size: 20px; font-weight: bold; margin-bottom: 0; margin-top:1.5em; padding: 0;">Release Year</p>'

# --- DATABASE INTERFACE ---
def get_all_movies():
    items = db.fetch_all_movies()
    movies = [item["key"] for item in items]
    return movies

# ----- NAV -------
selected = option_menu(
    menu_title=None,
    options=["Add Movie", "View Movie List"],
    icons=["pencil-fill", "list-columns-reverse"],
    orientation="horizontal",
)
if selected == "Add Movie":
    st.header("Add New Movie")
    with st.form("movie_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        st.markdown(title_format, unsafe_allow_html=True)
        st.text_input("", placeholder="Enter movie title", key="movieTitle")
        st.markdown(year_format, unsafe_allow_html=True)
        st.slider("", 1970, 2030, value=datetime.today().year, step=1, key="year")

        "---"
        with st.expander("Comment"):
            comment = st.text_area("", placeholder="Enter a comment for this movie...")

        "---"
        submitted = st.form_submit_button("Add Movie")
        if submitted:
            movie_title = str(st.session_state["movieTitle"])
            release_year = str(st.session_state["year"])
            db.insert_movie(movie_title, release_year, comment)
            st.success("Movie added!")

if selected == "View Movie List":
    st.header("Movie List")
    all_movies = db.fetch_all_movies()

    if len(all_movies) != 0:
        for item in all_movies:
            title = item.get("key")
            year = item.get("year")
            comment = item.get("comment")

            with st.expander(title):
                st.write(year)
                st.write(comment)

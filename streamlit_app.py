import streamlit as st
from multiapp import MultiApp
from apps import youtube


app=MultiApp()

st.title("""Programas hechos en python """)

app.add_app('Youtube Downloader',youtube.app)





app.run()
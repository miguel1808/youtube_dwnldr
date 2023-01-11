import streamlit as st
from pytube import YouTube
import time
from os import path,rename

def app():
    

    direccion= path.expanduser("~/Downloads")
    
    def barra():
        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
            

        with st.spinner("Espera un momento..."):
            time.sleep(5)
        st.write('DEscarga completada')
    

    def audio():
        try:
            audio_file = yt.streams.filter(only_audio=True).first().download(direccion)
            base , ext = path.splitext(audio_file)
            new_file = base + '.mp3'
            rename(audio_file, new_file)
            
        except:
            st.write("Error al descargar el audio")
    
    def video():
        try:
            yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download(direccion)
            
        except:
            st.write("Error al descargar el video")
    
    try:
        url= st.text_input("Ingresa el url del video ")
        yt = YouTube(str(url))

        st.subheader("Nombre del video a descargar")
        st.write(yt.title )
        st.write( "autor: "+ yt.author )
        
        if (st.button( "Descargar solo audio", on_click=audio )):
            barra()

        if (st.button( "Descargar el video ", on_click=video )):
            barra()
        
    
    except:
        st.write("Ingresar el link del video")
    

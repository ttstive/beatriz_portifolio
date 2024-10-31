import streamlit as st
from pathlib import Path
from PIL import Image
import base64


# Função para carregar arquivos CSS e HTML
def load_css(file_path):
    with open(file_path) as f:
        return f"<style>{f.read()}</style>"

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Escondendo o menu de configurações



about_me = st.Page(
    page= "views//about_me.py",
    title="Sobre mim",
    default=True
)


reportagem = st.Page(
    page = "views/reportagens.py",
    title="Reportagens",
    default=False

)

pg = st.navigation(pages=[about_me, reportagem])


pg.run()

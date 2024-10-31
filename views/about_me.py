import streamlit as st
from pathlib import Path
from PIL import Image
import base64
import os


# Função para carregar arquivos CSS e HTML
def load_css(file_path):
    with open(file_path) as f:
        return f"<style>{f.read()}</style>"

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Escondendo o menu de configurações
hide_streamlit_style = """
    <style>
       #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""



# Carregar CSS e HTML
css_file = "assets/style.css"
html_file = "sobremim.html"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(load_css(css_file), unsafe_allow_html=True)


# Carregar foto e currículo
profile_photo = "assets/WhatsApp Image 2024-10-12 at 14.17.39.jpeg"
curriculo = "assets/Currículo 2024 att.pdf"
linkedin_link = "https://www.linkedin.com/in/beatriz-souza-a38815206/"
instagram_links = "https://www.instagram.com/sou_biazz_/"


# Carregar PDF como base64
with open(curriculo, "rb") as pdf_file:
    pdf_Byte = base64.b64encode(pdf_file.read()).decode("utf-8")

st.title("Jornalista e Repórter")

col1, col2= st.columns([2,1])

with col1:
    st.header("Beatriz Soares de Souza")
    
    st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap" rel="stylesheet">
    <style>
    .custom-font {
        font-family: 'Roboto', sans-serif;  /* substitua 'Roboto' pela fonte desejada */
        font-size: 24px;
        color: #e1e1e1;;  /* cor do texto */
        font-weight: bold;  /* negrito */
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Texto com estilo customizado
    st.markdown(
    """
    <span class="custom-font">
    Repórter de cobertura política em Brasília pelo SBT Amazonas. Antes, repórter estagiária no portal Metropoles.
    </span>
    """, 
    unsafe_allow_html=True
)
    
    # Espaçamento
    st.write("")
    
    # Botão de download do currículo estilizado com HTML e CSS
    st.markdown(f"""
        <a href="data:application/octet-stream;base64,{pdf_Byte}" download="{curriculo}">
            <button class="download-button">💌 Baixar Currículo</button>
            <br>
        </a>
        """, unsafe_allow_html=True)
    
    # Espaçamento
    st.write("")
    st.write("")
    st.write("")

    
    # Botão para enviar e-mail
    email_destino = "http://soaresbeatriz483@gmail.com"
    assunto = "Olá Beatriz"
    corpo_mensagem = "Gostaria de saber mais sobre o seu trabalho."
    mailto_link = f"mailto:{email_destino}?subject={assunto}&body={corpo_mensagem}"

    st.markdown(f"""
        <a href="{mailto_link}" target="_blank">
            <button class="email-button">Entrar em Contato</button>
        </a>
        """, unsafe_allow_html=True)
    

st.write("")
st.write("")
st.write("")
with col2:
    st.image(profile_photo, width=350)
    st.write("")

@st.cache_data()
def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Caminho para o seu arquivo HTML
html_file = 'sobremim.html'

# Usar um estado de sessão para armazenar o timestamp da última modificação
if 'last_modified_time' not in st.session_state:
    st.session_state.last_modified_time = 0
    st.session_state.html_content = ""

# Verificar se o arquivo foi modificado
last_modified_time = os.path.getmtime(html_file)

if last_modified_time != st.session_state.last_modified_time:
    # Carregar e armazenar o conteúdo HTML se o arquivo foi modificado
    st.session_state.html_content = load_html(html_file)
    st.session_state.last_modified_time = last_modified_time

# Exibir conteúdo HTML
st.markdown(st.session_state.html_content, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")




col3, col4 = st.columns([3,4])





with col3:
    st.markdown(f"""
       
        <a href="{linkedin_link}" target="_blank">
         <img src="data:image/png;base64,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" width="100" class="linkedin-image">
        </a>

    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
       
        <a href="{instagram_links}" target="_blank">
         <img src="data:image/jpeg;base64,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"width= 100" class="linkedin-image">
        </a>

    """, unsafe_allow_html=True)

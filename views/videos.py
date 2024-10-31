import streamlit as st 

# Função para carregar arquivos CSS
def load_css(file_path):
    with open(file_path) as f:
        return f"<style>{f.read()}</style>"

# Carregar o CSS
st.markdown(load_css("assets/estilo.css"), unsafe_allow_html=True)

# Escondendo o menu de configurações
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Reportagens Especiais")

# Lista de vídeos
videos = [
    {"title": "Reportagem sobre desaparecimento de criança", "file": "assets/IMG_3220.mp4", "description": "Descrição da Reportagem 1 sobre o caso..."},
    {"title": "Reportagem 2", "file": "assets/IMG_3219.mp4", "description": "Descrição da Reportagem 2 sobre o caso..."},
]

# Layout em colunas para exibir os vídeos e suas descrições
for video in videos:
    col1, col2 = st.columns([1, 2])  # Ajuste a proporção conforme necessário
    with col1:
        st.video(video["file"])  # Exibir vídeo
    with col2:
        st.markdown(f'<h3>{video["title"]}</h3>', unsafe_allow_html=True)  # Título
        st.markdown(f'<p>{video["description"]}</p>', unsafe_allow_html=True)  # Descrição

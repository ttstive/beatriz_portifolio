import streamlit as st 

# Função para carregar arquivos CSS
def load_css(file_path):
    with open(file_path) as f:
        return f"<style>{f.read()}</style>"

# Carregar o CSS
st.markdown(load_css("assets/style.css"), unsafe_allow_html=True)

# Escondendo o menu de configurações
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Reportagens")

# Lista de vídeos
videos = [
    {"title": "Caso João Miguel", "file": "assets/WhatsApp Video 2024-10-31 at 12.42.46.mp4", "description": "O menino de apenas 10 está desaparecido há 11 dias. Familiares já espalharam cartazes e estão desesperados por notícias da criança."},
    {"title": "Jornalistas contra desinformação nas eleições", "file": "assets/IMG_2570.MP4", "description": "Durante evento de tecnologia contra desinformação, entrevistei a ministra Carmen Lúcia, presidente do TSE."},
    {"title": "Novo salário mínimo", "file": "assets/IMG_2885.MP4", "description": "Governo federal envia ao Congresso Nacional a previsão de aumento do salário mínimo em 2025."},
    {"title": "Queimadas na Amazônia", "file": "assets/IMG_4392.MP4", "description": "Governo federal e estadual buscam unir forças para combater os incêndios florestais e mitigar os efeitos da seca severa que afeta o Amazonas."},
    {"title": "Calor vai bater recorde no Distrito Federal:", "file": "assets/IMG_2890.MP4", "description": "A temperatura alta e baixa umidade do ar não vão dar trégua para o brasiliense tão cedo. O INMET explica o motivo."},
    {"title": "Entrada ao vivo: ", "file": "assets/IMG_4631.mp4", "description": "Entrevista feita ao vivo com o senador Confúcio Moura, diretamente do seu gabinete no Senado Federal. \n Falamos sobre obras públicas no estado do senador."}

]

# Layout em colunas para exibir os vídeos e suas descrições
for video in videos:
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.video(video["file"])  # Exibir vídeo com fundo branco
    with col2:
        st.markdown(f'<h3>{video["title"]}</h3>', unsafe_allow_html=True)  # Título
        st.markdown(f'<p>{video["description"]}</p>', unsafe_allow_html=True)  # Descrição
    st.markdown('</div>', unsafe_allow_html=True)

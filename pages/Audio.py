import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from model import transcriptActionExtractor # type: ignore

def audiotoText(audio_file):
    """Converts an uploaded audio file to text using SOpenAi Whisper.

    Args:
        audio_file: A Streamlit `UploadedFile` object containing the audio data.

    Returns:
        The transcribed text as a string, or None if an error occurs.
    """
    # Function to load API Key
    load_dotenv()
  
    client = OpenAI()
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    # print(transcription.text)
    return transcription.text



# Set page layout
st.set_page_config(page_title="Meet Focus")
os.environ["STREAMLIT_THEME"] = "dark"

# define main page streamlit style to hide few extra things
hide_streamlit_style= """
<style>
#MainMenu {visibility: hidden;}
.reportview-container .sidebar-content {display: none;}
.stDeployButton {visibility: hidden;}
#stDecoration {display: none;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# App Logo
logo_path = "logo.png"
# logo style
logo_style = """
<style>
.css-override {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
</style>
"""
st.markdown(logo_style, unsafe_allow_html=True)
# create a horizental container for the logo and title
col1, col2 = st.columns(2)

# display logo in the first column
with col1:
    st.image(logo_path, width=100)  # Adjust width as needed

# display tittle in second column
with col2:
    st.title("Meet Focus")

# Ask user ro upload audio file
audio_file = st.file_uploader("Upload Audio File; Max size 25MB", type=["wav", "mp3", "mp4", "mpeg", "mpga", "m4a", "webm"])

if audio_file:
    # convert audio to text
    text = audiotoText(audio_file)
    
    # extract actions
    if text:
        response = transcriptActionExtractor(text)
        st.write(response) 

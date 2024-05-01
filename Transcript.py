import os
import streamlit as st
from model import transcriptActionExtractor  # type: ignore

def main():
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

    
    # Chat Input
    prompt = st.chat_input("Enter Meeting transcript")
    
    # pass transcript to a model
    if prompt:
        response = transcriptActionExtractor(prompt)
        st.write(response) 




# call function
if __name__ =='__main__':
    main()
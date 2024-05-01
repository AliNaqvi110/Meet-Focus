# Meet Focus

# Introduction
<p>This project offers a user-friendly Streamlit application (MITAI) that streamlines the process of extracting actionable items from meeting transcripts. It caters to both text input and audio uploads, making it a versatile tool for capturing key takeaways from your meetings.</p>

# Features:
1. <b>Text Input:</b> Effortlessly paste your meeting transcript directly into the designated text field.<br>
2. <b>Audio Upload:</b> Upload audio files in various formats (wav, mp3, mp4, mpeg, mpga, m4a, webm) for automatic transcription.<br>
3. <b>OpenAI Whisper Integration:</b> Leverages the power of OpenAI Whisper to generate accurate transcripts from uploaded audio files.<br>
4. <b>Amazon Titan Text G1 Express Integration:</b> Analyzes transcripts (from text or audio) using Amazon Titan Text G1 Express to identify actionable items and assign them to specific participants mentioned in the transcript.<br>
5. <b>Action Item Display:</b> Provides a clear and concise list of extracted action items, including the assignee (if identified) and a detailed description.<br>

# Benefits:
1. <b>Increased Efficiency:</b> Saves valuable time by automating the action item extraction process.<br>
2. <b>Improved Accuracy:</b> Reduces the risk of missing important points by leveraging advanced AI technology.<br>
3. <b>Enhanced Collaboration:</b> Facilitates clear communication and task delegation by assigning action items to participants.<br>
4. <b>Accessibility:</b> Supports both text input and audio uploads, catering to various meeting recording preferences.<br>

# Dependencies and Installation
<p>To install the Gemini Pro Pdf Chatbot, please follow these steps:</p>

1. Clone the repository to your local machine.<br>

2. Install the required dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.

    ```shell
    OPENAI_API_KEY=your_secret_api_key
    ```

4. Setup your AWS Configuration in your local environment.


## Usage

To use the Meet Focus, follow these steps:

1. Ensure that you have installed the required dependencies, configure the AWS environment locally, and added the Open API key to the `.env` file.

2. Run the `app.py` file using the Streamlit CLI. Execute the following command:

    ```
    streamlit run Transcript.py
    ```

3. The application will launch in your default web browser, displaying the user interface.

4. Paste Meeting transcript in the chat input and you will receive results.

5. Select Audio from the sloder and upload audio file of the meeting. Actions will be displayed.

## Contributing
<p>We welcome contributions from the community to improve and expand Gemini Meet Focus. If you have suggestions or would like to contribute, please create a pull request or open an issue.</p>

## License
<p>Meet Focus App is licensed under the MIT License.</p>



# Problem1-Sentiment-Analysis

It is a web application built with Flask that allows users to upload audio files for sentiment analysis. The application utilizes AssemblyAI's transcription and sentiment analysis capabilities to analyze the emotions and sentiments expressed in the audio content.

## Screenshot
![Web App Screenshot](https://github.com/gulshan-100/Problem1-Sentiment-Analysis/blob/main/Screenshot-demo.png)


## Features
1. Upload audio files in various formats (MP3, WAV, OGG, FLAC).
2. Transcribe audio and perform sentiment analysis.
3. View detailed sentiment analysis results including text, sentiment, confidence, start, and end times.

## Installation 
To get started with this project, follow these steps:

1. Clone this repository
```
git clone https://github.com/yourusername/Problem1-Sentiment-Analysis.git
cd Problem1-Sentiment-Analysis
```
2. Set Up a Virtual Environment
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Set Up Environment Variables
```
aai.settings.api_key = <Your_API_Key>
```
5. Run the Application
```
python app.py
```
The application will start on `http://127.0.0.1:5000/`.

## USAGE
1. **Open Your Browser**

    Navigate to `http://127.0.0.1:5000/` to access the frontend interface.

2. **Upload an Audio File**

    Click the file input to select an audio file from your computer and submit it. Supported file formats are MP3, WAV, OGG, and FLAC.

3. **View Results**

    After uploading, the application will process the audio and display sentiment analysis results including text segments, sentiment, confidence, start, and end times.






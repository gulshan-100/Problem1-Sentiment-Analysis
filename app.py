
from flask import Flask, request, jsonify, send_from_directory
import io
import assemblyai as aai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

# Set your AssemblyAI API key
aai.settings.api_key = "api-key"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        try:
            # Initialize AssemblyAI transcriber
            transcriber = aai.Transcriber()

            # Read the file into memory
            file_stream = io.BytesIO(file.read())

            # Set up transcription configuration
            config = aai.TranscriptionConfig(sentiment_analysis=True)
            
            # Transcribe the audio file
            transcript = transcriber.transcribe(file_stream, config)

            # Extract sentiment analysis results
            sentiment_results = [
                {
                    'text': result.text,
                    'sentiment': result.sentiment,
                    'confidence': result.confidence,
                    'start': result.start,
                    'end': result.end
                }
                for result in transcript.sentiment_analysis
            ]

            return jsonify({'results': sentiment_results})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'File type not allowed'}), 400

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg', 'flac'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

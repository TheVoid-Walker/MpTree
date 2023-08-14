from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    mp4_file = request.files['file']
    new_name = request.form['new_name']
    youtube_link = request.form.get('youtube_link')  # Use get() method

    if mp4_file and mp4_file.filename.endswith('.mp4'):
        mp3_file = new_name if new_name else mp4_file.filename.replace('.mp4', '.mp3')

        mp4_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(mp4_file.filename))
        mp3_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(mp3_file))

        mp4_file.save(mp4_path)

        try:
            ffmpeg_extract_audio(mp4_path, mp3_path)
            os.remove(mp4_path)  # Delete the uploaded MP4 file

            return render_template('download.html', mp3_path=mp3_file)
        except Exception as e:
            return f"An error occurred: {e}"
    elif youtube_link:
        modified_link = youtube_link.replace("youtube.com", "ssyoutube.com")
        return f"Modified link: {modified_link}"
    else:
        return "Please upload a valid MP4 file or paste a YouTube link."




@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], secure_filename(filename), as_attachment=True)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
import re
from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    format = request.form['format']

    youtube_regex = r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})'
    match = re.match(youtube_regex, video_url)
    if not match:
        return "Invalid YouTube link."

    try:
        youtube = YouTube(video_url)
        if format == 'video':
            video = youtube.streams.get_highest_resolution()
            video_filename = video.download()
            response = send_file(video_filename, as_attachment=True)
            os.remove(video_filename)
            return response
        elif format == 'audio':
            audio = youtube.streams.get_audio_only()
            audio_filename = audio.download()
            mp3_filename = audio_filename.split('.')[0] + '.mp3'
            os.rename(audio_filename, mp3_filename)
            response = send_file(mp3_filename, as_attachment=True)
            os.remove(mp3_filename)
            return response
        else:
            return "Invalid download format."
    except:
        return "An error occurred during download."

if __name__ == '__main__':
    app.run()

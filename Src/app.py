from flask import Flask, render_template, redirect, request, flash, session, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import random
import uuid
import mutagen
import librosa
import urllib
from mutagen.wave import WAVE
from pathlib import Path
from pydub import AudioSegment

UPLOAD_FOLDER = '..\Data\Gen_Audio'

app = Flask(__name__)
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=LAPTOP-Q0DB1ITI\SQLEXPRESS;DATABASE=DB;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

#app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://LAPTOP-Q0DB1ITI\SQLEXPRESS/DB?driver=SQL+Server?trusted_connection=yes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"
db = SQLAlchemy(app)


@app.route('/save-record', methods=['POST'])
def save_record():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    file_name = str(uuid.uuid4()) + ".mp3"
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    pack = {"status": "Good", "filename": full_file_name}
    update_sql_audio(pack)
    return pack
    
# Define Modules for storing Text and Audio Path
class TextAudioPair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    audio = db.Column(db.String(200), default="path/to/your/wav/file")
    duration = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Task {self.id}>"

def get_audio_duration(filename):
    src = filename
    dst = filename.replace(".mp3", ".wav")
    
    # convert mp3 to wav                                                            
    sound = AudioSegment.from_file(src)
    sound.export(dst, format="wav")
    y, sr = librosa.load(Path(dst))
    duration = librosa.get_duration(y=y, sr=sr)
    return duration

def update_sql_audio(data):
    sql_id = session.get("ID")
    file_path = data["filename"]
    before = TextAudioPair.query.get(sql_id)
    before.id = sql_id
    before.audio = file_path.replace(".mp3", ".wav")
    before.duration = get_audio_duration(file_path)
    db.session.commit()

@app.route("/", methods=["GET"])
def index():
    pairs = TextAudioPair.query.all()
    selected_pairs = []
    idx_selected_pairs = []
    for idx, pair in enumerate(pairs):

        if pair.audio == "path/to/your/wav/file":
            selected_pairs.append(pair)
            idx_selected_pairs.append(idx)
        
    len_of_pairs = len(selected_pairs)
    rand = random.randint(0, len_of_pairs-1)
    session["ID"] = idx_selected_pairs[rand]+1
    #session["pair"]=pairs[idx_selected_pairs[rand]]
    return render_template("index.html", pair=pairs[idx_selected_pairs[rand]])

if __name__ == "__main__":
    app.run(debug=True)
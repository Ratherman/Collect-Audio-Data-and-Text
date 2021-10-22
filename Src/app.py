from flask import Flask, render_template, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
import os
import random
import uuid

UPLOAD_FOLDER = '..\Data\Gen_Audio'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://LAPTOP-Q0DB1ITI\SQLEXPRESS/DB?driver=SQL+Server?trusted_connection=yes"
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

    def __repr__(self):
        return f"<Task {self.id}>"
def update_sql_audio(data):
    sql_id = session.get("ID")
    file_path = data["filename"]

    before = TextAudioPair.query.get(sql_id)
    before.id = sql_id
    before.audio = file_path
    db.session.commit()

@app.route("/", methods=["GET"])
def index():
    pairs = TextAudioPair.query.limit(5).all()
    len_of_pairs = len(pairs)
    target_index = random.randint(0, len_of_pairs-1)
    session["ID"] = target_index+1
    return render_template("index.html", pair=pairs[target_index])

if __name__ == "__main__":
    app.run(debug=True)
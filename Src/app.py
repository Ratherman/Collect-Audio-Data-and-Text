from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pyaudio
import os
import uuid

UPLOAD_FOLDER = 'files'



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://LAPTOP-Q0DB1ITI\SQLEXPRESS/DB?driver=SQL+Server?trusted_connection=yes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

# Add on 10/20
@app.route('/')
def root():
    return app.send_static_file('index.html')

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
    return '<h1>Success</h1>'

# # Define Modules for storing Text and Audio Path
# class TextAudioPair(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(500), nullable=False)
#     audio = db.Column(db.String(200), default="path/to/your/wav/file")

#     def __repr__(self):
#         return f"<Task {self.id}>"

# @app.route("/", methods=["GET"])
# def index():
#     pairs = TextAudioPair.query.all()
#     return render_template("index.html", pairs=pairs)

if __name__ == "__main__":
    app.run(debug=True)
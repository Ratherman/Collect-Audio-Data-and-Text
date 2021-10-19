from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://LAPTOP-Q0DB1ITI\SQLEXPRESS/DB?driver=SQL+Server?trusted_connection=yes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define Modules for storing Text and Audio Path
class TextAudioPair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    audio = db.Column(db.String(200), default="path/to/your/wav/file")

    def __repr__(self):
        return f"<Task {self.id}>"

@app.route("/", methods=["GET"])
def index():
    pairs = TextAudioPair.query.all()
    return render_template("index.html", pairs=pairs)

if __name__ == "__main__":
    app.run(debug=True)
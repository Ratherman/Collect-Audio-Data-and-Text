# Collect-Audio-Data-and-Text
#### Video Demo:  <URL HERE>
#### Description:

# About Me:
* My Name: Eric Cheng
* City and Country: Tainan, Taiwan
* Contact Info: [ratherman5796@gmail.com](ratherman5796@gmail.com)
* [Github Repo](https://github.com/Ratherman/Collect-Audio-Data-and-Text)
* Lastest Updated Date: 2021/10/30

# About this Project:
* Purpose:
    * The purpose is to help AI Teams to collect audio-and-text pairs of data. With tons of pairs of data collected, it's likely to teach a Text-To-Speech AI model to speak!
    * ![](https://github.com/Ratherman/Collect-Audio-Data-and-Text/blob/main/Src/static/img/tts.jpg)

# File Structure:
- Data/
    - Gen_Audio/ # This folder is used to store the generated recordings.
- Src/
    - static/
        - css/
            - main.css # Somehow beautify the user interfacec.
        - img/
            - tts.jpg # This picture will be showed once index page is loaded.
    - templates/
        - base.html # Base template of webpage.
        - index.html # Homepage of my project.
    - app.py # Core src code, mostly follow the framework of Flask
    - Insert Data To Db.ipynb # Use this notebook to (1) get posts , (2) split them into words and sentences, and (3) insert texts into DB.
- .gitignore
- README.md

# Project Structure:
* Database: Microsoft SQL
    * For each row of data, it contains (1) text/sentence, (2) path of audio file, (3) duration.
    * (1) text/sentence
        * Source: https://www.theguardian.com/uk
        * After crawl the posts from the above mentioned link, split them into words and sentences and insert into DB.
    * (2) path of audio file
        * The path will be decided after we finished recording the word/sentence.
        * After the recording generates, the corresponding path will be inserted into DB.
    * (3) duration
        * "Duration" means duration of a certain recordings. It's usually no more than 15 sec.
        * This attribute will be decided once the recoding is generated. 
* Framework: Flask
    * Use flask_sqlalchemy to TALK to DB.
    * After setting up the environment, use `flask run` to trigger this project.

# Setup Setting up Env
* Step 1: Make sure you've installed anaconde.
* Step 2: `conda create -n "CADAT" python=3.8`
* Step 3: `conda activate CADAT`
* Step 4: `pip install jupyter notebook`
* Step 5: `pip install beautifulsoup4`
* Step 6: `pip install requests`
* Step 7: `pip install numpy`
* Step 8: `pip install pandas`
* Step 9: `pip install pyodbc`
* Step 10: `pip install flask-sqlalchemy`
* Step 11: `pip install flask`
* Step 12: `pip install ffmpeg`
* Step 13: `pip install pydub`
* Step 13: Download [ffmpeg.exe](https://www.ffmpeg.org/download.html) for your OS, and then append this .exe file your into your **path**.

# About How to ... please check:
* [How to Connect Flask to MSSQL?](https://github.com/Ratherman/Collect-Audio-Data-and-Text#how-to-connect-flask-to-mssql)
* [How to install MSSQL on Windows 10?](https://github.com/Ratherman/Collect-Audio-Data-and-Text#how-to-install-mssql-on-windows-10)

## How to Connect Flask to MSSQL?
* Watch this [YouTube Video](https://www.youtube.com/watch?v=Z1RJmh_OqeA) for basic Flask implementation.
* Read this [StackoverFlow](https://stackoverflow.com/questions/46739295/connect-to-mssql-database-using-flask-sqlalchemy) Forum for connecting Flask to MSSQL.
* Step 1: Import packages
```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

```
* Step 2: Configure **app** and Create **db** instance
```
app = Flask(__name__)

params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=HARRISONS-THINK;DATABASE=LendApp;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
```

* Step 3: Setup the table (Demo)
```
class audio_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    audio_path = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return "<Content %r>" % self.content
```

* Step 4: Create Database
* Go to command line (anaconda prompt) and do the following:
* `python`
* `from app import db`
* `db.create_all()`

## How to install MSSQL on Windows 10?
* If needed, you're encouraged to follow this [Tutorial](https://www.guru99.com/download-install-sql-server.html).
* Step 1: Go to this [website](https://www.microsoft.com/en-in/sql-server/sql-server-downloads) and download the express version, i.e., SQL Server 2019 Express.
* Step 2: Open the **.exe** file.
* Step 3: Choose the **Basic** option.
* Step 4: Click **Accept** and **Choose the installed location**.
* Step 5: Create a database named DB, which will be the one we used in this project.
* (Optional) Step 5: Click **Install SSMS** and a webpage would be popped up.
* (Optional) Step 6: Click the hypytertext **"下載 SQL Server Management Studio (SSMS) 18.10"**.
* (Optional) Step 7: Open the **.exe** file.
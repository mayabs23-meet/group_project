from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyASx2vWHHg418m4HX4eKbxOrIqC75zACo8",
  "authDomain": "meet---2022.firebaseapp.com",
  "projectId": "meet---2022",
  "storageBucket": "meet---2022.appspot.com",
  "messagingSenderId": "115400578724",
  "appId": "1:115400578724:web:a8565930f311175a6db831",
  "measurementId": "G-G009ZDNMKG",
  "databaseURL": "https://meet---2022-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


#routes















#routes


if __name__ == '__main__':
    app.run(debug=True)
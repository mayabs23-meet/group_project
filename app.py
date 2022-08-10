from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



config={
    
 'apiKey' : "AIzaSyAJtm7Cq1a6b1QLQjhKmPOe8E3fksBCiqs",

  'authDomain' : "group-project-4e0f3.firebaseapp.com",

  'databaseURL' : "https://group-project-4e0f3-default-rtdb.europe-west1.firebasedatabase.app",

  'projectId' : "group-project-4e0f3",

  'storageBucket' : "group-project-4e0f3.appspot.com",

  'messagingSenderId' : "186968763610",

  'appId' : "1:186968763610:web:6117e386dd366e351289e3",

  'measurementId' : "G-L4Q7MTF9JG"

}



firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()
app=Flask(__name__)




app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'




@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return render_template('index.html')
        except:
           error = "Authentication failed"
           return error
        return render_template("signin.html")
    else:
        return render_template("signin.html")





@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return render_template('index.html')
        except:
           error = "Authentication failed"
           return error
        return render_template("signup.html")
    else:
        return render_template("signup.html")




@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=="POST":
        name = request.form['vname']
        email=request.form["vemail"]
        ID=request.form["vid"]
        hours=request.form["vhours"]
        volunteer={"name":name,"email":email,"ID":ID,"hours":hours}
        print(volunteer)
        #db.push("volunteers").get(volunteers)
        all_volunteers = db.child("volunteers").get().val()
        if ID in all_volunteers:
           volunteer_from_db = db.child("volunteers").child(ID).get().val() 
           volunteer_from_db["hours"] += hours
           db.child("volunteers").child(ID).uptade(volunteer_from_db)
        else:
            db.child("volunteers").child(ID).set(volunteer)
        total_hours = db.child("volunteers").child(ID).get().val()["hours"]

        return render_template("index.html", message="You volunteered a total of " + str(total_hours) + "! Thanks!!")
    else:
        return render_template("index.html")
        

    





if __name__ == '__main__':
    app.run(debug=True)





    
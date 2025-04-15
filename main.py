from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Database configuration (SQLite in this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a sample table/model
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.username}>"

# Create the database and tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/doctor")
def doctor():
    return render_template("doctor.html")


@app.route("/appointment")
def appointment():
    return render_template("appointment.html")


@app.route("/staff")
def staff():
    return render_template("staff.html")

@app.route('/patient')
def patient():
    return render_template('patient.html')  # Note the space before .html

@app.route('/doctor_login')
def doctor_login():
    return render_template("doctor_login.html")  # Note the space before .html

@app.route("/doctor_signin")
def doctor_signin():
    return render_template("doctor_signin.html")  # Note the space before .html






if __name__ == "__main__":
    app.run(debug=True)



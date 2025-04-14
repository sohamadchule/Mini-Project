from flask import Flask, render_template,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("sample.html")

@app.route("/doctor")
def doctor():
    return render_template("doctor.html")

@app.route("/staff")
def staff():
    return render_template("staff.html")

if __name__ == "__main__":
    app.run(debug=True)



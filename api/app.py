from flask import app, Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/artes")
def artes():
    return render_template("Artes.html")

@app.route("/Break-In-Time")
def BIT():
    return render_template("Break_in_Time.html")

@app.route("/Projeto_Integrador")
def API():
    return render_template("Projeto_Integrador.html")


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/samples")
def samples():
	return render_template("samples.html")

@app.route("/resume")
def resume():
	return render_template("resume.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/photography")
def photography():
	return render_template("photography.html")

if __name__ == "__main__":
	app.run(debug=True)
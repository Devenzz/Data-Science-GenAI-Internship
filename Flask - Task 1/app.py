from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        user_text = request.form.get("username")
        result = user_text.upper()

    return render_template("index.html", output=result)

if __name__ == "__main__":
    app.run(debug=True)
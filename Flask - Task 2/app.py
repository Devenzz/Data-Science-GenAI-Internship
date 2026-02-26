from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    regex = ""
    text = ""
    highlighted_text = ""

    if request.method == "POST":

        regex = request.form.get("regex").strip()
        text = request.form.get("text").strip()

        try:
            if re.fullmatch(regex, text):
                #highlighted_text = f"<b>{text}</b>"
                highlighted_text = f"<span class='highlight'>{text}</span>"

            else:
                highlighted_text = "No Match Found"

        except:
            highlighted_text = "Invalid Regex Pattern"
            
            
    return render_template(
        "index.html",
         highlighted_text=highlighted_text,
         regex=regex,
        text=text
    )


    #return render_template(
       # "index.html",
      #  highlighted_text=highlighted_text
    #)

if __name__ == "__main__":
    app.run(debug=True, port=5002
)

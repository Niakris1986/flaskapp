from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]
        city = request.form["city"]
        language = request.form["language"]
        return render_template(
            "result.html", name=username, age=age, city=city, language=language)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

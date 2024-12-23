import secrets

from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    number1, number2, operation = request.form["number1"], \
                                  request.form["number2"], request.form["operation"]

    try:
        num1, num2 = int(number1), int(number2)
        match operation:
            case "add":
                result = num1 + num2
                flash(f"Результат: {result}")
            case "multiply":
                result = num1 * num2
                flash(f"Результат: {result}")
            case "power":
                result = num1 ** num2
                flash(f"Результат: {result}")
            case "divide":
                try:
                    result = num1 // num2
                    flash(f"Результат: {result}")
                except ZeroDivisionError as e:
                    flash(f"Ошибка: деление на ноль!")
    except ValueError:
        flash("Ошибка, введите корректные числа")

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

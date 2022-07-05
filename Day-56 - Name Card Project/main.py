# .............................. Name Card ................................ #
# ............. Created and modified by N.S.Bhanuprakash on 16-05-2022 .....#

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def name_card():
    return render_template("/index.html")


if __name__ == "__main__":
    app.run(debug=True)

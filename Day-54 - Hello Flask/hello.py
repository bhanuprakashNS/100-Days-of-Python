# ......................  Flask server .................................... #
# ............. Created and modified by N.S.Bhanuprakash on 11-05-2022 .....#
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align : center">Hello, World!</h1>' \
           '<p>This is a gif image</p>' \
           '<img src="https://media4.giphy.com/media/1lk1IcVgqPLkA/giphy.webp?' \
           'cid=ecf05e47m48zpb5ewlgtjqfbrif7aju3aatxloey7e7p4y48&rid=giphy.webp&ct=g">'


def make_bold(function):

    def made_bold():
        string = function()
        return f"<b>{string}</b>"

    return made_bold


def make_italic(function):

    def made_italic():
        string = function()
        return f"<em>{string}</em>"

    return made_italic


def make_underline(function):

    def made_underline():
        string = function()
        return f"<u>{string}</u>"

    return made_underline


@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "bye!"


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name} and your lucky number is {number}!"


if __name__ == "__main__":
    app.run(debug=True)

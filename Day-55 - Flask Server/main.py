# ............ Higher-Lower Game through Flask server ..................... #
# ............. Created and modified by N.S.Bhanuprakash on 15-05-2022 .....#

from flask import Flask
import random

rand_number = random.randint(0, 10)
print(rand_number)

app = Flask(__name__)


@app.route("/")
def guess_number():
    return '<h1>Guess a number between 0 to 9!</h1>' \
           '<img src="https://media3.giphy.com/media/eCAoHEREmZtCtsaosu/200w.webp?' \
           'cid=ecf05e47du5ichyimn1locbvy8cvqovatjqia9rdtn9rnj32&rid=200w.webp&ct=g">'


@app.route("/<int:number>")
def get_number(number):
    user_number = number
    if user_number > rand_number:
        return f'<h1 style="color:blue">Guessed number is too high!</h1>' \
               f'<img src="https://media4.giphy.com/media/3o72FgCqjuQGeF90Nq/100.webp?' \
               f'cid=ecf05e47bjgel3530zg71475dzmgfneuk0tk6zu2n3hodofu&rid=100.webp&ct=g">'
    elif user_number < rand_number:
        return f'<h1 style="color:red">Guessed number is too low!</h1>' \
               f'<img src="https://media2.giphy.com/media/j5bsZqX1KTKngMyu90/200w.webp?' \
               f'cid=ecf05e47kvj0ngphooebmthpqwvd5pqpvc7ci68wa540tkg6&rid=200w.webp&ct=g">'
    else:
        return f'<h1 style="color:green">You guessed it correct!</h1>' \
               f'<img src="https://media1.giphy.com/media/D0pY2cCYaJBcQ5v4Cs/200w.webp?' \
               f'cid=ecf05e471akv8jeift6ly4x4cp948fcl7lrxbqbwo0n1sgev&rid=200w.webp&ct=g">'


if __name__ == "__main__":
    app.run(debug=True)



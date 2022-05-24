# ........... Flash Card - A Language memorising app .................... #
# ......... Created and Modified by N.S.Bhanuprakash on 09-04-2022 ....... #
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FROM_LANGUAGE = "French"
TO_LANGUAGE = "English"
number = None

words_data = pandas.read_csv("./data/french_words.csv")
words_dict = words_data.to_dict("dict")
# remaining_words = words_data.to_dict("list")
# print(remaining_words)
# # print(f"{remaining_words['English'].index('part')}")
words_to_learn = {"French": [], "English": []}
words_to_learn_dict = {"French": "English"}
# print(words_dict)

# ---------------------------- Access Data ------------------------------- #


def generate_number():
    global number
    number = random.randint(0, len(words_data)-1)
    return number


def translate(value):
    global number
    if number is None:
        pass
    else:
        canvas_front.itemconfig(language_label, text=f"{TO_LANGUAGE}", fill="white")
        canvas_front.itemconfig(card_background, image=card_back_image)
        english_meaning = words_dict[value][number]
        canvas_front.itemconfig(word_label, text=f"{english_meaning}", fill="white")
        if english_meaning in words_dict["English"] or english_meaning in words_to_learn["English"]:
            pass
        else:
            words_to_learn["English"].append(english_meaning)
            words_to_learn["French"].append(words_dict["French"][number])

        words_to_learn_dict[words_dict["French"][number]] = english_meaning

        data = pandas.DataFrame(words_to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)


def generate_word(value):
    global words_dict

    if value == "French":

        random_number = generate_number()
        # print("right")
        canvas_front.itemconfig(language_label, text=f"{FROM_LANGUAGE}", fill="black")
        canvas_front.itemconfig(card_background, image=card_front_image)
        random_french_word = words_dict[value][random_number]
        canvas_front.itemconfig(word_label, text=f"{random_french_word}", fill="black")

        # print(random_french_word)
        # french_list = remaining_words[value]
        # # print(french_list)
        # index = list(french_list).index(f"{random_french_word}")
        # # print(index)
        # translated_meaning = remaining_words["English"][index]
        # # print(translated_meaning)
        # del list(remaining_words[value])[index]
        # print(len(list(remaining_words[value])))
        # print(list(remaining_words[value]))
        # # list(remaining_words["English"]).remove(translated_meaning)
        # del list(remaining_words["English"])[index]
        # pending_words = pandas.DataFrame(remaining_words)
        # pending_words.to_csv("remaining_words.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(string="Flash Card App")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

canvas_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas_front.create_image(400, 263, image=card_front_image)
canvas_front.grid(row=0, column=0, columnspan=2)
language_label = canvas_front.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_label = canvas_front.create_text(400, 263, text="", font=("Arial", 60, "bold"))

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=lambda value="French": generate_word(value))
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=lambda value="English": translate(value))
wrong_button.grid(row=1, column=0)

generate_word("French")

window.mainloop()

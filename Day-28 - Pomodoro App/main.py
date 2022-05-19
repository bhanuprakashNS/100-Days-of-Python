# ........................... Pomodoro App ................................ #
# ............. Created and modified by N.S.Bhanuprakash on 06-04-2022 .....#
import time
from tkinter import *
import itertools
from tkinter import simpledialog

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

reps = 8
check_mark = ""
timer = None
pause = itertools.cycle([1, 0])
value = 0
time_now = 0

# -------- Initialising main window and updating work and break times ---- #

window = Tk()
window.update_idletasks()
WORK_MIN = simpledialog.askinteger(title="Work Time Duration", prompt="What's your work time in minutes?")
if WORK_MIN is None:
    WORK_MIN = 0.1
SHORT_BREAK_MIN = simpledialog.askinteger(title="Short Break Time Duration", prompt="What's your Short Break time in minutes?")
if SHORT_BREAK_MIN is None:
    SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = simpledialog.askinteger(title="Long Break Time Duration", prompt="What's your Long Break time in minutes?")
if LONG_BREAK_MIN is None:
    LONG_BREAK_MIN = 0.1

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global value, check_mark
    window.after_cancel(timer)
    timer_label.config(text="Timer", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=GREEN)
    count_label.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
    global reps
    reps = 0
    check_mark = ""
    value = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, value
    value = 0
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    if reps % 8 == 0:
        timer_label.config(text="Long Break", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work Time", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps, check_mark, value, time_now
    time_now = count
    count_min = time_now//60
    count_sec = time_now % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # Pausing the program and showing current time
    if value == 1:
        timer_label.config(text="Paused", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=RED)
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Continuing the program and count-down
    elif value == 0:
        if reps % 8 == 0:
            timer_label.config(text="Long Break", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=RED)
        elif reps % 2 == 0:
            timer_label.config(text="Short Break", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=PINK)
        else:
            timer_label.config(text="Work Time", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=GREEN)

        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        # Begins Count-down
        if count > 0:
            global timer
            timer = window.after(1000, count_down, time_now-1)
        # Switches between work time and breaks by calling start_timer function,
        # Also counting number of pomodoros
        else:
            start_timer()
            if reps % 2 == 0:
                check_mark += "✔"
                count_label.config(text=check_mark)


# ---------------- ADD PAUSE/CONTINUE FUNCTIONALITY ------------------- #


def pause_continue():
    global value, time_now
    value = next(pause)
    print(value)
    if value == 0:
        count_down(time_now)


# ---------------------------- UI SETUP ------------------------------- #


# window = Tk()
window.title("Pomodoro - The Time Management App")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=PINK, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=PINK, command=reset_timer)
reset_button.grid(row=2, column=2)

count_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
count_label.grid(row=3, column=1)

pause_button = Button(text="Pause/Continue", bg=PINK, command=pause_continue)
pause_button.grid(row=4, column=2)

time.sleep(0.5)

# window.update_idletasks()

# work = simpledialog.askinteger(title="Work Time Duration", prompt="What's your work time in minutes?")
# short = simpledialog.askinteger(title="Short Break Time Duration", prompt="What's your Short Break time in minutes?")
# long = simpledialog.askinteger(title="Long Break Time Duration", prompt="What's your Long Break time in minutes?")

window.mainloop()

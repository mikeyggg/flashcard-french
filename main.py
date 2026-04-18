import tkinter
import pandas

BACKGROUND_COLOR = "#B1DDC6"
TOP_TEXT = ("Ariel",40,"italic")
BOTTOM_TEXT = ("Ariel",60,"bold")


try:
    words = pandas.read_csv('./data/words_to_learn.csv')
except:
    words = pandas.read_csv('./data/french_words.csv')



current_word = words.sample()


def flip_cards():
    card.delete("all")
    card.grid(row=0, column=0, columnspan=2)
    card.create_image(0, 0, image=back_images, anchor="nw")
    card.create_text(400, 150, text="English", font=TOP_TEXT)
    card.create_text(400, 263, text=current_word["English"].values[0], font=BOTTOM_TEXT)


def new_word():
    global current_word
    global TIMER
    current_word = words.sample()
    screen.after_cancel(TIMER)

    card.delete("all")
    card.grid(row=0, column=0, columnspan=2)
    card.create_image(0, 0, image=front_image, anchor="nw")
    card.create_text(400, 150, text="French", font=TOP_TEXT)
    card.create_text(400, 263, text=current_word["French"].values[0], font=BOTTOM_TEXT)
    TIMER = screen.after(3000,flip_cards)



def learned_word():
    global current_word
    global words

    words = words.drop(current_word.index[0])
    words.to_csv('./data/words_to_learn.csv', index=False)


def known_word():
    learned_word()
    new_word()






screen = tkinter.Tk()
screen.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
screen.geometry("900x700")
TIMER = screen.after(3000,flip_cards)


front_image = tkinter.PhotoImage(file="./images/card_front.png")
back_images = tkinter.PhotoImage(file="./images/card_back.png")

card = tkinter.Canvas(screen, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(row=0, column=0, columnspan=2)
card.create_image(0, 0, image=front_image, anchor="nw")
card.create_text(400, 150, text="French", font = TOP_TEXT)
card.create_text(400, 263, text= current_word["French"].values[0], font = BOTTOM_TEXT)



right_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image= right_image,highlightthickness=0,bd= 0,bg=BACKGROUND_COLOR,command=known_word)
right_button.grid(row=1,column=1)

wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image= wrong_image,highlightthickness=0,bd = 0,bg=BACKGROUND_COLOR,command=new_word)
wrong_button.grid(row=1,column=0)



screen.mainloop()
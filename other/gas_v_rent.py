
import tkinter
import pandas as pd

full_year = pd.read_pickle('data/full_year_dat_pickle.pkl')
gas = pd.read_pickle('data/gas_dat_pickle.pkl')

# Create window
window = tkinter.Tk()
window.title("Rectangle")

# Create a canvas
canvas = tkinter.Canvas(window, width=500, height=1000)

# Create a rectangle
square = canvas.create_rectangle(50, 150, 250, 350, fill='red', tags="square", width=0)
square2 = canvas.create_rectangle(50, 150, 250, 350, fill='black', tags="square2")
square3 = canvas.create_rectangle(50, 500, 250, 700, fill='red', tags="square3", width=0)
square4 = canvas.create_rectangle(50, 500, 250, 700, fill='black', tags="square4")

# Create a button
year = 2011
num = 0


def next_year():
    """

    """
    global year
    global num
    if year < 2018:
        year += 1
        num += 1
        canvas.coords(square2, 50 + full_year.iloc[num]['shift'], 150 + full_year.iloc[num]['shift'],
                      50 + full_year.iloc[num]['size'],
                      150 + full_year.iloc[num]['size'])
        canvas.coords(square4, 50 + gas.iloc[num]['shift'], 500 + gas.iloc[num]['shift'],
                      50 + gas.iloc[num]['size'],
                      500 + gas.iloc[num]['size'])
        if full_year.iloc[num]['size'] > 200:
            canvas.itemconfig(square2, outline="green", width=(full_year.iloc[num]['size'] - 200))
            canvas.itemconfigure(text_year, text="Year: " + str(year))
        else:
            canvas.itemconfig(square2, outline="green", width=0)
            canvas.itemconfigure(text_year, text="Year: " + str(year))
        if gas.iloc[num]['size'] > 200:
            canvas.itemconfig(square4, outline="green", width=(gas.iloc[num]['size'] - 200))
        else:
            canvas.itemconfig(square4, outline="green", width=0)
    elif year == 2018:
        year = 2011
        num = 0
        canvas.itemconfig(square2, outline="green", width=0)
        canvas.itemconfig(square4, outline="green", width=0)
        canvas.coords(square2, 50 + full_year.iloc[num]['shift'], 150 + full_year.iloc[num]['shift'],
                      50 + full_year.iloc[num]['size'],
                      150 + full_year.iloc[num]['size'])
        canvas.coords(square4, 50 + gas.iloc[num]['shift'], 500 + gas.iloc[num]['shift'],
                      50 + gas.iloc[num]['size'],
                      500 + gas.iloc[num]['size'])
        canvas.itemconfigure(text_year,
                             text="Year: " + str(year))
    # Place button


button = tkinter.Button(window,
                        text="Next Year",
                        command=next_year)
button.pack()

# Show current year
text_year = canvas.create_text(180, 125,
                               text="Year: " + str(year))
text_year_2 = canvas.create_text(100, 125,
                                 text="Year: 2011", fill='red')
text_label = canvas.create_text(350, 250,
                                 text="Square Feet", fill='blue')
text_label2 = canvas.create_text(350, 600,
                                 text="Gallon of Gasoline", fill='blue')
text_label3 = canvas.create_text(250, 25,
                                 text="What will 2011 prices buy you for the rest of the decade?", fill='blue')

# Pack canvas
canvas.pack()

# Run mainloop
window.mainloop()

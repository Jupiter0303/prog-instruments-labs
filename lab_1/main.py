import tkinter as tk
from tkinter import (Tk,
                     Label,
                     Button,
                     Radiobutton,
                     Entry,
                     StringVar,
                     IntVar,
                     messagebox
                     )

import tkinter.ttk as ttk

counter_a = 0
counter_b = 0
counter_c = 0


def main1():
    global MAIN_WINDOW
    MAIN_WINDOW = Tk()  # after successful this main ui should appear

    MAIN_WINDOW.geometry("600x1000+300+100")
    va = IntVar()
    va.set(1)
    w = Label(MAIN_WINDOW,
              text="What do you wish to buy today?"
              )  # ,justify=LEFT
    w.pack(anchor=W)
    r1 = Radiobutton(
        MAIN_WINDOW,
        text='Cosmetics',
        variable=va,
        value=1,
        justify=LEFT,
        command=cosmetics
    )
    r2 = Radiobutton(
        MAIN_WINDOW,
        text='clothing',
        variable=va,
        value=2,
        justify=LEFT,
        command=clothing
    )
    r1.pack()
    r2.pack()

    MAIN_WINDOW.mainloop()


def increment_a():
    global counter_a
    counter_a = counter_a + 1


def increment_b():
    global counter_b
    counter_b = counter_b + 1


def increment_c():
    global counter_c
    counter_c = counter_c + 1

    # Function for cosmetics


def cosmetics():
    question1_label = Label(MAIN_WINDOW,
                            text="Select desired product",
                            justify=LEFT
                            )
    question1_label.pack(anchor=W)
    answer_var1 = IntVar()
    Radiobutton(
        MAIN_WINDOW,
        text='shampoo and Conditioner',
        variable=answer_var1,
        value=1,
        command=shampoo
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='Face wash',
        variable=answer_var1,
        value=2,
        command=facewash
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='soap',
        variable=answer_var1,
        value=3,
        command=soap
    ).pack(anchor=W)
    # Function for clothing


def clothing():
    question2_label = Label(MAIN_WINDOW,
                            text="Select desired product",
                            justify=LEFT
                            )
    question2_label.pack(anchor=W)
    answer_var2 = IntVar()
    Radiobutton(
        MAIN_WINDOW,
        text='Shirt for men',
        variable=answer_var2,
        value=1,
        command=shirt_men
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='Shirt for women',
        variable=answer_var2,
        value=2,
        command=shirt_women
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='Denim Jeans',
        variable=answer_var2,
        value=3,
        command=denims
    ).pack(anchor=W)

# Function for shampoo !!!
def shampoo():
    # 1st
    label = Label(MAIN_WINDOW, text="Select the most appropriate answer:", justify=LEFT)
    question3_label = Label(MAIN_WINDOW, text="1. What type of hair do u have?", justify=LEFT)
    question3_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Oily', variable=answer_var3, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Normal', variable=answer_var3, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Dry', variable=answer_var3, value=3, command=increment_c).pack(anchor=W)

    # 2nd
    question4_label = Label(MAIN_WINDOW, text="2. What type of hair do u have?", justify=LEFT)
    question4_label.pack(anchor=W)
    answer_var4 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Thick', variable=answer_var3, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Normal', variable=answer_var3, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Fine', variable=answer_var3, value=3, command=increment_c).pack(anchor=W)

    # 3rd
    question5_label = Label(MAIN_WINDOW,
                            text="3. Presently your hair is",
                            justify=LEFT
                            )
    question5_label.pack(anchor=W)
    answer_var5 = IntVar()
    Radiobutton(
        MAIN_WINDOW,
        text='Natural',
        variable=answer_var5,
        value=1,
        command=increment_a
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='Coloured or Highlighted',
        variable=answer_var5,
        value=2,
        command=increment_b
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='Permed',
        variable=answer_var5,
        value=3,
        command=increment_c
    ).pack(anchor=W)

    # 4th
    question6_label = Label(
        MAIN_WINDOW,
        text="4. How frequently do you wash your hair?",
        justify=LEFT
    )
    question6_label.pack(anchor=W)
    answer_var6 = IntVar()
    Radiobutton(
        MAIN_WINDOW,
        text='Once a week',
        variable=answer_var6,
        value=1,
        command=increment_a
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='Twice a week',
        variable=answer_var6,
        value=2,
        command=increment_b
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='Everyday',
        variable=answer_var6,
        value=3,
        command=increment_c
    ).pack(anchor=W)

    # 5th
    question7_label = Label(
        MAIN_WINDOW,
        text="5. How often do you use a heat tool?",
        justify=LEFT
    )
    question7_label.pack(anchor=W)
    answer_var7 = IntVar()
    Radiobutton(
        MAIN_WINDOW,
        text='Never',
        variable=answer_var7,
        value=1,
        command=increment_a
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='Sometimes',
        variable=answer_var7,
        value=2,
        command=increment_b
    ).pack(anchor=W)
    Radiobutton(
        MAIN_WINDOW,
        text='Everyday',
        variable=answer_var7,
        value=3,
        command=increment_c
    ).pack(anchor=W)

    # 6th
    question8_label = Label(MAIN_WINDOW,
                            text="6. How often do you use a hair product?",
                            justify=LEFT
                            )
    question8_label.pack(anchor=W)
    answer_var8 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Never',
                variable=answer_var8,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Sometimes',
                variable=answer_var8,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Everyday',
                variable=answer_var8,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 7th
    question9_label = Label(MAIN_WINDOW,
                            text="7. Do you have splitends?",
                            justify=LEFT
                            )
    question9_label.pack(anchor=W)
    answer_var9 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='None',
                variable=answer_var9,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Few',
                variable=answer_var9,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Plenty',
                variable=answer_var9,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    Button(MAIN_WINDOW,
           text="Submit",
           width=10,
           height=1,
           bg="white",
           command=shampoo_recommendation
        ).place(x=300, y=700)
    Button(MAIN_WINDOW,
           text="buy",
           width=10,
           height=1,
           bg="white",
           command=buy
        ).place(x=400, y=700)


def shampoo_recommendation():
    if (counter_a > counter_b and counter_a > counter_c):
        messagebox.showinfo("Your ideal shampoo:",
                            "L'Oreal 6 Oil Nourish shampoo"
                            )
    elif (counter_b > counter_c and counter_b > counter_a):
        messagebox.showinfo("Your ideal shampoo ",
                            "L'Oreal Hair Spa Nourishing shampoo"
                            )
    elif (counter_c > counter_a and counter_c > counter_b):
        messagebox.showinfo("Your ideal shampoo",
                            "Dove Intense Repair shampoo"
                            )
    elif (counter_a == counter_b):
        messagebox.showinfo("Your ideal shampoo",
                            "L'Oreal Hair Spa Nourishing shampoo"
                            )
    elif (counter_b == counter_c):
        messagebox.showinfo("Your ideal shampoo",
                            "Dove Intense Repair shampoo"
                            )
    elif (counter_a == counter_c):
        messagebox.showinfo("Your ideal shampoo",
                            "L'Oreal Hair Spa Nourishing shampoo"
                            )
    elif (counter_a == counter_b and counter_b == counter_c):
        messagebox.showinfo("Your ideal shampoo",
                            "L'Oreal Hair Spa Nourishing shampoo"
                            )


# Function for facewash !!!
def facewash():
    # 1st
    label = Label(MAIN_WINDOW,
                  text="Select the most appropriate answer:",
                  justify=LEFT
                  )
    question3_label = Label(MAIN_WINDOW,
                            text="1. What type of skin do u have?",
                            justify=LEFT
                            )
    question3_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Oily',
                variable=answer_var3,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Normal',
                variable=answer_var3,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Dry',
                variable=answer_var3,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 2nd
    question4_label = Label(MAIN_WINDOW,
                            text="2. How often do you have skin problems(pimple,acne)?",
                            justify=LEFT
                            )
    question4_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Frequently',
                variable=answer_var3,
                value=1,
                command=increment_a
                ).pack(anchor=W)
    (Radiobutton(MAIN_WINDOW,
                text='Sometimes',
                variable=answer_var3,
                value=2,
                command=increment_b
            ).pack(anchor=W))
    Radiobutton(MAIN_WINDOW,
                text='Never',
                variable=answer_var3,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 3rd
    question5_label = Label(MAIN_WINDOW,
                            text="3. How does your skin react to 2 hours of sun exposure without sunscreen?",
                            justify=LEFT
                            )
    question5_label.pack(anchor=W)
    answer_var5 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Skin Burns',
                variable=answer_var5,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Minor Burns',
                variable=answer_var5,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Never Burns',
                variable=answer_var5,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 4th
    question6_label = Label(MAIN_WINDOW,
                            text="4. Does new skin care often make your skin itch,burn or irritate?",
                            justify=LEFT
                            )
    question6_label.pack(anchor=W)
    answer_var6 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Yes',
                variable=answer_var6,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Yes, sometimes',
                variable=answer_var6, value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='No',
                variable=answer_var6,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 5th
    question7_label = Label(MAIN_WINDOW,
                            text="5. How often do you wash your face?",
                            justify=LEFT
                            )
    question7_label.pack(anchor=W)
    answer_var7 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Once a day',
                variable=answer_var7,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Twice a day',
                variable=answer_var7,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='More than twice a day',
                variable=answer_var7,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 6th
    question8_label = Label(MAIN_WINDOW,
                            text="6. How much makeup do you use on a daily basis?",
                            justify=LEFT
                        )
    question8_label.pack(anchor=W)
    answer_var8 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='None',
                variable=answer_var8,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Little',
                variable=answer_var8,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Full Coverage',
                variable=answer_var8,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 7th
    question9_label = Label(MAIN_WINDOW,
                            text="7. How often is your skin sensitive?",
                            justify=LEFT
                            )
    question9_label.pack(anchor=W)
    answer_var9 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Never',
                variable=answer_var9,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Sometimes',
                variable=answer_var9,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='All the time',
                variable=answer_var9,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    Button(MAIN_WINDOW,
           text="Submit",
           width=10,
           height=1,
           bg="white",
           command=facewash_recommendation
        ).place(x=300, y=700)
    Button(MAIN_WINDOW,
           text="buy",
           width=10,
           height=1,
           bg="white",
           command=buy
        ).place(x=400, y=700)


def facewash_recommendation():
    if (counter_a > counter_b and counter_a > counter_c):
        messagebox.showinfo("Your ideal facewash:",
                            "Himalaya Herbal Purifying Neem Face Wash"
                            )
    elif (counter_b > counter_c and counter_b > counter_a):
        messagebox.showinfo("Your ideal shampoo ",
                            "Garnier Skin Naturals Light Complete facewash"
                            )
    elif (counter_c > counter_a and counter_c > counter_b):
        messagebox.showinfo("Your ideal shampoo",
                            "Biotique Bio Honey Gel facewash")
    elif (counter_a == counter_b):
        messagebox.showinfo("Your ideal shampoo",
                            "Garnier Skin Naturals Light Complete facewash"
                            )
    elif (counter_b == counter_c):
        messagebox.showinfo("Your ideal shampoo",
                            "Biotique Bio Honey Gel facewash"
                            )
    elif (counter_a == counter_c):
        messagebox.showinfo("Your ideal shampoo",
                            "Garnier Skin Naturals Light Complete facewash"
                            )
    elif (counter_a == counter_b and counter_b == counter_c):
        messagebox.showinfo("Your ideal shampoo",
                            "Garnier Skin Naturals Light Complete facewash"
                            )


# Function for soap !!!
def soap():
    # 1st
    label = Label(MAIN_WINDOW,
                  text="Select the most appropriate answer:",
                  justify=LEFT)
    question3_label = Label(MAIN_WINDOW,
                            text="1. What type of skin you have?",
                            justify=LEFT
                            )
    question3_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Oily',
                variable=answer_var3,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Normal',
                variable=answer_var3,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Dry',
                variable=answer_var3,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 2nd
    question4_label = Label(MAIN_WINDOW,
                            text="2. Is your skin sensitive?",
                            justify=LEFT
                            )
    question4_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='No',
                variable=answer_var3,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Little',
                variable=answer_var3,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Very much',
                variable=answer_var3,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 3rd
    question5_label = Label(MAIN_WINDOW,
                            text="3. How often your skin react to change in skin products?",
                            justify=LEFT
                            )
    question5_label.pack(anchor=W)
    answer_var5 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Does not react',
                variable=answer_var5,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Sometimes',
                variable=answer_var5,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Never',
                variable=answer_var5,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 4th
    question6_label = Label(MAIN_WINDOW,
                            text="4. What fragrance do you like?",
                            justify=LEFT
                        )
    question6_label.pack(anchor=W)
    answer_var6 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Strawberry',
                variable=answer_var6,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Cocoa',
                variable=answer_var6,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Citrus',
                variable=answer_var6,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 5th
    question7_label = Label(MAIN_WINDOW,
                            text="5. How many bathing soaps do you buy per month?",
                            justify=LEFT
                            )
    question7_label.pack(anchor=W)
    answer_var7 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='1-2',
                variable=answer_var7,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='3-4',
                variable=answer_var7,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='More',
                variable=answer_var7,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 6th
    question8_label = Label(MAIN_WINDOW,
                            text="6. How satisfied are you with your soap?",
                            justify=LEFT
                            )
    question8_label.pack(anchor=W)
    answer_var8 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Satisfied',
                variable=answer_var8,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Neither satisfied nor dissatisfied',
                variable=answer_var8,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Dissatisfied',
                variable=answer_var8,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 7th
    question9_label = Label(MAIN_WINDOW,
                            text="7. Do you prefer soap with colour and fragrance?",
                            justify=LEFT
                            )
    question9_label.pack(anchor=W)
    answer_var9 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Yes',
                variable=answer_var9,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Only fragrance',
                variable=answer_var9,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='No',
                variable=answer_var9,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    Button(MAIN_WINDOW,
           text="Submit",
           width=10,
           height=1,
           bg="white",
           command=soap_recommendation
        ).place(x=300, y=700)
    Button(MAIN_WINDOW,
           text="buy",
           width=10,
           height=1,
           bg="white",
           command=buy
        ).place(x=400, y=700)


def soap_recommendation():
    if (counter_a > counter_b and counter_a > counter_c):
        messagebox.showinfo("Your ideal soap:",
                            "Dove Cream Beauty Bathing bar"
                            )
    elif (counter_b > counter_c and counter_b > counter_a):
        messagebox.showinfo("Your ideal soap:",
                            "Biotique Bio Almond Oil Nourishing soap"
                            )
    elif (counter_c > counter_a and counter_c > counter_b):
        messagebox.showinfo("Your ideal soap:",
                            "Pears Pure and Gentle"
                            )
    elif (counter_a == counter_b):
        messagebox.showinfo("Your ideal soap:",
                            "Biotique Bio Almond Oil Nourishing soap"
                            )
    elif (counter_b == counter_c):
        messagebox.showinfo("Your ideal soap:",
                            "Pears Pure and Gentle"
                            )
    elif (counter_a == counter_c):
        messagebox.showinfo("Your ideal soap:",
                            "Biotique Bio Almond Oil Nourishing soap"
                            )
    elif (counter_a == counter_b and counter_b == counter_c):
        messagebox.showinfo("Your ideal soap:",
                            "Biotique Bio Almond Oil Nourishing soap"
                            )


# Function for shirt (men) !!!
def shirt_men():
    # 1st
    label = Label(MAIN_WINDOW,
                  text="Select the most appropriate answer:",
                  justify=LEFT
                  )
    question3_label = Label(MAIN_WINDOW,
                            text="1. What is your size?",
                            justify=LEFT
                            )
    question3_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW,
                text='Small',
                variable=answer_var3,
                value=1,
                command=increment_a
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Medium',
                variable=answer_var3,
                value=2,
                command=increment_b
            ).pack(anchor=W)
    Radiobutton(MAIN_WINDOW,
                text='Large',
                variable=answer_var3,
                value=3,
                command=increment_c
            ).pack(anchor=W)

    # 2nd
    question4_label = Label(MAIN_WINDOW, text="2. What type of collar?", justify=LEFT)
    question4_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Classic', variable=answer_var3, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Button', variable=answer_var3, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Mandarian', variable=answer_var3, value=3, command=increment_c).pack(anchor=W)

    # 3rd
    question5_label = Label(MAIN_WINDOW, text="3. What kind of shirt do you want?", justify=LEFT)
    question5_label.pack(anchor=W)
    answer_var5 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Western', variable=answer_var5, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Casual', variable=answer_var5, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Formal', variable=answer_var5, value=3, command=increment_c).pack(anchor=W)

    # 4th
    question6_label = Label(MAIN_WINDOW, text="4. What kind of sleeve do you prefer?", justify=LEFT)
    question6_label.pack(anchor=W)
    answer_var6 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Long', variable=answer_var6, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Short', variable=answer_var6, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Sleeveless', variable=answer_var6, value=3, command=increment_c).pack(anchor=W)

    # 5th
    question7_label = Label(MAIN_WINDOW, text="5. What kind of fabric do you prefer?", justify=LEFT)
    question7_label.pack(anchor=W)
    answer_var7 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Linen', variable=answer_var7, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Cotton', variable=answer_var7, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Silk', variable=answer_var7, value=3, command=increment_c).pack(anchor=W)

    # 6th
    question8_label = Label(MAIN_WINDOW, text="6. Select the type of fitting", justify=LEFT)
    question8_label.pack(anchor=W)
    answer_var8 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Skinny fit', variable=answer_var8, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Classic Fit', variable=answer_var8, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Modern Fit', variable=answer_var8, value=3, command=increment_c).pack(anchor=W)

    # 7th
    question9_label = Label(MAIN_WINDOW, text="7. For what type of occasion do you need this shirt?", justify=LEFT)
    question9_label.pack(anchor=W)
    answer_var9 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Formal funcgtion', variable=answer_var9, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Party wear', variable=answer_var9, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Social gathering', variable=answer_var9, value=3, command=increment_c).pack(anchor=W)

    Button(MAIN_WINDOW, text="Submit", width=10, height=1, bg="white", command=shirt_men_recommendation).place(x=300, y=700)
    Button(MAIN_WINDOW, text="buy", width=10, height=1, bg="white", command=buy).place(x=400, y=700)


def shirt_men_recommendation():
    if (counter_a > counter_b and counter_a > counter_c):
        messagebox.showinfo("Your ideal Shirt:", "Peter England Navy Blue Solid Shirt")
    elif (counter_b > counter_c and counter_b > counter_a):
        messagebox.showinfo("Your ideal Shirt:", "GAP Olive Solid Shirt")
    elif (counter_c > counter_a and counter_c > counter_b):
        messagebox.showinfo("Your ideal Shirt:", "Peter England Black Solid Shirt")
    elif (counter_a == counter_b):
        messagebox.showinfo("Your ideal Shirt:", "GAP Olive Solid Shirt")
    elif (counter_b == counter_c):
        messagebox.showinfo("Your ideal Shirt:", "Peter England Black Solid Shirt")
    elif (counter_a == counter_c):
        messagebox.showinfo("Your ideal Shirt:", "GAP Olive Solid Shirt")
    elif (counter_a == counter_b and counter_b == counter_c):
        messagebox.showinfo("Your ideal Shirt:", "GAP Olive Solid Shirt")


# Function for shirt (women) !!!
def shirt_women():
    # 1st
    label = Label(MAIN_WINDOW, text="Select the most appropriate answer:", justify=LEFT)
    question3_label = Label(MAIN_WINDOW, text="1. What is your size?", justify=LEFT)
    question3_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Small', variable=answer_var3, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Medium', variable=answer_var3, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Large', variable=answer_var3, value=3, command=increment_c).pack(anchor=W)

    # 2nd
    question4_label = Label(MAIN_WINDOW, text="2. What type of neck do you prefer?", justify=LEFT)
    question4_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW, text='V-neck', variable=answer_var3, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Turtleneck', variable=answer_var3, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Low neck', variable=answer_var3, value=3, command=increment_c).pack(anchor=W)

    # 3rd
    question5_label = Label(MAIN_WINDOW, text="3. What kind of shirt do you want?", justify=LEFT)
    question5_label.pack(anchor=W)
    answer_var5 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Western', variable=answer_var5, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Casual', variable=answer_var5, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Formal', variable=answer_var5, value=3, command=increment_c).pack(anchor=W)

    # 4th
    question6_label = Label(MAIN_WINDOW, text="4. What kind of sleeve do you prefer?", justify=LEFT)
    question6_label.pack(anchor=W)
    answer_var6 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Long', variable=answer_var6, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Short', variable=answer_var6, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Sleeveless', variable=answer_var6, value=3, command=increment_c).pack(anchor=W)

    # 5th
    question7_label = Label(MAIN_WINDOW, text="5. What kind of fabric do you prefer?", justify=LEFT)
    question7_label.pack(anchor=W)
    answer_var7 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Linen', variable=answer_var7, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Cotton', variable=answer_var7, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Silk', variable=answer_var7, value=3, command=increment_c).pack(anchor=W)

    # 6th
    question8_label = Label(MAIN_WINDOW, text="6. Select the type of fitting", justify=LEFT)
    question8_label.pack(anchor=W)
    answer_var8 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Skinny fit', variable=answer_var8, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Classic Fit', variable=answer_var8, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Modern Fit', variable=answer_var8, value=3, command=increment_c).pack(anchor=W)

    # 7th
    question9_label = Label(MAIN_WINDOW, text="7. For what type of occasion do you need this shirt?", justify=LEFT)
    question9_label.pack(anchor=W)
    answer_var9 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Formal funcgtion', variable=answer_var9, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Party wear', variable=answer_var9, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Social gathering', variable=answer_var9, value=3, command=increment_c).pack(anchor=W)

    Button(MAIN_WINDOW, text="Submit", width=10, height=1, bg="white", command=shirt_women_recommendation).place(x=300, y=700)
    Button(MAIN_WINDOW, text="buy", width=10, height=1, bg="white", command=buy).place(x=400, y=700)


def shirt_women_recommendation():
    if (counter_a > counter_b and counter_a > counter_c):
        messagebox.showinfo("Your ideal Shirt:", "GAP Blue Fitted Boyfriend Shirt")
    elif (counter_b > counter_c and counter_b > counter_a):
        messagebox.showinfo("Your ideal Shirt:", "H&M Olive Solid Shirt")
    elif (counter_c > counter_a and counter_c > counter_b):
        messagebox.showinfo("Your ideal Shirt:", "Vero Moda Black Solid Top")
    elif (counter_a == counter_b):
        messagebox.showinfo("Your ideal Shirt:", "H&M Olive Solid Shirt")
    elif (counter_b == counter_c):
        messagebox.showinfo("Your ideal Shirt:", "Vero Moda Black Solid Top")
    elif (counter_a == counter_c):
        messagebox.showinfo("Your ideal Shirt:", "H&M Olive Solid Shirt")
    elif (counter_a == counter_b and counter_b == counter_c):
        messagebox.showinfo("Your ideal Shirt:", "H&M Olive Solid Shirt")


# Function for denims !!!
def denims():
    # 1st
    label = Label(MAIN_WINDOW, text="Select the most appropriate answer:", justify=LEFT)
    question3_label = Label(MAIN_WINDOW, text="1. What is your size?", justify=LEFT)
    question3_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Small', variable=answer_var3, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Medium', variable=answer_var3, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Large', variable=answer_var3, value=3, command=increment_c).pack(anchor=W)

    # 2nd
    question4_label = Label(MAIN_WINDOW, text="2. What kind of fitting do you prefer?", justify=LEFT)
    question4_label.pack(anchor=W)
    answer_var3 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Skinny', variable=answer_var3, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Bootcut', variable=answer_var3, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Pegged', variable=answer_var3, value=3, command=increment_c).pack(anchor=W)

    # 3rd
    question5_label = Label(MAIN_WINDOW, text="3. How often do you wear jeans?", justify=LEFT)
    question5_label.pack(anchor=W)
    answer_var5 = IntVar()
    Radiobutton(MAIN_WINDOW, text='More than once a week', variable=answer_var5, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Once a week', variable=answer_var5, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Once a month', variable=answer_var5, value=3, command=increment_c).pack(anchor=W)

    # 4th
    question6_label = Label(MAIN_WINDOW, text="4. What colour do you prefer?", justify=LEFT)
    question6_label.pack(anchor=W)
    answer_var6 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Blue', variable=answer_var6, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='White', variable=answer_var6, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Black', variable=answer_var6, value=3, command=increment_c).pack(anchor=W)

    # 5th
    question7_label = Label(MAIN_WINDOW, text="5. How often do you buy jeans?", justify=LEFT)
    question7_label.pack(anchor=W)
    answer_var7 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Whenever I like', variable=answer_var7, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Every few months', variable=answer_var7, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='When my current pair cannot be worn anymore', variable=answer_var7, value=3, command=increment_c).pack(
        anchor=W)

    # 6th
    question8_label = Label(MAIN_WINDOW, text="6. What type of jeans do you buy?", justify=LEFT)
    question8_label.pack(anchor=W)
    answer_var8 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Cheap', variable=answer_var8, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Moderate', variable=answer_var8, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Expensive', variable=answer_var8, value=3, command=increment_c).pack(anchor=W)

    # 7th
    question9_label = Label(MAIN_WINDOW, text="7. Which is your favourite brand?", justify=LEFT)
    question9_label.pack(anchor=W)
    answer_var9 = IntVar()
    Radiobutton(MAIN_WINDOW, text='Levis', variable=answer_var9, value=1, command=increment_a).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='Mufti', variable=answer_var9, value=2, command=increment_b).pack(anchor=W)
    Radiobutton(MAIN_WINDOW, text='H&M', variable=answer_var9, value=3, command=increment_c).pack(anchor=W)

    Button(MAIN_WINDOW, text="Submit", width=10, height=1, bg="white", command=denims_recommendation).place(x=300, y=700)
    Button(MAIN_WINDOW, text="buy", width=10, height=1, bg="white", command=buy).place(x=400, y=700)


def denims_recommendation():
    if (counter_a > counter_b and counter_a > counter_c):
        messagebox.showinfo("Your ideal Jeans:", "Levis Blue Highrise Jeans")
    elif (counter_b > counter_c and counter_b > counter_a):
        messagebox.showinfo("Your ideal Jeans:", "H&M White Biker Jeans")
    elif (counter_c > counter_a and counter_c > counter_b):
        messagebox.showinfo("Your ideal Jeans:", "Mufti Black Slimfit Jeans")
    elif (counter_a == counter_b):
        messagebox.showinfo("Your ideal Jeans:", "Tommy Hilfiger Slimfit Jeans")
    elif (counter_b == counter_c):
        messagebox.showinfo("Your ideal Jeans:", "Calvin Klein Slimfit Jeans")
    elif (counter_a == counter_c):
        messagebox.showinfo("Your ideal Jeans:", "Tommy Hilfiger Ripped Jeans")
    elif (counter_a == counter_b and counter_b == counter_c):
        messagebox.showinfo("Your ideal Jeans:", "H&M distressed Jeans")


def buy():
    print("Visit this link to buy your product: https://www.amazon.in/")


# Function for login screen
def login():
    uname = username.get()
    pwd = password.get()
    if uname == '' or pwd == '':
        message.set("Fill the empty field!!!")
    else:
        if uname == "Chandler" and pwd == "Monica":
            message.set("Login success")
            login_screen.destroy()
            main1()
        else:
            message.set("Wrong username or password!!!")


global login_screen
login_screen = Tk()
# Setting title of screen
login_screen.title("Login Form")
# setting height and width of screen
login_screen.geometry("300x250")
# declaring variable
global message
global username
global password
username = StringVar()
password = StringVar()
message = StringVar()
# Creating layout of login form
Label(login_screen, width="300", text="Please enter details below", bg="deep sky blue", fg="white").pack()
# Username Label
Label(login_screen, text="Username * ").place(x=20, y=40)
# Username textbox
Entry(login_screen, textvariable=username).place(x=90, y=42)
# Password Label
Label(login_screen, text="Password * ").place(x=20, y=80)
# Password textbox
Entry(login_screen, textvariable=password, show="*").place(x=90, y=82)
# Label for displaying login status[success/failed]
Label(login_screen, text="", textvariable=message).place(x=95, y=100)
# Login button
Button(login_screen, text="Login", width=10, height=1, bg="white", command=login).place(x=105, y=130)
login_screen.mainloop()
# calling function Loginform
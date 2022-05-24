from tkinter import *
import random
import webbrowser
import time
from datetime import datetime
import dishes


# set up files for dishes and recipes
dishes.createFiles()

# clear function to clear displayed dishes
def clear():
    try:
        food_label.destroy()
        labele.destroy()
        decide_button["state"] = NORMAL
    except:
        food_label.destroy()
        decide_button["state"] = NORMAL


# closing time of my nearest grocery store
def time():
    start = datetime.now().replace(hour=21, minute=0)
    morning = datetime.now().replace(hour=7, minute=0)
    end = datetime.now()
    if start < end and end> morning:
        timer = "is closed.."
    else:
        timer = end - start
    time_label.config(text="Center Eleven schlüsst ih: " + str(timer))
    time_label.after(1000, time)

# add your favorite recipe
d = {}
with open("C:/Foodinator/dishes/recipe.txt") as f:
    for line in f:
        (key, val) = line.split(",")
        d[key] = val

choices =[
    ("Egal", 0),
    ("Vegetarisch", 1),
    ("S'Mami chocht", 2),
    ("S'Mami isch weg", 3)
]
def rightPath():
    path_int = mode.get()
    if path_int == 0:
        path = "C:/Foodinator/dishes/all.txt"
    elif path_int == 1:
        path = "C:/Foodinator/dishes/vegi.txt"
    elif path_int == 2:
        path = "C:/Foodinator/dishes/big.txt"
    else:
        path = "C:/Foodinator/dishes/schnell.txt"
    return path

def getdish():
    path = rightPath()
    with open(path, 'rt') as file:
        dishes = file.readlines()
    return dishes[random.randint(0, len(dishes)-1)]
    file.close()

def callback(url):
    webbrowser.open_new(url)

def callback2(x, y):
    global labele
    labele = Label(root, text="Für das bruchsch es Rezept...?")
    labele.place(x=x, y=y+15)

# generate a random dish according to constraints
def decideClick():
    global food_label
    name = getdish()
    food_label = Label(root, text=name)
    x = random.randint(10, 600)
    y = random.randint(300, 500)
    food_label.place(x=x, y=y)

    if name[:-1] in d.keys():
        food_label.bind("<Button-1>", lambda e: callback(d.get(name[:-1])))
    else:
        food_label.bind("<Button-1>", lambda e: callback2(x, y))

    decide_button["state"] = DISABLED

# Add a new dish to the correct file
def addClick():
    try:
        new_dish = e.get()
        if len(new_dish) > 0:
            add_button["state"] = NORMAL
            path = rightPath()
            file1 = open(path, "a")
            file1.write(new_dish+"\n")
            file1.close()
            went_well_label = Label(root, text=new_dish +" wurde hinzugefügt!")
            went_well_label.pack()
        else:
            error_label = Label(root, text="Konnte nicht hinzugefügt werden...")
            error_label.pack()

    except:
        error_label = Label(root, text="Konnte nicht hinzugefügt werden")
        error_label.pack()

# remove a dish
def removeClick():
    to_remove = e.get()
    is_in_there = False
    if len(to_remove) > 0:
        path = rightPath()
        f = open(path, "r")
        a = [to_remove]
        lst = []
        for line in f:
            for word in a:
                if word in line:
                    line = line.replace(word, '')
                    is_in_there = True
            lst.append(line)
        f.close()
        f = open(path, "w")
        for line in lst:
            f.write(line)
        f.close()

        if is_in_there == True:
            went_well_label = Label(root, text=to_remove + " wurde gelöscht!")
            went_well_label.pack()
        else:
            not_well_label = Label(root, text=to_remove + " ist nicht im Rezeptbuch")
            not_well_label.pack()
    else:
        not_well_label = Label(root, text="Keine Idee ist leider in im Rezeptbuch")
        not_well_label.pack()

# render GUI
root = Tk()
root.title("Was git's?")
root.geometry("700x600")

label = Label(root, text="Hüt hani Lust uf...", bd=10)
label.pack()

mode = IntVar()
mode.set("0")

for text, modus in choices:
    Radiobutton(root, text=text, variable=mode, value=modus).pack()


e = Entry(root)


del_button = Button(root, text="Menu löschen", command=removeClick)
add_button = Button(root, text="Menu hinzufügen", command=addClick)
decide_button = Button(root, text="Was gits..?", command=decideClick)
clear_button = Button(root, text="Clear to run again", command=clear)

time_label = Label(root)
time_label.place(x=50, y=50)

decide_button.pack()
add_button.place(x=500, y=30)
e.place(x=500, y=60)
del_button.place(x=500, y=80)
clear_button.pack()
time()
root.mainloop()

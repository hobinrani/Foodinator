# this script creates the files and recipes to store your favorite dishes
from pathlib import Path
from os import path
import os

def doesDirExsist():
    return path.exists("C:/Foodinator/dishes")

def createFiles():
    dir_path = "C:/Foodinator/dishes"
    if doesDirExsist():
        return
    else:
        os.makedirs(dir_path)
        f = open("C:/Foodinator/dishes/all.txt", "w")
        f.close()
        b = open("C:/Foodinator/dishes/big.txt", "w")
        b.close()
        q = open("C:/Foodinator/dishes/schnell.txt", "w")
        q.close()
        v = open("C:/Foodinator/dishes/vegi.txt", "w")
        v.close()
        rezepte = open("C:/Foodinator/dishes/recipe.txt", "w")
        rezepte.close()
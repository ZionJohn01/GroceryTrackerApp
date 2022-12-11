import re
import string
import sys

def printsomething():
    print("Hello from python!")
    

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v
def readCount():
    with open('GroceryList.txt', 'r') as f:
        readContents = f.readlines()
    count = [[readContents.count(item), item] for item in readContents]
    count = str(count)
    count = count.replace("\n", "")
    print(count)
def histogramCount():
    with open('GroceryList.txt', 'r') as f:
        readContents = f.readlines()
    count = [readContents.count(item) for item in readContents]
    for i in readContents:
        print(readContents[i], " ", ("-" * count[i]))
        i = i + 1



    

def readList():
    with open('GroceryList.txt', 'r') as f:
        readContents = f.readlines()
    print(readContents)
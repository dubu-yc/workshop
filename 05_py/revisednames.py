#Yoonah Chang, Josephine Lee, Josh Kloepfer
#SoftDev
#K05 -- REVISED Python Random Name Generator
#2021-09-26

#discovered that randint > rand, adding "period 1/2: " makes output more readable
#should the lists be a separate file? are mini lists better for testing to see if it works?
#contributions- yoonah: period 1/2 comments, josh: randint and lists, josephine: use of a function

import random

list1 = ["Rayat", "William", "Michelle", "Lucas", "Ivan"];
list2 = ["Yoonah", "Joshua", "Alif", "Josephine", "Andrew"];

def printName():
    print("period 1: " + list1[random.randint(0, len(list1) - 1)])
    print("period 2: " + list2[random.randint(0, len(list2) - 1)])
printName()

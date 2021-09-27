#Yoonah Chang, Josephine Lee, Josh Kloepfer
#SoftDev
#K05 -- REVISED Python Random Name Generator
#2021-09-26

#SUMMARY OF TRIO DISCUSSION
#good code is reusable code.
#DISCOVERIES
#randint > rand, adding "period 1/2: " makes output more readable
#QUESTIONS
#should the lists be a separate file? are mini lists better for testing to see if it works?
#COMMENTS
#contributions- yoonah: period 1/2 comments, josh: randint and lists, josephine: use of a function

import random
students = {
        'list1': ["Rayat", "William", "Michelle", "Lucas", "Ivan"],
        'list2': ["Yoonah", "Joshua", "Alif", "Josephine", "Andrew"]
}

def printName():
    print("period 1: " + students["list1"][random.randint(0, len(list1) - 1)])
    print("period 2: " + students["list2"][random.randint(0, len(list2) - 1)])
printName()
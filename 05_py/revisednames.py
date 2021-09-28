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

students={
'list1': ['Alejandro Alonso', 'Aryaman Goenka', 'Angela Zhang', 'Christopher Liu', 'Deven Maheshwari',
       'Emma Buller', 'Ella Krechmer', 'Gavin McGinley', 'Haotian Gan', 'Ivan Lam', 'Ishraq Mahid',
       'Ivan Mijacika', 'Julia Nelson', 'Lucas Lee', 'Lucas Tom Wong', 'Michelle Lo', 'Oscar Wang',
       'Owen Yaggy', 'Renggeng Zheng', 'Shriya Anand', 'Shyne Choi','Sadid Ethun', 'Tomas Acuna','Theo Fahey',
       'Tina Nguyen', 'Tami Takada', 'William Chen', 'Yusuf Elsharawy', 'Zhaoyu Lin'],                                  #names we know from period 1
'list2': ['Alif Abdullah', 'Andrew Juang', 'Andy Lin', 'Austin Ngan', 'Annabel Zhang', 'Daniel Sooknanan',
       'Eric Guo', 'Eliza Knapp', 'Hebe Huang', 'Han Zhang', 'Yoonah Chang', 'Joshua Kloepfer', 'Josephine Lee', 'Jonathan Wu',
       'Jesse Xie', 'Justin Zou', 'Kevin Cao', 'Liesel Wong', 'Michael Borczuk', 'Mark Zhu', 'Noakai Aronesty',
       'Patrick Ging','Qina Liu', 'Rachel Xiao', 'Raymond Yeung', 'Sophie Liu', 'Shadman Rakib','Thomas Yu',
       'Wenhao Dong', 'Yaying Liang Li', 'Yuqing Wu'],                                                                  #names we know from period 2
}

def printName():
    print('period 1: ' + students['list1'][random.randint(0, len(students['list1']) - 1)] #find a random number between 0 and the number of elements in the list,
    print('period 2: ' + students['list2'][random.randint(0, len(students['list2']) - 1)]) #excluding the last number, that number will be the index.
printName()


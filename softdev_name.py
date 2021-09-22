#Yoonah Chang, Michael Borczuk, Kevin Cao (Team Sneakers)
#SoftDev
#K01-- Python Random Name Generator
#2021-09-22

import random

pd1 = ['Patrick Ging', 'Owen Yaggy', 'Haotian Gan', 'Ishraq Mahid', 'Ivan Lam']
pd2 = ['Kevin Cao', 'Raymond Yueng', 'Michael Borczuk', 'Yoonah Chang :)', 'Han Zhang <3', 'Austin Ngan', 'Noakai Aronesty']

print("period 1: " + pd1[int(random.random() * len(pd1))])
print("period 2: " + pd2[int(random.random() * len(pd2))])


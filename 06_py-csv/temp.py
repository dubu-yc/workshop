#Yoonah Chang, Michael Borczuk, Kevin Cao (Team Sneakers)
#SoftDev
#K06 -- StI/O: Divine your Destiny!
#2021-09-28

import csv
import random

num = 0

dict = {
}

with open('occupations.csv', mode ='r') as file:   
    
   # reading the CSV file
    csvFile = csv.DictReader(file)

   # add contents to dictionary
    for lines in csvFile:
        dict[lines['Job Class']] = float(lines['Percentage']) * 10

# keeps on generating a number when rand is greater than total percentage
while True:
    num = random.randint(0, 1000)
    if num < dict['Total']:
        break

counter = 0

# adds to counter and once it hits the randomly generated number, it prints the key
for key in dict.keys():
    if counter + dict[key] > num:
        print(key)
        break
    else:
        counter += dict[key]

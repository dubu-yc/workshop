# DOCUMENTATION by Team Sneakers: Michael Borczuk, Kevin Cao, Yoonah Chang
### CSV I/O
We first imported the CSV module, and we read the given file as a dictionary. We went through each line in the file and paired job classes with their 
corresponding percentages using a dictionary. Essentially, the inital goal was to input a job, and receive a percentage as output.
### DICTIONARY
Dictionaries help store values using keys. Every key has a corresponding value, so when you input a key, you can get the associated value. However, one key cannot have more than one value associated with it. Think of it like an f(x) function!
### LIST
Lists are like dictionaries, but instead of a string key, they use a numerical index. Lists start at index 0. Think of it as an ordered grocery list, but starting at 0 instead of 1! Here, lists just return the value associated with the index.
### GITHUB FLAVORED MARKDOWN
Github markdown utilize hashtags! The more hashtags you put before a line of text, the smaller the test will be. There are other symbols that you can use to change the format of your text. For example, asterisks make the text italic. Think of Discord markdown!
Click this link to learn more about GitHub markdown: https://guides.github.com/features/mastering-markdown/
### WEIGHTED RANDOMIZED SELECTION
We took the values (probabilities) that we had in our dictionary and multiplied them by 10, in order to not have to deal with decimals. (Decimals = bad!) 
We utilized the random module to generate a random number between 0 and 999, inclusive of both. 
Every occupation has an interval of integers that vary in size depending how large or small the probabilities were. 
Next, we checked to see which interval our randomized number would fall into.
We used our dictionary to find which job class was associated with that interval. Voila!

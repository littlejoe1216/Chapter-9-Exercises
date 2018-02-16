#Joe Gutierrez - 2/1/18 - Chapter 9 - Exercise 3

#Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

file = input('Enter file name: ')

try :
    fhand = open(file)
except :
    print ('Cannot open file:' , file , '.' , 'retry.')
    exit()

email = dict()

for line in fhand :
    if not line.startswith('From') : continue
    words = line.split()
    email[words[1]] = email.get(words[1], 0) + 1

print (email)

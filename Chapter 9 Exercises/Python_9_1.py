#Joe Gutierrez - 2/1/18 - Chapter 9 - Exercise 1

#Write a program that reads the words in words.txt and stores them as keys in a dictionary.
#It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

Dictionary as a set of counters


newdict = dict()
count = 0
fhand = open('words.txt')



inp = fhand.read()
inp = inp.split() 



for word in inp :
    count = count + 1
    newdict[word] = [count]

print ('big') in newdict

print ('and') in newdict

print ('bird') in newdict



#Joe Gutierrez - 2/1/18 - Chapter 9 - Exercise 2

#Write a program that categorizes each mail message by which day of the week the commit was done. 
#To do this look for lines that start with "From", then look for the third word and
#keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

fname = input("Enter a file name: ")
fhand = open(fname)

days = dict()

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        dow = words[2]
        days[dow] = days.get(dow,0) + 1


print (days)

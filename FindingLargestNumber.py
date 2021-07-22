#This program finds the largest number in the given array of numbers

largestnumber_sofar = 0
for items in [2,4,6,34,23,56,98,43,42,44]:
    if largestnumber_sofar < items:
        largestnumber_sofar = items
print(largestnumber_sofar)
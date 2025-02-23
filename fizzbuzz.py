#Create a program that will run through the integers 1 to 25.
#If the number is a multiple of 3, print "Fizz"
#If the number is a multiple of 5, print "Buzz"
#If the number is a multiple of 3 and 5 print "FizzBuzz"
#If the number is not any of the stated multiples, print the number.
#Each output is on it's own line
#Also include in your repo a .drawio file that flowcharts out the logic

#Here is a section of sample output:
#Buzz
#11
#Fizz
#13
#14
#FizzBuzz

for i in range(1, 26):
    if i == 15:
        print("FizzBuzz")
    if i == 3:
        print("Fizz")
    if i == 6:
        print("Fizz")
    if i == 9:
        print("Fizz")
    if i == 12:
        print("Fizz")
    if i == 18:
        print("Fizz")
    if i == 21:
        print("Fizz")
    if i == 24:
        print("Fizz")
    if i == 5:
        print("Buzz")
    if i == 10:
        print("Buzz")
    if i == 20:
        print("Buzz")
    if i == 25:
        print("Buzz")
    else:
        print(i)


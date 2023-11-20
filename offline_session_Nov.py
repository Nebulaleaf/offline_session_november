# 1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year when they turn 100 years old
name = input("What's your name?\n")
age = int(input("What's your age?\n"))
current_year = 2023
difference = 100 - age
year = current_year + difference
print(f"Hi {name}, you will hit the 100th birthday in the year {year}")

# Write a program that asks a user for a number five times and returns the lowest one.
my_list = []

while len(my_list) < 5:
        item = int(input("Enter a number: "))
        my_list.append(item)
   

my_list.sort()
smallest_number = my_list[0]
print("The smallest number is:", smallest_number)

# Write a code to convert temperatures to and from °Celsius and °Fahrenheit.
temp_cels = float(input("What's the temperature in Celsius?\n"))
temp_fahrenheit = temp_cels * 1.8 + 32 #used a comma instead of period and it took me ages to get the error -.-
print(f"It's {temp_fahrenheit}")

# Write a function to count even and odd numbers from a series of numbers. 
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output : 
# Number of even numbers : 5 
# Number of odd numbers : 4

def count_num():
    even = 0
    odd = 0

    for i in range(1, 10):
        if i % 2 == 0:
             even += 1
        else:
             odd += 1
    
    print(f"even numbers: {even}")
    print(f"odd numbers: {odd}")

count_num()

# Write a function which iterates the integers from 0 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". 
# Hint: Remember the modulo operator from first homework? 
# Sample Output : 
# fizzbuzz 
# 1 
# 2 
# fizz 
# 4 
# buzz

def fizzbuzz():
    for i in range(0, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif  i % 3 == 0:
            print("fizz")
        else:
            print(i)

fizzbuzz()

#Write a function to calculate a dog's age in dog's years. 
#Note : For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years. 
#Expected Output : 
#Input a dog's age in human years: 15 
#The dog's age in dog's years is 73
# first year = 10.5
# second year = 10.5
# every other year = 4


def dogsyear (h_age):
    if h_age <= 0:
        print("It's not even born yet! Please provide valid age")
    elif h_age == 1:
        d_age = 10.5
        print(f"Your dog is {d_age} old.")
    elif h_age == 2:
        d_age = 10.5 * 2
        print(f"Your dog is {d_age} old.")
    else:
        d_age = 10.5 * 2 + (h_age - 2) * 4
        print(f"Your dog is {d_age} old.")

h_age = int(input("What's the age of the dog in human years?\n"))

dogsyear(h_age)

# Write a function to construct the following pattern, using a nested loop. 
# Expected Output : 
# 1 
# 22 
# 333 
# 4444 
# 55555 
# 666666 
# 7777777 
# 88888888 
# 999999999

def pyramide():
    for i in range(1, 10):  # Outer loop
        for j in range(1, 10):  # Inner loop
            print(i, end='')
            if i <= j:
                break
        print() #honestly, this whole exercise was just trial and error with the exercise of session 4 (?), I don't "get it" but it works -.-

pyramide()

# Write a function which removes characters from a string which are an odd index

def remove_odd_index_chars(input_string):
    result = ""
    for i in range(len(input_string)):
        if i % 2 == 0:
            result += input_string[i]
    return result

input_string = "Whatever!"
result = remove_odd_index_chars(input_string)
print(result)
#this I couldnt figure out myself, the part with "for i in range" I did but the whole function to work I couldnt manage

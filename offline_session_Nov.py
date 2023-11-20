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




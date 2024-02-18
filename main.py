# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
total_char = nr_letters + nr_symbols + nr_numbers

wanted_numbers = random.sample(numbers, nr_numbers)
wanted_symbols = random.sample(symbols, nr_symbols)
wanted_letters = random.sample(letters, nr_letters)
joined_total_nu = "".join(wanted_numbers)
joined_total_sy = "".join(wanted_symbols)
joined_total_le = "".join(wanted_letters)
joined_total = joined_total_le + joined_total_nu + joined_total_sy
# random_joined_total = random.sample(joined_total, total_char)
# joined_random_joinded_total = "".join(random_joined_total)
# print(joined_random_joined_total)
print(joined_total)

# print(random.sample(joined_total, total_char))

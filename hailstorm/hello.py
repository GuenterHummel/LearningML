import argparse
import random

parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
args = parser.parse_args()

print('Hello, ' + args.name + '!')

print("Günter", "likes", "Python")

pizza_5 = ["Napoli", "Funghi", "Diavolo", "Quattro Stagioni", "Margherita"]
print(pizza_5)
pizza_5[0] = "Hawaii"
print(pizza_5)

print(random.choice(pizza_5))

print (random.randrange(10, 100))

print ('1d100 = ' + str(random.randint(1, 100)))
print ('1d20  = ' + str(random.randint(1, 20)))
print ('1d12  = ' + str(random.randint(1, 12)))
print ('1d10  = ' + str(random.randint(1, 10)))
print ('1d8   = ' + str(random.randint(1, 8)))
print ('1d6   = ' + str(random.randint(1, 6)))
print ('1d4   = ' + str(random.randint(1, 4)))

pizza_top_5 = ("Diavolo", "Quattro Stagioni", "Margherita", "Napoli", "Funghi")
print(pizza_top_5)

print(pizza_top_5[0])
print(random.choice(pizza_top_5))

p1, p2, p3, p4, p5 = pizza_top_5
print(p1, p2, p3, p4, p5)
print(type(p1))

first_primes = (2, 3, 5, 7)
first_primes_auto = 2, 3, 5, 7

print(first_primes)
print(first_primes_auto)


fruits = {'Apple', 'Banana', 'Orange', 'Ananas'}
fruits.update({"Pear", "Plum", "Cherry"})


message = ["Python", "has", "several", "loop", "variants"]
for i in range(len(message)):
    print(i, message[i], end=',')
print()
for current_word in message:
    print(current_word, end=' ')
print()

for i, ch in enumerate("fun with chars"):
    if i % 2 != 0:
        print(ch + "_", end=",")
    else:
        print(ch.upper(), end="")

print()

def pizza_price (n, collect_self):
    pizza_price = 11
    pizza_price_discount = 0

    if collect_self:
        pizza_price_discount = 2

    pizza_price_adjust = 1
    if n >= 5:
        pizza_price_adjust = 0.9

    total = n * pizza_price * pizza_price_adjust

    return total - (n * pizza_price_discount)

print ("pizza_price(2, False) = " + str(pizza_price(2, False)))
print ("pizza_price(2, True)  = " + str(pizza_price(2, True)))
print ("pizza_price(7, True)  = " + str(pizza_price(7, True)))

for i in range (1, 7):
    print (i, "*", i, "=", (i ** 2))

print()

def print_number_triangle(n):
    for i in range (1, n + 1):
        for j in range (1, i + 1):
            print (j, end=" ")
        print()

print_number_triangle(4)
print()

def print_number_triangle_adv(n):
    num = 1
    for i in range (1, n + 1):
        for j in range (1, i + 1):
            print (num , end=" ")
            num += 1
        print()

print_number_triangle_adv(4)
print()

def print_char_triangle(n):
    letter = "A"
    for i in range (1, n + 1):
        for j in range (1, i + 1):
            print (letter, end=" ")
        letter = chr(ord(letter) + 1)
        print()

print_char_triangle(4)
print()

def print_k_shaped(n):
    for y in range (n, 0, -1):
        print_letters(y)

    for y in range(1, n + 1):
        print_letters(y)

def print_letters(y):
    letter = "A"
    for x in range(1, y + 1):
        print(letter, end=" ")
        letter = chr(ord(letter) + 1)
    print()


print_k_shaped(5)
print()


#Problem statement:
"""
You get a rare chance to work with Hermione Granger at Hogwarts.
The night is dark, the corridors echo with whispers, and she urgently needs to light her way
using the spell “LUMOS”.
To prepare, Hermione reaches into her enchanted pouch that contains glowing runes (letters).
She pulls out one rune at a time, each shining faintly in the dark.

Your task is to determine the earliest step at which Hermione can first form the word “LUMOS”
from the runes she has collected so far.
The order of runes does not matter (Hermione is smart enough to rearrange them).
Ignore case (both uppercase and lowercase letters work).
If it is impossible to form “LUMOS” from the given sequence of runes, print -1.
"""

# So firstly we check if LUMOS can be made from the input or not so we have to check for
# Availaibility of all the letter. Assuming the input is a string

letter_bag = input("Enter the string: ").lower() # Convert everything to lowercase for ease later on

word_req=['l','u','m','o','s']
last_step=-1

for letter in word_req:
    if letter in letter_bag:
        last_step=max(last_step, letter_bag.find(letter)) 
        # Find method is return the first location the letter is encoutered
    else:
        print("Hermione cannot form the word LUMOS")
        print(-1)
        exit()

print(f"The last step where Hermione will find the word lumos is: {last_step+1}") # Since it has zero based indexing we add one
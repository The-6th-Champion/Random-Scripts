from sequence import Sequence

# Create a sequence of lowercase letters
alphabet_iterator = Sequence(97, 97 + 26, chr)

# print the first letter's value
print(alphabet_iterator.start)

# print the last letter's value
print(alphabet_iterator.end)

# print the current letter
print(alphabet_iterator.current)

# print all the letters in the sequence
print(alphabet_iterator.sequence)

# move back a letter, and print it
alphabet_iterator.move_forward(1, True)
print(alphabet_iterator.current)

# move forward 3 letters, and print it
alphabet_iterator.move_forward(3)
print(alphabet_iterator.current)

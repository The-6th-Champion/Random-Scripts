typeOf = input("What are you inputting? (bin or text)\n")
text = input("Type that input here\n")

if typeOf == "bin":
    bin_list = text.split()
    ascii_string = ""
    for thing in bin_list:
        ascii_string += chr(int(thing, 2))
    print(ascii_string)
elif typeOf == "text":
    bin_string = ""
    for letter in text:
        bin_string += bin(ord(letter))
    print(bin_string.replace("0b", " "))
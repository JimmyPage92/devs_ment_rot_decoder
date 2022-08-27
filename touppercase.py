user_input = input("Provide text: ")
decodetext = ""


for letter in user_input:
    letter_position: int = ord(letter)
    if letter_position <= 109:
        decodetext += chr(letter_position + 13)
    else:
        decodetext += chr(letter_position - 13)
else:
    if letter.upper():
        if letter_position <= 77:
            decodetext += chr((letter_position + 13) % 26 + 97)
        else:
            decodetext += chr((letter_position - 13) % 26 + 97)

print(decodetext)


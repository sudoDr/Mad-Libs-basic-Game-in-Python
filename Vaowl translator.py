def translate(phrase):
    translation = ""

    # The 'for' loop goes through every single character in your phrase
    for letter in phrase:
        # The 'if' statement checks if the letter is a vowel
        # We use .lower() so we don't have to write A, E, I, O, U separately
        if letter.lower() in "aeiou":
            # If it's a vowel, check if it was originally uppercase
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            # If it's NOT a vowel, just keep the original letter
            translation = translation + letter

    return translation


# Testing the translator
user_input = input("Enter a phrase to translate: ")
print(translate(user_input))
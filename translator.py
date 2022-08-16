#translates all the vowels to "g"

def translate(phrase):
    translated_word = ''
    for letter in phrase:
        # if letter in ["a", "e", "i", "o", "u" ]:
        if letter in "aeiouAEIOU":
            if letter.isupper():
                translated_word = translated_word + "G"
            else:
                translated_word = translated_word + "g"
        else:
            translated_word = translated_word + letter
    return translated_word

print(translate(input("Enter your word of choice: ")))

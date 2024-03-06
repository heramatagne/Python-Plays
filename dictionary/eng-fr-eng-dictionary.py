# This program creates an English to French and French to English translation dictionary.

# This dictionary translates a word from English to French.
english_to_french_dictionary = {
    "apricot": "abricot",
    "banana": "banane",
    "cherry": "cerise",
    "guava": "goyave",
    "orange": "orange",
    "african plum": "prune"
}

# This dictionary translates a word from French to English.
french_to_english_dictionary = {
    "abricot": "apricot",
    "banane": "banana",
    "cerise": "cherry",
    "goyave": "guava",
    "orange": "orange",
    "prune": "african plum",
}

# Language selection
language_choice = input("Enter 'EF' for English to French translation or 'FE' for French to English translation: ").upper()

if language_choice == "EF":
    word = input("Please enter a word to translate: ").lower()
    # English to French translation
    if word in english_to_french_dictionary:
        translation = english_to_french_dictionary[word]
        print(f"{word} is {translation} in French.")
    else:
        print(f"{word} is not in memory.")

elif language_choice == "FE":
    word = input("Please enter a word to translate: ").lower()
    # French to English translation
    if word in french_to_english_dictionary:
        translation = french_to_english_dictionary[word]
        print(f"{word} is {translation} in English.")
    else:
        print(f"{word} is not in memory")

else:
    print("Invalid choice. Please enter 'EF' or 'FE'.")

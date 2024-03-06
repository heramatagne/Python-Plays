def translate(language_choice, word):
    if language_choice == "EF":
        if word in english_to_french_dictionary:
            translation = english_to_french_dictionary[word]
            return f"{word} is {translation} in French."
        else:
            return f"{word} is not in memory."
    elif language_choice == "FE":
        if word in french_to_english_dictionary:
            translation = french_to_english_dictionary[word]
            return f"{word} is {translation} in English."
        else:
            return f"{word} is not in memory"
    else:
        return "Invalid choice. Please enter 'EF' or 'FE'."

# English to French translation dictionary
english_to_french_dictionary = {
    "apricot": "abricot",
    "banana": "banane",
    "cherry": "cerise",
    "guava": "goyave",
    "orange": "orange",
    "african plum": "prune"
}

# French to English translation dictionary
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

if language_choice in ["EF", "FE"]:
    word = input("Please enter a word to translate: ").lower()
    translation_result = translate(language_choice, word)
    print(translation_result)
else:
    print("Invalid choice. Please enter 'EF' or 'FE'.")

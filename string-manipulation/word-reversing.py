# Ask the user for a word
word = input("Please enter a word: ")

# Split the word into a list of characters
word_characters = list(word)

# Reverse the list of characters
reversed_word_characters = reversed(word_characters)

# Join the reversed characters back into a string
reverse_word = ''.join(reversed_word_characters)

# Display the original word and its reverse
print("Your word is:", word, "and the reverse is:", reverse_word)

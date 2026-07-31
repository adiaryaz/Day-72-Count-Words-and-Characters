def count_words_and_characters(input_string):
    num_characters = len(input_string)

    words = input_string.split()
    num_words = len(words)

    return num_words, num_characters


input_string = input("Enter a string: ")

num_words, num_characters = count_words_and_characters(input_string)

print(f"Number of words: {num_words}")
print(f"Number of characters (including spaces): {num_characters}")
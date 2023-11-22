def count_letters(input_string):
    # Initialize an empty dictionary to store the letter counts
    letter_count = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a letter (alphabetical)
        if char.isalpha():
            # Convert the character to uppercase to ensure case insensitivity
            char = char.upper()
            # Increment the count for the letter in the dictionary
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count

input_string = "AaBb"
result = count_letters(input_string)
print(result)
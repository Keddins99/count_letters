def count_letters(input_string):
    letter_count = {}

    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            char_upper = char.upper()
            letter_count[char_upper] = letter_count.get(char_upper, 0) + 1

    return letter_count

# Example usage:
input_string = "AaBb"
result = count_letters(input_string)
print(result)

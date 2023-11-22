def count_letters(input_string):
    letter_count = {}

    for char in input_string:
        if char.isalpha():
            char = char.upper()
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count

input_string = "AaBb"
result = count_letters(input_string)
print(result)
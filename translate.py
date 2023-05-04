def first_letters(input_string):
    result = ""
    in_quotes = False
    skip_until = None

    for i, char in enumerate(input_string):
        if skip_until is not None and i < skip_until:
            continue

        if char == '(':
            skip_until = input_string.find(')', i) + 1
            continue
        
        if char == '"':
            in_quotes = not in_quotes
            continue
        
        if not in_quotes and char.isalpha() and (i == 0 or not input_string[i-1].isalpha()):
            result += char.lower()

    return result

file_name = "input_text.txt"
output = ""

with open(file_name, "r") as file:
    for line in file:
        line = line.replace('"', '')  # remove quotes from line
        line = line.replace('I\'m', 'I')
        output += first_letters(line)

print(output)
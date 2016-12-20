mapping = { '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}

def convert(string):
    split_string = string.split('.')
    result = 0
    for key, value in enumerate(split_string):
        string_length = len(value)
        if key > 0:
            c = string_length
        else:
            c = 0
        for i in value:
            count = mapping[i]
            result += count * (10 ** (string_length - c - 1))
            c += 1
    return result

print(convert('1230.123'))

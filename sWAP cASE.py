def swap_case(s):
    swapped = ""
    for letter in s:
        if letter.isupper():
            swapped += letter.lower()
        else:
            swapped += letter.upper()
            
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

def reverse(text):
    return text[::-1]


def is_palindrom(text):
    return text == reverse(text)


something = input("Enter something:")
if is_palindrom(something):
    print('This is a palindrom')
else:
    print('This is not a palindrom')
from itertools import zip_longest


def grouper(n, iterable, filler='x'):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=filler)


def phone_letter_converter(phone_number):
        from string import ascii_lowercase, digits
        phone_number = phone_number.lower()
        for letters, digit in zip(grouper(3, ascii_lowercase),
                                  digits[1:]):
            for l in letters:
                phone_number = phone_number.replace(l, digit)
        return phone_number

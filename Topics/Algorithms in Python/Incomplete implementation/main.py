import string


def startswith_capital_counter(names):

    counter = 0

    for name in names:
        if name[0] in string.ascii_uppercase:
            counter += 1

    return counter

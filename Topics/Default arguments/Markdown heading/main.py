def heading(string, level=1):
    if level <= 1:
        return f'{"#"} {string}'
    elif level < 6:
        return f'{level * "#"} {string}'
    else:
        return f'{6 * "#"} {string}'

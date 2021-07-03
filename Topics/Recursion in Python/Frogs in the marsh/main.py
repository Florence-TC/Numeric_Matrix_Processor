def number_of_frogs(year):
    if year == 1:    # base case n=1
        return 120
    else:      # case n>1
        return 2 * (number_of_frogs(year - 1) - 50)

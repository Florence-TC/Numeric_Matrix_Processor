def range_sum(numbers, start, end):
    total = 0

    for number in numbers:
        if int(start) <= int(number) <= int(end):
            total += int(number)

    return total


input_numbers = input().split()
a, b = input().split()
print(range_sum(input_numbers, a, b))

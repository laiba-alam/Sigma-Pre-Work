def max_min(numbers):
    highest = numbers[0]
    lowest = numbers[0]
    for number in numbers[1:]:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number

    return [lowest, highest]

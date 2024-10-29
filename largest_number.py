def largest_number(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

the_list = [43,1,33,1,23,32,324]

print(largest_number(the_list))
# 1. create a highest_even function that prints a highest envn number from a given list

def highest_even(li):
    highest_even_number = 0
    for number in li:
        if number % 2 == 0:
            if highest_even_number < number:
                highest_even_number = number
    return highest_even_number
print(highest_even([10, 2, 30, 44, 81]))

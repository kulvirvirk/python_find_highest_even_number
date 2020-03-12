# 1. create a highest_even function that prints a highest envn number from a given list

def highest_even(li):
    highest_even_number = 0
    for number in li:
        if number % 2 == 0:
            if highest_even_number < number:
                highest_even_number = number
    return highest_even_number
print(highest_even([10, 2, 30, 44, 81]))


# instructor's solution


#====================================================
# instructor's solution 

# def highest_even(li):
#   #create a empty list called evens []
#   evens = []
#   #iterate through orginal is to separate only even numbers
#   for item in li:
#     if item % 2 == 0:
#       #add all the even numbers to new evens list
#       evens.append(item)
#   #use max() function, which returns a highest number    
#   return max(evens)
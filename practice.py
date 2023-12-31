# prices = [10,20,30]
# sum = 0
# for price in prices:
#     sum += price
# print(f"the total price is {sum}")



# numbers = [95,43,134,76,89]
# largest = 0
# for number in numbers:
#     if number > largest:
#         largest = number
# print(f"the largest number is {largest}")



numbers = [1,1,2,3,3,4,5]
numbers2 = []
for number in numbers:
    if number not in numbers2:
        numbers2.append(number)
print(numbers2)        

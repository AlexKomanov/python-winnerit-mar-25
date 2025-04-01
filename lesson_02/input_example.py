# name = input("Enter your name: ")
# print(name)
# age = input("Enter your age: ")
# print(age)

# num_a = input("Enter number 1: ")
# num_b = input("Enter number 2: ")
# print(type(num_a))
# print(type(num_b))
# print(num_a + num_b)


# num_a = int(input("Enter number 1: "))
# num_b = int(input("Enter number 2: "))
# print(num_a + num_b)

# num_a = int(input("Enter number 1: "))
# num_b = float(input("Enter number 2: "))
# print(num_a + num_b)


numbers = input("Enter 2 numbers separated by space: ")
numbers_with_split = numbers.split()
print(numbers)
print(numbers_with_split)
print(type(numbers_with_split[0]))
print(type(numbers_with_split[1]))

number_1 = int(numbers_with_split[0])
number_2 = int(numbers_with_split[1])

print(type(number_1))
print(type(number_2))

my_list = []
print(type(my_list))
my_list = list()
print(type(my_list))

# index    0, 1, 2,   3,   4. most coding languages start at 0 more math oriented languages start with 1
numbers = [2, 6, 10, 12.5, 0] # can comment on same line as the code
print(numbers)
print(type(numbers))

print(numbers[1])
print(type(numbers[1]))
print([2, 6, 10, 12.5, 0][1])
print(6)
print(numbers[1]*2.5)
print(type(numbers[1]*2.5))

# name_of_list_we_want)_to_index[index]
print(numbers[3])
print(type(numbers[3]))

# index     0,       1         2        3
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods[1])
print(type(foods[1]))
print(foods[1].upper())

x = 12
y = 15.5 
z = "Z"

random_list = [x, y, z]
print(random_list[0])
print(type(random_list[0]))

print(random_list[1])
print(type(random_list[1]))

print(random_list[2])
print(type(random_list[2]))

my_fav_num = random_list[0]
print(my_fav_num)

# index     0,       1         2        3
foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.append("cheeseburger")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
#THIS DOES NOT WORK
#foods = foods.append("cheeseburger")
#print(foods)
foods.insert(0, "pho") 
print(foods)

foods.remove("pho")
print(foods)

#foods.remove("burrito")

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.append("pizza")
print(foods)
foods.remove("pizza")
print(foods)
foods.remove("pizza")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods)
del foods[1]
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.pop())
print(foods)

# index     0,       1         2        3
foods = ["pizza", "tacos", "dim sum", "sushi"]

# method of the list class called .sort is used only for list!!
# built-in function called sorted() any type of iterate
# 
# sort() IN PLACE 
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.sort())
print(foods)
print(foods.sort(reverse=True))
print(foods)

# sorted is Out of Place
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(sorted(foods))
print(foods)
foods = sorted(foods)
print(foods)
foods = sorted(foods, reverse=True)
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.reverse()
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods[2]

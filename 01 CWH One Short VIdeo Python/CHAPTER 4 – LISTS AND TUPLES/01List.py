# List in Python

# List is a collection which is ordered and changeable.
# List is a collection which is ordered and changeable. Allows duplicate members.
# List can be created by using []
# List items are ordered, changeable, and allow duplicate values
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# List can be created with the list() function
# List items can be of any data type, and are indexed. The items in a list can be of any data type.
# List can have different data types



product = ["Apple", "orange", "banana", 5, 6, 7, 2.5, False, "green", "pineapple"]

print(product) # ['Apple', 'orange', 'banana', 5, 6, 7, 2.5, False, 'green', 'pineapple']

print(product[0]) # Apple

print(product[-1]) # pineapple

print(product[0:3]) # ['Apple', 'orange', 'banana']

print(product[::2]) # ['Apple', 'banana', 6, 2.5, 'green']

product[0] = "New Apple"

print(product)  # ['New Apple', 'orange', 'banana', 5, 6, 7, 2.5, False, 'green', 'pineapple']

print(len(product)) # 10

product.append("Watermelon")

print(product) # ['New Apple', 'orange', 'banana', 5, 6, 7, 2.5, False, 'green', 'pineapple', 'Watermelon']

product.remove("orange")

print(product) # ['New Apple', 'banana', 5, 6, 7, 2.5, False, 'green', 'pineapple', 'Watermelon']

product.pop()

print(product) # ['New Apple', 'banana', 5, 6, 7, 2.5, False, 'green', 'pineapple']

product.pop(0)

print(product) # ['banana', 5, 6, 7, 2.5, False, 'green', 'pineapple']

print("printing with for loop...")
for i in product:
    print(i)

product.clear()

print(product) # []




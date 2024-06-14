# List - Shopping List
# milk, bread, butter, poha
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit


shopping_list = ["milk", "bread", "butter", "poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("curd")   # Add item in the end
print(shopping_list)
shopping_list.insert(3, "jam")   # Add item in the middle
print(shopping_list)

shopping_list.extend(["chips","salt"])  # Add multiple items in the end
print(shopping_list)

shopping_list.remove("bread")  # Remove item
print(shopping_list.pop())  # Remove last item
print(shopping_list)
print(shopping_list.index("butter"))
shopping_list.reverse()
print(shopping_list)
# print(shopping_list.pop(2)) # Remove item from index 2 --> poha
# print(shopping_list) # ['chips', 'curd', 'jam', 'butter', 'milk']
shopping_list.sort()
print(shopping_list)  # ['butter', 'chips', 'curd', 'jam', 'milk']
shopping_list[0] = "Pramod"   # Replace with Pramod
print(shopping_list)  # ['Pramod', 'chips', 'curd', 'jam', 'milk']
# my_list=[1, 2, 3, 4, True, 3.14, "Usha"]
# print(type(my_list)) # <class 'list'>

# Create a list
fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

# append() - Add an item at the end
fruits.append("Orange")
print("After append():", fruits)

# insert() - Insert an item at a specific position
fruits.insert(1, "Grapes")
print("After insert():", fruits)

# remove() - Remove a specific item
fruits.remove("Banana")
print("After remove():", fruits)

# pop() - Remove the last item
removed_item = fruits.pop()
print("After pop():", fruits)
print("Removed Item:", removed_item)

# copy() - Create a copy of the list
new_list = fruits.copy()
print("Copied List:", new_list)

# clear() - Remove all items from the list
fruits.clear()
print("After clear():", fruits)
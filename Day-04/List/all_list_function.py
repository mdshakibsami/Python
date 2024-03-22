states_of_america = ["delaware","pennsylvania","new jersy","georgia","connecticut","maryland","new maxico"]
# .append()---->add an item to the end of the list
states_of_america.append("sakib")
last_element = states_of_america[-1]
print(f"last elements: {last_element}")
# .extend()---->add all the items of an iterable to the end of the list
add_states = ["sarjiya","jamaika","speras"]
states_of_america.extend(add_states)
print(states_of_america)
# .insert()---->insert an item at the specified index
states_of_america.insert(3,"ariya")
index3 =states_of_america[3]
print(f"at index 3: {index3}")
# .remove()---->removes item present at the given index
states_of_america.remove("sakib")
print(states_of_america)
# .clear()---->removes all items from the list
states_of_america.clear()
l= len(states_of_america)
print(f"length of list: {l}")
# .pop----> return and remove that elements at the given index
numbers = [2, 3, 5, 7, 5, 5, 1, 0]
rm= numbers.pop(3)
print(f"poped element: {rm}")
print(f"list: {numbers}")
# .index()---->returns the index of the first matched item
ind = numbers.index(5)
print(f"index of 5: {ind}")
# .count()---->returns the count of the specified item in the list
count5 = numbers.count(5)
print(f"count of five: {count5}")
# .sort()---->sort the list in ascending/descending order
         #ascending order
numbers.sort()
print(f"ascending order: {numbers}")
         #descending order
numbers.sort(reverse=True)
print(f"descending order: {numbers}")
# .reverse()---->reverse the item of the list
numbers.reverse()
print(f"reverse order: {numbers}")
# .copy---->returns the shallow copy of the list
newList = numbers.copy()
print(f"new list: {newList}")

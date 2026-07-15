"""
2. sets
set will be allow only unique value. can't accept duplicate values.
get data form 1D .
Heteregoneous
- It won't allow duplicate values.
- indexing and slicing is not possible
- set is mutable

add - .add()
delete - .discard(), .remove()
"""

empty_set = set()
print(empty_set)
print(type(empty_set))

items_to_bye = {'banana', 'apple', 'mango', }
items_to_bye.add('grape')
print(items_to_bye)

items_to_bye.discard('apple')
print(items_to_bye)

items_to_bye.remove('banana')
print(items_to_bye)

items_to_bye.clear()
print(items_to_bye)

items = {'1.1', '1', 'apple', 'banana', 'grape', 'mango'}

items.intersection(items)
print(items)


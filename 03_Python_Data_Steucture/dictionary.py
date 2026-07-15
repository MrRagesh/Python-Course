"""
4. Dictionary

dictionary contains key:value pairs.
indexing and slicing not possible
can't change the key and can be change the value.

- 2D
- heterogenous
- mutable
- indexing and slicing in not possible
- don't create duplicate keys but you can create a duplicate values.



empty = {
    "maths" : 89,
    "physics" : 90,
    "chemistry" : 90,
    "tamil" : 100
}

print(empty)

empty["tamil"] = 98
print(type(empty))
print(empty)

empty2 = {"potato": 5,
 "tomato": 2,
 "apple": 3.5
 }
print(empty2)
"""
import pandas as pd

maths_student_marks = {
    "names" : ["ragesh", "saru", "bala", "mohan","ram"],
    "maths" : [45,65,76,54,98],
    "science" : [100,65,99,89,98],
}
print(maths_student_marks)
print("")

df = pd.DataFrame(data=maths_student_marks)

print(df)






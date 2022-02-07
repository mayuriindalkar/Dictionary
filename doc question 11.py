# Q11.Write a Python script to merge two Python dictionaries

# dict1={2:20,3:40,4:40}
# dict2={5:50,1:10,6:60}
# d=dict1.copy()
# d.update(dict2)
# print(d)

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

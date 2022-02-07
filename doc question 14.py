# Q14.Write a Python program to multiply all the items in a dictionary.



my_dict = {'data1':5,'data2':4,'data3':7}
result=1
for key in my_dict:    
    result=result * my_dict[key]
print(result)
dict={}
x=0
for i in range(1,16):
    i=i**2
    x+=1
    dict.update({x:i})
print(dict)
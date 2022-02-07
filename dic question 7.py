a=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
b={}
c=[]
i=0
while i<len(a):
    b.update(a[i])
    i+=1
for i in b.values():
     if i not in c:
          c.append(i)
print(c)
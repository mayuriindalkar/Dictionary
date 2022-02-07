# i=1
# a=[]
# b=[]
# while i<11:
#     student_name=input("enter the name :-")
#     marks=input("enter the marks :-")
#     a.append(student_name)
#     b.append(marks)
#     i+=1
# dic={}
# j=0
# e=[]
# while j<len(a):
#     d=a[j],b[j]
#     j+=1
#     e.append(d)
# dic.update(e)
# print(dic)




i=1
a=[]
b=[]
while i<11:
    student_list=input("enter the name : ")
    marks=int(input("enter the number : "))
    a.append(student_list)
    b.append(marks)
    i=i+1
dic={}
j=0
e=[]
while j<len(a):
    c=a[j],b[j]
    j=j+1
    e.append(c)
dic.update(e)
print(dic)
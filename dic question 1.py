# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)
# for key in dic1:
#     if key in dic2:
#         dic2[key]=dic1[key]+dic2[key]
#     else:
#         dic2[key]=dic1[key]
# print(dic2)






# for i in dic1.keys():
#     keys=i
#     for j in dic2.keys():
#         keys2=j
#         for k in dic3.keys():
#             keys3=k
#             if keys2==keys==keys3:
#                 print()



dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for key in dic1:
    if key in dic2:
        dic2[key]=dic1[key]+dic2[key]
    else:
        dic2[key]=dic1[key]
dic2.update(dic3)
print(dic2)
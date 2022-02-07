# Q12.Write a Python program to iterate over dictionaries using for loops



# d = {'mayuri': 1, 'prathu': 2, 'mayu': 3} 
# for name_key, value in d.items():
#      print(name_key, 'corresponds to ', d[name_key]) 



statesAndCapitals = {
					'Gujarat' : 'Gandhinagar',
					'Maharashtra' : 'Mumbai',
					'Rajasthan' : 'Jaipur',
					'Bihar' : 'Patna'
					}
print('List Of given states:\n')
for state in statesAndCapitals:
	print(state)
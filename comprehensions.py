# lists
numbers = [x+1 for x in range(10) if x%2 == 1]
numbers2 = [x**2 for x in range(10) if x%2 == 1]
# dictionaries
keys = {"a", "b", "c", "d", "e"}
values = numbers2
new_dic = {k: v for k, v in zip(keys, values)}
# sets
emails = ("zok@gmail.com", "toaq@gmail.com", "yoas@gmail.com")
new_set = {x.lower() for x in emails}
print(new_dic)
print(numbers, numbers2)
print(new_set)
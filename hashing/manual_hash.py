def my_hash(data):
    return sum(
        index * ord(x)
        for index, x in enumerate(repr(data).lstrip("'"), start=1)
    )

print(my_hash('this'))
print(my_hash('thit'))
print(my_hash('that'))
print(my_hash(12))
print(my_hash(hash))
print(my_hash(list))
print(my_hash(dict))

# Simplest version that I was able to find.
# It has a fixed length and just used the modulo op

hash_map = [x for x in range(23, 49)]


print(hash_map[11%len(hash_map)])
print(hash_map[12%len(hash_map)])
print(hash_map[13%len(hash_map)])
print(hash_map[14%len(hash_map)])
print(hash_map[15%len(hash_map)])

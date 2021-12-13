objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
n = len(objects)
ans = n
for i in range(n):
    for j in range(i):
        if id(objects[i]) == id(objects[j]):
            ans -= 1
            break

print(ans)


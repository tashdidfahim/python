a = [1, 2, 3, 5, 7, 3, 1, 2, 8, 9, 4]
# a.sort()
# a.reverse()
print("1", len(a))
print("2", a[::-2])
print("3", min(a))
a.append(0)
a.insert(4, 6)
a.remove(9)
print("4", a)
c = "Fahim"
d = "Tashdid"
c, d = d, c
print(c,d)
from collections import defaultdict
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

print(d)


s = 'mississippi'
d = defaultdict(int)
for k in s:
  d[k] += 1
print(d)


from collections import defaultdict
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d)



data = [1, 2, 1, 3, 3, 1, 4, 2]

# %matplotlib inline
import matplotlib.pyplot as plt
plt.hist(data)
plt.show()
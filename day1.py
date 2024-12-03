import re
from collections import Counter

cola = []
colb = []
with open('input/01') as file:
    for line in file:
        res = re.findall(r"[\d]+", line)
        cola.append(int(res[0]))
        colb.append(int(res[1]))


aCount = Counter(cola)
bCount = Counter(colb)

sum = 0

for num in cola:
   sum += num * (bCount.get(num) or 0)
print(sum)

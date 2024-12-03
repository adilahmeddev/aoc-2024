data = [[*map(int, l.split())] for l in open('input/02')]

def without(nums: list[int], r: int):
    nums.pop(r)
    return nums
def permutations(nums: list[int]):
    return [without(nums.copy(),i) for i,_ in enumerate(nums) ]
def isSafe(numbers):
    if len(numbers)==1:
        return True
    else:
        diff = [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]
        return all(0<i<4 for i in diff) or all(-4<i<0 for i in diff)
count = 0
for line in data:
    perms = permutations(line)
    if any([True for i in perms if isSafe(i)]):
        count+=1

print(count)

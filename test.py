nums = [1,13,10,12,31]

nums_rev = []

for i in nums:
    nums_rev.append(int(str(i)[::-1]))

print(len(set(nums_rev+nums)))

# d = 12
# print(str(d)[::-1])
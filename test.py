left = 1
right = 22
# p=[]
# for i in range(left,right+1):
#     is_t = True
#     for t in str(i):
#         if t == '0' or i % int(t) != 0:
#             is_t = False
#             break
#     if is_t:

#         p.append(i)
# print(p)

self_dividing_numbers = []
for num in range(left, right + 1):
    is_self_dividing = True
          
    for digit_str in str(num):
        digit = int(digit_str)
        if digit == 0 or num % digit != 0:
            is_self_dividing = False
            break
    if is_self_dividing:
        self_dividing_numbers.append(num)
      

print(self_dividing_numbers)


# print(list(set(n for n in p if p.count(n) > 1)))

# print([num for num in range(left, right + 1) if all(i != '0' and num % int(i) == 0 for i in str(num))])
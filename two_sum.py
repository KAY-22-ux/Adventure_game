nums = [3,2,4]
target = 6 
seen = {}
for i, num in enumerate(nums):
difference = target - num
if difference in seen:
return [seen[difference], i]
seen[num] = i
return []

# for i in nums:
#     difference = abs(i- target)
#     if  difference  in nums:
#         print(nums.index(i) , nums.index(difference))
#     else:
#         continue

# print()
# print(list.index(2))
# print(4 in list)

# my_list = [1, 2, 3, 4]
# target = 5

# for i in my_list:
#     diff = abs(target - i)
#     if diff in my_list:
#         print(my_list.index(i), my_list.index(diff))
#     else:
#         continue

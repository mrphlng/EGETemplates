nums = list(map(int, open('58484.txt').readlines()))
c = 0
max_num = 0
min_num = 20001
for num in nums:
    if num % 10 == 5 and num >= 99 and num <= 1000:
        min_num = min(min_num, num)
for i in range(len(nums) - 1):
    if ((nums[i] >= 999 and nums[i] <= 10000) + (nums[i + 1] >= 999 and nums[i + 1] <= 10000)) == 1:
        if (nums[i] ** 2 + nums[i + 1] ** 2) % min_num == 0:
            c += 1
            max_num = max(nums[i] ** 2 + nums[i + 1] ** 2, max_num)
print(c,max_num)
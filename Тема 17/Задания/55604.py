nums = list(map(int,open('55604.txt').readlines()))
c = 0
max_num = 0
min_num = 10001
for num in nums:
    if (abs(num) % 100) // 10 == abs(num) % 10:
        min_num = min(min_num, num)
for i in range(len(nums) - 1):
    if ((abs(nums[i]) % 10) == (abs(nums[i + 1]) % 100) // 10) or ((abs(nums[i + 1]) % 10) == (abs(nums[i]) % 100) // 10):
        if (abs(nums[i]) % 7 == 0) != (abs(nums[i + 1]) % 7 == 0):
            if nums[i] ** 2 + nums[i + 1] ** 2 <= min_num ** 2:
                c += 1
                max_num = max(nums[i] ** 2 + nums[i + 1] ** 2, max_num)
print(c, max_num)
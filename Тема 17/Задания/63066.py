nums = list(map(int, open('63066.txt').readlines()))
c = 0
max_num = 0
for num in nums:
    if max_num % 1000 == 321:
        max_num = max(max_num, num)
for i in range(len(nums) - 2):
    if ((10000 <= nums[i] <= 99999) + (10000 <= nums[i + 1] <= 99999) + (10000 <= nums[i + 2] <= 99999)) == 2:
        if ((nums[i] % 5 == 0) + (nums[i + 1] % 5 == 0) + (nums[i + 2] % 5 == 0)) >= 1:
            if (nums[i] + nums[i + 1] + nums[i + 2]) > max_num:
                c += 1
                max_num = max(nums[i] + nums[i + 1] + nums[i + 2],max_num)
print(c,max_num)

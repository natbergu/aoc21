nums = [int(line) for line in open("input.txt")]
count = 0
for i, num in enumerate(nums[3:], 3):
    oldthree = sum(nums[i-3:i])
    newthree = sum(nums[i-2:i+1])
    if newthree > oldthree:
        count += 1

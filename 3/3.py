nums = [line.strip() for line in open("input.txt")]
def most(lst, i):
    c0 = c1 = 0
    for num in lst:
        if num[i] == "0":
            c0 += 1
        else:
            c1 += 1
    return "0" if c0 > c1 else "1"
def least(lst, i):
    c0 = c1 = 0
    for num in lst:
        if num[i] == "0":
            c0 += 1
        else:
            c1 += 1
    return "0" if c0 <= c1 else "1"
def reduce(nums, f):
    lst = nums.copy()
    i = 0
    while len(lst) > 1 and i < 12:
        s = f(lst, i)
        lst = list(filter(lambda num: num[i] == s, lst))
        i += 1
    return lst[0]
o2rating = reduce(nums, most)
co2rating = reduce(nums, least)
print(int(o2rating, 2) * int(co2rating, 2))

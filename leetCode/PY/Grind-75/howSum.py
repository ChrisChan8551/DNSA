
def howSum(target, nums):
    if target == 0:
        return []
    if target < 0:
        return None
    for num in nums:
        remainder = target - num
        result = howSum(remainder,nums)
        
    return


print(howSum(7, [2, 3]))  # [3,2,2]
print(howSum(7, [5, 3, 4, 7]))  # [4,3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2,2,2,2]
print(howSum(300, [7, 14]))  # None

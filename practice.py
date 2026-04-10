
def find_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num

    return max_num   

numbers = [1, 2, 3, 4, 5, 6]
print(find_max(numbers))    


def find_min(nums):
    min_num = nums[0]
    for num in nums:
     if num < min_num:
            min_num = num

    return min_num
    
numbers0 = [3,2,8,10,5,1]
print(find_min(numbers0))

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    


numbers_1 = [2, 7, 11, 15]
target = 9
print(two_sum(numbers_1, target))
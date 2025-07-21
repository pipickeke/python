"""
两数之和

题目描述：给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
"""


def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = num - target
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []



print("###################")

def two_sum_2(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = num - target
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []







if __name__ == '__main__':
    list = [1,2,3,5,2]
    print(f"res: {two_sum_2(list, 4)}")




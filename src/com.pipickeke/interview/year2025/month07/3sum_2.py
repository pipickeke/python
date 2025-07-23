
"""
三数之和（3Sum）

找出所有和为 0 的三元组，不能重复。

"""

def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, n-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left > 0 and nums[left] == nums[left+1]:
                    left += 1
                while right > 0 and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"结果：{three_sum(nums)}")


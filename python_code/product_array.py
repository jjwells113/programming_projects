# 238. Product of Array Except Self
# Example problem from Leetcode

# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Johnathan Wells

from functools import reduce

class Solution:
    def productExceptSelf(nums: list[int]) -> list[int] :
        answer = []
        for val in nums:
            temp = nums.copy()
            temp.remove(val)
            answer.append(reduce(lambda a, b: a*b, temp))
        
        return answer
    
nums = [1,2,3,4,5]
print(Solution.productExceptSelf(nums))
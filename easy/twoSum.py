# -*- coding: utf-8 -*-
__author__ = 'kong90'

# Question
"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Subscribe to see which companies asked this question
"""


# # Version 1.0 Time Limit Exceeded 我以为数据是无序的
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         flag = True
#         for i, one_num in enumerate(nums):
#             for j, two_num in enumerate(nums):
#                 if i != j and one_num + two_num == target and flag:
#                     flag = False
#                     return i + 1, j + 1
#         if flag is True:
#             return "NO"


# Version 2.0 Runtime Error 数据有负数,而且是递减的 [-1,-2,-3,-4,-5] -8
# class Solution(object):
#     def get_index(self, nums, target):
#         max_ = len(nums) - 1
#         _nums = reversed(nums)
#         for i, num in enumerate(_nums):
#             if num <= target:
#                 return max_ - i
#
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#
#         x = self.get_index(nums, target)
#         flag = True
#         another_nums = [k for k in nums[:x + 1]]
#         another_nums.reverse()
#         for i, one_num in enumerate(nums[:x + 1]):
#             for j, two_num in enumerate(another_nums):
#                 if one_num != two_num and one_num + two_num == target and flag:
#                     flag = False
#                     return i + 1, len(nums[:x+1]) - j
#         if flag is True:
#             return "NO"

# Version 3.0 Time Limit Exceeded 当数据量达到 n = 76时, 时间为4.21205091476 n = 6 时间为 0.0552141666412, n**2 / 2
# 估计  n = 1000 将达到可观的1521.476984s
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = True
        another_nums = [k for k in nums]
        another_nums.reverse()
        for i, one_num in enumerate(nums):
            for j, two_num in enumerate(another_nums):
                if one_num != two_num and one_num + two_num == target and flag:
                    flag = False
                    return i + 1, len(nums) - j
        if flag is True:
            return "NO"
def test():
    a = Solution()
    a.twoSum([25046,25048,25050,25052,25054,25056,25058,25060,25062,25064,25066,25068,25070,25072,25074,25076,25078,25080,25082,25084,25086,25088,25090,25092,25094,25096,25098,25100,25102,25104,25106,25108,25110,25112,25114,25116,25118,25120,25122,25124,25126,25128,25130,25132,25134,25136,25138,25140,25142,25144,25146,25148,25150,25152,25154,25156,25158,25160,25162,25164,25166,25168,25170,25172,25174,25176,25178,25180,25182,25184,25186,25188,25190,25192,25194,25196]
,16021)

if __name__ == "__main__":

    # test()
    from timeit import Timer
    t1 = Timer("test()", "from __main__ import test")
    print t1.timeit(10000)


# 终极版
class Solution(object):
    def twoSum(self, num, target):
        process={}
        for index in range(len(num)):
            if target-num[index] in process: # in 比 for 快好多??
                return [process[target-num[index]]+1,index+1]
            process[num[index]]=index

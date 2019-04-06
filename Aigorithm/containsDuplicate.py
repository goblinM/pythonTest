# 给定一个整数数组，判断是否存在重复元素。

# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #方案一 有个问题一旦数组过大
        if nums:
            i = 0
            while i < len(nums) - 1:
                if nums.count(nums[i]) >= 2:
                    return True
                i += 1
            return False
        else:
            return False
        #方案二
        # if nums:
        #     diff_list = list(set(nums))
        #     if len(diff_list) != len(nums):
        #         return True
        #     return False
        # else:
        #     return False
        # 方案三
        # return len(nums) != len(list(set(nums)))

solution = Solution()
# print(solution.containsDuplicate([2,14,18,22,22]))
print([2,14,18,22,22].index(22))
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max=max(nums)
        first_max_index=nums.index(first_max)
        if nums.count(first_max)>=2:
            return -1
        if len(nums)==1:
            return 0
        nums.remove(first_max)
        second_max=max(nums)
        if first_max>=2*second_max:
            return first_max_index
        else:
            return -1

if __name__ == '__main__':
    nums = [1]
    solution = Solution()
    print(solution.dominantIndex(nums))
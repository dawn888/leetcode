class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                print(nums[i],nums[j])
                if nums[j]==target-nums[i]:
                    return(i,j)


#nums=[3,2,4]
#target=6
#solution=Solution()
#print(solution.twoSum(nums, target))

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for  k,v in enumerate(seasons):
    print(k,v)



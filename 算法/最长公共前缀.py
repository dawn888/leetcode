
class Solution:
    #水平扫描
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        print(strs)

            
solution=Solution()
strs=["flower","flow","flight"]
solution.longestCommonPrefix(strs)

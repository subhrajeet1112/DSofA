class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        for i in range(1,len(nums)):

            if nums[k] == nums[i]:
                continue
            elif nums[k] != nums[i]:
                k = k+1
                nums[k] = nums[i]
                continue
            else:
                pass
        k = k+1
        nums = nums[:k]
        return k












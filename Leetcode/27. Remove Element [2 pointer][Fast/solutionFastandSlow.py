class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Fast and Slow Pointer
        k = 0
        for i in range(0,len(nums)):
            if nums[i] == val:
                continue
            elif nums[i] != val:
                nums[i],nums[k] = nums[k],nums[i]
                k=k+1
                continue
            else:
                pass
        return k

<pre
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
        return k
</pre>

So the Way it works is we have a two pointers K and I respectively. We keep our slow pointer K at 0. Think of K as the place we would siwtch 
our (findings) with. So what is the findings then ? Our findings are anything that is not k not equals (!=) to the value given in the argument.
Why ?
Well think of this is a way to push our unique elements not equal to value to the left of the array. Doing this would automactically sort our 
given values to the right and our unique values to the left of the array. 



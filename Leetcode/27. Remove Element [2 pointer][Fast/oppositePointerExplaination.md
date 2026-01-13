<pre>
  class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Opposite Ends
        k = len(nums)-1
        i = 0
        while i <= k:
            if nums[i] == val:
                nums[i],nums[k] = nums[k],nums[i]
                k = k-1
            elif nums[i] != val:
                i = i+1
        return k+1
</pre>

[3,2,2,3]
Say we have an array. 
We have two pointer at i= 0 which will traverse the array while our pointer k will allow us to switch positions with our value at i.
Reason for while loop and NOT for loop ?
The reason is that while we can use for loop for 2 pointer in case of opposite pointer since we switch elements from the back of the array we
need to check what we switched with. Hence we cannot have a automatical increment of the loop. Rather we increment it ONLY when the value of the
nums[i] is not equal (!=) to val. 
Why i<=k ?
Well the loop should end when they both meet right ? because you have checked everything from the left and the right. But we also cannot go 
beyond our loop index so we cannnot do **i!=0**. 

Why did we return k+1?
nums[k] would be the last element of the sortedArray after removing the value elements to the right of the array. But i believe the question
slices the nums at the end like so : nums[0:k] since with slicig the element at k is not included we have to increment it by 1 so it gets included.



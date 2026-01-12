Selection sort is sorting technique where we pick/select the smallest/largest value then switch it with the item in the end of array or the beginning. 
Example :
Say we have an array = [4,6,3,2,9,1]
Here we have a loop starting from 0 through the length of the array. First we find/select the smallest item from the array which is 1.
We then switch it with where the item our loop is currenlty at i.e index 0. So arr[0] gets switched with the 1. So the array becomes :
[1,6,3,2,9,4]

When we end our first iteration we can be sure that our first element is the smallest value uptil now. We may also later encounter similar values as the
smallest but then again it wont matter because they would be placed after this wihtout breaking any order.


<pre>
  def selectionSort(nums):
    for i in range(0,len(nums)):
        min = nums[i]
        #Min Function Loop
        for j in range(i+1,len(nums)):
            if nums[j] < min:
                min = nums[j]
        rep = nums.index(min,i)
        nums[i],nums[rep] = min,nums[i]
    return nums
</pre>

Explination of Code:
We first assume the minimum to be the first value of array. The inner loop bascially finds the minimum value for the arr from i through n. 
but why i through n and not 0 thorugh n ?
Because we dont need to search behind the array. The array behind i is already sorted. 
For example:
array = [4,6,3,2,9,1]
<pre>
nums[j] < min
</pre>
we first find assume the min be 4. 
Why ?
So that we can have a way to compare. This is like a mathematical assumption. By assuming the first as the smallest value we can comapre it with the rest of the elements.
So this code here comapres each successive elemnet of after i with min i.e the element at i itself.
During this loop the min can become any element of the array from i through n. 
After this loop it gives the FINAL Minimum for that subarray arr[i:n]
<pre>
rep = nums.index(min,i)
nums[i],nums[rep] = min,nums[i]
</pre>
We can then replace our min with the value at arr[i]
IF 
1. min is the arr[i] itself then we dont have to replace but i does get replaced :)
2. if min is the arr[>i] then we have to switch places. So the min values get switched with arr[i].


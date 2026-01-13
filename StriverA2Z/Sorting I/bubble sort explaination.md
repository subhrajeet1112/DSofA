<pre>
def bubbleSort(nums):
    n = len(nums)-1
    for j in range(n):
        for i in range(0,n-j):
            if nums[i] > nums[i+1]:
                nums[i+1],nums[i] = nums[i],nums[i+1]
    return nums
</pre>


So what is this sort doing ? 
1. why is n = len(nums)-1 ?
we did it because we dont need to access/ repeat till the last element. ONlLY needs to check the second last element since we are already
checkig with if arr[i] > arr[n+1]. So we are already checking for the last one without going over it.

2. Why do you need j in range(n)?
This is the outer loop which allows us to go through the loops again and again after the inner loop. Once the inner loops completes it places
the largest element at the end. Next loop would allow us to put our second largest to the right of the array.
So it continues till we have sorted array. where the condidtion <pre> nums[i] > nums[i+1] </pre> doesnt work anymore.

3. What is the inner loop i doing and why is it from 0 thorugh n-j?
The inner loops sorts shifts each number from index 0 to the next place if arr[i] > arr[i+1] so larger numbers gets switched to the right.
IF a number is the lagrest of the array then it gets switched continuously till it is placed at the end of the array.
Then since we know that the last place is the lagrest of the array. We can decrease our range with every iteration with (n-j) since j is the
number of times the lagrest place got sorted . So if j =2 then that means we sorted 2 numbers to the end of the array and hence we only need to
check n-j where n = len(arr)-1.

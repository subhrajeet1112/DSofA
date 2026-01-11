Link to Problem :
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Before we jump to any solution. We might need to do a quick referesher of Two Pointer Technique/Approach. Dont be caught up in the name. Honeslty it could be called anything.
What we are focusing on is how is works? Why does it work ? [More on it later]
So essentially what two pointer does is keeps track of **2 Indices** at the same time instead of just one in a normal loop. 
This allows us the search/perform tasks quicker since we have access to two elements at the same time.
If you can use douple loops this might be an answer to your problem. Either way you may solve it using a normal loop but it will be much slower.

Explaination of Solution :
<pre>
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
</pre>

To understand this solutions we will have to look at what it does exaclty.
We start we k at 0th index and i at 1st index. So k = 1 and i = 0.
Why ?
Because we need two pointers.
Think of the K index at the standard of comparision. We compare each number with K. See how we said "compare each number". How will we do it ? we use the I index pointer. The I pointer 
will allow us to traverse the array without moving our main standard of comparision. So I moves 1 step to the right every loop cycle starting for 1. 
Why starting for 1?
Well if we start both at 0 then essentially we are wasting 1 comparsion. Either way we can at 0 or 1 but starting I from 1 is better. 

<pre>
for i in range(0,len(nums)):
</pre>
This line allows us to traverse in the array without moving K unless specified.

Next we compare the elements arr[k] and arr[i].
Remember k pointer is always behind the i pointer so this is bascially comparing the elements which come subsequenlty after kth index with the element of K. 

<pre>
if nums[k] == nums[i]:
    continue
</pre>
If it matches then move the K pointer up a index.
Do nothing 
Why ?
This means we haven't found a unique elements. So while keeping the K pointer same move to the next value of i. This is why we use continue.


<pre>
elif nums[k] != nums[i]:
    k = k+1
    nums[k] = nums[i]
    continue
</pre>
If there comes a point where the value at K doesnt match value at I. This means we found our next unique element. 
Hence move this to the next position of Kth element. Hence we do k = k+1
then we replace our the element at arr[k+1] with arr[i]. 
Then this continues on till the end of the arr. 

<pre>
k = k+1
nums = nums[:k]
return k
</pre>

Now the final bit of code. K pointer now points to the last unique element of the subarray. 
[1,2,3,4,5,2,3,3,4,5]
If this is the array at last then K points to the element 5. 
so k = 4 since we started k=0. 
We did k = k+1 since we want a count of the number without the 0 and also that it helps us with slicing the original array. 
Next we slice the original arrary till the last unique number. 
<pre>
nums[:k]    
</pre>
The code bascially means take the element from 0th index till K-1 th index. Since K = 5 ( we did k = k+1 earlier) so it takes the element from 0 to 4th index. 
Hence our output 














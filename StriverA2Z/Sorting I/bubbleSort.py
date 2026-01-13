def bubbleSort(nums):
    n = len(nums)-1
    for j in range(n):
        for i in range(0,n-j):
            if nums[i] > nums[i+1]:
                nums[i+1],nums[i] = nums[i],nums[i+1]
    return nums
    

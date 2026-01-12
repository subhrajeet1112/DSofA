def selectionSort(nums):
    for i in range(0,len(nums)):
        min = nums[i]
        #Min Function Loop
        for j in range(i,len(nums)):
            if nums[j] < min:
                min = nums[j]
        rep = nums.index(min,i)
        nums[i],nums[rep] = min,nums[i]
    return nums

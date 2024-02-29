def twoSum(numbers, target):
    # def binarySearch(l, r, goal):
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] == goal:
    #             return mid
    #         elif nums[mid] < goal:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
        
    #     return - 1
    
    # for i in range(len(nums)):
    #     goal = target - nums[i]
    #     goalId = binarySearch(i+1, len(nums)-1, goal)
    #     if goalId != -1:
    #         return [i+1, goalId+1]
    ###Two pointerr###
    l = 0 
    r = len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l+1, r+1]

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))
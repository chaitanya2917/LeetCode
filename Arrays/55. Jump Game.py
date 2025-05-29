#  Greedy Problem

#Python optimal
# time complexity -> O(n) 
# Space complexity -> O(1)


#python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_steps=0
        for i in range(len(nums)):
            if(i>max_steps):
                return False
            max_steps=max(max_steps,i+nums[i])
            if(max_steps>=len(nums)-1):
                return True
        return True


#CPP

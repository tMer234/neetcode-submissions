class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_streak = 0
        streaks = [0]
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_streak += 1
                streaks.append(curr_streak)
            else:
                curr_streak = 0 
                
        return max(streaks)

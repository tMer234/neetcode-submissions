# time O(n), space O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        non_val_count = len(nums)
        while i < non_val_count:
            if nums[i] == val:
                nums[i] = nums[non_val_count -1]
                non_val_count -= 1
            else:
                i += 1
        return non_val_count
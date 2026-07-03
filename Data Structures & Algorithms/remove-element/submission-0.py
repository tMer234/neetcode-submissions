class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_count = 0
        i = 0
        while i < len(nums)-val_count:
            if nums[i] == val:
                val_count += 1
                nums = self.shift_left(nums,i)
            else:
                i +=1 
        return len(nums) - val_count

    def shift_left(self, nums, index):
        for j in range(index,len(nums)-1):
            nums[j] = nums[j+1]
        return nums
        
#brute force
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            right_arr = arr[i+1:]
            if right_arr:
                arr[i] = max(right_arr)
            else:
                arr[i] = -1
        return arr

#time complexity O(n^2)
#space complexity O(n)
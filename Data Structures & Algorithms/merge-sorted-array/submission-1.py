class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
              
        def mergesort(arr,s,e):
            mm = 0
            if  s>=e:
                return arr
            else:
                mm = (s+e)//2
                print(mm)
            mergesort(arr,s,mm)
            mergesort(arr,mm+1,e)
            merge_inplace(arr,s,mm,e)
            return arr
        def merge_inplace(arr,s,mm,e):
            L = arr[s:mm+1]
            R = arr[mm+1: e+1]
            i = 0
            j = 0
            k = s
            while i < len(L) and j<len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1
            while i < len(L):
                arr[k] = L[i]
                i+=1
                k+=1
            while j < len(R):
                arr[k] = R[j]
                j+=1
                k+=1

          
        mergesort(nums1,0,m+n-1)


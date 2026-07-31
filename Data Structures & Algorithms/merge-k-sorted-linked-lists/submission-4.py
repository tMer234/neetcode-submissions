# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(len(lists))
        if len(lists) == 0:
            
            return None
        
        def mergetwolists(list1, list2):
            curr1 = list1
            curr2 = list2
            merged_list = ListNode(0)
            merged_curr = merged_list
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    merged_curr.next = curr1
                    curr1 = curr1.next
                else:
                    merged_curr.next = curr2
                    curr2 = curr2.next
                merged_curr = merged_curr.next

            merged_curr.next = curr1 or curr2
            return merged_list.next
        

        i = 0
        while i < len(lists)-1:
            lists[i+1] = mergetwolists(lists[i], lists[i+1])
            i += 1
        return lists[i]

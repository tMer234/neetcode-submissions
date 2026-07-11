#brute force time complexity O(n^2) space complexity O(n)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches[0] in students:
            if sandwiches[0] == students[0]:
                #student takes and dequeues
                if len(students) == 1:
                    return 0
                else:
                    students = students[1:]
                    sandwiches = sandwiches[1:]
            else:
                #student goes to back of the queue 
                students = students[1:] + [students[0]]
        return len(students)

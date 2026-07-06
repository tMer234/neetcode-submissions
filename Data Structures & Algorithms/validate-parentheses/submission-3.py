class Solution:
    def isValid(self, s: str) -> bool:
        opens_to_closes = {'(' : ')', '{' : '}', '[': ']'}
        stack_opens = []
        for i in s:
            if i in opens_to_closes:
                stack_opens.append(i)
            else:
                if not stack_opens:
                    return False
                else:
                    if i == opens_to_closes[stack_opens[-1]]:
                        stack_opens.pop()
                    else:
                        return False
        return True if not stack_opens else False
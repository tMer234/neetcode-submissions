class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in range(len(operations)):
            if operations[i] == "+":
                scores.append(int(scores[-1]) + int(scores[-2]))
            elif operations[i] == "D":
                scores.append(2*int(scores[-1]))
            elif operations[i] == "C":
                scores.pop()
            else:
                scores.append(operations[i])
        print(scores)
        sum = 0
        for score in scores:
            sum += int(score)
        return sum

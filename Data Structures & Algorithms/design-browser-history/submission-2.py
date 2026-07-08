class webPage:
    def __init__(self, homepage: str, next = None, prev = None):
        self.homepage = homepage
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = webPage(homepage)
        self.tail = self.head
        self.size = 1

    def visit(self, url: str) -> None:
        new = webPage(url)
        temp = self.tail
    
        new.prev = temp
        temp.next = new
        self.tail = new
        self.size += 1


    def back(self, steps: int) -> str:
        temp = self.tail
        n = 0
        while temp.prev and n < steps:
            temp = temp.prev
            n+=1
        self.tail = temp
        return self.tail.homepage

    def forward(self, steps: int) -> str:
        temp = self.tail;
        n = 0
        while temp.next and n < steps:
            temp = temp.next
            n+=1
        self.tail = temp
        return self.tail.homepage

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
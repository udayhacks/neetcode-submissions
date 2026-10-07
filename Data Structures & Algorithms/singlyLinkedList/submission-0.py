from collections import deque
class LinkedList:
    
    def __init__(self):
        self.data = deque([])
        


    
    def get(self, index: int) -> int:
        if  index >= len(self.data) : 
            return -1
        for i in range(len(self.data)) :
            if i == index :
                return self.data[i]
        

        
            
            
        
        

    def insertHead(self, val: int) -> None:
        if not self.data:
            self.data.append(val)
        else:
            self.data.appendleft(val)





        

    def insertTail(self, val: int) -> None:
        self.data.append(val)

        

    def remove(self, index: int) -> bool:
        n = len(self.data)
        for i in range(n):
            if i == index:
                self.data.remove(self.data[index])
                return True
        return False
        
        

    def getValues(self) -> List[int]:
        ans = []

        for i in self.data:
            ans.append(i)
        return ans
        

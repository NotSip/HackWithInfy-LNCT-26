class MyCircularDeque:


    def __init__(self, k: int):
        self.item = [None] * k
        self.size = k
        self.front = self.rear = -1        

    def insertFront(self, value: int) -> bool:
        if self.front == -1:
            self.front = self.rear = 0
        elif (self.rear+1) % self.size == self.front:
            return False
        else:
            self.front = ( self.front-1 + self.size )% self.size
        self.item[self.front] = value    
        return True


        

    def insertLast(self, value: int) -> bool:
        if self.front == -1:
            self.front = self.rear = 0
        elif (self.rear+1) % self.size == self.front:
            return False
        else:
            self.rear = (self.rear + 1)% self.size
        self.item[self.rear] = value
        return True
            


    def deleteFront(self) -> bool:
        if self.front == -1:
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
            return True
        else:
            self.front = (self.front +1) % self.size
            return True       

    def deleteLast(self) -> bool:
        if self.front == -1:
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
            return True
        else:
            self.rear = (self.rear-1 + self.size) % self.size
            return True   
        

    def getFront(self) -> int:
        if self.front == self.rear == -1:
            return -1
        return self.item[self.front]

        

    def getRear(self) -> int:
        if self.front == self.rear == -1:
            return -1
        return self.item[self.rear]
        

    def isEmpty(self) -> bool:
        if self.front == self.rear == -1:
            return True
        else:
            return False

        

    def isFull(self) -> bool:
        if (self.rear+1) % self.size == self.front:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# Jason McKinlay
# Max Heap

class MaxHeap:
    '''
        >>> h = MaxHeap()
        >>> h.getMax
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [10, 5]
        >>> h.insert(14)
        >>> h._heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(14)
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> h.insert(20)
        >>> h
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.insert(20)
        >>> h
        [20, 20, 14, 14, 2, 10, 11, 5, 9]
        >>> h.getMax
        20
        >>> h._leftChild(1)
        20
        >>> h._rightChild(1)
        14
        >>> h._parent(1)
        >>> h._parent(6)
        14
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMax()
        20
        >>> h._heap
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.deleteMax()
        20
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> len(h)
        7
        >>> h.getMax
        14
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMax(self):
        if self._heap == []:
            return None
        return self._heap[0]

    def _parent(self,index):
        if index <= 1:
            return None
        return self._heap[index // 2 - 1]

    def _leftChild(self,index):
        if index * 2 <= len(self._heap):
            return self._heap[index * 2 - 1]
        return None

    def _rightChild(self,index):
        if index * 2 + 1 <= len(self._heap):
            return self._heap[index * 2]
        return None

    def insert(self,x):
        self._heap.append(x)
        index = len(self._heap)
        
        while self._parent(index) is not None:
            parent_index = index // 2
            if self._heap[index - 1] > self._heap[parent_index - 1]:
                self._heap[index - 1], self._heap[parent_index - 1] = self._heap[parent_index - 1], self._heap[index - 1]
                index = parent_index
            else:
                return None
    

    def deleteMax(self):
        if len(self)==0:
            return None       
         
        elif len(self)==1:
            removed=self._heap[0]
            self._heap=[]
            return removed 

        else:
            max = self.getMax
            index = 1
            self._heap[0] = self._heap[len(self._heap) - 1]
            self._heap.pop()
            
            while 2 * index + 1 <= len(self._heap):
                new_index = index
                if self._leftChild(index) > self._heap[index - 1] or self._leftChild(index) == self._rightChild(index):
                    new_index = 2 * index
                if self._rightChild(index) > self._leftChild(index):
                    new_index = 2 * index + 1

                if new_index != index:
                    self._heap[index - 1], self._heap[new_index - 1] = self._heap[new_index - 1], self._heap[index - 1]
                    index = new_index
                else:
                    return max

            return max


def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [8, 5, 4, 3.1, 2, 1, 0, -15, -15, -15]
    '''
    max_heap = MaxHeap()
    for value in numList:
        max_heap.insert(value)

    sorted = []
    for i in range(len(max_heap)):
        sorted.append(max_heap.deleteMax())

    return sorted


def run_tests():
    import doctest
    doctest.testmod(verbose=True)
    
if __name__ == "__main__":
    run_tests()
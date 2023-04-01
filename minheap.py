arr = [16,10,39,9,35,70,45,40,50,8,80]

class min_heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2
    
    def l_child(self, i):
        return 2*i + 1
    
    def r_child(self,i):
        return 2*i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, k):
        self.heap.append(k)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def del_min(self):
        if len(self.heap) == 0:
            return None
        min_elem = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)
        return min_elem

    def heapify_down(self, i):
        min_elem = i
        left = self.l_child(i)
        right = self.r_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_elem]:
            min_elem = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[min_elem]:
            min_elem = right

        if i != min_elem:
            self.swap(i, min_elem)
            self.heapify_down(min_elem)
            

    def print_heap(self):
        print(self.heap)

heap = min_heap()
for m in arr:
    heap.insert(m)
    heap.print_heap()

heap.del_min()
heap.print_heap()
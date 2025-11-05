import sys
class MaxHeap:
    '''
    Max Heap Implementation in Python (0-based index)
    '''
    def __init__(self):
        self.heap_list = []  # now purely 0-based, no dummy at index 0

    @property
    def size(self):
        '''Returns the size of this heap'''
        return len(self.heap_list)

    def parent(self, index):
        '''Return the parent index of a node at index'''
        return (index - 1) // 2

    def l_child(self, index):
        '''Return the index of the left child node of a given index'''
        return 2 * index + 1

    def r_child(self, index):
        '''Return the index of the right child node of a given index'''
        return 2 * index + 2

    def is_leaf(self, index):
        '''Returns true if the given index is a leaf node'''
        return self.l_child(index) >= self.size

    def swap(self, i, j):
        '''Swap two nodes in the heap'''
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]

    def insert(self, element):
        '''
        Insert an element into the heap and maintain heap property
        '''
        self.heap_list.append(element)
        current = self.size - 1

        while current > 0 and self.heap_list[current] > self.heap_list[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def max_heapify(self, i):
        '''
        Heapify node at index i
        '''
        l = self.l_child(i)
        r = self.r_child(i)
        largest = i

        if l < self.size and self.heap_list[l] > self.heap_list[largest]:
            largest = l

        if r < self.size and self.heap_list[r] > self.heap_list[largest]:
            largest = r

        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest)

    def build_max_heap(self, unsorted_list):
        '''
        Build a max heap from an unsorted list
        '''
        self.heap_list = unsorted_list[:]
        for i in range((self.size // 2) - 1, -1, -1):
            self.max_heapify(i)

    def extract_max(self):
        '''
        Extract and return the maximum element from the heap
        '''
        if self.size == 0:
            return None
        if self.size == 1:
            return self.heap_list.pop()

        popped = self.heap_list[0]
        self.heap_list[0] = self.heap_list.pop()
        self.max_heapify(0)
        return popped

    def __str__(self):
        return str(self.heap_list)


def main():
    my_heap = MaxHeap()
    my_heap.insert(1)
    print(my_heap)
    my_heap.insert(4)
    print(my_heap)
    my_heap.insert(10)
    print(my_heap)
    my_heap.insert(13)
    print(my_heap)
    my_heap.insert(17)
    print(my_heap)
    my_heap.insert(9)
    print(my_heap)
    my_heap.insert(22)
    print(my_heap)

    print("\nSorted Output:")
    while my_heap.size > 0:
        print(my_heap.extract_max())

    print("\nBuilding from list [4, 12, 45, 23, 11]:")
    my_heap.build_max_heap([4, 12, 45, 23, 11])
    print(my_heap)


if __name__ == '__main__':
    main()

class CustomList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.array = [None] * self.capacity

    def append(self, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = item
        self.size += 1

    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = item
        self.size += 1

    def remove(self, item):
        for i in range(self.size):
            if self.array[i] == item:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j+1]
                self.array[self.size - 1] = None
                self.size -= 1
                if 0 < self.size < self.capacity // 4:
                    self._resize(self.capacity // 2)
                return
        raise ValueError("Item not found")

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def set(self, index, item):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = item

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __len__(self):
        return self.size

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"

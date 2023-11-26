class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        if capacity < 0:
            raise ValueError("Invalid capacity of the jar")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        if size > self.capacity:
            raise ValueError("Exceeds capacity")
        if size < 0:
            raise ValueError("Too few cookies")
        self._size = size

jar = Jar()
jar.deposit(11)
print(jar)


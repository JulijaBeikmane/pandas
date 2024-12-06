class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError("Capacity must be a non-negative integer.")

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity or (self.size + n) > self.capacity:
            raise ValueError("Too much cookies")
        else:
            self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Number of cookies to withdraw must be a non-negative integer.")
        else:
            self._size -= n
        # if self.capacity < self.capacity:
        #     raise ValueError("Number of cookies to withdraw must be a non-negative integer.")
        
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
jar = Jar(18)
jar.deposit(10)
jar.withdraw(3)
print(jar)

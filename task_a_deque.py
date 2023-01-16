# ID 78867214

class Deque:
    def __init__(self, maximum_size):
        self.items = [None] * maximum_size
        self.maximum_size = maximum_size
        self.head = 0
        self.tail = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def there_is_no_place(self):
        return self.size == self.maximum_size

    def push_back(self, index):
        if self.there_is_no_place():
            raise IndexError(f'there is no place for push_back({index})')
        self.tail = (self.tail + 1) % self.maximum_size
        self.items[self.tail] = index
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError("empty deque for pop_back()")
        data = self.items[self.tail]
        self.tail = (self.tail - 1) % self.maximum_size
        self.size -= 1
        return data

    def push_front(self, index):
        if self.there_is_no_place():
            raise IndexError(f'there is no place for push_front({index})')
        self.head = (self.head - 1) % self.maximum_size
        self.items[self.head] = index
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("empty deque for pop_front()")
        data = self.items[self.head]
        self.head = (self.head + 1) % self.maximum_size
        self.size -= 1
        return data


if __name__ == '__main__':
    number = int(input())
    deque = Deque(int(input()))
    for _ in range(number):
        command, *params = input().strip().split()
        try:
            result = getattr(deque, command)(*params)
            if result:
                print(result)
        except AttributeError:
            raise AttributeError(f"method: {command}, not found.")
        except IndexError:
            print("error")


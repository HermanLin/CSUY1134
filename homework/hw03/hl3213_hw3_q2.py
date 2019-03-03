import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def __getitem__(self, ind):
        if not(0 <= ind <= (self.n - 1)):
            raise IndexError("Invalid Index")
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if not(0 <= ind <= (self.n - 1)):
            raise IndexError("Invalid Index")
        self.data_arr[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def extend(self, other_iterable):
        for elem in other_iterable:
            self.append(elem)

    #insert(self, index, val)
    def insert(self, index, val):
        if index > self.n:
            raise IndexError("Invalid Index")
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        for x in range(self.n, index, -1):
            self.data_arr[x] = self.data_arr[x - 1]
        self.data_arr[index] = val

    #pop(self)
    def pop(self):
        if self.n == 0:
            raise IndexError("Invalid Index")
        ret = self.data_arr[self.n - 1]
        self.data_arr[self.n] = None
        self.n -= 1
        if self.n <= self.capacity // 4:
            self.resize(self.capacity // 2)
        return ret
    '''
    def pop(self, index):
        if self.n == 0 or index > self.n:
            raise IndexError("Invalid Index")
        ret = self.data_arr[index]
        self.data_arr[index] = None
        self.n -= 1
        if self.n <= int(self.capacity / 4):
            self.resize(int(self.capacity / 2))
        return ret
    '''
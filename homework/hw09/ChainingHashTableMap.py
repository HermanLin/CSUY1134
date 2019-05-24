import random
from UnsortedArrayMap import UnsortedArrayMap



class ChainingHashTableMap:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N


    def __init__(self, N=64):
        self.N = N
        #self.table = [UnsortedArrayMap() for i in range(self.N)]
        self.table = [None for i in range(self.N)]
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.hash_function(key)
        if isinstance(self.table[i], UnsortedArrayMap):
            curr_bucket = self.table[i]
            return curr_bucket[key]
        return self.table[i].value

    def __setitem__(self, key, value):
        '''
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)
        '''
        i = self.hash_function(key)
        if isinstance(self.table[i], UnsortedArrayMap):
            curr_bucket = self.table[i]
            old_size = len(curr_bucket)
            curr_bucket[key] = value
            new_size = len(curr_bucket)
        elif self.table[i] is None:
            self.table[i] = UnsortedArrayMap.Item(key, value)
            old_size = 0
            new_size = 1
        else:
            new_bucket = UnsortedArrayMap()
            old_item = self.table[i]
            self.table[i] = new_bucket
            new_bucket[old_item.key] = old_item.value
            new_bucket[key] = value
            old_size = 1
            new_size = 2
        if new_size > old_size:
            self.n += 1
        if self.n > self.N:
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        '''
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        del curr_bucket[key]
        self.n -= 1
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)
        '''
        i = self.hash_function(key)
        if isinstance(self.table[i], UnsortedArrayMap):
            curr_bucket[key]
        else:
            self.table[i] = None
        self.n -= 1
        if self.n < (self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        '''
        for curr_bucket in self.table:
            for key in curr_bucket:
                yield key
        '''
        for elem in self.table:
            if isinstance(elem, UnsortedArrayMap):
                for key in elem:
                    yield key
            else:
                yield elem.key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val

def print_hash_table(ht):
    for i in range(ht.N):
        print(i, ": ", sep="", end="")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print("(", key, ", ", curr_bucket[key], ")", sep="", end=" ")
        print()


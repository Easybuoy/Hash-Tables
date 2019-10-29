# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        key_idx = self._hash_mod(key)

        if self.storage[key_idx] == None:
            self.storage[key_idx] = LinkedPair(key, value)
        else:
            existing_key = self.storage[key_idx]
            while existing_key and existing_key.key != key:
                prev, existing_key = existing_key, existing_key.next

            if existing_key:
                existing_key.value = value

            else:
                prev.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        print('keyy', key)
        # hashed_key = self._hash_mod(key)

        # existing_key = self.storage[key]
        # print(existing_key.value, 'exits')
        # print(existing_key.key, key)
        # if (existing_key.key == key):
        #     del existing_key.value
        # print(existing_key.value, 'exist key')
        # while not existing_key:

        # if self.storage[hashed_key]:
        #     del self.storage[hashed_key]
        # else:

        # print('warning, key not found')
        # if key in self.storage:
        #     del self.storage[key]
        #     return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key]:
            existing_key = self.storage[hashed_key]
            while existing_key.key != key:
                existing_key = existing_key.next
            return existing_key.value
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        newCapacity = self.capacity * 2
        new_storage = [None] * newCapacity

        for i in range(len(self.storage)):
            new_storage[i] = self.storage[i]

        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
    print(ht.remove(0))

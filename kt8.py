class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashed_key = self._hash(key)
        for pair in self.table[hashed_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hashed_key].append([key, value])

    def get(self, key):
        hashed_key = self._hash(key)
        for pair in self.table[hashed_key]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        hashed_key = self._hash(key)
        for i, pair in enumerate(self.table[hashed_key]):
            if pair[0] == key:
                del self.table[hashed_key][i]
                return
        raise KeyError("Key not found in the hash table")


if __name__ == "__main__":
    hash_table = HashTable(size=10)

    hash_table.insert("apple", 10)
    hash_table.insert("banana", 20)
    hash_table.insert("orange", 30)

    print("Значение для ключа 'banana':", hash_table.get("banana"))

    hash_table.remove("banana")

    print("Значение для ключа 'banana' после удаления:", hash_table.get("banana"))

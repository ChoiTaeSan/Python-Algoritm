class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def delete(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

htable = HashTable()
htable.add("name", "John")
print(htable.get("name"))
htable.delete("name")
print(htable.get("name"))

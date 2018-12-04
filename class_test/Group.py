class Group:
    def __init__(self,arr = []):
        self._arr = arr
    def __setitem__(self, key, value):
        self.arr[key] = value
    def __getitem__(self, item):
        return self._arr[item]
class User():
    def __init__(self,ten,age,data = {}) -> None:
        super().__init__()
        self._ten = ten
        self.age = age
        self.data = data
    @property
    def ten(self):
        return self._ten
    @ten.setter
    def ten(self,ten):
        self._ten = ten
    def __setitem__(self, key, value):
        self.data[key] = value
    def __getitem__(self, item):
        return self.data[item]
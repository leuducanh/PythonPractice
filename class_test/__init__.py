from class_test.User import User
from class_test.Group import Group

if __name__ == "__main__":
    print("123")
    u = User("A",1)
    print("123")
    print(u.age)
    print("123")
    u.ten = "abc"
    print(u.ten)

    u["a"] = "a"
    print(u["a"])

    g = Group([1,2,3])


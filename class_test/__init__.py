# from class_test.User import User
# from class_test.Group import Group

def make_tag(tagname):

    def wrapper(f):
        def print_html(text):
            return '<%(tag)s>%(text)s' % dict(tag=tagname,text=f(text))
        return print_html
    return wrapper

@make_tag("a")
@make_tag("b")
def transform(text):
    return text.upper()

if __name__ == "__main__":
    # print("123")
    # u = User("A",1)
    # print("123")
    # print(u.age)
    # print("123")
    # u.ten = "abc"
    # print(u.ten)

    # u["a"] = "a"
    # print(u["a"])

    # g = Group([1,2,3])
    print(transform("haha"))




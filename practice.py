# 1
def demo(name, age):
    print(name, age)


demo("Kelly", 25)


# 2
def func1(*args):
    for arg in args:
        print(f"Hello {arg}")


func1(1, 2, 3)
func1(50, 11, "Ann", "Kim")


# 3
def calc(a, b):
    """
    :param a: int first value
    :param b: int second value
    :return: int total value
    """
    add = a + b
    sub = a - b
    return add, sub


ans = calc(40, 10)
print(ans)


# 4
def show_employee(name, salary=9000):
    print(name, salary)


show_employee("Ben", 500)
show_employee("Alfred")


# 5
def outer_func(a, b):
    """This serves as an outer function"""
    def inner_func(a, b):
        add = a + b
        return add

    res = inner_func(a, b)
    return res + 5


x = outer_func(5, 10)
print(x)

# 6







